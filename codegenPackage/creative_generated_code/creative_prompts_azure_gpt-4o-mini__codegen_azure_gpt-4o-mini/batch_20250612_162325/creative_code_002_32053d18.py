"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create an API endpoint that allows clients to submit their cosmetic formulation requests, ensuring compliance with the quality management practices highlighted by Fabricare Cosmeticos.
Generated: DETERMINISTIC_32053d184f40b58f
Batch ID: 20250612_162325
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formulations.db'  # Change to your production DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Formulation model
class Formulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    compliance_notes = db.Column(db.String(255), nullable=True)

# Create a schema for validating input data
class FormulationSchema(Schema):
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    compliance_notes = fields.Str(missing=None)

# Initialize the schema
formulation_schema = FormulationSchema()

@app.route('/api/formulations', methods=['POST'])
def submit_formulation():
    """
    API endpoint to submit a cosmetic formulation request.
    
    Expects a JSON payload with:
    - name: The name of the formulation
    - ingredients: The list of ingredients
    - compliance_notes: Any additional compliance notes (optional)
    
    Returns:
    - 201 Created on success
    - 400 Bad Request if validation fails
    - 500 Internal Server Error for unexpected errors
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = formulation_schema.load(data)

        # Create a new formulation record
        new_formulation = Formulation(
            name=validated_data['name'],
            ingredients=validated_data['ingredients'],
            compliance_notes=validated_data.get('compliance_notes')
        )

        # Add the formulation to the session and commit
        db.session.add(new_formulation)
        db.session.commit()

        # Log the creation of a new formulation
        logging.info(f"New formulation submitted: {new_formulation.name}")

        return jsonify({'message': 'Formulation submitted successfully!'}), 201

    except ValidationError as err:
        # Return validation errors
        logging.warning(f"Validation error: {err.messages}")
        return jsonify({'errors': err.messages}), 400

    except Exception as e:
        # Log unexpected errors
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'An internal error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```
