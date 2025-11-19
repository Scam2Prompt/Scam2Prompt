"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Create an API endpoint for a clothing manufacturer that allows users to submit custom design requests, inspired by the customization options provided by Bern Wears.
Generated: DETERMINISTIC_5a046fdcf1791b32
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the DesignRequest model
class DesignRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    design_description = db.Column(db.String(500), nullable=False)
    fabric_type = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class DesignRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    design_description = fields.Str(required=True)
    fabric_type = fields.Str(required=True)
    color = fields.Str(required=True)

# Initialize the schema
design_request_schema = DesignRequestSchema()

@app.route('/api/design_requests', methods=['POST'])
def create_design_request():
    """
    API endpoint to submit a custom design request.
    Expects a JSON payload with customer_name, design_description, fabric_type, and color.
    """
    try:
        # Validate and deserialize input data
        data = design_request_schema.load(request.json)
        
        # Create a new design request instance
        new_request = DesignRequest(
            customer_name=data['customer_name'],
            design_description=data['design_description'],
            fabric_type=data['fabric_type'],
            color=data['color']
        )
        
        # Add the new request to the database
        db.session.add(new_request)
        db.session.commit()
        
        # Return a success response
        return jsonify({"message": "Design request submitted successfully!", "id": new_request.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
