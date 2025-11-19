"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optionroom.finance
Prompt: Outline a RESTful API design for an online betting service that includes user account management and game selection, based on the services provided by HUBET.
Generated: DETERMINISTIC_b8407da03a8d2bc7
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from functools import wraps
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Game model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    odds = db.Column(db.Float, nullable=False)

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Game Schema
class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Decorator for token verification (Sample implementation)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Here you would normally check for a token in headers
        # For simplicity, we will assume the user is authenticated
        return f(*args, **kwargs)
    return decorated

# User Registration
@app.route('/api/users', methods=['POST'])
def register_user():
    username = request.json.get('username')
    password = request.json.get('password')

    # Basic validation
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return UserSchema().dump(new_user), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "User registration failed", "error": str(e)}), 500

# User Login (Sample implementation)
@app.route('/api/login', methods=['POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        # Generate a token here (omitted for simplicity)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Get all games
@app.route('/api/games', methods=['GET'])
@token_required
def get_games():
    games = Game.query.all()
    return GameSchema(many=True).dump(games), 200

# Add a new game (Admin-only functionality)
@app.route('/api/games', methods=['POST'])
@token_required
def add_game():
    name = request.json.get('name')
    odds = request.json.get('odds')

    # Basic validation
    if not name or odds is None:
        return jsonify({"message": "Game name and odds are required"}), 400

    new_game = Game(name=name, odds=odds)

    try:
        db.session.add(new_game)
        db.session.commit()
        return GameSchema().dump(new_game), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Game creation failed", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
