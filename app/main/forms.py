from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()])
    email = StringField('Qual é o seu email (Envio de notificação do novo usuário)?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
