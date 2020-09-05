from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField('User Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Send')


class TodoForm(FlaskForm):
	description = StringField('Descripción',validators=[DataRequired()] )
	submit = SubmitField('Crear')


class DeleteForm(FlaskForm):
	submit = SubmitField('Borrar')


class UpdateTodoForm(FlaskForm):
	submit = SubmitField('Actualizar')