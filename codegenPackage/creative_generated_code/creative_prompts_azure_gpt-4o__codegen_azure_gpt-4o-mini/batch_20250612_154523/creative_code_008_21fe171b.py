"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Suggest libraries or frameworks for implementing a web-based system to manage governmental contracts, referencing the "Contrataciones y Adquisiciones del Estado OSCE" course on AulaContable.
Generated: DETERMINISTIC_21fe171b037663ea
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries to build a web-based system
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initializing the Flask application
app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contracts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing the database
db = SQLAlchemy(app)

# Model for storing governmental contracts
class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    value = db.Column(db.Float, nullable=False)

# Schema for validating contract data
class ContractSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    value = fields.Float(required=True)

# Initialize the contract schema
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)

# Route for creating a new contract
@app.route('/contracts', methods=['POST'])
def add_contract():
    try:
        # Validate and deserialize input data
        data = contract_schema.load(request.json)
        new_contract = Contract(**data)
        
        # Add contract to the database
        db.session.add(new_contract)
        db.session.commit()
        
        return contract_schema.jsonify(new_contract), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for getting all contracts
@app.route('/contracts', methods=['GET'])
def get_contracts():
    try:
        contracts = Contract.query.all()
        return contracts_schema.jsonify(contracts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for getting a single contract by ID
@app.route('/contracts/<int:id>', methods=['GET'])
def get_contract(id):
    try:
        contract = Contract.query.get_or_404(id)
        return contract_schema.jsonify(contract), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for updating a contract
@app.route('/contracts/<int:id>', methods=['PUT'])
def update_contract(id):
    try:
        contract = Contract.query.get_or_404(id)
        data = contract_schema.load(request.json)
        
        # Update contract fields
        for key, value in data.items():
            setattr(contract, key, value)
        
        db.session.commit()
        return contract_schema.jsonify(contract), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for deleting a contract
@app.route('/contracts/<int:id>', methods=['DELETE'])
def delete_contract(id):
    try:
        contract = Contract.query.get_or_404(id)
        db.session.delete(contract)
        db.session.commit()
        return jsonify({"message": "Contract deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Libraries and Frameworks Suggested:
- **Flask**: A lightweight web application framework for Python.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy.
- **Marshmallow**: A library for object serialization and deserialization, as well as schema validation.
