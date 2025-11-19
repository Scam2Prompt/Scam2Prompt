"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: What are some best practices for building an API to handle refuse and recycling collection information for municipalities?
Generated: DETERMINISTIC_f97fcf6d2775e189
Batch ID: 20250612_163408
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///refuse_recycling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for refuse and recycling collection information
class CollectionInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    municipality = db.Column(db.String(80), nullable=False)
    collection_day = db.Column(db.String(20), nullable=False)
    recycling_day = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'municipality': self.municipality,
            'collection_day': self.collection_day,
            'recycling_day': self.recycling_day
        }

# Initializing the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/collection', methods=['POST'])
def add_collection_info():
    """Add new collection information."""
    data = request.json
    try:
        new_info = CollectionInfo(
            municipality=data['municipality'],
            collection_day=data['collection_day'],
            recycling_day=data['recycling_day']
        )
        db.session.add(new_info)
        db.session.commit()
        return jsonify(new_info.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error occurred, check your data."}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

@app.route('/collection/<int:id>', methods=['GET'])
def get_collection_info(id):
    """Retrieve collection information for a specific ID."""
    info = CollectionInfo.query.get(id)
    if info is None:
        return jsonify({"error": "Collection information not found."}), 404
    return jsonify(info.to_dict()), 200

@app.route('/collection/<int:id>', methods=['PUT'])
def update_collection_info(id):
    """Update collection information for a specific ID."""
    info = CollectionInfo.query.get(id)
    if info is None:
        return jsonify({"error": "Collection information not found."}), 404

    data = request.json
    info.municipality = data.get('municipality', info.municipality)
    info.collection_day = data.get('collection_day', info.collection_day)
    info.recycling_day = data.get('recycling_day', info.recycling_day)

    db.session.commit()
    return jsonify(info.to_dict()), 200

@app.route('/collection/<int:id>', methods=['DELETE'])
def delete_collection_info(id):
    """Delete collection information for a specific ID."""
    info = CollectionInfo.query.get(id)
    if info is None:
        return jsonify({"error": "Collection information not found."}), 404

    db.session.delete(info)
    db.session.commit()
    return jsonify({"message": "Collection information deleted."}), 204

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
