from models import Pet, Species, db
from app import app

db.drop_all()
db.create_all()

s1 = Species(species_code="dog", species_name="Dog")
s2 = Species(species_code="cat", species_name="Cat")
s3 = Species(species_code="porcupine", species_name="Porcupine")

p1 = Pet(
    name="Milo",
    species="cat",
    photo_url="https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg",
    age=4,
)

p2 = Pet(
    name="Sonic",
    species="porcupine",
    photo_url="https://i.natgeofe.com/k/dfc55ac8-a221-4390-b440-72ebfe2bfc39/hedgehog-staring_3x2.jpg",
    age=2,
)
p3 = Pet(
    name="Rex",
    species="dog",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Labrador_Retriever_portrait.jpg/1200px-Labrador_Retriever_portrait.jpg",
    age=5,
)

db.session.add_all([s1, s2, s3, p1, p2, p3])
db.session.commit()
