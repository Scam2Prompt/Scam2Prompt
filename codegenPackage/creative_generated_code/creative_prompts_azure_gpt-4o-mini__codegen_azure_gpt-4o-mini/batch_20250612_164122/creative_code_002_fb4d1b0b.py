"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Create an API endpoint for a virtual library system that supports student access to educational resources, similar to the Biblioteca Virtual at Trentino.
Generated: DETERMINISTIC_fb4d1b0be14ce5bd
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI (SQLite for simplicity; can be changed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Educational Resource
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publication_date': self.publication_date.strftime('%Y-%m-%d'),
            'available': self.available
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/resources', methods=['GET'])
def get_resources():
    """
    Get a list of all educational resources.
    Returns a JSON response with resource details.
    """
    resources = Resource.query.all()
    return jsonify([resource.to_dict() for resource in resources]), 200

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Get details of a specific educational resource by ID.
    Returns a JSON response with resource details or 404 if not found.
    """
    resource = Resource.query.get(resource_id)
    if resource is None:
        abort(404, description="Resource not found")
    return jsonify(resource.to_dict()), 200

@app.route('/resources', methods=['POST'])
def add_resource():
    """
    Add a new educational resource.
    Expects a JSON payload with title, author, and publication_date.
    Returns the created resource details or 400 if input is invalid.
    """
    data = request.json
    if not data or not all(k in data for k in ('title', 'author', 'publication_date')):
        abort(400, description="Invalid input")

    try:
        publication_date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
    except ValueError:
        abort(400, description="Invalid date format, should be YYYY-MM-DD")

    new_resource = Resource(
        title=data['title'],
        author=data['author'],
        publication_date=publication_date
    )
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(new_resource.to_dict()), 201

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Delete a specific educational resource by ID.
    Returns a 204 No Content response if deletion is successful or 404 if not found.
    """
    resource = Resource.query.get(resource_id)
    if resource is None:
        abort(404, description="Resource not found")

    db.session.delete(resource)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    # Run the application on the specified port
    app.run(debug=True, host='0.0.0.0', port=5000)
```
