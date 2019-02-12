from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

#forms for our pitches has 3 input fields
class PitchForm(FlaskForm):
    category = StringField('Pitch Your Idea' ,validators=[Required()])
    title = StringField('Entre Your Name' ,validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = StringField('Review title' ,validators=[Required()])
    submit = SubmitField('Submit')   
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')