"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chayatime.com
Prompt: Suggest an API to integrate a "Franchise Inquiry" form into the ChayaTime website, allowing users to submit their details directly.
Generated: DETERMINISTIC_61973d03bee641b3
Batch ID: 20250612_153246
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
from sqlalchemy.exc import IntegrityError
import os

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///franchise_inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the FranchiseInquiry model to store inquiries
class FranchiseInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<FranchiseInquiry {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit a franchise inquiry
@app.route('/api/franchise-inquiry', methods=['POST'])
def submit_inquiry():
    # Validate incoming JSON data
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Extract data from the request
    name = data['name']
    email = data['email']
    phone = data['phone']
    message = data.get('message', '')

    # Create a new inquiry instance
    new_inquiry = FranchiseInquiry(name=name, email=email, phone=phone, message=message)

    # Attempt to save the inquiry to the database
    try:
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry submitted successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Inquiry with this email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```
