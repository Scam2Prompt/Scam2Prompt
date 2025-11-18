"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Write code to implement a pay-to-unlock post system for a subscription-based social media platform, similar to Fansliebe's locked posts feature.
Generated: DETERMINISTIC_376a98caa2820777
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_media.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Model for Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_locked = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for Transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/posts', methods=['POST'])
def create_post():
    """Create a new post."""
    data = request.json
    if not data or not all(k in data for k in ("content", "price")):
        abort(400, description="Invalid post data.")
    
    new_post = Post(content=data['content'], price=data['price'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created", "post_id": new_post.id}), 201

@app.route('/posts/<int:post_id>/unlock', methods=['POST'])
def unlock_post(post_id):
    """Unlock a post for a user."""
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        abort(400, description="User ID is required.")
    
    user = User.query.get(user_id)
    post = Post.query.get(post_id)

    if not user or not post:
        abort(404, description="User or Post not found.")
    
    if not post.is_locked:
        return jsonify({"message": "Post is already unlocked."}), 200

    if user.balance < post.price:
        abort(403, description="Insufficient balance.")

    # Deduct the price from user's balance
    user.balance -= post.price
    post.is_locked = False

    # Record the transaction
    transaction = Transaction(user_id=user_id, post_id=post_id, amount=post.price)
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Post unlocked.", "post_content": post.content}), 200

@app.route('/users/<int:user_id>/balance', methods=['GET'])
def get_balance(user_id):
    """Get the balance of a user."""
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found.")
    return jsonify({"user_id": user_id, "balance": user.balance}), 200

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    if not data or 'username' not in data:
        abort(400, description="Invalid user data.")

    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
