"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ttrumpwallet.com
Prompt: Write code to integrate a waitlist feature for a cryptocurrency wallet, similar to the $TRUMP Wallet waitlist, using Python and Flask.
Generated: DETERMINISTIC_d48ad9b404a6e110
Batch ID: 20250612_145114
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
import re

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waitlist.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Waitlist
class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Waitlist {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Route to join the waitlist
@app.route('/waitlist', methods=['POST'])
def join_waitlist():
    data = request.get_json()

    # Validate input
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    email = data['email'].strip()

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Check if the email is already in the waitlist
    existing_entry = Waitlist.query.filter_by(email=email).first()
    if existing_entry:
        return jsonify({'message': 'You are already on the waitlist'}), 200

    # Add to waitlist
    new_entry = Waitlist(email=email)

    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Successfully added to the waitlist'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'error': f'Could not add to waitlist: {str(e)}'}), 500

# Route to retrieve waitlist entries
@app.route('/waitlist', methods=['GET'])
def get_waitlist():
    try:
        waitlist_entries = Waitlist.query.all()
        result = [{'id': entry.id, 'email': entry.email, 'joined_at': entry.joined_at} for entry in waitlist_entries]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': f'Could not retrieve waitlist: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

This code implements a simple waitlist feature for a cryptocurrency wallet using Flask and SQLite. It includes routes to join the waitlist and retrieve waitlist entries, with proper validation, error handling, and comments.
