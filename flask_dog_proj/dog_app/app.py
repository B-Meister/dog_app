from flask import Flask, render_template, request
from .models import *
import requests


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dogpics.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return "This is a successful Flask app!"

    @app.route('/render')
    def render():
        return render_template('home.html')

    @app.route('/render_w_insert/<insert>')
    def render_w_insert(insert):
        return render_template('insert.html', insertion=insert)

    @app.route('/puppy')
    def puppy():
        json = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image = json['message']
        return render_template('dog.html', picture=image, blob=json)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'Database reset!'

    @app.route('/save_dog')
    def save_dog():
        json = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image = json['message']
        breed = image.split('/')[4]
        return render_template('save_dog.html', picture=image, breed=breed)

    @app.route('/saved_dog', methods=['POST'])
    def saved_dog():
        image = request.values['doglink']
        name = request.values['dogname']
        breed = request.values['dogbreed']
        dog = Dog(image=image, name=name, breed=breed)
        DB.session.add(dog)
        DB.session.commit()
        return render_template('saved_dog.html', picture=image, breed=breed, name=name)

    @app.route('/dog_list')
    def dog_list():
        dogs = Dog.query.all()
        names = [record.name for record in dogs]
        # breed = [record.breed for record in dogs]
        return render_template('dog_list.html', names=names)

    @app.route('/view_dog', methods=['POST'])
    def view_dogs():
        name = request.values['dogname']
        dog = Dog.query.filter_by(name=name).all()[0]
        return render_template('saved_dog.html', picture=dog.image, name=dog.name, breed=dog.breed)





    return app



