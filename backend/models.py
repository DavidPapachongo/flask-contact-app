from flask_login import UserMixin
from __init__ import db


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(1000),nullable=False)
    contacts = db.relationship('Contacts', backref='users', lazy=True)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    
    def __init__(self, fullname, phone, email,user_id):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.user_id = user_id
