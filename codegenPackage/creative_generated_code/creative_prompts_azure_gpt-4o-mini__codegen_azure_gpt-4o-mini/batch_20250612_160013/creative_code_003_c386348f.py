"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Can you provide an example of an API that handles card activation and user ID management?
Generated: DETERMINISTIC_c386348fc2cf3a24
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Card
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    cards = db.relationship('Card', backref='user', lazy=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/activate_card', methods=['POST'])
def activate_card():
    """
    Activate a card for a user.
    Expects JSON with 'card_number' and 'user_id' fields.
    """
    data = request.get_json()

    try:
        card_number = data['card_number']
        user_id = data['user_id']
    except (KeyError, TypeError):
        raise BadRequest("Missing 'card_number' or 'user_id' in request data.")

    # Find the card and user
    card = Card.query.filter_by(card_number=card_number).first()
    user = User.query.get(user_id)

    # Error handling for card and user existence
    if card is None:
        raise NotFound("Card not found.")
    if user is None:
        raise NotFound("User not found.")

    # Activate the card if it is not already active
    if card.is_active:
        return jsonify({"message": "Card is already active."}), 400

    card.is_active = True
    card.user_id = user.id
    db.session.commit()

    return jsonify({"message": "Card activated successfully."}), 200

@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    Expects JSON with 'username'.
    """
    data = request.get_json()

    if 'username' not in data:
        raise BadRequest("Missing 'username' in request data.")

    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully.", "user_id": new_user.id}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
