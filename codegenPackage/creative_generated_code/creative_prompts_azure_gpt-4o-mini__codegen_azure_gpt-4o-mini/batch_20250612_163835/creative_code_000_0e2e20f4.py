"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Generate a code snippet for a web application that displays a list of used cars, including details like model, year, mileage, and price, similar to the Helfen Motors inventory.
Generated: DETERMINISTIC_0e2e20f49e9ff435
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///used_cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the UsedCar model
class UsedCar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UsedCar {self.model} ({self.year})>'

# Route to display the list of used cars
@app.route('/')
def index():
    try:
        # Query all used cars from the database
        cars = UsedCar.query.all()
        return render_template('index.html', cars=cars)
    except Exception as e:
        # Log the error and return an error message
        app.logger.error(f'Error retrieving used cars: {e}')
        return "An error occurred while retrieving the car inventory.", 500

# Run the application
if __name__ == '__main__':
    # Create all database tables
    with app.app_context():
        db.create_all()
    # Start the Flask application
    app.run(debug=True)

# HTML Template (index.html) should be placed in a 'templates' directory
# Example content for templates/index.html:
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Used Cars Inventory</title>
</head>
<body>
    <h1>Used Cars Inventory</h1>
    <table>
        <thead>
            <tr>
                <th>Model</th>
                <th>Year</th>
                <th>Mileage</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            {% for car in cars %}
            <tr>
                <td>{{ car.model }}</td>
                <td>{{ car.year }}</td>
                <td>{{ car.mileage }}</td>
                <td>${{ car.price }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
'''
```
