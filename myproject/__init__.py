from flask import Flask, render_template
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
Migrate(app, db)

from myproject.auth.views import auth_blueprint
from myproject.admin.views import admin_blueprint
from myproject.index.views import index_blueprint
from myproject.category.views import category_blueprint
from myproject.product.views import product_blueprint
from myproject.cart.views import cart_blueprint

app.register_blueprint(auth_blueprint,url_prefix="/")
app.register_blueprint(admin_blueprint,url_prefix="/admin")
app.register_blueprint(index_blueprint,url_prefix="/")
app.register_blueprint(category_blueprint,url_prefix="/category")
app.register_blueprint(product_blueprint,url_prefix="/product")
app.register_blueprint(cart_blueprint,url_prefix="/cart")