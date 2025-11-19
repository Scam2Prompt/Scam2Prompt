"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Create an API endpoint for a travel application that provides details about unique experiences in Chile, specifically focusing on horse riding tours in the Melado Valley.
Generated: DETERMINISTIC_e26a9057c9e442d7
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

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class HorseRidingTour(db.Model):
    """Model representing a horse riding tour in Melado Valley."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(50), nullable=False)  # e.g., "2 hours", "Full day"
    price = db.Column(db.Float, nullable=False)  # Price in local currency
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'price': self.price,
            'location': self.location
        }

@app.route('/api/tours', methods=['GET'])
def get_tours():
    """API endpoint to get a list of horse riding tours."""
    try:
        tours = HorseRidingTour.query.all()
        return jsonify([tour.to_dict() for tour in tours]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tours/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    """API endpoint to get details of a specific horse riding tour."""
    try:
        tour = HorseRidingTour.query.get_or_404(tour_id)
        return jsonify(tour.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tours', methods=['POST'])
def add_tour():
    """API endpoint to add a new horse riding tour."""
    try:
        data = request.json
        new_tour = HorseRidingTour(
            title=data['title'],
            description=data['description'],
            duration=data['duration'],
            price=data['price'],
            location=data['location']
        )
        db.session.add(new_tour)
        db.session.commit()
        return jsonify(new_tour.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tours/<int:tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    """API endpoint to delete a horse riding tour."""
    try:
        tour = HorseRidingTour.query.get_or_404(tour_id)
        db.session.delete(tour)
        db.session.commit()
        return jsonify({'message': 'Tour deleted successfully'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
