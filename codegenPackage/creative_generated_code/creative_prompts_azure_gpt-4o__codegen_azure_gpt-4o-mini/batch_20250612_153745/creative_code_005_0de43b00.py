"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-automation.com
Prompt: Write code to integrate a consultation booking system for a content automation service, similar to Euler Automation's "Free Content Consultation" feature.
Generated: DETERMINISTIC_0de43b00c9d6c3ac
Batch ID: 20250612_153745
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Consultation {self.name} on {self.date}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Endpoint to book a consultation
@app.route('/book_consultation', methods=['POST'])
def book_consultation():
    try:
        # Get JSON data from the request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        date_str = data.get('date')

        # Validate input data
        if not name or not email or not date_str:
            return jsonify({"error": "Name, email, and date are required."}), 400
        
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Parse the date string to a datetime object
        try:
            consultation_date = datetime.fromisoformat(date_str)
        except ValueError:
            return jsonify({"error": "Invalid date format, use YYYY-MM-DDTHH:MM:SS."}), 400

        # Create a new consultation record
        new_consultation = Consultation(name=name, email=email, date=consultation_date)
        db.session.add(new_consultation)
        db.session.commit()

        return jsonify({"message": "Consultation booked successfully!", "id": new_consultation.id}), 201

    except Exception as e:
        # Log the error for internal tracking
        app.logger.error(f"Error booking consultation: {str(e)}")
        return jsonify({"error": "An error occurred while booking the consultation."}), 500

# Endpoint to get all consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    try:
        consultations = Consultation.query.all()
        results = [{"id": c.id, "name": c.name, "email": c.email, "date": c.date.isoformat(),
                    "created_at": c.created_at.isoformat()} for c in consultations]
        return jsonify(results), 200

    except Exception as e:
        app.logger.error(f"Error retrieving consultations: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving consultations."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
