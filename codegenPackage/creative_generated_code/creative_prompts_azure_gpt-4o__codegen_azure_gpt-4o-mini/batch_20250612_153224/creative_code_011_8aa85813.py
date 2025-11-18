"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Suggest a framework for building an e-commerce platform to sell Ecoplast furniture, including features like dealer registration and customer login.
Generated: DETERMINISTIC_8aa85813e8953711
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_platform.py

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)

# Initialize the database
db = SQLAlchemy(app)

# Define the User model for customer and dealer registration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'customer' or 'dealer'

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for dealer registration
@app.route('/register/dealer', methods=['POST'])
def register_dealer():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_dealer = User(username=username, password=hashed_password, role='dealer')

    db.session.add(new_dealer)
    db.session.commit()

    return jsonify({'message': 'Dealer registered successfully!'}), 201

# Route for customer registration
@app.route('/register/customer', methods=['POST'])
def register_customer():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_customer = User(username=username, password=hashed_password, role='customer')

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': 'Customer registered successfully!'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['role'] = user.role
        return jsonify({'message': 'Login successful!', 'role': user.role}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully!'}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page not found!'}), 404

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
