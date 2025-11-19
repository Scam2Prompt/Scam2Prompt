"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Illustrate how to implement a search feature in a car dealership web app that allows users to find vehicles based on specific criteria, similar to the Helfen Motors offerings.
Generated: DETERMINISTIC_6c5976a1c5b21034
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Car {self.make} {self.model} {self.year}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Search endpoint for cars
@app.route('/search', methods=['GET'])
def search_cars():
    """
    Search for cars based on query parameters.
    Query parameters:
        - make: The make of the car (e.g., 'Toyota')
        - model: The model of the car (e.g., 'Camry')
        - year: The year of the car (e.g., 2020)
        - price_max: The maximum price of the car (e.g., 30000)
    Returns:
        A JSON response containing the list of matching cars.
    """
    try:
        # Get query parameters
        make = request.args.get('make')
        model = request.args.get('model')
        year = request.args.get('year', type=int)
        price_max = request.args.get('price_max', type=float)

        # Build the query
        query = Car.query

        if make:
            query = query.filter(Car.make.ilike(f'%{make}%'))
        if model:
            query = query.filter(Car.model.ilike(f'%{model}%'))
        if year:
            query = query.filter(Car.year == year)
        if price_max is not None:
            query = query.filter(Car.price <= price_max)

        # Execute the query and get results
        results = query.all()

        # Convert results to a list of dictionaries
        cars = [{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year, 'price': car.price} for car in results]

        # Return the results as JSON
        return jsonify(cars), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
