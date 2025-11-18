"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin.pages.dev
Prompt: Suggest tools or frameworks to build a platform where users can earn cryptocurrency rewards based on social media engagement, like the Gaimin-Portal's $GMRX reward system.
Generated: DETERMINISTIC_a8a3e80361079724
Batch ID: 20250612_152656
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
from sqlalchemy.exc import IntegrityError
import bcrypt
import jwt
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for JWT
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    rewards = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Database model for Engagement
class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    points = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('engagements', lazy=True))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password').encode('utf-8')

    # Hash the password
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    # Create new user
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists!'}), 409

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password').encode('utf-8')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

# Endpoint to add engagement points
@app.route('/engagement', methods=['POST'])
def add_engagement():
    data = request.get_json()
    token = request.headers.get('Authorization').split(" ")[1]

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user_id = decoded['user_id']

        points = data.get('points')
        engagement = Engagement(user_id=user_id, points=points)
        db.session.add(engagement)

        # Update the user's rewards
        user = User.query.get(user_id)
        user.rewards += points
        db.session.commit()

        return jsonify({'message': 'Engagement recorded and rewards updated!'}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!'}), 401

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
