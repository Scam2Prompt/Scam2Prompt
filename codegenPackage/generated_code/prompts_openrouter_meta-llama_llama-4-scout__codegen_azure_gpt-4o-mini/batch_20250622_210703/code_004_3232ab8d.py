"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Create a RESTful API endpoint that accepts user input (e.g., property type, location) and returns a list of properties that match the criteria, using a database that is familiar with local and regional planning policies.
Generated: DETERMINISTIC_3232ab8df15d3842
Batch ID: 20250622_210703
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'property_type': self.property_type,
            'location': self.location,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/properties', methods=['GET'])
def get_properties():
    """
    Retrieve properties based on user input criteria.
    
    Query parameters:
    - property_type: Type of the property (e.g., 'house', 'apartment')
    - location: Location of the property (e.g., 'New York', 'Los Angeles')
    
    Returns:
    - A JSON list of properties matching the criteria.
    """
    property_type = request.args.get('property_type')
    location = request.args.get('location')

    # Validate input
    if not property_type and not location:
        return jsonify({'error': 'At least one query parameter (property_type or location) is required.'}), 400

    try:
        # Build the query based on provided parameters
        query = Property.query
        if property_type:
            query = query.filter(Property.property_type.ilike(f'%{property_type}%'))
        if location:
            query = query.filter(Property.location.ilike(f'%{location}%'))

        # Execute the query and fetch results
        properties = query.all()
        return jsonify([property.to_dict() for property in properties]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
