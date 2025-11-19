"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Create a sample API that allows users to book consultations for creative services, reflecting the user experience principles highlighted by Swell Creative Management.
Generated: DETERMINISTIC_21a49f66a020313e
Batch ID: 20250612_161235
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

# Initialize the database
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'service_type': self.service_type,
            'date_time': self.date_time.isoformat(),
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book a consultation
@app.route('/api/consultations', methods=['POST'])
def book_consultation():
    try:
        # Get data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'user_name' not in data or 'service_type' not in data or 'date_time' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new consultation
        consultation = Consultation(
            user_name=data['user_name'],
            service_type=data['service_type'],
            date_time=datetime.fromisoformat(data['date_time'])
        )

        # Add to the database
        db.session.add(consultation)
        db.session.commit()

        return jsonify(consultation.to_dict()), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all consultations
@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    try:
        consultations = Consultation.query.all()
        return jsonify([consultation.to_dict() for consultation in consultations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following installed:
- Flask
- Flask-SQLAlchemy

You can install them using pip:
```bash
pip install Flask Flask-SQLAlchemy
```

### Database Configuration
Make sure to set the `DATABASE_URL` environment variable for production use, or it will default to a SQLite database file named `consultations.db`.
