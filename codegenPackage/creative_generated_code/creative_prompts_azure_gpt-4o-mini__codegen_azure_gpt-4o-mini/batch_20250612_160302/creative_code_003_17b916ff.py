"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.xyz
Prompt: How do I implement a domain purchase inquiry system that captures user details like on Idex.xyz?
Generated: DETERMINISTIC_17b916ffbff3859d
Batch ID: 20250612_160302
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    domain_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, domain_name, message):
        self.name = name
        self.email = email
        self.domain_name = domain_name
        self.message = message

# Create a schema for inquiries
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

# Route to capture domain inquiries
@app.route('/inquiry', methods=['POST'])
def create_inquiry():
    # Extract data from request
    data = request.get_json()

    # Validate incoming data
    name = data.get('name')
    email = data.get('email')
    domain_name = data.get('domain_name')
    message = data.get('message', '')

    if not name or not email or not domain_name:
        return jsonify({'error': 'Name, email, and domain name are required.'}), 400
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Create a new inquiry
    new_inquiry = Inquiry(name=name, email=email, domain_name=domain_name, message=message)

    try:
        db.session.add(new_inquiry)
        db.session.commit()
        return InquirySchema().dump(new_inquiry), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    inquiries = Inquiry.query.all()
    return InquirySchema(many=True).dump(inquiries), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to have Flask, Flask-SQLAlchemy, and Flask-Marshmallow installed in your environment to run this application:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```
