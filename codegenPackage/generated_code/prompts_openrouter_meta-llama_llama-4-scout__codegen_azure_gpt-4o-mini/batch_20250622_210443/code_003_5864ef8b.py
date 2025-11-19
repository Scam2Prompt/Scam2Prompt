"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Create an API endpoint to retrieve a list of comparable properties for a given property, using data from the Brazilian real estate market, as described in the website's content.
Generated: DETERMINISTIC_5864ef8b7d24c6a0
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Property
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'price': self.price,
            'size': self.size,
            'bedrooms': self.bedrooms
        }

# API endpoint to retrieve comparable properties
@app.route('/api/properties/comparable', methods=['GET'])
def get_comparable_properties():
    try:
        # Get property ID from query parameters
        property_id = request.args.get('id', type=int)
        if property_id is None:
            return jsonify({'error': 'Property ID is required'}), 400

        # Fetch the target property
        target_property = Property.query.get(property_id)
        if target_property is None:
            return jsonify({'error': 'Property not found'}), 404

        # Retrieve comparable properties based on criteria (e.g., same location and similar price range)
        comparable_properties = Property.query.filter(
            Property.location == target_property.location,
            Property.id != target_property.id,
            Property.price.between(target_property.price * 0.9, target_property.price * 1.1)
        ).all()

        # Convert properties to dictionary format
        comparable_properties_list = [property.to_dict() for property in comparable_properties]

        return jsonify(comparable_properties_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
