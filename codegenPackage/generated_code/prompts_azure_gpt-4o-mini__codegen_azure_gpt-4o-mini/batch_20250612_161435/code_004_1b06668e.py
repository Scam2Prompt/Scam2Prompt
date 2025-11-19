"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: Suggest a RESTful API design for a villa rental service that includes endpoints for searching villas by location and amenities, based on the offerings of Villa Andreas in Kefalonia.
Generated: DETERMINISTIC_1b06668e2f5e940c
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///villas.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Villa model representing the villa rental properties
class Villa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert Villa object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'amenities': self.amenities.split(',')  # Split amenities into a list
        }

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/villas', methods=['GET'])
def search_villas():
    """
    Search for villas based on location and amenities.
    Query parameters:
    - location: str (optional)
    - amenities: str (comma-separated list, optional)
    """
    location = request.args.get('location')
    amenities = request.args.get('amenities')

    query = Villa.query

    if location:
        query = query.filter(Villa.location.ilike(f'%{location}%'))  # Case-insensitive search

    if amenities:
        amenities_list = [amenity.strip() for amenity in amenities.split(',')]
        for amenity in amenities_list:
            query = query.filter(Villa.amenities.ilike(f'%{amenity}%'))  # Filter by each amenity

    try:
        villas = query.all()
        return jsonify([villa.to_dict() for villa in villas]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/villas', methods=['POST'])
def add_villa():
    """
    Add a new villa to the database.
    Request body should be a JSON object with 'name', 'location', and 'amenities'.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'location', 'amenities')):
        return jsonify({'error': 'Missing required fields'}), 400

    new_villa = Villa(
        name=data['name'],
        location=data['location'],
        amenities=data['amenities']
    )

    try:
        db.session.add(new_villa)
        db.session.commit()
        return jsonify(new_villa.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
