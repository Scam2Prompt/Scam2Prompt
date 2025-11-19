"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atvisaabogados.com
Prompt: Develop a RESTful API endpoint that allows users to schedule consultations for immigration services, similar to the booking system described on AT Visa Abogados.
Generated: DETERMINISTIC_c51d18ac073c50d0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Consultation {self.id} - {self.name}>'

# Create database and tables
with app.app_context():
    db.create_all()

@app.route('/api/consultations', methods=['POST'])
def schedule_consultation():
    """
    Schedule a new consultation for immigration services.
    
    Request JSON structure:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "date": "2023-10-01T10:00:00",
        "service_type": "Visa Application"
    }
    """
    data = request.get_json()

    # Validate request data
    if not data or not all(key in data for key in ('name', 'email', 'date', 'service_type')):
        abort(400, description="Missing required fields: name, email, date, service_type")

    # Parse date and validate format
    try:
        consultation_date = datetime.fromisoformat(data['date'])
    except ValueError:
        abort(400, description="Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)")

    # Check for existing consultations at the same time
    existing_consultation = Consultation.query.filter_by(date=consultation_date).first()
    if existing_consultation:
        abort(409, description="A consultation is already scheduled at this time.")

    # Create a new consultation
    new_consultation = Consultation(
        name=data['name'],
        email=data['email'],
        date=consultation_date,
        service_type=data['service_type']
    )

    # Add to the session and commit to the database
    db.session.add(new_consultation)
    db.session.commit()

    # Return the created consultation
    return jsonify({"id": new_consultation.id, "message": "Consultation scheduled successfully."}), 201

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(409)
def conflict(error):
    return jsonify({"error": str(error)}), 409

@app.errorhandler(Exception)
def handle_exception(error):
    """Generic error handler for unexpected errors."""
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=os.getenv('DEBUG', 'True') == 'True')
```
