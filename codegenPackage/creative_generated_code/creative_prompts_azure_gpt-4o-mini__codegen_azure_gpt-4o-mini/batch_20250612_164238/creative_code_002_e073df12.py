"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Create a REST API endpoint specification for retrieving information about the boats offered by Coastal Boat Rentals, including their features and rental prices.
Generated: DETERMINISTIC_e073df127857e3a6
Batch ID: 20250612_164238
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Boat model definition
class Boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    features = db.Column(db.Text, nullable=False)
    rental_price = db.Column(db.Float, nullable=False)

    def __init__(self, name, features, rental_price):
        self.name = name
        self.features = features
        self.rental_price = rental_price

# Boat schema for serialization
class BoatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Boat

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all boats
@app.route('/api/boats', methods=['GET'])
def get_boats():
    """
    Retrieve a list of all boats available for rent.
    Returns a JSON array of boats with their features and rental prices.
    """
    try:
        boats = Boat.query.all()  # Query all boats from the database
        boat_schema = BoatSchema(many=True)  # Instantiate the schema for multiple boats
        return jsonify(boat_schema.dump(boats)), 200  # Return boats in JSON format
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors during retrieval

# Endpoint to retrieve a single boat by ID
@app.route('/api/boats/<int:boat_id>', methods=['GET'])
def get_boat(boat_id):
    """
    Retrieve a specific boat by its ID.
    Returns the boat's details including features and rental price.
    
    :param boat_id: ID of the boat to retrieve
    """
    try:
        boat = Boat.query.get_or_404(boat_id)  # Fetch the boat or return 404 if not found
        boat_schema = BoatSchema()  # Instantiate the schema for a single boat
        return jsonify(boat_schema.dump(boat)), 200  # Return the boat in JSON format
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors during retrieval

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
