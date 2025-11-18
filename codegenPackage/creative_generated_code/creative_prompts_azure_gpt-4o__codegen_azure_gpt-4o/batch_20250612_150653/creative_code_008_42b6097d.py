"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Suggest APIs for managing and analyzing data from shelters and helplines, such as those supported by Sauti Kenya, to improve organizational capacity and sustainability.
Generated: DETERMINISTIC_42b6097dd440349a
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation that provides a framework for managing and analyzing shelter and helpline data using Flask (API framework) and SQLAlchemy (ORM for database). The code is production-ready, clean, and adheres to best practices.

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database (replace with your production database URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy for database management
db = SQLAlchemy(app)

# Define Shelter model
class Shelter(db.Model):
    __tablename__ = 'shelters'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Shelter name
    location = db.Column(db.String(100), nullable=False)  # Shelter location
    capacity = db.Column(db.Integer, nullable=False)  # Maximum capacity
    current_occupancy = db.Column(db.Integer, nullable=False)  # Current number of occupants

    def to_dict(self):
        """Convert the Shelter object into a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity,
            'current_occupancy': self.current_occupancy
        }

# Create tables in the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to fetch all shelters
@app.route('/shelters', methods=['GET'])
def get_shelters():
    try:
        shelters = Shelter.query.all()
        return jsonify([shelter.to_dict() for shelter in shelters]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new shelter
@app.route('/shelters', methods=['POST'])
def add_shelter():
    data = request.get_json()
    try:
        # Validate input
        if not all(key in data for key in ['name', 'location', 'capacity', 'current_occupancy']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new shelter
        new_shelter = Shelter(
            name=data['name'],
            location=data['location'],
            capacity=data['capacity'],
            current_occupancy=data['current_occupancy']
        )
        db.session.add(new_shelter)
        db.session.commit()
        return jsonify(new_shelter.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to update shelter information
@app.route('/shelters/<int:shelter_id>', methods=['PUT'])
def update_shelter(shelter_id):
    data = request.get_json()
    try:
        shelter = Shelter.query.get_or_404(shelter_id)

        # Update shelter details
        shelter.name = data.get('name', shelter.name)
        shelter.location = data.get('location', shelter.location)
        shelter.capacity = data.get('capacity', shelter.capacity)
        shelter.current_occupancy = data.get('current_occupancy', shelter.current_occupancy)

        db.session.commit()
        return jsonify(shelter.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete a shelter
@app.route('/shelters/<int:shelter_id>', methods=['DELETE'])
def delete_shelter(shelter_id):
    try:
        shelter = Shelter.query.get_or_404(shelter_id)
        db.session.delete(shelter)
        db.session.commit()
        return jsonify({'message': 'Shelter deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to analyze data (Example: Calculate average occupancy rate)
@app.route('/shelters/analytics', methods=['GET'])
def analyze_data():
    try:
        shelters = Shelter.query.all()
        if not shelters:
            return jsonify({'message': 'No shelters found for analysis'}), 404

        total_capacity = sum(shelter.capacity for shelter in shelters)
        total_occupancy = sum(shelter.current_occupancy for shelter in shelters)
        average_occupancy_rate = (total_occupancy / total_capacity) * 100 if total_capacity else 0

        return jsonify({'average_occupancy_rate': average_occupancy_rate}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Key Features:
- **CRUD API endpoints** (`GET`, `POST`, `PUT`, `DELETE`) for managing shelter data.
- **Data analysis endpoint** to calculate the average occupancy rate.
- **Error handling** for database operations.
- **Validation** for user input.
- **Production-ready** (use an appropriate database in production and set `debug=False` in Flask).
