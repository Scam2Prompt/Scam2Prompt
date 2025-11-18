"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Write code to create a fixed-price NFT sales platform with item limits and additional item fees, as outlined in the VIP Management pricing plans.
Generated: DETERMINISTIC_03d087da6cbc9f41
Batch ID: 20250612_151457
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
from web3 import Web3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFT items
class NFTItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_sold = db.Column(db.Boolean, default=False)

# Pricing plans for VIP Management
PRICING_PLANS = {
    'basic': {'item_limit': 5, 'additional_item_fee': 0.01},
    'premium': {'item_limit': 15, 'additional_item_fee': 0.005},
    'vip': {'item_limit': 30, 'additional_item_fee': 0.002}
}

# Endpoint to create a new NFT item
@app.route('/create_nft', methods=['POST'])
def create_nft():
    """
    Create a new NFT item for sale.
    Expects JSON payload with 'owner', 'price', and 'plan_type'.
    """
    try:
        data = request.json
        owner = data['owner']
        price = float(data['price'])
        plan_type = data['plan_type']
        
        if plan_type not in PRICING_PLANS:
            return jsonify({'error': 'Invalid plan type'}), 400

        item_limit = PRICING_PLANS[plan_type]['item_limit']

        # Check the current item count for the owner
        current_item_count = NFTItem.query.filter_by(owner=owner).count()

        if current_item_count >= item_limit:
            return jsonify({'error': 'Item limit reached'}), 403

        # Create a new NFT item
        new_nft = NFTItem(owner=owner, price=price)
        db.session.add(new_nft)
        db.session.commit()

        return jsonify({'message': 'NFT created successfully', 'nft_id': new_nft.id}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to purchase an NFT item
@app.route('/purchase_nft/<int:nft_id>', methods=['POST'])
def purchase_nft(nft_id):
    """
    Purchase an NFT item by its ID.
    Expects JSON payload with 'buyer' and 'payment_method'.
    """
    try:
        data = request.json
        buyer = data['buyer']
        payment_method = data['payment_method']

        # Find the NFT item
        nft_item = NFTItem.query.get(nft_id)

        if nft_item is None:
            return jsonify({'error': 'NFT item not found'}), 404

        if nft_item.is_sold:
            return jsonify({'error': 'NFT item already sold'}), 403

        # Here we would include logic for payment processing with the selected method
        web3 = Web3(Web3.HTTPProvider(os.environ.get('ETH_NODE_URL')))
        # Assuming payment processing is done using web3 and smart contracts
        # payment_success = web3.eth.sendTransaction({...})

        nft_item.is_sold = True
        db.session.commit()

        return jsonify({'message': 'Purchase successful', 'nft_id': nft_id}), 200

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Please ensure that you have set up the necessary environment variables (`DATABASE_URL`, `ETH_NODE_URL`) and installed the required libraries (`Flask`, `Flask-SQLAlchemy`, `web3`) to run this application.
