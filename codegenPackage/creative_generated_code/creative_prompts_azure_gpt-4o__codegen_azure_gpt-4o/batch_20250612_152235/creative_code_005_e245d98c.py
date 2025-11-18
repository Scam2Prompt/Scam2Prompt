"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Suggest a library or framework to implement referral systems for a sports betting platform, similar to the "Powered by Referral" feature on CoChilli SportsBook.
Generated: DETERMINISTIC_e245d98c5e38860f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation using Python with the Flask framework and SQLAlchemy for database handling to create a referral system. This code includes comments and best practices.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Referral model
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.String(50), nullable=False)
    referred_id = db.Column(db.String(50), unique=True, nullable=False)
    reward = db.Column(db.String(50), nullable=False)  # Example: 'Bonus Points'

    def __repr__(self):
        return f"<Referral(referrer_id={self.referrer_id}, referred_id={self.referred_id}, reward={self.reward})>"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a referral
@app.route('/create-referral', methods=['POST'])
def create_referral():
    """
    Create a referral entry in the database.
    Expected JSON payload:
    {
        "referrer_id": "user123",
        "referred_id": "user456"
    }
    """
    data = request.json
    referrer_id = data.get('referrer_id')
    referred_id = data.get('referred_id')

    if not referrer_id or not referred_id:
        return jsonify({"error": "referrer_id and referred_id are required"}), 400

    # Create referral object with reward logic
    reward = "Bonus Points"  # Example reward logic
    referral = Referral(referrer_id=referrer_id, referred_id=referred_id, reward=reward)

    try:
        db.session.add(referral)
        db.session.commit()
        return jsonify({"message": "Referral created successfully", "referral": {
            "referrer_id": referrer_id,
            "referred_id": referred_id,
            "reward": reward
        }}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": f"Referred ID '{referred_id}' already exists"}), 409

# Endpoint to get all referrals for a referrer
@app.route('/get-referrals/<referrer_id>', methods=['GET'])
def get_referrals(referrer_id):
    """
    Get all referrals for a given referrer ID.
    """
    referrals = Referral.query.filter_by(referrer_id=referrer_id).all()
    return jsonify({"referrals": [
        {"referrer_id": r.referrer_id, "referred_id": r.referred_id, "reward": r.reward}
        for r in referrals
    ]})

# Error handler for generic 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `sqlite:///referrals.db` with your production-ready database URI (e.g., a PostgreSQL or MySQL connection string).
2. The referral reward logic (`reward = "Bonus Points"`) should be updated to match your business requirements.
3. Error handling for edge cases is included (e.g., duplicate `referred_id` or missing required fields).
