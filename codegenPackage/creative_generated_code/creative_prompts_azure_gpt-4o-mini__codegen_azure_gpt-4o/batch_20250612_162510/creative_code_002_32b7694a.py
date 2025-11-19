"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayb-sd.org
Prompt: Create an API that connects small business owners with resources for capacity building and skills training, reflecting the mission of جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_32b7694abd1ae347
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the Resource model to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'url': self.url
        }

# Routes

@app.route('/resources', methods=['GET'])
def get_resources():
    """
    Retrieve all resources.
    """
    try:
        resources = Resource.query.all()
        return jsonify([resource.to_dict() for resource in resources]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to fetch resources', 'details': str(e)}), 500

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    """
    Retrieve a specific resource by ID.
    """
    try:
        resource = Resource.query.get(resource_id)
        if not resource:
            return jsonify({'error': 'Resource not found'}), 404
        return jsonify(resource.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to fetch the resource', 'details': str(e)}), 500

@app.route('/resources', methods=['POST'])
def create_resource():
    """
    Add a new resource.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'category' not in data or 'url' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        new_resource = Resource(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            url=data['url']
        )
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(new_resource.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to create resource', 'details': str(e)}), 500

@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    Update an existing resource by ID.
    """
    try:
        data = request.get_json()
        resource = Resource.query.get(resource_id)
        if not resource:
            return jsonify({'error': 'Resource not found'}), 404

        resource.name = data.get('name', resource.name)
        resource.description = data.get('description', resource.description)
        resource.category = data.get('category', resource.category)
        resource.url = data.get('url', resource.url)

        db.session.commit()
        return jsonify(resource.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to update resource', 'details': str(e)}), 500

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Delete a resource by ID.
    """
    try:
        resource = Resource.query.get(resource_id)
        if not resource:
            return jsonify({'error': 'Resource not found'}), 404

        db.session.delete(resource)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to delete resource', 'details': str(e)}), 500

# Error Handling
@app.errorhandler(404)
def handle_404(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def handle_500(error):
    """
    Handle 500 errors.
    """
    return jsonify({'error': 'Internal server error'}), 500

# Main Execution
if __name__ == '__main__':
    # Create the database tables if not already present
    with app.app_context():
        db.create_all()

    # Start the Flask server
    app.run(debug=True)
```
