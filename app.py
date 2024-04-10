"""Pet adoption application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretsecret12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_all_pets():
    """Displays all pets, separating available from not available"""

    avail_pets = Pet.query.filter_by(available = True).all()
    nonavail_pets = Pet.query.filter_by(available = False).all()
    return render_template('home.html', 
                           avail_pets=avail_pets,
                           nonavail_pets=nonavail_pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Shows pet form and handles form submission"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        #creates new pet from AddPetForm data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} was added!", "success")
        return redirect ('/')
    else:
        return render_template("form.html", form = form)
    

@app.route('/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    """Shows edit pet form and handles form submission"""
    
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name}'s info was edited!", "success")
        return redirect ('/')
    else:
        return render_template ('profile.html', 
                                pet = pet,
                                form = form)
