from flask import Flask
from flask import render_template
from flask import request
import os
import sqlite3

# インスタンス作成
app = Flask(__name__)

# ルーティング
from forms import UserInfoForm

# 情報入力
@app.route("/", methods=["POST","GET"])
def enter_form():
    # フォーム生成
    form = UserInfoForm(request.form)

    # POST:フォーム送信後
    if request.method == "POST":
        # お名前
        name = form.name.data
        # 会社名
        company = form.company.data
        # お電話番号
        tel = form.tel.data
        # メールアドレス
        email = form.email.data
        # お問い合わせ概要
        inquiry = form.inquiry.data
        if inquiry=="seminar":
            inquiry = "セミナー・講演のご依頼"
        elif inquiry == "consultant":
            inquiry = "相談・コンサルティングのご依頼"
        else:
            inquiry = "その他"
        # お問い合わせ内容
        note = form.note.data

        # 実行環境で条件分岐をする
        if os.getenv('GAE_ENV', '').startswith('standard'):
            # クラウド環境の場合
            from google.cloud import storage
            # GCS上のdbを取得する
            client = storage.Client()
            bucket_name = "sample-form-404507.appspot.com"
            bucket = client.get_bucket(bucket_name)
            blob_name = "sample-form-db/from.db"
            blob = bucket.blob(blob_name)
            blob.download_to_filename('/tmp/from.db')

            # databaseにレコードを追加
            con = sqlite3.connect('/tmp/from.db')
            cur = con.cursor()
            cur.execute('INSERT INTO form (name, company, tel, email, inquiry, note) VALUES (?, ?, ?, ?, ?, ?)',
                        (name, company, tel, email, inquiry, note))
            con.commit()
            con.close()

            # レコードを上書き保存する
            client = storage.Client()
            bucket_name = "sample-form-404507.appspot.com"
            bucket = client.get_bucket(bucket_name)
            blob_name = "sample-form-db/from.db"
            blob = bucket.blob(blob_name)
            blob.upload_from_filename('/tmp/from.db')

            return render_template("thanks.html",form = form)

        else:
            # ローカル環境の場合
            # databaseにレコードを追加
            con = sqlite3.connect('database/form.db')
            cur = con.cursor()
            cur.execute('INSERT INTO form (name, company, tel, email, inquiry, note) VALUES (?, ?, ?, ?, ?, ?)',
                        (name, company, tel, email, inquiry, note))
            con.commit()
            con.close()

        return render_template("thanks.html",form = form)

    # GET:フォーム送信前
    else:
        return render_template("index.html",form=form)

"""
# 本番環境では使わない！！
# デバック時に使うこと
if __name__== '__main__':
    app.run(debug=True)
"""