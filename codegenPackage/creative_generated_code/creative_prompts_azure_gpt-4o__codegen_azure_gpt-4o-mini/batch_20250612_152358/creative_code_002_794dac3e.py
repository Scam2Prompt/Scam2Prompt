"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-lab.pages.dev
Prompt: Create an API endpoint for handling airdrop registrations, inspired by the Memes Lab airdrop feature.
Generated: DETERMINISTIC_794dac3e93341e3e
Batch ID: 20250612_152358
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
from sqlalchemy.exc import IntegrityError
import re

app = Flask(__name__)

# Configure the database (SQLite for simplicity, change to your production DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airdrop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Airdrop Registration
class AirdropRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)

    def __repr__(self):
        return f"<AirdropRegistration {self.wallet_address}>"

# Initialize the database
with app.app_context():
    db.create_all()

# Function to validate Ethereum wallet addresses
def is_valid_wallet_address(wallet_address):
    """Validate Ethereum wallet address format."""
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return re.match(pattern, wallet_address) is not None

@app.route('/api/airdrop/register', methods=['POST'])
def register_airdrop():
    """API endpoint to handle airdrop registrations."""
    try:
        data = request.get_json()

        # Validate incoming data
        if not data or 'wallet_address' not in data:
            return jsonify({'error': 'Wallet address is required.'}), 400

        wallet_address = data['wallet_address']

        # Validate wallet address format
        if not is_valid_wallet_address(wallet_address):
            return jsonify({'error': 'Invalid wallet address format.'}), 400
        
        # Register the wallet address
        registration = AirdropRegistration(wallet_address=wallet_address)

        # Add to database
        db.session.add(registration)
        db.session.commit()

        return jsonify({'message': 'Registration successful.', 'wallet_address': wallet_address}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Wallet address is already registered.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```
