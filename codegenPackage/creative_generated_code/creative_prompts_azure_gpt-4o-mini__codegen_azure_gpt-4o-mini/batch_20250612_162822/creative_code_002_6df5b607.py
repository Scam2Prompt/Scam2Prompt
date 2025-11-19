"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Create a RESTful API endpoint that allows users to submit inquiries for construction services, ensuring it includes fields for service type, name, email, and phone, as outlined by ExpertStroy's consultation form.
Generated: DETERMINISTIC_6df5b6079d1d9eb0
Batch ID: 20250612_162822
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
from marshmallow import ValidationError
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Create the Inquiry schema
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Create the database and tables
with app.app_context():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# API endpoint to submit inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        service_type = data.get('service_type')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not all([service_type, name, email, phone]):
            return jsonify({'error': 'All fields are required.'}), 400

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Create a new Inquiry instance
        new_inquiry = Inquiry(
            service_type=service_type,
            name=name,
            email=email,
            phone=phone
        )

        # Add to session and commit to database
        db.session.add(new_inquiry)
        db.session.commit()

        # Return the created inquiry as a response
        inquiry_schema = InquirySchema()
        return inquiry_schema.jsonify(new_inquiry), 201

    except ValidationError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
