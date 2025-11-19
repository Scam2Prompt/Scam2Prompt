"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Create a sample API that allows users to book consultations for creative services, reflecting the user experience principles highlighted by Swell Creative Management.
Generated: DETERMINISTIC_21a49f66a020313e
Batch ID: 20250612_161235
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Consultation {self.name} for {self.service} at {self.date_time}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to book a consultation
@app.route('/book', methods=['POST'])
def book_consultation():
    """
    Book a new consultation by providing user details and service information.
    Expects JSON payload with name, email, service, and date_time.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not all(field in data for field in ['name', 'email', 'service', 'date_time']):
            return jsonify({'error': 'Missing data'}), 400
        
        # Parse date_time to ensure it's in the correct format
        date_time = datetime.fromisoformat(data['date_time'])

        # Create a new consultation instance
        consultation = Consultation(
            name=data['name'],
            email=data['email'],
            service=data['service'],
            date_time=date_time
        )

        # Add the consultation to the database
        db.session.add(consultation)
        db.session.commit()

        return jsonify({'message': 'Consultation booked successfully', 'id': consultation.id}), 201
    
    except ValueError as e:
        # Handle invalid date_time format
        return jsonify({'error': 'Invalid date_time format. Use ISO format.'}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

# Endpoint to list all consultations
@app.route('/consultations', methods=['GET'])
def list_consultations():
    """
    Retrieve a list of all booked consultations.
    Returns a JSON array of consultations with their details.
    """
    try:
        consultations = Consultation.query.all()
        return jsonify([{
            'id': c.id,
            'name': c.name,
            'email': c.email,
            'service': c.service,
            'date_time': c.date_time.isoformat()
        } for c in consultations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Set debug mode from environment variable
    debug_mode = os.getenv('DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)
```
