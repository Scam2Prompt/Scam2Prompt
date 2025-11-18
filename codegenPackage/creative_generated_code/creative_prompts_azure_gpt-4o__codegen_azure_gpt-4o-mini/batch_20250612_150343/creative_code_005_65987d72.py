"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Suggest an API for integrating a contact form that allows users to submit their details for consultation or free measurements, as highlighted on the webpage.
Generated: DETERMINISTIC_65987d723f54e572
Batch ID: 20250612_150343
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
from flask_marshmallow import Marshmallow
import re
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

# Contact schema
class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """
    API endpoint to submit contact details for consultation or free measurements.
    Expects a JSON payload with name, email, phone, and message.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate required fields
        if not data or not all(key in data for key in ("name", "email", "message")):
            return jsonify({"error": "Missing required fields"}), 400

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        # Create a new contact
        new_contact = Contact(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),  # Optional
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()

        # Serialize the response
        contact_schema = ContactSchema()
        return contact_schema.jsonify(new_contact), 201

    except Exception as e:
        # Log the exception (would normally log to a file or monitoring system)
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
