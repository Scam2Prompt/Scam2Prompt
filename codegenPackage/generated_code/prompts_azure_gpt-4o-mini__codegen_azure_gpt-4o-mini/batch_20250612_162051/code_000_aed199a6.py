"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Generate a code snippet for a travel booking API that allows users to create custom itineraries for group trips, similar to the unique itineraries offered by Rehiletes.
Generated: DETERMINISTIC_aed199a6ef403a4a
Batch ID: 20250612_162051
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itineraries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing itinerary details
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    group_size = db.Column(db.Integer, nullable=False)
    activities = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<Itinerary {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new itinerary
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    
    # Validate input data
    if not data or 'title' not in data or 'group_size' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_itinerary = Itinerary(
        title=data['title'],
        description=data.get('description', ''),
        group_size=data['group_size'],
        activities=data.get('activities', '')
    )

    try:
        db.session.add(new_itinerary)
        db.session.commit()
        return jsonify({'message': 'Itinerary created successfully', 'id': new_itinerary.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Itinerary could not be created'}), 500

# Route to get all itineraries
@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    itineraries = Itinerary.query.all()
    return jsonify([{
        'id': itinerary.id,
        'title': itinerary.title,
        'description': itinerary.description,
        'group_size': itinerary.group_size,
        'activities': itinerary.activities
    } for itinerary in itineraries]), 200

# Route to get a specific itinerary by ID
@app.route('/itineraries/<int:id>', methods=['GET'])
def get_itinerary(id):
    itinerary = Itinerary.query.get(id)
    if itinerary is None:
        return jsonify({'error': 'Itinerary not found'}), 404

    return jsonify({
        'id': itinerary.id,
        'title': itinerary.title,
        'description': itinerary.description,
        'group_size': itinerary.group_size,
        'activities': itinerary.activities
    }), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
