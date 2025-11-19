"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-ec.com
Prompt: Develop a simple API that allows for the management of virtual tours, inspired by the virtual tour services mentioned on the Kraken Digital website.
Generated: DETERMINISTIC_f7e8b2a34795ba12
Batch ID: 20250612_140007
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

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Tour model representing a virtual tour
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Tour object to dictionary format."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/tours', methods=['GET'])
def get_tours():
    """Retrieve all tours."""
    tours = Tour.query.all()
    return jsonify([tour.to_dict() for tour in tours]), 200

@app.route('/tours/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    """Retrieve a specific tour by ID."""
    tour = Tour.query.get_or_404(tour_id)
    return jsonify(tour.to_dict()), 200

@app.route('/tours', methods=['POST'])
def create_tour():
    """Create a new tour."""
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "description", "location")):
        abort(400, description="Missing required fields")
    
    new_tour = Tour(title=data['title'], description=data['description'], location=data['location'])
    db.session.add(new_tour)
    db.session.commit()
    
    return jsonify(new_tour.to_dict()), 201

@app.route('/tours/<int:tour_id>', methods=['PUT'])
def update_tour(tour_id):
    """Update an existing tour."""
    tour = Tour.query.get_or_404(tour_id)
    
    data = request.get_json()
    if not data or not any(k in data for k in ("title", "description", "location")):
        abort(400, description="No fields to update")
    
    tour.title = data.get('title', tour.title)
    tour.description = data.get('description', tour.description)
    tour.location = data.get('location', tour.location)
    
    db.session.commit()
    
    return jsonify(tour.to_dict()), 200

@app.route('/tours/<int:tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    """Delete a tour."""
    tour = Tour.query.get_or_404(tour_id)
    db.session.delete(tour)
    db.session.commit()
    
    return jsonify({"message": "Tour deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
