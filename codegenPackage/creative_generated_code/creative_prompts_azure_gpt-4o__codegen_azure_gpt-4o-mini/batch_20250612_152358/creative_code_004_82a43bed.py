"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getfree.co.in
Prompt: Suggest tools or frameworks to build a referral tracking system for cryptocurrency faucets, referencing the referral and earning features mentioned on GetFree.co.in.
Generated: DETERMINISTIC_82a43bed15e4f333
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracking_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Referral
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False, unique=True)  # unique identifier for the user
    referral_code = db.Column(db.String, nullable=False, unique=True)  # unique referral code
    earnings = db.Column(db.Float, default=0.0)  # earnings from referrals

    def __repr__(self):
        return f"<Referral {self.user_id}, Code: {self.referral_code}, Earnings: {self.earnings}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new referral
@app.route('/referral', methods=['POST'])
def create_referral():
    data = request.get_json()
    
    if not data or 'user_id' not in data or 'referral_code' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'User ID and Referral Code are required.'}), 400
    
    new_referral = Referral(user_id=data['user_id'], referral_code=data['referral_code'])
    
    try:
        db.session.add(new_referral)
        db.session.commit()
        return jsonify({'message': 'Referral created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Conflict', 'message': 'User ID or Referral Code already exists.'}), 409

# Route to track earnings for a referral
@app.route('/referral/<referral_code>/earnings', methods=['GET'])
def get_earnings(referral_code):
    referral = Referral.query.filter_by(referral_code=referral_code).first()
    
    if not referral:
        return jsonify({'error': 'Not Found', 'message': 'Referral not found.'}), 404
    
    return jsonify({'user_id': referral.user_id, 'earnings': referral.earnings}), 200

# Route to update earnings for a referral
@app.route('/referral/<referral_code>/earnings', methods=['PUT'])
def update_earnings(referral_code):
    data = request.get_json()
    
    if not data or 'earnings' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Earnings value is required.'}), 400
    
    referral = Referral.query.filter_by(referral_code=referral_code).first()
    
    if not referral:
        return jsonify({'error': 'Not Found', 'message': 'Referral not found.'}), 404
    
    referral.earnings += data['earnings']  # Add to existing earnings
    
    try:
        db.session.commit()
        return jsonify({'message': 'Earnings updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
