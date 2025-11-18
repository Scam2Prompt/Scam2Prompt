"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Develop an API that allows users to transfer funds instantly to other users, as described in the Hyiprio money transfer feature.
Generated: DETERMINISTIC_7b94a72a359005e0
Batch ID: 20250612_150345
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing a User in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to handle fund transfers between users
@app.route('/transfer', methods=['POST'])
def transfer_funds():
    data = request.get_json()

    # Validate request data
    if not data or 'from_user' not in data or 'to_user' not in data or 'amount' not in data:
        raise BadRequest("Invalid request data. 'from_user', 'to_user', and 'amount' are required.")

    from_user = data['from_user']
    to_user = data['to_user']
    amount = data['amount']

    # Check for valid amount
    if amount <= 0:
        raise BadRequest("Transfer amount must be greater than zero.")

    # Lookup users in the database
    sender = User.query.filter_by(username=from_user).first()
    receiver = User.query.filter_by(username=to_user).first()

    # Verify sender and receiver exist
    if not sender:
        raise NotFound(f"User '{from_user}' not found.")
    if not receiver:
        raise NotFound(f"User '{to_user}' not found.")

    # Ensure sender has sufficient balance
    if sender.balance < amount:
        raise BadRequest("Insufficient funds for transfer.")

    # Perform the transfer
    try:
        sender.balance -= amount
        receiver.balance += amount
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest("An error occurred while processing the transfer.")

    return jsonify({
        "message": "Transfer successful",
        "from_user": sender.username,
        "to_user": receiver.username,
        "amount": amount,
        "new_balance": sender.balance
    }), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
