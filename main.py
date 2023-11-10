from flask import Flask
from flask import render_template
from flask import request

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
        # お問い合わせ内容
        note = form.note.data

        # 出力
        return render_template("thanks.html")

    # GET:フォーム送信前
    else:
        return render_template("index.html",form=form)

"""
# デバック時に使う
if __name__== '__main__':
    app.run(debug=True)
"""