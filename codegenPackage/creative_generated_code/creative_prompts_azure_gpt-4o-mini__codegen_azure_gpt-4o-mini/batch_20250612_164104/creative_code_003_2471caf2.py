"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villachandon.com.br
Prompt: Create an API endpoint for a pet care application that allows users to submit and retrieve pet medical history.
Generated: DETERMINISTIC_2471caf2539291b9
Batch ID: 20250612_164104
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_care.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the PetMedicalHistory model
class PetMedicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    medical_condition = db.Column(db.String(200), nullable=False)
    treatment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert the model to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'pet_name': self.pet_name,
            'owner_name': self.owner_name,
            'medical_condition': self.medical_condition,
            'treatment': self.treatment,
            'date': self.date.isoformat()  # Convert date to ISO format
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/pet-medical-history', methods=['POST'])
def submit_medical_history():
    """Endpoint to submit a new pet medical history."""
    data = request.json

    # Validate incoming data
    required_fields = ['pet_name', 'owner_name', 'medical_condition', 'treatment', 'date']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Create a new PetMedicalHistory object
    new_history = PetMedicalHistory(
        pet_name=data['pet_name'],
        owner_name=data['owner_name'],
        medical_condition=data['medical_condition'],
        treatment=data['treatment'],
        date=data['date']
    )

    # Add the new entry to the database
    try:
        db.session.add(new_history)
        db.session.commit()
        return jsonify(new_history.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Could not save the medical history.'}), 500

@app.route('/api/pet-medical-history', methods=['GET'])
def get_medical_history():
    """Endpoint to retrieve all pet medical histories."""
    histories = PetMedicalHistory.query.all()
    return jsonify([history.to_dict() for history in histories]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
