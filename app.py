from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, Species
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "GHHJHGPUTVJIUEXV09269"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def show_home_page():
    """Renders Home Page"""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Renders page for adding a pet and sends new pet information to db"""

    form = AddPetForm()
    species_query = db.session.query(Species.species_code, Species.species_name).all()
    species_list = [(i.species_code, i.species_name) for i in species_query]
    form.species.choices = species_list
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        photo_url = str(photo_url) if photo_url else None
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{name} has been added", "p-3 mb-2 bg-success text-white")
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Renders pet details page and sends updated pet information to db"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.availible = form.availible.data
        db.session.commit()
        flash(f"{pet.name} has been edited", "p-3 mb-2 bg-success text-white")
        return redirect("/")
    else:
        return render_template("pet_details.html", pet=pet, form=form)
