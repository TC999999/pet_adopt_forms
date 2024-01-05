from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", validators=[InputRequired()])
    photo_url = StringField(
        "Photo URL", validators=[URL()], render_kw={"style": "width: 100ch"}
    )
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", render_kw={"rows": "4", "cols": "100"})
    # availible = BooleanField("Availible")


class EditPetForm(FlaskForm):
    """Form for editing pet information"""

    photo_url = StringField(
        "Photo URL", validators=[URL()], render_kw={"style": "width: 80ch"}
    )
    notes = TextAreaField("Notes", render_kw={"rows": "4", "cols": "100"})
    availible = BooleanField("Availible")
