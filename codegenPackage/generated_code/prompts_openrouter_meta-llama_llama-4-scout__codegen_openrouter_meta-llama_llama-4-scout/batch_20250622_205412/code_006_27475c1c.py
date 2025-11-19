"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Suggest libraries for building a web application that allows customers to order food online and make reservations, similar to Amici's website functionality.
Generated: DETERMINISTIC_27475c1c36248079
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Create a Flask application instance
app = Flask(__name__)
CORS(app)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_order.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Define models
class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)


class Menu(db.Model):
    """Menu model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Order(db.Model):
    """Order model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, menu_id, quantity):
        self.user_id = user_id
        self.menu_id = menu_id
        self.quantity = quantity


class Reservation(db.Model):
    """Reservation model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    party_size = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, date, time, party_size):
        self.user_id = user_id
        self.date = date
        self.time = time
        self.party_size = party_size


# Define schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order


class ReservationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reservation


# Create database tables
with app.app_context():
    db.create_all()


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        new_user = User(data['name'], data['email'], data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    try:
        if request.method == 'GET':
            menu_items = Menu.query.all()
            menu_schema = MenuSchema(many=True)
            return jsonify(menu_schema.dump(menu_items)), 200
        elif request.method == 'POST':
            data = request.json
            new_menu_item = Menu(data['name'], data['description'], data['price'])
            db.session.add(new_menu_item)
            db.session.commit()
            return jsonify({'message': 'Menu item created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/order', methods=['POST'])
def order():
    try:
        data = request.json
        new_order = Order(data['user_id'], data['menu_id'], data['quantity'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/reservation', methods=['POST'])
def reservation():
    try:
        data = request.json
        new_reservation = Reservation(data['user_id'], data['date'], data['time'], data['party_size'])
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({'message': 'Reservation created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
```
