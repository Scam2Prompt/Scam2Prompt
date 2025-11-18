"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Create an API to calculate and display the consistency multiplier (1.2X volume) for wallets that transacted in at least six distinct months.
Generated: DETERMINISTIC_350d8c3575ac3645
Batch ID: 20250612_153648
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
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Wallet model
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Wallet {self.wallet_address}>'

# Create the database and the Wallet model if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to calculate the consistency multiplier
@app.route('/api/consistency_multiplier', methods=['GET'])
def calculate_consistency_multiplier():
    try:
        # Query for wallets that have transacted in at least six distinct months
        wallets = db.session.query(
            Wallet.wallet_address,
            db.func.strftime('%Y-%m', Wallet.transaction_date).label('transaction_month')
        ).distinct().group_by(Wallet.wallet_address, 'transaction_month').having(db.func.count(Wallet.transaction_date) >= 6).all()

        # Prepare a list of wallet addresses that meet the criteria
        qualifying_wallets = {wallet.wallet_address for wallet in wallets}

        # Calculate the consistency multiplier for each qualifying wallet
        multiplier = {wallet: "1.2X volume" for wallet in qualifying_wallets}

        # Return the result in JSON format
        return jsonify(multiplier), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500
    except Exception as ex:
        # Handle other potential errors
        return jsonify({"error": str(ex)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
