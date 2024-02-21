from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired

class PetForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(message="Name can't be blank")])
    species = StringField('Species', validators=[InputRequired(message="Name can't be blank")])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = StringField('Notes')
    available = BooleanField('Available?')