from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding new pet"""
    name = StringField("Pet Name", validators = 
                       [InputRequired(message="Pet must have a name")])
    
    species = SelectField("Species", choices = 
                         [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
                         validators = [InputRequired(message="Must select species")])
    
    age = IntegerField("Age", validators=
                       [NumberRange(0, 30, message="Invalid age"),Optional()])
    
    photo_url = StringField("Photo URL", validators = 
                            [URL(message="Invalid URL"), Optional()])
    
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing existing pet"""
    photo_url = StringField("Photo URL", validators = 
                            [URL(message="Invalid URL"), Optional()])
    
    notes = TextAreaField("Notes")
    
    available = BooleanField("Available")