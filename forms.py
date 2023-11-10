from wtforms import Form

from wtforms.fields import (
    StringField, PasswordField, DateField,
    SelectField, BooleanField, TextAreaField,
    SubmitField
)
# python3.11以上の場合
from wtforms.fields.html5 import EmailField
# python 3.11未満の場合
# from wtforms.fields import EmailField

from wtforms.validators import (
    DataRequired, Email, EqualTo
)


class UserInfoForm(Form):
    # 名前：文字列入力
    name = StringField("お名前", render_kw={"placeholder":"(例)山田 太郎"}, validators=[DataRequired("お名前の入力は必須です")])
    # 年齢：静数値入力
    company = StringField("会社名", render_kw={"placeholder":"〇〇〇〇株式会社"})
    # お電話番号：文字列入力
    tel = StringField("お電話番号",render_kw={"placeholder":"012-3456-7890"})
    # メールアドレス：メールアドレス入力
    email = EmailField("メールアドレス", render_kw={"placeholder":"xxxx@example.com"}, validators=[EqualTo("confirm_password", "メールアドレスが一致しません")])
    # メールアドレス(確認用)：メールアドレス入力
    confirm_email = EmailField("メールアドレス確認", render_kw={"placeholder":"xxxx@example.com"}, validators=[Email("メールアドレスのフォーマットではありません")])
    # お問い合わせ概要：セレクトボックス
    inquiry = SelectField("お問い合わせ概要", choices=[("seminar", "セミナー・講演のご依頼"),("consultant", "相談・コンサルティングのご依頼"),("others","その他")])
    # お問い合わせ内容：テキストボックス
    note = TextAreaField("お問い合わせ内容", validators=[DataRequired("お問い合わせ内容を入力してください")])
    # 同意：真偽値入力
    privacy = BooleanField("プライバシーポリシーに同意する", validators=[DataRequired("プライバシーポリシーへの同意が必要です")])
    # ボタン
    submit = SubmitField("送信")