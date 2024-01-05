from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Species(db.Model):
    """table for list of species"""

    __tablename__ = "pet_species"

    species_code = db.Column(db.Text, primary_key=True)
    species_name = db.Column(db.Text, nullable=False, unique=True)

    def __repr__(self):
        s = self
        return f"<Species code={s.species_code} species={s.species_name}>"


class Pet(db.Model):
    """table for list of pets"""

    __tablename__ = "adoptable_pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(
        db.Text, db.ForeignKey("pet_species.species_code"), nullable=False
    )
    photo_url = db.Column(
        db.Text,
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png",
    )
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    availible = db.Column(db.Boolean, default=True)

    spec = db.relationship("Species", backref="pet")

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species}>"
