from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class GuestbookForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    content = TextAreaField('内容', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('提交')
