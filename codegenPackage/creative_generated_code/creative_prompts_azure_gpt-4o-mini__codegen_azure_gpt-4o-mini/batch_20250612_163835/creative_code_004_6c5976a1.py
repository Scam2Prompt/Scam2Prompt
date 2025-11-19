"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Illustrate how to implement a search feature in a car dealership web app that allows users to find vehicles based on specific criteria, similar to the Helfen Motors offerings.
Generated: DETERMINISTIC_6c5976a1c5b21034
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define a Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Vehicle object to a dictionary for easy JSON serialization."""
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'price': self.price
        }

# Create the database and the Vehicle table if it does not exist
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_vehicles():
    """Search for vehicles based on query parameters."""
    
    # Get search criteria from the query parameters
    make = request.args.get('make')
    model = request.args.get('model')
    year = request.args.get('year', type=int)
    max_price = request.args.get('max_price', type=float)

    # Initialize a query on the Vehicle model
    query = Vehicle.query

    # Apply filters based on provided criteria
    if make:
        query = query.filter(Vehicle.make.ilike(f'%{make}%'))
    if model:
        query = query.filter(Vehicle.model.ilike(f'%{model}%'))
    if year:
        query = query.filter(Vehicle.year == year)
    if max_price:
        query = query.filter(Vehicle.price <= max_price)

    # Execute the query and retrieve results
    try:
        vehicles = query.all()
        # Convert results to dictionaries for JSON serialization
        return jsonify([vehicle.to_dict() for vehicle in vehicles]), 200
    except Exception as e:
        # Handle any exceptions that occur during the query
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
