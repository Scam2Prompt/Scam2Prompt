"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Develop a REST API endpoint to query available properties on sunnyhurghada.com based on criteria like maximum price, number of bedrooms, and location.
Generated: DETERMINISTIC_b0a99a75db849658
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///properties.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'location': self.location,
            'price': self.price,
            'bedrooms': self.bedrooms
        }

@app.route('/api/properties', methods=['GET'])
def get_properties():
    """GET endpoint to query available properties based on criteria."""

    # Get query parameters
    max_price = request.args.get('max_price', type=float)
    num_bedrooms = request.args.get('bedrooms', type=int)
    location = request.args.get('location', type=str)

    # Build the query
    query = Property.query

    if max_price is not None:
        query = query.filter(Property.price <= max_price)
    if num_bedrooms is not None:
        query = query.filter(Property.bedrooms == num_bedrooms)
    if location:
        query = query.filter(Property.location.ilike(f'%{location}%'))

    try:
        properties = query.all()
        return jsonify([property.to_dict() for property in properties]), 200
    except SQLAlchemyError as e:
        # Log the error (logging not included in this snippet for brevity)
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```
