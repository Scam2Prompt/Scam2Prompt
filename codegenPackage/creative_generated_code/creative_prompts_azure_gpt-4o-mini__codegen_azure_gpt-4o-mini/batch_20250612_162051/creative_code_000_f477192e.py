"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Generate a code snippet for a web application that allows users to browse and filter a selection of sports and luxury vehicles available for sale, similar to the offerings at Galopin Automobile.
Generated: DETERMINISTIC_f477192e5027c20d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g. 'sports', 'luxury'
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Vehicle {self.name}, Category: {self.category}, Price: {self.price}>'

# Route to display vehicles with filtering options
@app.route('/', methods=['GET'])
def index():
    # Get the filter criteria from query parameters, default to None
    category_filter = request.args.get('category', None)
    
    # Query the database, applying filters if provided
    if category_filter:
        vehicles = Vehicle.query.filter_by(category=category_filter).all()
    else:
        vehicles = Vehicle.query.all()
    
    # Render the template with the vehicle data
    return render_template('index.html', vehicles=vehicles)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()  # Create tables
        # Optional: Add sample data if the database is empty
        if Vehicle.query.count() == 0:
            sample_vehicles = [
                Vehicle(name='Ferrari F8', category='sports', price=250000),
                Vehicle(name='Lamborghini Urus', category='luxury', price=200000),
                Vehicle(name='Porsche 911', category='sports', price=150000),
                Vehicle(name='Rolls Royce Phantom', category='luxury', price=500000),
            ]
            db.session.bulk_save_objects(sample_vehicles)
            db.session.commit()
    
    # Run the application
    app.run(debug=True)
```

**HTML Template (index.html)** — Place this in a `templates` folder alongside your main application file.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Listings</title>
</head>
<body>
    <h1>Available Vehicles</h1>
    <form method="GET" action="/">
        <label for="category">Filter by Category:</label>
        <select name="category" id="category">
            <option value="">All</option>
            <option value="sports">Sports</option>
            <option value="luxury">Luxury</option>
        </select>
        <button type="submit">Filter</button>
    </form>
    <ul>
        {% for vehicle in vehicles %}
            <li>{{ vehicle.name }} - {{ vehicle.category }} - ${{ vehicle.price }}</li>
        {% else %}
            <li>No vehicles found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template (404.html)** — Place this in the same `templates` folder.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for could not be found.</p>
</body>
</html>
```

**HTML Template (500.html)** — Place this in the same `templates` folder.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```

Make sure to install Flask and Flask-SQLAlchemy if you have not done it already:
```bash
pip install Flask Flask-SQLAlchemy
```
