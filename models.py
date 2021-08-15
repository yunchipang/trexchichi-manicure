from app import db
from datetime import date, datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.Date)
    signup_date = db.Column(db.Date, default=date.today())
    cash = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.now())
    category = db.Column(db.String(20), nullable=False)
    details = db.Column(db.String(100))
    # define foreign_key source
    users = db.relationship('User', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return '<Transaction %r>' % (self.id)

class Topup(db.Model):
    __tablename__ = 'topups'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # define foreign_key source
    users = db.relationship('User', backref=db.backref('topups', lazy=True))

    def __repr__(self):
        return '<Topup %r>' % (self.id)