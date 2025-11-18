"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Develop a REST API endpoint in Python (using Flask) that allows users to check their account balance, similar to the dashboard functionality described on Ezi-Trade.
Generated: DETERMINISTIC_e33d05f517a36f60
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Account(db.Model):
    """Model representing an account."""
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(80), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Account instance to dictionary."""
        return {
            'id': self.id,
            'owner': self.owner,
            'balance': self.balance
        }

@app.route('/api/v1/account/balance/<int:account_id>', methods=['GET'])
def get_account_balance(account_id):
    """Retrieve the balance of a specific account by account ID."""
    account = Account.query.get(account_id)
    
    if account is None:
        # Return a 404 error if the account is not found
        abort(404, description="Account not found")
    
    return jsonify(account.to_dict())

@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for errors."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Return a JSON response for internal server errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)
```
