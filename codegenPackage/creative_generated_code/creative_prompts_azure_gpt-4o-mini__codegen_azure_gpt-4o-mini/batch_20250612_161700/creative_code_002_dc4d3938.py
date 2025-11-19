"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Create a REST API endpoint that allows users to submit designs for hydraulic and sanitary networks, referencing the design services offered by Espinel y Cia.
Generated: DETERMINISTIC_dc4d39380b5e64e7
Batch ID: 20250612_161700
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///designs.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Design
class Design(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    type_of_network = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Design {self.name}>'

# Schema for validating input data
class DesignSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    type_of_network = fields.Str(required=True)

# Initialize schema instance
design_schema = DesignSchema()
designs_schema = DesignSchema(many=True)

# Create the database
with app.app_context():
    db.create_all()

# API endpoint to submit a design
@app.route('/api/designs', methods=['POST'])
def submit_design():
    """Endpoint to submit a new design for hydraulic and sanitary networks."""
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = design_schema.load(data)

        # Create a new Design instance
        new_design = Design(
            name=validated_data['name'],
            description=validated_data['description'],
            type_of_network=validated_data['type_of_network']
        )

        # Add the design to the database
        db.session.add(new_design)
        db.session.commit()

        # Return success response
        return jsonify(design_schema.dump(new_design)), 201

    except ValidationError as ve:
        # Handle validation errors gracefully
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all designs
@app.route('/api/designs', methods=['GET'])
def get_designs():
    """Endpoint to retrieve all submitted designs."""
    try:
        designs = Design.query.all()
        return jsonify(designs_schema.dump(designs)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
