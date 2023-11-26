#!/usr/bin/env python3
from flask import Flask
from api.products import products_bp
from api.users import users_bp

app = Flask(__name__)

app.register_blueprint(products_bp)
app.register_blueprint(users_bp)