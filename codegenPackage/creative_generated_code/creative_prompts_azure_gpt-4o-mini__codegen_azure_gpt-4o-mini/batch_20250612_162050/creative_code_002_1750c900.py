"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Create a REST API endpoint for a service that provides information about window and door installation, inspired by the services offered by NellyServis.
Generated: DETERMINISTIC_1750c900257ab0c2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///installations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Installation model
class Installation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for validating and serializing Installation data
class InstallationSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Create an endpoint to retrieve all installations
@app.route('/api/installations', methods=['GET'])
def get_installations():
    """Retrieve all window and door installations."""
    installations = Installation.query.all()
    schema = InstallationSchema(many=True)
    return jsonify(schema.dump(installations)), 200

# Create an endpoint to add a new installation
@app.route('/api/installations', methods=['POST'])
def add_installation():
    """Add a new window or door installation."""
    schema = InstallationSchema()
    try:
        # Validate and deserialize input data
        installation_data = schema.load(request.json)
        new_installation = Installation(**installation_data)
        db.session.add(new_installation)
        db.session.commit()
        return jsonify(schema.dump(new_installation)), 201
    except ValidationError as e:
        return jsonify({"errors": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create an endpoint to retrieve a specific installation by ID
@app.route('/api/installations/<int:id>', methods=['GET'])
def get_installation(id):
    """Retrieve a specific installation by ID."""
    installation = Installation.query.get(id)
    if installation is None:
        return jsonify({"error": "Installation not found"}), 404
    schema = InstallationSchema()
    return jsonify(schema.dump(installation)), 200

# Create an endpoint to update an installation by ID
@app.route('/api/installations/<int:id>', methods=['PUT'])
def update_installation(id):
    """Update an existing installation by ID."""
    installation = Installation.query.get(id)
    if installation is None:
        return jsonify({"error": "Installation not found"}), 404
    
    schema = InstallationSchema()
    try:
        # Validate and deserialize input data
        installation_data = schema.load(request.json)
        for key, value in installation_data.items():
            setattr(installation, key, value)
        db.session.commit()
        return jsonify(schema.dump(installation)), 200
    except ValidationError as e:
        return jsonify({"errors": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create an endpoint to delete an installation by ID
@app.route('/api/installations/<int:id>', methods=['DELETE'])
def delete_installation(id):
    """Delete an installation by ID."""
    installation = Installation.query.get(id)
    if installation is None:
        return jsonify({"error": "Installation not found"}), 404
    db.session.delete(installation)
    db.session.commit()
    return jsonify({"message": "Installation deleted"}), 204

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
