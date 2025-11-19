"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancellationflights.com
Prompt: How can I create an API endpoint to handle account suspension requests in a RESTful service?
Generated: DETERMINISTIC_fe8281118e2876cc
Batch ID: 20250612_155259
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Account model
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    is_suspended = db.Column(db.Boolean, default=False)

# Account schema for serialization
class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/suspend_account/<int:account_id>', methods=['POST'])
def suspend_account(account_id):
    """
    Suspend an account by ID.

    :param account_id: ID of the account to suspend
    :return: JSON response with the updated account information or error message
    """
    # Fetch the account from the database
    account = Account.query.get(account_id)
    
    # Check if the account exists
    if account is None:
        raise NotFound(f"Account with ID {account_id} not found.")

    # Check if the account is already suspended
    if account.is_suspended:
        return jsonify({"message": "Account is already suspended."}), 400

    # Suspend the account
    account.is_suspended = True
    db.session.commit()

    # Return the updated account information
    account_schema = AccountSchema()
    return jsonify(account_schema.dump(account)), 200

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle NotFound exceptions."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle BadRequest exceptions."""
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
