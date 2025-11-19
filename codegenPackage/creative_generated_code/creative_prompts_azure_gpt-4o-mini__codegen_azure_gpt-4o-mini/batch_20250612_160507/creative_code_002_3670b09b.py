"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.uk
Prompt: How can I create an API to handle inquiries for domain names like 1inch.uk, including fields for name, email, and offer amount?
Generated: DETERMINISTIC_3670b09b5a927fbd
Batch ID: 20250612_160507
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
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the domain inquiries
class DomainInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    offer_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.name} - {self.offer_amount}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to handle inquiries
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    # Validate incoming JSON payload
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input, JSON data required'}), 400

    name = data.get('name')
    email = data.get('email')
    offer_amount = data.get('offer_amount')

    # Validate required fields
    if not name or not email or offer_amount is None:
        return jsonify({'error': 'Name, email, and offer amount are required fields.'}), 400

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Create a new inquiry instance
    new_inquiry = DomainInquiry(name=name, email=email, offer_amount=offer_amount)

    try:
        # Add and commit the new inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Inquiry already exists or database error'}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
