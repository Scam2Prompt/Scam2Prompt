"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Create a REST API for managing user accounts in a crypto casino, including features for registration, deposits, withdrawals, and bonus activation.
Generated: DETERMINISTIC_015ae6e37ab43c23
Batch ID: 20250612_154307
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
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

# Initialize app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'  # Change to your preferred database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    bonuses_active = db.Column(db.Boolean, default=False)

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists."}), 409

    return jsonify({"message": "User created successfully."}), 201

# Route for user deposits
@app.route('/deposit', methods=['POST'])
def deposit():
    """Deposit funds into the user account."""
    user_id = request.json.get('user_id')
    amount = request.json.get('amount')

    if amount <= 0:
        return jsonify({"error": "Deposit amount must be greater than zero."}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    user.balance += amount
    db.session.commit()

    return jsonify({"message": "Deposit successful.", "new_balance": user.balance}), 200

# Route for user withdrawals
@app.route('/withdraw', methods=['POST'])
def withdraw():
    """Withdraw funds from the user account."""
    user_id = request.json.get('user_id')
    amount = request.json.get('amount')

    if amount <= 0:
        return jsonify({"error": "Withdrawal amount must be greater than zero."}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    if amount > user.balance:
        return jsonify({"error": "Insufficient funds."}), 400

    user.balance -= amount
    db.session.commit()

    return jsonify({"message": "Withdrawal successful.", "new_balance": user.balance}), 200

# Route for toggling bonus activation
@app.route('/activate_bonus', methods=['POST'])
def activate_bonus():
    """Activate bonuses for the user."""
    user_id = request.json.get('user_id')
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    user.bonuses_active = not user.bonuses_active
    db.session.commit()

    return jsonify({"message": "Bonus activation toggled.", "bonuses_active": user.bonuses_active}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure you have the required packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Werkzeug
```
