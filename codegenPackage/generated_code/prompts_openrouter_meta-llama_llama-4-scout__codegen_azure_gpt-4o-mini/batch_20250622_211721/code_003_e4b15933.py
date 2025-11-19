"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Design a RESTful API for a Simon's Cat e-commerce platform, including endpoints for product listings, shopping cart management, and user rewards.
Generated: DETERMINISTIC_e4b1593391608116
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simons_cat_ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    products = db.relationship('Product', secondary='cart_product', lazy='subquery')

class CartProduct(db.Model):
    __tablename__ = 'cart_product'
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

class UserReward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, default=0)

# Schemas for serialization
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

class CartSchema(Schema):
    id = fields.Int()
    user_id = fields.Int(required=True)
    products = fields.List(fields.Int())

class UserRewardSchema(Schema):
    id = fields.Int()
    user_id = fields.Int(required=True)
    points = fields.Int()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Endpoint to add a product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        product_data = request.json
        product_schema = ProductSchema()
        product = product_schema.load(product_data)
        new_product = Product(**product)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to manage shopping cart
@app.route('/cart/<int:user_id>', methods=['GET', 'POST'])
def manage_cart(user_id):
    if request.method == 'GET':
        cart = Cart.query.filter_by(user_id=user_id).first()
        cart_schema = CartSchema()
        return jsonify(cart_schema.dump(cart)), 200 if cart else 404

    if request.method == 'POST':
        cart_data = request.json
        cart_schema = CartSchema()
        try:
            cart = cart_schema.load(cart_data)
            new_cart = Cart(user_id=user_id)
            db.session.add(new_cart)
            db.session.commit()
            return jsonify(cart_schema.dump(new_cart)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Endpoint to manage user rewards
@app.route('/rewards/<int:user_id>', methods=['GET', 'POST'])
def manage_rewards(user_id):
    if request.method == 'GET':
        reward = UserReward.query.filter_by(user_id=user_id).first()
        reward_schema = UserRewardSchema()
        return jsonify(reward_schema.dump(reward)), 200 if reward else 404

    if request.method == 'POST':
        reward_data = request.json
        reward_schema = UserRewardSchema()
        try:
            reward = reward_schema.load(reward_data)
            new_reward = UserReward(user_id=user_id, points=reward['points'])
            db.session.add(new_reward)
            db.session.commit()
            return jsonify(reward_schema.dump(new_reward)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
