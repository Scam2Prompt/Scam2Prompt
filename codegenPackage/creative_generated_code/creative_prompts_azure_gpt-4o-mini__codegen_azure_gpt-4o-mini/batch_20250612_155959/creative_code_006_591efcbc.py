"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: How can I implement a pay-to-unlock post feature for a social media platform, taking inspiration from Lovr's advanced feed system?
Generated: DETERMINISTIC_591efcbc4498a0bb
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os

# Initialize Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')  # Set your Stripe secret key

db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    balance = db.Column(db.Float, default=0.0)  # User balance for unlocking posts

# Post model for the database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)  # Price to unlock the post
    unlocked_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # User who unlocked the post

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(
        username=data['username'],
        password=generate_password_hash(data['password'])
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid username or password!"}), 401

# Endpoint to create a post
@app.route('/post', methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized access!"}), 401

    data = request.json
    new_post = Post(content=data['content'], price=data['price'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!"}), 201

# Endpoint to unlock a post
@app.route('/unlock/<int:post_id>', methods=['POST'])
def unlock_post(post_id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized access!"}), 401

    user = User.query.get(session['user_id'])
    post = Post.query.get(post_id)

    if post is None:
        return jsonify({"message": "Post not found!"}), 404

    if user.balance < post.price:
        return jsonify({"message": "Insufficient balance!"}), 403

    # Simulating a payment processing with Stripe (assumed to be handled elsewhere)
    try:
        user.balance -= post.price  # Deduct the amount from user balance
        post.unlocked_by = user.id
        db.session.commit()
        return jsonify({"message": "Post unlocked successfully!"}), 200
    except Exception as e:
        db.session.rollback()  # Rollback on error
        return jsonify({"message": "Error unlocking post.", "error": str(e)}), 500

# Endpoint to add funds to user balance (mock example)
@app.route('/add_funds', methods=['POST'])
def add_funds():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized access!"}), 401

    data = request.json
    user = User.query.get(session['user_id'])
    user.balance += data['amount']
    db.session.commit()
    return jsonify({"message": "Funds added successfully!", "new_balance": user.balance}), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask application
``` 

Make sure to install Flask and SQLAlchemy by running:
```bash
pip install Flask Flask-SQLAlchemy stripe
``` 

Also, set up the `STRIPE_SECRET_KEY` environment variable to your actual Stripe secret key for payment processing.
