"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create an API endpoint that allows clients to submit their cosmetic formulation requests, ensuring compliance with the quality management practices highlighted by Fabricare Cosmeticos.
Generated: DETERMINISTIC_32053d184f40b58f
Batch ID: 20250612_162325
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formulations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for cosmetic formulations
class Formulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    compliance_notes = db.Column(db.Text, nullable=True)

# Schema for validating incoming requests
class FormulationSchema(Schema):
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    compliance_notes = fields.Str(required=False)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to submit cosmetic formulation requests
@app.route('/api/formulations', methods=['POST'])
def submit_formulation():
    # Parse and validate incoming JSON data
    schema = FormulationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "details": err.messages}), 400

    # Create a new formulation entry
    new_formulation = Formulation(
        name=data['name'],
        ingredients=data['ingredients'],
        compliance_notes=data.get('compliance_notes')
    )

    # Add to the database and commit
    try:
        db.session.add(new_formulation)
        db.session.commit()
        logging.info(f"New formulation submitted: {new_formulation.name}")
        return jsonify({"message": "Formulation submitted successfully", "id": new_formulation.id}), 201
    except Exception as e:
        logging.error(f"Database error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Failed to submit formulation"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
