"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: Create an API endpoint for a home remodeling service that allows users to book a free consultation and select design options, similar to the process outlined by Marble Classic.
Generated: DETERMINISTIC_ca02c8519cd07191
Batch ID: 20250612_155531
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///consultations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    design_option = db.Column(db.String(100), nullable=False)
    consultation_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/consultation', methods=['POST'])
def book_consultation():
    """
    API endpoint to book a free consultation.
    Expects JSON data with name, email, phone, design_option, and consultation_date.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'design_option', 'consultation_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Create a new consultation record
        consultation = Consultation(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            design_option=data['design_option'],
            consultation_date=datetime.fromisoformat(data['consultation_date'])
        )

        # Add the consultation to the database
        db.session.add(consultation)
        db.session.commit()

        return jsonify({'message': 'Consultation booked successfully!', 'consultation_id': consultation.id}), 201

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred while booking the consultation.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
