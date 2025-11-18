"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Write code to set up a scalable e-commerce platform using Smart Validation's e-commerce hosting solution. Include secure transaction handling and customizable shopping cart features.
Generated: DETERMINISTIC_2fc542d2af30d364
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configurations for the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Shopping cart model
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.Text, nullable=False)  # JSON string of items

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json['username']
        password = request.json['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({"message": "Login successful!"}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to log out a user
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

# Route to add items to the shopping cart
@app.route('/cart', methods=['POST'])
@login_required
def add_to_cart():
    try:
        item = request.json['item']  # Expecting item as a JSON object
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        
        if not cart:
            cart = Cart(user_id=current_user.id, items='[]')
            db.session.add(cart)

        # Load current items, append the new item, and save
        items = eval(cart.items)  # In production, use JSON
        items.append(item)
        cart.items = str(items)  # Save back as string

        db.session.commit()
        return jsonify({"message": "Item added to cart!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to view the shopping cart
@app.route('/cart', methods=['GET'])
@login_required
def view_cart():
    try:
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        return jsonify({"items": eval(cart.items) if cart else []}), 200  # Use JSON in production
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handling for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set up your environment variables and install the necessary packages (`Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `Flask-Login`, `Werkzeug`) before running the application.
