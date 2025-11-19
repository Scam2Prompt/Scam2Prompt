"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Describe the target population for the St. Andrew’s School Project for The Young and suggest a suitable API for managing educational resources for these children.
Generated: DETERMINISTIC_28b16df49e398d25
Batch ID: 20250612_163857
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///educational_resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the EducationalResource model
class EducationalResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    age_group = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Resource {self.title}>'

# Create the database
with app.app_context():
    db.create_all()

# API endpoint to add a new educational resource
@app.route('/resources', methods=['POST'])
def add_resource():
    data = request.get_json()
    new_resource = EducationalResource(
        title=data['title'],
        description=data['description'],
        age_group=data['age_group']
    )
    try:
        db.session.add(new_resource)
        db.session.commit()
        return jsonify({'message': 'Resource added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Resource could not be added. Please check the data.'}), 400

# API endpoint to get all educational resources
@app.route('/resources', methods=['GET'])
def get_resources():
    resources = EducationalResource.query.all()
    return jsonify([{
        'id': resource.id,
        'title': resource.title,
        'description': resource.description,
        'age_group': resource.age_group
    } for resource in resources]), 200

# API endpoint to get a specific educational resource by ID
@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = EducationalResource.query.get_or_404(resource_id)
    return jsonify({
        'id': resource.id,
        'title': resource.title,
        'description': resource.description,
        'age_group': resource.age_group
    }), 200

# API endpoint to delete a resource by ID
@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = EducationalResource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({'message': 'Resource deleted successfully!'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
