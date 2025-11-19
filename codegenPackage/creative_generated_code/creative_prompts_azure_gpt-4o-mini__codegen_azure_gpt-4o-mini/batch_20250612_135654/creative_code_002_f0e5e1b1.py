"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Create an API that offers online modules for emotional well-being, inspired by the METATIME methodologies, including empathy and spatial-temporal perception.
Generated: DETERMINISTIC_f0e5e1b15d45e35d
Batch ID: 20250612_135654
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

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database (for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_wellbeing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Module model
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Define the schema for input validation
class ModuleSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all modules
@app.route('/api/modules', methods=['GET'])
def get_modules():
    try:
        modules = Module.query.all()
        module_schema = ModuleSchema(many=True)
        return jsonify(module_schema.dump(modules)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new module
@app.route('/api/modules', methods=['POST'])
def create_module():
    try:
        json_data = request.get_json()
        module_schema = ModuleSchema()
        module_data = module_schema.load(json_data)
        
        new_module = Module(**module_data)
        db.session.add(new_module)
        db.session.commit()
        
        return jsonify(module_schema.dump(new_module)), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a module by ID
@app.route('/api/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    try:
        module = Module.query.get_or_404(module_id)
        module_schema = ModuleSchema()
        return jsonify(module_schema.dump(module)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a module
@app.route('/api/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    try:
        json_data = request.get_json()
        module_schema = ModuleSchema()
        module_data = module_schema.load(json_data)
        
        module = Module.query.get_or_404(module_id)
        module.title = module_data['title']
        module.description = module_data['description']
        
        db.session.commit()
        
        return jsonify(module_schema.dump(module)), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a module
@app.route('/api/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    try:
        module = Module.query.get_or_404(module_id)
        db.session.delete(module)
        db.session.commit()
        return jsonify({"message": "Module deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
