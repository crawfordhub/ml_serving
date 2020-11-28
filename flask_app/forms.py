from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IndexForm(FlaskForm):
    index_request = StringField('Index', validators=[DataRequired()])
    submit = SubmitField('Sign In')
