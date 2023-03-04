from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class OptOutForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired(), Length(min=3, max=50)])
    last_name = StringField('last_name', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')



