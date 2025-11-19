"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Create an API that offers online modules for emotional well-being, inspired by the METATIME methodologies, including empathy and spatial-temporal perception.
Generated: DETERMINISTIC_f0e5e1b15d45e35d
Batch ID: 20250612_135654
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

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_wellbeing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Module model
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Create a schema for input validation
class ModuleSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    content = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new module
@app.route('/modules', methods=['POST'])
def create_module():
    try:
        # Validate input data
        module_schema = ModuleSchema()
        data = module_schema.load(request.json)

        # Create a new module instance
        new_module = Module(
            title=data['title'],
            description=data['description'],
            content=data['content']
        )
        db.session.add(new_module)
        db.session.commit()

        return jsonify({"message": "Module created successfully", "id": new_module.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating module: {e}")
        return jsonify({"error": "An error occurred while creating the module."}), 500

# API endpoint to retrieve all modules
@app.route('/modules', methods=['GET'])
def get_modules():
    try:
        modules = Module.query.all()
        module_schema = ModuleSchema(many=True)
        return jsonify(module_schema.dump(modules)), 200
    except Exception as e:
        logging.error(f"Error retrieving modules: {e}")
        return jsonify({"error": "An error occurred while retrieving modules."}), 500

# API endpoint to retrieve a specific module by ID
@app.route('/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    try:
        module = Module.query.get_or_404(module_id)
        module_schema = ModuleSchema()
        return jsonify(module_schema.dump(module)), 200
    except Exception as e:
        logging.error(f"Error retrieving module {module_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the module."}), 500

# API endpoint to update a module
@app.route('/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    try:
        module = Module.query.get_or_404(module_id)
        module_schema = ModuleSchema()
        data = module_schema.load(request.json)

        # Update module fields
        module.title = data['title']
        module.description = data['description']
        module.content = data['content']
        db.session.commit()

        return jsonify({"message": "Module updated successfully"}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating module {module_id}: {e}")
        return jsonify({"error": "An error occurred while updating the module."}), 500

# API endpoint to delete a module
@app.route('/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    try:
        module = Module.query.get_or_404(module_id)
        db.session.delete(module)
        db.session.commit()
        return jsonify({"message": "Module deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting module {module_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the module."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
