"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Write Python code to create an online donation system for a non-profit organization, including features for tracking donations and generating financial reports, inspired by the "موقع جمع التبرعات" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_d52a4d089c2e0514
Batch ID: 20250612_153224
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

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Database model for Donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.donor_name}, Amount: {self.amount}>'

# Route to create a new donation
@app.route('/donate', methods=['POST'])
def create_donation():
    try:
        data = request.get_json()
        new_donation = Donation(
            donor_name=data['donor_name'],
            amount=data['amount']
        )
        db.session.add(new_donation)
        db.session.commit()
        return jsonify({'message': 'Donation recorded successfully!', 'id': new_donation.id}), 201
    except Exception as e:
        logging.error(f'Error while creating donation: {e}')
        return jsonify({'error': 'Failed to record donation.'}), 400

# Route to get all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    try:
        donations = Donation.query.all()
        return jsonify([{'id': donation.id, 'donor_name': donation.donor_name, 'amount': donation.amount, 'date': donation.date} for donation in donations]), 200
    except Exception as e:
        logging.error(f'Error while retrieving donations: {e}')
        return jsonify({'error': 'Failed to retrieve donations.'}), 500

# Route to generate financial report
@app.route('/report', methods=['GET'])
def generate_report():
    try:
        donations = Donation.query.all()
        total_donations = sum(donation.amount for donation in donations)
        report = {
            'total_donations': total_donations,
            'number_of_donations': len(donations),
            'donations': [{'donor_name': donation.donor_name, 'amount': donation.amount, 'date': donation.date} for donation in donations]
        }
        return jsonify(report), 200
    except Exception as e:
        logging.error(f'Error while generating report: {e}')
        return jsonify({'error': 'Failed to generate report.'}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
