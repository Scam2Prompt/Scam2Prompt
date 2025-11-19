"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greviufinance.co
Prompt: Describe how to set up a referral program using Greviufinance's commission structure in a web application.
Generated: DETERMINISTIC_19eb690d4554721f
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Referral model
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, nullable=False)
    referred_email = db.Column(db.String(120), unique=True, nullable=False)
    commission_earned = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Referral {self.referred_email}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new referral
@app.route('/referral', methods=['POST'])
def create_referral():
    data = request.get_json()
    
    # Validate incoming data
    if not data or 'referrer_id' not in data or 'referred_email' not in data:
        return jsonify({'error': 'Invalid data provided'}), 400

    new_referral = Referral(referrer_id=data['referrer_id'], referred_email=data['referred_email'])

    try:
        db.session.add(new_referral)
        db.session.commit()
        return jsonify({'message': 'Referral created successfully', 'referral': new_referral.referred_email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Referral with this email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to update commission for a referral
@app.route('/referral/<int:id>/commission', methods=['PATCH'])
def update_commission(id):
    data = request.get_json()

    if not data or 'commission_earned' not in data:
        return jsonify({'error': 'Invalid data provided'}), 400

    referral = Referral.query.get(id)
    if not referral:
        return jsonify({'error': 'Referral not found'}), 404

    referral.commission_earned += data['commission_earned']

    try:
        db.session.commit()
        return jsonify({'message': 'Commission updated successfully', 'commission': referral.commission_earned}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main block to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
