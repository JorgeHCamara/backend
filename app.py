from flask import Flask
from flask_restful import Api
from models.product import db
from resources.product_resource import ProductResource
from routes import initialize_routes
from config import Config

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)

db.init_app(app)

initialize_routes(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
