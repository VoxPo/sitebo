from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class formLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha =  PasswordField('Senha', validators=[DataRequired(), Length(6 ,12)])
    submitLogin = SubmitField('Login')

class formNovoUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    celular = StringField('Celular', validators=[])
    cpf = StringField('CPF', validators=[])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 12)])
    senhaConfirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Criar conta')