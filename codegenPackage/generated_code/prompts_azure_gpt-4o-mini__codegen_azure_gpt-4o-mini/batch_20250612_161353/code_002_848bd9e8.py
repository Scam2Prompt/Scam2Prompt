"""
Generated Code Metadata:
========================
Original URL: https://000000011.xyz
Prompt: Generate code for a web application that utilizes PRQ's colocation services, focusing on scalability and performance.
Generated: DETERMINISTIC_848bd9e8de31464f
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///colocation_services.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Colocation model
class Colocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Colocation {self.name}>'

# Define the schema for input validation
class ColocationSchema(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    capacity = fields.Int(required=True)

# Initialize the schema
colocation_schema = ColocationSchema()
colocations_schema = ColocationSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new colocation service
@app.route('/colocations', methods=['POST'])
def add_colocation():
    try:
        # Validate and deserialize input
        data = request.get_json()
        colocation_data = colocation_schema.load(data)

        # Create a new colocation instance
        new_colocation = Colocation(**colocation_data)
        db.session.add(new_colocation)
        db.session.commit()

        return jsonify(colocation_schema.dump(new_colocation)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all colocations
@app.route('/colocations', methods=['GET'])
def get_colocations():
    try:
        colocations = Colocation.query.all()
        return jsonify(colocations_schema.dump(colocations)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific colocation by ID
@app.route('/colocations/<int:id>', methods=['GET'])
def get_colocation(id):
    try:
        colocation = Colocation.query.get_or_404(id)
        return jsonify(colocation_schema.dump(colocation)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a colocation service
@app.route('/colocations/<int:id>', methods=['PUT'])
def update_colocation(id):
    try:
        data = request.get_json()
        colocation_data = colocation_schema.load(data)

        colocation = Colocation.query.get_or_404(id)
        for key, value in colocation_data.items():
            setattr(colocation, key, value)

        db.session.commit()
        return jsonify(colocation_schema.dump(colocation)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a colocation service
@app.route('/colocations/<int:id>', methods=['DELETE'])
def delete_colocation(id):
    try:
        colocation = Colocation.query.get_or_404(id)
        db.session.delete(colocation)
        db.session.commit()
        return jsonify({"message": "Colocation deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Marshmallow

### Instructions
1. Set up a virtual environment and install the required packages.
2. Set the `DATABASE_URL` environment variable for your database connection.
3. Run the application using `python app.py`.
