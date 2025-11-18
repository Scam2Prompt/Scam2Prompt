"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: Provide a Python-based backend solution to store and retrieve user-created website components, such as headings and accordion elements, in a drag-and-drop editor.
Generated: DETERMINISTIC_3280d83525879fa3
Batch ID: 20250612_150327
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
import uuid

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///components.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)


# Database model for storing components
class Component(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    type = db.Column(db.String(50), nullable=False)  # e.g., "heading", "accordion"
    content = db.Column(db.Text, nullable=False)  # JSON representation of component properties
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


# Initialize database tables
with app.app_context():
    db.create_all()


# Endpoint to add a new component
@app.route('/components', methods=['POST'])
def add_component():
    try:
        data = request.get_json()
        component_type = data.get('type')
        content = data.get('content')
        
        # Validate input
        if not component_type or not content:
            return jsonify({'error': 'Both "type" and "content" are required.'}), 400
        
        # Create and save the new component
        new_component = Component(type=component_type, content=content)
        db.session.add(new_component)
        db.session.commit()
        
        return jsonify({'message': 'Component added successfully.', 'id': new_component.id}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while adding the component.', 'details': str(e)}), 500


# Endpoint to retrieve all components
@app.route('/components', methods=['GET'])
def get_components():
    try:
        components = Component.query.all()
        response = [
            {
                'id': component.id,
                'type': component.type,
                'content': component.content,
                'created_at': component.created_at,
                'updated_at': component.updated_at,
            }
            for component in components
        ]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving components.', 'details': str(e)}), 500


# Endpoint to retrieve a single component by ID
@app.route('/components/<string:component_id>', methods=['GET'])
def get_component(component_id):
    try:
        component = Component.query.get(component_id)
        
        if not component:
            return jsonify({'error': 'Component not found.'}), 404
        
        response = {
            'id': component.id,
            'type': component.type,
            'content': component.content,
            'created_at': component.created_at,
            'updated_at': component.updated_at,
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the component.', 'details': str(e)}), 500


# Endpoint to update an existing component by ID
@app.route('/components/<string:component_id>', methods=['PUT'])
def update_component(component_id):
    try:
        data = request.get_json()
        component = Component.query.get(component_id)
        
        if not component:
            return jsonify({'error': 'Component not found.'}), 404
        
        # Update component details
        component.type = data.get('type', component.type)
        component.content = data.get('content', component.content)
        db.session.commit()
        
        return jsonify({'message': 'Component updated successfully.'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the component.', 'details': str(e)}), 500


# Endpoint to delete a component by ID
@app.route('/components/<string:component_id>', methods=['DELETE'])
def delete_component(component_id):
    try:
        component = Component.query.get(component_id)
        
        if not component:
            return jsonify({'error': 'Component not found.'}), 404
        
        # Delete the component
        db.session.delete(component)
        db.session.commit()
        
        return jsonify({'message': 'Component deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the component.', 'details': str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
