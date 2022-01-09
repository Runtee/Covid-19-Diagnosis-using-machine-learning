from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    firstName = db.Column(db.String(64), unique=False)
    middleName = db.Column(db.String(64), unique=False)
    surName = db.Column(db.String(64), unique=False)
    email = db.Column(db.String(64), unique=False)
    DOB = db.Column(db.Date, unique=False)
    phone = db.Column(db.Integer, unique=False)
    state = db.Column(db.String(64), unique=False)
    LGA = db.Column(db.String(64), unique=False)
    caddress = db.Column(db.String(64), unique=False)
    # NOK = db.Column(db.String(64), unique=False)
    bgroup = db.Column(db.String(64), unique=False)
    gtype = db.Column(db.String(64), unique=False)
    sex = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return 'profile' % self.id


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    profiles = db.relationship('Profile', backref='role')

    def __repr__(self):
        return 'user is' % self.username
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
