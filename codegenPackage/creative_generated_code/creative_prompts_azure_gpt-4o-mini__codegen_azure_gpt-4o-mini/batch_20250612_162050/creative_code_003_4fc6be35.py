"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Develop an API endpoint that retrieves information on different types of generators, including portable gas and diesel options, as mentioned by Birlik Jeneratör.
Generated: DETERMINISTIC_4fc6be357e736c53
Batch ID: 20250612_162050
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///generators.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Generator model
class Generator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(30), nullable=False)
    power_output = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Generator model instance to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'fuel_type': self.fuel_type,
            'power_output': self.power_output,
            'brand': self.brand
        }

# API endpoint to retrieve information about generators
@app.route('/api/generators', methods=['GET'])
def get_generators():
    """Retrieve a list of generators from the database."""
    try:
        generators = Generator.query.all()  # Query all generators
        return jsonify([generator.to_dict() for generator in generators]), 200
    except SQLAlchemyError as e:
        # Log the error (could be replaced with a proper logging system)
        print(f"Database error: {e}")
        return jsonify({'error': 'Failed to retrieve generators'}), 500

# API endpoint to add a new generator
@app.route('/api/generators', methods=['POST'])
def add_generator():
    """Add a new generator to the database."""
    data = request.get_json()  # Get JSON data from the request
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    new_generator = Generator(
        type=data.get('type'),
        fuel_type=data.get('fuel_type'),
        power_output=data.get('power_output'),
        brand=data.get('brand')
    )
    
    try:
        db.session.add(new_generator)  # Add the new generator
        db.session.commit()  # Commit the session
        return jsonify(new_generator.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session on error
        print(f"Database error: {e}")
        return jsonify({'error': 'Failed to add generator'}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(e):
    """Return a 404 error message."""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    """Return a 500 error message."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```
