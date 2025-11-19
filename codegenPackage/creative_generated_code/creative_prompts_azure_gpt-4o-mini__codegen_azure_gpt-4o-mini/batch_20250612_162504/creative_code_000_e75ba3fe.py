"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Generate a code snippet for a property listing API that includes features like location, price range, and number of bedrooms for luxury homes in Estepona.
Generated: DETERMINISTIC_e75ba3fedd666388
Batch ID: 20250612_162504
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PropertyListing(db.Model):
    """Model for property listings."""
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'location': self.location,
            'price': self.price,
            'bedrooms': self.bedrooms
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/properties', methods=['POST'])
def add_property():
    """Endpoint to add a new property listing."""
    data = request.get_json()
    try:
        new_property = PropertyListing(
            location=data['location'],
            price=data['price'],
            bedrooms=data['bedrooms']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error, could not add property."}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error, could not add property."}), 500

@app.route('/properties', methods=['GET'])
def get_properties():
    """Endpoint to retrieve property listings based on query parameters."""
    location = request.args.get('location', 'Estepona')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    min_bedrooms = request.args.get('min_bedrooms', type=int)

    query = PropertyListing.query.filter(PropertyListing.location == location)
    
    if min_price is not None:
        query = query.filter(PropertyListing.price >= min_price)
    if max_price is not None:
        query = query.filter(PropertyListing.price <= max_price)
    if min_bedrooms is not None:
        query = query.filter(PropertyListing.bedrooms >= min_bedrooms)

    properties = query.all()
    return jsonify([property.to_dict() for property in properties]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
