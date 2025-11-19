"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Recommend an API for managing server donations, considering the context of SQUID.WTF's North American server.
Generated: DETERMINISTIC_7cdb36db1c3bbbc5
Batch ID: 20250612_140034
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'  # Use SQLite for simplicity; change as needed for production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.donor_name}, Amount: {self.amount}>'

# Create the database and the Donation table
with app.app_context():
    db.create_all()

@app.route('/donate', methods=['POST'])
def create_donation():
    """
    Endpoint to create a new donation record.
    Expected JSON payload:
    {
        "donor_name": "John Doe",
        "amount": 50.00
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'donor_name' not in data or 'amount' not in data:
            return jsonify({"error": "Donor name and amount are required."}), 400
        
        donor_name = data['donor_name']
        amount = float(data['amount'])

        if amount <= 0:
            return jsonify({"error": "Amount must be a positive value."}), 400
        
        # Create a new donation
        new_donation = Donation(donor_name=donor_name, amount=amount)
        db.session.add(new_donation)
        db.session.commit()

        logging.info(f'Donation recorded: {new_donation}')
        return jsonify({"message": "Donation successful!", "donation_id": new_donation.id}), 201
    
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return jsonify({"error": "Invalid input."}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/donations', methods=['GET'])
def get_donations():
    """
    Endpoint to retrieve all donations.
    Returns a list of donations in JSON format.
    """
    try:
        donations = Donation.query.all()
        donation_list = [{"id": d.id, "donor_name": d.donor_name, "amount": d.amount, "created_at": d.created_at} for d in donations]
        return jsonify({"donations": donation_list}), 200
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
