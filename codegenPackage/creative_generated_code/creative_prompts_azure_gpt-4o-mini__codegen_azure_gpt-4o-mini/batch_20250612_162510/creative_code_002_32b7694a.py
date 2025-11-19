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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'url': self.url
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/resources', methods=['GET'])
def get_resources():
    """Retrieve all resources for capacity building and skills training."""
    resources = Resource.query.all()
    return jsonify([resource.to_dict() for resource in resources]), 200

@app.route('/resources', methods=['POST'])
def add_resource():
    """Add a new resource to the database."""
    data = request.json
    try:
        new_resource = Resource(
            title=data['title'],
            description=data['description'],
            category=data['category'],
            url=data['url']
        )
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(new_resource.to_dict()), 201
    except KeyError as e:
        raise BadRequest(f'Missing required field: {str(e)}')
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """Retrieve a specific resource by its ID."""
    resource = Resource.query.get(resource_id)
    if resource is None:
        raise NotFound("Resource not found")
    return jsonify(resource.to_dict()), 200

@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """Update a specific resource by its ID."""
    resource = Resource.query.get(resource_id)
    if resource is None:
        raise NotFound("Resource not found")
    
    data = request.json
    try:
        resource.title = data.get('title', resource.title)
        resource.description = data.get('description', resource.description)
        resource.category = data.get('category', resource.category)
        resource.url = data.get('url', resource.url)
        
        db.session.commit()
        return jsonify(resource.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """Delete a specific resource by its ID."""
    resource = Resource.query.get(resource_id)
    if resource is None:
        raise NotFound("Resource not found")
    
    db.session.delete(resource)
    db.session.commit()
    return jsonify({'message': 'Resource deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
Make sure to install the required libraries with:
```bash
pip install Flask Flask-SQLAlchemy
```
