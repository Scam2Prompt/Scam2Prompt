"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lalitarora.in
Prompt: Create an API endpoint for a leadership training platform that allows users to access resources and tools, similar to the offerings of KW Academy of Excellence.
Generated: DETERMINISTIC_d662cf0d4d89d037
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leadership_training.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Retrieve a list of all leadership training resources.
    """
    try:
        resources = Resource.query.all()
        return jsonify([resource.to_dict() for resource in resources]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Add a new resource to the leadership training platform.
    Expects a JSON payload with 'title', 'description', and 'url'.
    """
    data = request.get_json()

    # Validate input
    if not data or not 'title' in data or not 'url' in data:
        return jsonify({'error': 'Title and URL are required.'}), 400

    new_resource = Resource(
        title=data['title'],
        description=data.get('description', ''),
        url=data['url']
    )

    try:
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(new_resource.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
