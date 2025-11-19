"""
Generated Code Metadata:
========================
Original URL: https://alicebeauty.bg
Prompt: Illustrate how to implement a promotional discount feature in a web application for Alice Beauty's gift cards and special offers.
Generated: DETERMINISTIC_942ff271102cf34e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid
import json

app = Flask(__name__)

# In-memory database for demonstration (replace with actual database in production)
promotions_db = {}
gift_cards_db = {}

class Promotion:
    def __init__(self, name, discount_percentage, start_date, end_date, applicable_products=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date
        self.applicable_products = applicable_products or []
        self.is_active = False

    def activate(self):
        current_date = datetime.now().date()
        if self.start_date <= current_date <= self.end_date:
            self.is_active = True
        return self.is_active

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'discount_percentage': self.discount_percentage,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'applicable_products': self.applicable_products,
            'is_active': self.is_active
        }

class GiftCard:
    def __init__(self, amount, expiry_date):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.expiry_date = expiry_date
        self.balance = amount
        self.is_active = True

    def apply_discount(self, cart_total):
        if not self.is_active or datetime.now().date() > self.expiry_date:
            return 0
        
        discount = min(self.balance, cart_total)
        self.balance -= discount
        if self.balance <= 0:
            self.is_active = False
        return discount

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'expiry_date': self.expiry_date.isoformat(),
            'balance': self.balance,
            'is_active': self.is_active
        }

@app.route('/api/promotions', methods=['POST'])
def create_promotion():
    try:
        data = request.get_json()
        required_fields = ['name', 'discount_percentage', 'start_date', 'end_date']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        promotion = Promotion(
            name=data['name'],
            discount_percentage=data['discount_percentage'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d').date(),
            applicable_products=data.get('applicable_products', [])
        )
        
        promotion.activate()
        promotions_db[promotion.id] = promotion
        
        return jsonify(promotion.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/promotions/<promotion_id>', methods=['GET'])
def get_promotion(promotion_id):
    try:
        if promotion_id not in promotions_db:
            return jsonify({'error': 'Promotion not found'}), 404
        
        promotion = promotions_db[promotion_id]
        return jsonify(promotion.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/giftcards', methods=['POST'])
def create_gift_card():
    try:
        data = request.get_json()
        required_fields = ['amount', 'expiry_date']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        gift_card = GiftCard(
            amount=data['amount'],
            expiry_date=datetime.strptime(data['expiry_date'], '%Y-%m-%d').date()
        )
        
        gift_cards_db[gift_card.id] = gift_card
        return jsonify(gift_card.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/giftcards/<gift_card_id>', methods=['GET'])
def get_gift_card(gift_card_id):
    try:
        if gift_card_id not in gift_cards_db:
            return jsonify({'error': 'Gift card not found'}), 404
        
        gift_card = gift_cards_db[gift_card_id]
        return jsonify(gift_card.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/checkout', methods=['POST'])
def checkout():
    try:
        data = request.get_json()
        required_fields = ['cart_items', 'total_amount']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        total_amount = float(data['total_amount'])
        final_amount = total_amount
        applied_promotions = []
        applied_gift_cards = []

        # Apply promotions
        for promotion_id in data.get('promotion_ids', []):
            if promotion_id in promotions_db:
                promotion = promotions_db[promotion_id]
                if promotion.is_active:
                    discount = total_amount * (promotion.discount_percentage / 100)
                    final_amount -= discount
                    applied_promotions.append({
                        'promotion_id': promotion_id,
                        'discount_amount': discount
                    })

        # Apply gift cards
        for gift_card_id in data.get('gift_card_ids', []):
            if gift_card_id in gift_cards_db:
                gift_card = gift_cards_db[gift_card_id]
                discount = gift_card.apply_discount(final_amount)
                final_amount -= discount
                applied_gift_cards.append({
                    'gift_card_id': gift_card_id,
                    'discount_amount': discount
                })

        return jsonify({
            'original_amount': total_amount,
            'final_amount': max(0, final_amount),
            'applied_promotions': applied_promotions,
            'applied_gift_cards': applied_gift_cards
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
