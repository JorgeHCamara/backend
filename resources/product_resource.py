from flask import request, jsonify
from flask_restful import Resource
from models.product import db, Product
from schemas import ProductSchema

product_schema = ProductSchema(session=db.session)
products_schema = ProductSchema(session=db.session, many=True)

class ProductDatabase:
    @staticmethod
    def fetch_all_products():
        return Product.query.all()

    @staticmethod
    def add_product(product):
        db.session.add(product)
        db.session.commit()

class ProductResource(Resource):
    def get(self):
        products = ProductDatabase.fetch_all_products()
        return jsonify({'products': products_schema.dump(products)})

class AddProductResource(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        product = product_schema.load(data)
        ProductDatabase.add_product(product)
        return jsonify({
            "success": True,
            "message": "Product added successfully",
            "product": product_schema.dump(product)
        })