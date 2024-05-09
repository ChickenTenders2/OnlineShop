from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sneaker(db.Model):
    __tablename__ = 'sneakers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.String(64))
    description = db.Column(db.Text)
    imageTag = db.Column(db.String(64))
