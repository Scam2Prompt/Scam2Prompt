"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Develop a REST API endpoint for retrieving store locations and contact details, formatted like the addresses provided on Navkar Furniture's website.
Generated: DETERMINISTIC_62f26acae7f73d84
Batch ID: 20250612_153224
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///store_locations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow for serialization
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the StoreLocation model
class StoreLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)

    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

# Create a Marshmallow schema for serializing the StoreLocation data
class StoreLocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreLocation

# Initialize the schema
store_location_schema = StoreLocationSchema(many=True)

# API endpoint to retrieve store locations and contact details
@app.route('/api/store-locations', methods=['GET'])
def get_store_locations():
    try:
        # Query all store locations from the database
        locations = StoreLocation.query.all()
        
        # Serialize the results
        result = store_location_schema.dump(locations)

        return jsonify(result), 200  # Return with HTTP 200 status code
    except Exception as e:
        # Handle any unexpected errors and return a 500 status code
        return jsonify({"error": str(e)}), 500

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```
This code sets up a simple Flask REST API that allows you to retrieve store locations and their contact details. Adjust the database settings and schema according to your needs.
