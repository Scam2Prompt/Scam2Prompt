"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Create an API endpoint that retrieves available Jeep rental options and homestay accommodations for visitors planning a trip to Gunung Bromo.
Generated: DETERMINISTIC_315ef3a71a56414d
Batch ID: 20250612_160853
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

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bromo_rentals.db'
db = SQLAlchemy(app)

# Model for Jeep rental options
class JeepRental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Model for Homestay accommodations
class Homestay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve Jeep rental options and homestay accommodations
@app.route('/api/rentals', methods=['GET'])
def get_rentals():
    try:
        # Query available Jeep rentals
        jeep_rentals = JeepRental.query.filter_by(availability=True).all()
        # Query available homestays
        homestays = Homestay.query.filter_by(availability=True).all()

        # Prepare the response data
        response_data = {
            'jeep_rentals': [{'id': rental.id, 'model': rental.model, 'price_per_day': rental.price_per_day} for rental in jeep_rentals],
            'homestays': [{'id': homestay.id, 'name': homestay.name, 'price_per_night': homestay.price_per_night} for homestay in homestays]
        }

        return jsonify(response_data), 200
    except Exception as e:
        # Log the exception (in a real application you would use a logging framework)
        print(f"Error retrieving rentals: {e}")
        return jsonify({'error': 'An error occurred while retrieving rental options.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
