"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Create an API endpoint for listing properties available for rent in Bogotá, including details like location, size, and price, similar to the listings on Inmobiliaria Capri's site.
Generated: DETERMINISTIC_68c369f09f25c7b1
Batch ID: 20250612_161700
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

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'  # Use a SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)  # Size in square meters
    price = db.Column(db.Float, nullable=False)  # Price in currency

    def serialize(self):
        """Convert the Property object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'location': self.location,
            'size': self.size,
            'price': self.price
        }

# Endpoint to list properties available for rent in Bogotá
@app.route('/api/properties', methods=['GET'])
def list_properties():
    try:
        # Query the database for all properties
        properties = Property.query.all()
        # Serialize the properties into a list of dictionaries
        results = [property.serialize() for property in properties]
        return jsonify(results), 200  # Return results in JSON format with HTTP status 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500  # Return a 500 error for internal server errors

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()  # Create tables based on the defined models
    app.run(debug=True)  # Run the app in debug mode for development
```
