#!/usr/bin/env/python3
"""
endpoints for products
"""
from flask import Blueprint, jsonify, request
from models.engine.inventory_manager import Inventory_manager
from models.product import Product

#from models.base_model import to_dict

products_bp = Blueprint('products', __name__, url_prefix='/api')

@products_bp.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """
    listing all products
    """
    inventory_manager = Inventory_manager()
    products = inventory_manager.read_all_products()
    serialized_products = [Product.serialize(product) for product in products]
    return jsonify(serialized_products), 200

@products_bp.route("/products/<id>", methods=['GET'], strict_slashes=False)
def get_product(id):
    """
     retrieves details about a specific product based on id
    """
    im = Inventory_manager()
    product = im.read_specific_product(id)

    serialized_products = {
            "id": product.id,
            "product_name": product.product_name,
            "description": product.description,
            "quantity": product.quantity,
            "price": product.price,
            "supplier_id": product.supplier_id,
            "supplier_name": product.supplier.business_name if product.supplier else None,
            "location_id": product.location_id
        }

    return jsonify(serialized_products)


@products_bp.route("/products", methods=['POST'], strict_slashes=False)
def post_product():
    """
    posts a product into the db
    """

    data = request.get_json()
    #print(data)

    if 'description' not in data or data['description'] is None:
            return jsonify("Description is missing or None"), 400

    product_name = data.get("product_name")
    description = data.get("description")
    quantity = data.get("quantity")
    price = data.get("price")
    print(description)

    im = Inventory_manager()
    
    new_product = im.add_product(product_name, quantity, price, description)
    return jsonify(new_product), 201
    



if __name__ == '__main__':
   debug=True