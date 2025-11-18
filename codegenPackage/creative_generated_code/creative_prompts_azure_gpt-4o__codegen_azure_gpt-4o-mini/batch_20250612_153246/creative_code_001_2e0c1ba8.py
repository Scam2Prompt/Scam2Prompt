"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Develop an API that allows users to search for outdoor furniture collections by material properties such as "100% recyclable," "super resistant," or "ultra soft," as described in Nodo Italia's product offerings.
Generated: DETERMINISTIC_2e0c1ba8dd8947c0
Batch ID: 20250612_153246
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

app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class FurnitureCollection(db.Model):
    """Model representing a furniture collection."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    material_properties = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'material_properties': self.material_properties.split(',')
        }

@app.before_first_request
def create_tables():
    """Create database tables on the first request if they do not exist."""
    db.create_all()

@app.route('/api/furniture', methods=['GET'])
def search_furniture():
    """Search for furniture collections by material properties.

    Query parameters:
        - properties: Comma-separated list of material properties to search for.
    Returns:
        - A JSON response with matching furniture collections.
    """
    properties = request.args.get('properties')
    
    if not properties:
        return jsonify({"error": "No properties provided"}), 400

    # Split properties and strip whitespace
    properties_list = [prop.strip() for prop in properties.split(',')]
    
    try:
        # Query the database for collections that match any of the provided properties
        collections = FurnitureCollection.query.filter(
            FurnitureCollection.material_properties.in_(properties_list)
        ).all()

        # Convert collections to a list of dictionaries
        results = [collection.to_dict() for collection in collections]

        return jsonify(results), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set up the database and insert some sample data before running the API.
