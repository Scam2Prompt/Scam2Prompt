"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Generate code to create a virtual library system like "Biblioteca Virtual" mentioned on the Trentino website, allowing users to search and access digital resources.
Generated: DETERMINISTIC_7e111de85ca1b4a7
Batch ID: 20250612_151445
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)
# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for the resources in the library
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    resource_type = db.Column(db.String(50), nullable=False)  # e.g., 'Book', 'Article', etc.
    url = db.Column(db.String(255), nullable=False)  # Link to the digital resource

    def __repr__(self):
        return f"<Resource {self.title}>"

# Initialize the database (Run this once to create the database and tables)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to search resources by title or author
@app.route('/search', methods=['GET'])
def search_resources():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400

    try:
        # Search for resources by title or author (case-insensitive)
        resources = Resource.query.filter(
            (Resource.title.ilike(f"%{query}%")) |
            (Resource.author.ilike(f"%{query}%"))
        ).all()

        # Return the found resources as JSON
        return jsonify([{
            "id": res.id,
            "title": res.title,
            "author": res.author,
            "description": res.description,
            "resource_type": res.resource_type,
            "url": res.url
        } for res in resources]), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({"error": str(e)}), 500

# API endpoint to add a new resource to the library
@app.route('/resources', methods=['POST'])
def add_resource():
    data = request.json

    # Validate input data
    if not all(key in data for key in ['title', 'resource_type', 'url']):
        return jsonify({"error": "Title, resource_type, and url are required."}), 400

    new_resource = Resource(
        title=data['title'],
        author=data.get('author'),
        description=data.get('description'),
        resource_type=data['resource_type'],
        url=data['url']
    )

    try:
        db.session.add(new_resource)
        db.session.commit()
        return jsonify({"message": "Resource added successfully."}), 201
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
