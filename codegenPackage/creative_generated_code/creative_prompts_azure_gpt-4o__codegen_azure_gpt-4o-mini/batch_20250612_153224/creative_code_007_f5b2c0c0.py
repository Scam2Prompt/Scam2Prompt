"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.greenaapples.com
Prompt: Suggest an API for implementing a virtual consultation system that provides advice on therapies like "De-addiction Therapy," "Anger Management," and "Anxiety Management," based on the Green Apples e-Rx Clinic's services.
Generated: DETERMINISTIC_f5b2c0c032ab8cca
Batch ID: 20250612_153224
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Consultation Model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    therapy_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, therapy_type, description):
        self.therapy_type = therapy_type
        self.description = description

# Schema for serializing consultation data
class ConsultationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Consultation

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    consultations = Consultation.query.all()
    consultation_schema = ConsultationSchema(many=True)
    return jsonify(consultation_schema.dump(consultations)), 200

# Endpoint to create a new consultation
@app.route('/consultations', methods=['POST'])
def add_consultation():
    try:
        # Extract data from request
        data = request.get_json()
        therapy_type = data.get('therapy_type')
        description = data.get('description')

        # Validate input
        if not therapy_type or not description:
            raise BadRequest("Therapy type and description are required.")

        # Create a new consultation entry
        new_consultation = Consultation(therapy_type, description)
        db.session.add(new_consultation)
        db.session.commit()

        consultation_schema = ConsultationSchema()
        return jsonify(consultation_schema.dump(new_consultation)), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific consultation by ID
@app.route('/consultations/<int:id>', methods=['GET'])
def get_consultation(id):
    consultation = Consultation.query.get(id)
    if not consultation:
        raise NotFound("Consultation not found.")
    
    consultation_schema = ConsultationSchema()
    return jsonify(consultation_schema.dump(consultation)), 200

# Endpoint to update a specific consultation by ID
@app.route('/consultations/<int:id>', methods=['PUT'])
def update_consultation(id):
    consultation = Consultation.query.get(id)
    if not consultation:
        raise NotFound("Consultation not found.")
    
    data = request.get_json()
    consultation.therapy_type = data.get('therapy_type', consultation.therapy_type)
    consultation.description = data.get('description', consultation.description)
    
    db.session.commit()
    consultation_schema = ConsultationSchema()
    return jsonify(consultation_schema.dump(consultation)), 200

# Endpoint to delete a specific consultation by ID
@app.route('/consultations/<int:id>', methods=['DELETE'])
def delete_consultation(id):
    consultation = Consultation.query.get(id)
    if not consultation:
        raise NotFound("Consultation not found.")
    
    db.session.delete(consultation)
    db.session.commit()
    return jsonify({"message": "Consultation deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
