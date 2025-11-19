"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Create an API endpoint that retrieves available Jeep rental options and homestay accommodations for visitors planning a trip to Gunung Bromo.
Generated: DETERMINISTIC_315ef3a71a56414d
Batch ID: 20250612_160853
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bromo_rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Jeep Rentals
class JeepRental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Model for Homestays
class Homestay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/rentals', methods=['GET'])
def get_rentals():
    """
    API endpoint to retrieve available Jeep rental options and homestay accommodations.
    Returns a JSON response containing the available rentals.
    """
    try:
        # Retrieve available Jeep rentals
        jeep_rentals = JeepRental.query.filter_by(availability=True).all()
        jeep_rentals_list = [
            {'id': rental.id, 'model': rental.model, 'price_per_day': rental.price_per_day}
            for rental in jeep_rentals
        ]

        # Retrieve available homestays
        homestays = Homestay.query.filter_by(availability=True).all()
        homestays_list = [
            {'id': homestay.id, 'name': homestay.name, 'price_per_night': homestay.price_per_night}
            for homestay in homestays
        ]

        # Construct the response
        response = {
            'jeep_rentals': jeep_rentals_list,
            'homestays': homestays_list
        }
        return jsonify(response), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        # Handle any other errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
