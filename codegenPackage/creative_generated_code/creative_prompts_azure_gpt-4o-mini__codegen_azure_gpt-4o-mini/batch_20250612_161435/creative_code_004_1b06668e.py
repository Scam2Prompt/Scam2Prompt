"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Suggest a RESTful API design for a villa rental service that includes endpoints for searching villas by location and amenities, based on the offerings of Villa Andreas in Kefalonia.
Generated: DETERMINISTIC_1b06668e2f5e940c
Batch ID: 20250612_161435
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///villa_rental_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Villa
class Villa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'amenities': self.amenities.split(','),  # Convert to list
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to search villas by location and amenities
@app.route('/villas/search', methods=['GET'])
def search_villas():
    location = request.args.get('location', '').strip()
    amenities = request.args.get('amenities', '').strip().split(',')

    # Validate input
    if not location and not amenities:
        return jsonify({'error': 'At least one search parameter is required.'}), 400

    # Query villas based on location and amenities
    query = Villa.query
    if location:
        query = query.filter(Villa.location.ilike(f'%{location}%'))
    
    if amenities:
        for amenity in amenities:
            query = query.filter(Villa.amenities.ilike(f'%{amenity.strip()}%'))

    villas = query.all()
    
    return jsonify([villa.serialize() for villa in villas]), 200

# Error handling for integrity errors
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    return jsonify({'error': 'Database integrity error occurred.'}), 400

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
```
