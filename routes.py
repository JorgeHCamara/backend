from flask_restful import Api
from resources.product_resource import ProductResource, AddProductResource

def initialize_routes(api: Api):
    api.add_resource(ProductResource, '/products')
    api.add_resource(AddProductResource, '/products/add')