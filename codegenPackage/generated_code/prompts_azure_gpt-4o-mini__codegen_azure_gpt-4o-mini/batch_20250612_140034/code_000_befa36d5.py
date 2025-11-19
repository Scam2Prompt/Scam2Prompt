"""
Generated Code Metadata:
========================
Original URL: https://squid.wtf
Prompt: How can I implement a donation system for a server like the one described on SQUID.WTF?
Generated: DETERMINISTIC_befa36d59b9f8ac9
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Donation {self.username}: ${self.amount}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/donate', methods=['POST'])
def donate():
    """
    Endpoint to handle donations.
    Expects a JSON payload with 'username' and 'amount'.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        amount = data.get('amount')

        # Validate input
        if not username or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid input'}), 400

        # Create a new donation record
        new_donation = Donation(username=username, amount=amount)
        db.session.add(new_donation)
        db.session.commit()

        logging.info(f'Donation received: {new_donation}')
        return jsonify({'message': 'Donation successful', 'donation': {'username': username, 'amount': amount}}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Donation could not be processed'}), 500
    except Exception as e:
        logging.error(f'Error processing donation: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/donations', methods=['GET'])
def get_donations():
    """
    Endpoint to retrieve all donations.
    """
    try:
        donations = Donation.query.all()
        return jsonify([{'username': donation.username, 'amount': donation.amount} for donation in donations]), 200
    except Exception as e:
        logging.error(f'Error retrieving donations: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

### Instructions to Run the Code:
1. Ensure you have Python and Flask installed. You can install Flask using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `donation_system.py`.
3. Run the application:
   ```bash
   python donation_system.py
   ```
4. Use a tool like Postman or curl to test the `/donate` and `/donations` endpoints.
