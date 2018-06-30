from  flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')

class PitchingForm(FlaskForm):
    description = TextAreaField('Give a pitch',validators=[Required()])
    category = SelectField('Category', choices=[('Technology','Technology'),('Sports','Sports'),('Religion','Religion')])
    submit = SubmitField('Pitch!')

class CommentForm(FlaskForm):
    details = StringField('Write a comment',validators=[Required()])
    submit = SubmitField('Comment')