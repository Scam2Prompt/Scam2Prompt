"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: How can I implement an API that allows users to create digital collections inspired by Refik Anadol's work in AI-generated art?
Generated: DETERMINISTIC_4f7786529ecfaa8d
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Collection model
class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)
    artwork_url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Collection object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'artwork_url': self.artwork_url
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/collections', methods=['POST'])
def create_collection():
    """Create a new digital collection."""
    data = request.get_json()

    # Validate input data
    if not data or 'title' not in data or 'artwork_url' not in data:
        return jsonify({'error': 'Title and artwork URL are required.'}), 400

    new_collection = Collection(
        title=data['title'],
        description=data.get('description', ''),
        artwork_url=data['artwork_url']
    )

    try:
        db.session.add(new_collection)
        db.session.commit()
        return jsonify(new_collection.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Collection with this title already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/collections', methods=['GET'])
def get_collections():
    """Retrieve all digital collections."""
    collections = Collection.query.all()
    return jsonify([collection.to_dict() for collection in collections]), 200

@app.route('/collections/<int:collection_id>', methods=['GET'])
def get_collection(collection_id):
    """Retrieve a specific digital collection by ID."""
    collection = Collection.query.get(collection_id)
    if collection is None:
        return jsonify({'error': 'Collection not found.'}), 404
    return jsonify(collection.to_dict()), 200

@app.route('/collections/<int:collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """Delete a specific digital collection by ID."""
    collection = Collection.query.get(collection_id)
    if collection is None:
        return jsonify({'error': 'Collection not found.'}), 404

    db.session.delete(collection)
    db.session.commit()
    return jsonify({'message': 'Collection deleted successfully.'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
