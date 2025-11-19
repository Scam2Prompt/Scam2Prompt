"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Generate a code snippet for a web application that allows users to request personalized lighting solutions in Puerto Montt, incorporating energy-efficient technologies.
Generated: DETERMINISTIC_fd37a3a2846f7561
Batch ID: 20250612_155916
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

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lighting_solutions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for lighting solutions requests
class LightingSolutionRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    preferences = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Schema for validating requests
class LightingSolutionRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    location = fields.Str(required=True)
    preferences = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for submitting a lighting solution request
@app.route('/request-lighting-solution', methods=['POST'])
def request_lighting_solution():
    try:
        # Validate input data
        schema = LightingSolutionRequestSchema()
        data = schema.load(request.json)

        # Create a new lighting solution request
        new_request = LightingSolutionRequest(
            name=data['name'],
            email=data['email'],
            location=data['location'],
            preferences=data.get('preferences', '')
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        return jsonify({"message": "Request submitted successfully!"}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
