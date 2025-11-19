"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Design an API for a property management system that integrates with financial planners, mortgage brokers, accountants, and solicitors, similar to Bebold Properties' network of trusted experts.
Generated: DETERMINISTIC_c10b66eb564f7240
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Expert model
class Expert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Expert {self.name}, {self.profession}>'

# Define the Expert schema for serialization
class ExpertSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    profession = fields.Str(required=True)
    contact_info = fields.Str(required=True)

# Initialize the schema
expert_schema = ExpertSchema()
experts_schema = ExpertSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new expert
@app.route('/experts', methods=['POST'])
def add_expert():
    try:
        # Validate and deserialize input
        expert_data = expert_schema.load(request.json)
        new_expert = Expert(**expert_data)
        db.session.add(new_expert)
        db.session.commit()
        return expert_schema.jsonify(new_expert), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error adding expert: {e}")
        return jsonify({"error": "An error occurred while adding the expert."}), 500

# API endpoint to get all experts
@app.route('/experts', methods=['GET'])
def get_experts():
    try:
        experts = Expert.query.all()
        return experts_schema.jsonify(experts), 200
    except Exception as e:
        logging.error(f"Error retrieving experts: {e}")
        return jsonify({"error": "An error occurred while retrieving experts."}), 500

# API endpoint to get a specific expert by ID
@app.route('/experts/<int:id>', methods=['GET'])
def get_expert(id):
    try:
        expert = Expert.query.get_or_404(id)
        return expert_schema.jsonify(expert), 200
    except Exception as e:
        logging.error(f"Error retrieving expert with ID {id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the expert."}), 500

# API endpoint to update an expert
@app.route('/experts/<int:id>', methods=['PUT'])
def update_expert(id):
    try:
        expert = Expert.query.get_or_404(id)
        expert_data = expert_schema.load(request.json)
        for key, value in expert_data.items():
            setattr(expert, key, value)
        db.session.commit()
        return expert_schema.jsonify(expert), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating expert with ID {id}: {e}")
        return jsonify({"error": "An error occurred while updating the expert."}), 500

# API endpoint to delete an expert
@app.route('/experts/<int:id>', methods=['DELETE'])
def delete_expert(id):
    try:
        expert = Expert.query.get_or_404(id)
        db.session.delete(expert)
        db.session.commit()
        return jsonify({"message": "Expert deleted successfully."}), 204
    except Exception as e:
        logging.error(f"Error deleting expert with ID {id}: {e}")
        return jsonify({"error": "An error occurred while deleting the expert."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
