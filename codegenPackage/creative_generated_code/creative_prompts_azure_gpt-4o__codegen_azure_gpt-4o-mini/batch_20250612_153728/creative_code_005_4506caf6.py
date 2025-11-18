"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Create a REST API for managing architectural consulting services, including endpoints for booking consultations and showcasing expertise, as described on Celestia's site.
Generated: DETERMINISTIC_4506caf626015778
Batch ID: 20250612_153728
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

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for Consultation
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.String(50), nullable=False)
    expertise = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Consultation {self.client_name} on {self.date_time}>'

# Endpoint to book a consultation
@app.route('/consultations', methods=['POST'])
def book_consultation():
    """Book a new consultation."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('client_name', 'email', 'date_time', 'expertise')):
        return jsonify({"error": "Missing required fields"}), 400

    # Create a new consultation entry
    new_consultation = Consultation(
        client_name=data['client_name'],
        email=data['email'],
        date_time=data['date_time'],
        expertise=data['expertise']
    )

    try:
        db.session.add(new_consultation)
        db.session.commit()
        return jsonify({"message": "Consultation booked successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "An error occurred while booking the consultation"}), 500

# Endpoint to showcase expertise
@app.route('/expertise', methods=['GET'])
def showcase_expertise():
    """Showcase available expertise."""
    expertise_list = [
        {"field": "Urban Design", "description": "Creating sustainable urban spaces."},
        {"field": "Environmental Planning", "description": "Integrating environmental considerations into planning."},
        {"field": "Building Architecture", "description": "Designing functional and aesthetically pleasing buildings."},
        # Add more expertise fields as needed
    ]
    return jsonify(expertise_list), 200

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
