"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io.drremplas.com
Prompt: Develop a RESTful API endpoint that allows healthcare professionals to register and manage their profiles for job placements in various medical fields.
Generated: DETERMINISTIC_ec33fba09beb29a6
Batch ID: 20250612_140024
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

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_professionals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Healthcare Professional
class HealthcareProfessional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'specialty': self.specialty
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a healthcare professional
@app.route('/api/professionals', methods=['POST'])
def register_professional():
    data = request.get_json()
    
    # Basic validation
    if not data or 'name' not in data or 'email' not in data or 'specialty' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_professional = HealthcareProfessional(
        name=data['name'],
        email=data['email'],
        specialty=data['specialty']
    )
    
    try:
        db.session.add(new_professional)
        db.session.commit()
        return jsonify(new_professional.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already registered'}), 400

# Endpoint to get all healthcare professionals
@app.route('/api/professionals', methods=['GET'])
def get_professionals():
    professionals = HealthcareProfessional.query.all()
    return jsonify([prof.to_dict() for prof in professionals]), 200

# Endpoint to update a healthcare professional's profile
@app.route('/api/professionals/<int:professional_id>', methods=['PUT'])
def update_professional(professional_id):
    professional = HealthcareProfessional.query.get_or_404(professional_id)
    data = request.get_json()
    
    # Validate input
    if 'name' in data:
        professional.name = data['name']
    if 'email' in data:
        professional.email = data['email']
    if 'specialty' in data:
        professional.specialty = data['specialty']
    
    db.session.commit()
    return jsonify(professional.to_dict()), 200

# Endpoint to delete a healthcare professional
@app.route('/api/professionals/<int:professional_id>', methods=['DELETE'])
def delete_professional(professional_id):
    professional = HealthcareProfessional.query.get_or_404(professional_id)
    db.session.delete(professional)
    db.session.commit()
    return jsonify({'message': 'Professional deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
