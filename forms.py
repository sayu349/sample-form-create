from wtforms import Form

from wtforms.fields import StringField
from wtforms.fields import IntegerField
from wtforms.fields import PasswordField
from wtforms.fields import DateField
from wtforms.fields import RadioField
from wtforms.fields import SelectField
from wtforms.fields import BooleanField
from wtforms.fields import TextAreaField
from wtforms.fields import EmailField
from wtforms.fields import SubmitField

class UserInfoForm(Form):
    name = StringField("名前：", render_kw={"placeholder": "(例)山田 太郎"})

    submit = SubmitField("送信")