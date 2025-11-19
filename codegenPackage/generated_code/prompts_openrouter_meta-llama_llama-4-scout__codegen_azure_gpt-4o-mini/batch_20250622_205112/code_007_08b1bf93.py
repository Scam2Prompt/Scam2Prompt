"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Propose an API endpoint for retrieving wallet net worth and provide a sample response based on Bluwhale's wallet insights data.
Generated: DETERMINISTIC_08b1bf93edb6eb34
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallets.db'  # Example database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Wallet
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'balance': self.balance
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/wallet/net-worth/<int:user_id>', methods=['GET'])
def get_wallet_net_worth(user_id):
    """
    API endpoint to retrieve the net worth of a user's wallet.
    
    Args:
        user_id (int): The ID of the user whose wallet net worth is to be retrieved.
    
    Returns:
        JSON response containing the user's wallet net worth or an error message.
    """
    try:
        # Query the wallet for the given user_id
        wallet = Wallet.query.filter_by(user_id=user_id).first()
        
        if wallet is None:
            return jsonify({'error': 'Wallet not found for the given user ID.'}), 404
        
        # Return the wallet balance as net worth
        return jsonify({
            'user_id': user_id,
            'net_worth': wallet.balance
        }), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Sample Response
```json
{
    "user_id": 1,
    "net_worth": 1500.75
}
```
