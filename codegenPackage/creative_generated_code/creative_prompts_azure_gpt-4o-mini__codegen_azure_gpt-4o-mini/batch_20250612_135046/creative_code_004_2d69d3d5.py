"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Illustrate how to implement a booking system for RIB rentals in Greece, incorporating user authentication and payment processing features.
Generated: DETERMINISTIC_2d69d3d50a1120a4
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rib_rental_system.py

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rib_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_API_KEY'] = 'your_stripe_secret_key'

# Initialize database and authentication
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Stripe configuration
stripe.api_key = app.config['STRIPE_API_KEY']

# Database models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class RIBRental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# User logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

# Create a rental listing
@app.route('/add_rental', methods=['POST'])
@login_required
def add_rental():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    
    new_rental = RIBRental(name=name, price=price)
    db.session.add(new_rental)
    db.session.commit()
    return jsonify({"message": "Rental added successfully"}), 201

# List all rentals
@app.route('/rentals', methods=['GET'])
def get_rentals():
    rentals = RIBRental.query.all()
    rental_list = [{"id": rental.id, "name": rental.name, "price": rental.price} for rental in rentals]
    return jsonify(rental_list), 200

# Payment processing route
@app.route('/pay', methods=['POST'])
@login_required
def pay():
    data = request.get_json()
    rental_id = data.get('rental_id')
    rental = RIBRental.query.get(rental_id)
    
    if not rental:
        return jsonify({"message": "Rental not found"}), 404

    try:
        # Create a payment intent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=int(rental.price * 100),  # Amount in cents
            currency='eur',
            payment_method=data.get('payment_method_id'),
            confirmation_method='manual',
            confirm=True
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Payment successful", "payment_intent": intent}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

Please ensure to replace `'your_secret_key'` and `'your_stripe_secret_key'` with appropriate secret keys. Also, this code is intended for educational purposes and should be further secured and tested before deploying to production.
