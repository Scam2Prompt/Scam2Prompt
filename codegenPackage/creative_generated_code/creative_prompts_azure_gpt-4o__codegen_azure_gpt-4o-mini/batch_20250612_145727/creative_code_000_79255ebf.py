"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Write code to implement a subscription-based user feed system where posts can be locked and unlocked upon payment, similar to the Lovr platform's functionality.
Generated: DETERMINISTIC_79255ebf966b2176
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import HTTPException

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    subscription_status = db.Column(db.Boolean, default=False)

# Model for Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    locked = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for Payments (for tracking payment information)
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e)), e.code

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data:
        abort(400, 'Username is required!')
    
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'content' not in data:
        abort(400, 'Post content is required!')
    
    new_post = Post(content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify({'id': new_post.id, 'content': new_post.content, 'locked': new_post.locked}), 201

# Endpoint to unlock a post (requires payment)
@app.route('/posts/<int:post_id>/unlock', methods=['POST'])
def unlock_post(post_id):
    user_id = request.json.get('user_id')
    payment_amount = request.json.get('amount', 10.0)

    # Validate user and payment
    user = User.query.get(user_id)
    if not user:
        abort(404, 'User not found!')

    # Assume payment processing is done here
    new_payment = Payment(user_id=user.id, amount=payment_amount)
    db.session.add(new_payment)

    post = Post.query.get(post_id)
    if not post:
        abort(404, 'Post not found!')

    # Unlock the post
    post.locked = False
    db.session.commit()

    return jsonify({'message': 'Post unlocked successfully!', 'post_id': post.id}), 200

# Endpoint to view a post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        abort(404, 'Post not found!')

    return jsonify({
        'id': post.id,
        'content': post.content,
        'locked': post.locked
    }), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
