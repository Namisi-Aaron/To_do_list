from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Task

class AddTaskForm(FlaskForm):
    task = StringField('task', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Add')