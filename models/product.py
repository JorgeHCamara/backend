from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    color = db.Column(db.String(50))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    promotional_price = db.Column(db.Float)
