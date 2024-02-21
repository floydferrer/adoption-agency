from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, text, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'

app.app_context().push()

app.config['SECRET_KEY'] = '123456'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f'Added {name}')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/pets/<int:id>')
def view_pet(id):
    pet = Pet.query.get_or_404(id)
    return render_template('pet_details.html', pet=pet)

@app.route('/pets/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f'Updated {pet.name}')
        return redirect(f'/pets/{id}')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
