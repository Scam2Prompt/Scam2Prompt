"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Provide a solution architecture for digitizing the entire forestry value chain using tools like Optinex, Trimble Connected Forest, and Remsoft software, as detailed on ForestX's site.
Generated: DETERMINISTIC_8e771d4f6bff5965
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forestry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for the Forestry data
class ForestryData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value_chain_stage = db.Column(db.String(50), nullable=False)
    tool_used = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Create a schema for validation
class ForestryDataSchema(Schema):
    value_chain_stage = fields.String(required=True)
    tool_used = fields.String(required=True)
    description = fields.String()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add new forestry data
@app.route('/forestry', methods=['POST'])
def add_forestry_data():
    schema = ForestryDataSchema()
    try:
        # Validate incoming JSON data
        data = schema.load(request.json)

        # Create a new entry in the database
        new_data = ForestryData(
            value_chain_stage=data['value_chain_stage'],
            tool_used=data['tool_used'],
            description=data.get('description', '')
        )

        db.session.add(new_data)
        db.session.commit()

        logging.info("New forestry data added successfully.")
        return jsonify({"message": "Data added successfully!"}), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.exception("An error occurred while adding forestry data.")
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Route to get all forestry data
@app.route('/forestry', methods=['GET'])
def get_forestry_data():
    try:
        data = ForestryData.query.all()
        schema = ForestryDataSchema(many=True)
        return jsonify(schema.dump(data)), 200
    except Exception as e:
        logging.exception("An error occurred while retrieving forestry data.")
        return jsonify({"error": "An error occurred while retrieving data."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=False)
```
