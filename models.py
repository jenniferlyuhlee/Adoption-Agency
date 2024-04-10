"""Models for Adoption Agency."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet model for adopt database"""
    __tablename__ = 'pets'

    id = db.Column (db.Integer,
                    primary_key = True, 
                    autoincrement = True)
    name = db.Column (db.String,
                      nullable = False)
    species = db.Column (db.String,
                      nullable = False)
    photo_url = db.Column (db.String)
    age = db.Column (db.Integer)
    notes = db.Column (db.Text)
    available = db.Column (db.Boolean,
                      nullable = False,
                      default = True)

    