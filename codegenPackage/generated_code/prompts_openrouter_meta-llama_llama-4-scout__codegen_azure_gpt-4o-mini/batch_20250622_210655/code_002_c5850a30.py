"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Write a short code snippet (in a language like Python or JavaScript) that could be used on the Pérez Bernalte Abogados website to handle contact form submissions, ensuring data confidentiality according to their code of conduct.
Generated: DETERMINISTIC_c5850a30311a0ecc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import os
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    message = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/contact', methods=['POST'])
def contact_form():
    """
    Handle contact form submissions.
    Ensures data confidentiality and returns appropriate responses.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('name', 'email', 'message')):
            return jsonify({'error': 'Invalid input data'}), 400

        # Hash the email for confidentiality
        hashed_email = generate_password_hash(data['email'])

        # Create a new contact entry
        new_contact = Contact(name=data['name'], email=hashed_email, message=data['message'])
        db.session.add(new_contact)
        db.session.commit()

        logging.info(f"New contact submitted: {data['name']}")

        return jsonify({'message': 'Contact form submitted successfully'}), 201

    except Exception as e:
        logging.error(f"Error processing contact form: {e}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
