from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Dog(DB.Model):
    """Saving the data of a dog picture"""
    id = DB.Column(DB.Integer, primary_key=True)
    image = DB.Column(DB.Text)
    name = DB.Column(DB.Text)
    breed = DB.Column(DB.Text)

    def __repr__(self):
        # return 'A {} dog named {}'.format(self.breed, self.name) -option 2
        return f'A {self.breed} dog named {self.name}'
        # faster on the processor when you're trying to read
