"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Write code to create a search interface for filtering vehicles by brand, model, year, and price, similar to the functionality on the Cid Autos website.
Generated: DETERMINISTIC_1350c2282b473881
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vehicle_search.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Vehicle {self.brand} {self.model} ({self.year})>'

# Create the database and table
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the search interface
@app.route('/')
def index():
    return render_template('search.html')

# API endpoint to filter vehicles
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    try:
        # Get filters from query parameters
        brand = request.args.get('brand')
        model = request.args.get('model')
        year = request.args.get('year', type=int)
        price = request.args.get('price', type=float)

        # Start with all vehicles
        query = Vehicle.query

        # Apply filters if provided
        if brand:
            query = query.filter(Vehicle.brand.ilike(f'%{brand}%'))
        if model:
            query = query.filter(Vehicle.model.ilike(f'%{model}%'))
        if year:
            query = query.filter(Vehicle.year == year)
        if price is not None:
            query = query.filter(Vehicle.price <= price)

        # Execute query and get results
        vehicles = query.all()
        result = [{
            'id': vehicle.id,
            'brand': vehicle.brand,
            'model': vehicle.model,
            'year': vehicle.year,
            'price': vehicle.price
        } for vehicle in vehicles]

        # Return JSON response
        return jsonify(result), 200

    except Exception as e:
        # Log exception and return error response
        app.logger.error(f'Error fetching vehicles: {e}')
        return jsonify({'error': 'An error occurred while fetching vehicles.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/search.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Search</title>
    <script>
        async function searchVehicles() {
            const brand = document.getElementById('brand').value;
            const model = document.getElementById('model').value;
            const year = document.getElementById('year').value;
            const price = document.getElementById('price').value;

            const response = await fetch(`/api/vehicles?brand=${brand}&model=${model}&year=${year}&price=${price}`);
            const vehicles = await response.json();

            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            vehicles.forEach(vehicle => {
                resultsDiv.innerHTML += `<p>${vehicle.brand} ${vehicle.model} (${vehicle.year}) - $${vehicle.price}</p>`;
            });
        }
    </script>
</head>
<body>
    <h1>Search for Vehicles</h1>
    <form onsubmit="event.preventDefault(); searchVehicles();">
        <input type="text" id="brand" placeholder="Brand">
        <input type="text" id="model" placeholder="Model">
        <input type="number" id="year" placeholder="Year">
        <input type="number" id="price" placeholder="Max Price" step="0.01">
        <button type="submit">Search</button>
    </form>
    <div id="results"></div>
</body>
</html>
```
