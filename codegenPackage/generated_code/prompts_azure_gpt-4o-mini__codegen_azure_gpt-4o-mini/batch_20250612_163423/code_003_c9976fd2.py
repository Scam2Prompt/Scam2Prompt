"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Develop a RESTful API endpoint for a personal injury law firm that allows clients to submit details about their accidents, including types like truck accidents and slip and fall incidents.
Generated: DETERMINISTIC_c9976fd25e52b6de
Batch ID: 20250612_163423
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Accident model
class Accident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accident_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class AccidentSchema(Schema):
    accident_type = fields.String(required=True)
    description = fields.String(required=True)

# Initialize the schema
accident_schema = AccidentSchema()

@app.route('/api/accidents', methods=['POST'])
def submit_accident():
    """
    Endpoint to submit accident details.
    Expects a JSON payload with accident_type and description.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = accident_schema.load(data)

        # Create a new Accident instance
        new_accident = Accident(
            accident_type=validated_data['accident_type'],
            description=validated_data['description']
        )

        # Add the new accident to the database
        db.session.add(new_accident)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Accident submitted successfully", "id": new_accident.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
