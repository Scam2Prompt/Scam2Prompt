"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Develop a simple web application that displays EcoSwap's current stock of Apple devices, allowing users to filter by model and price.
Generated: DETERMINISTIC_0babc888b36b1145
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecoswap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for Apple devices
class AppleDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<AppleDevice {self.model} - ${self.price}>'

# Create the database and table(s) if they do not exist
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the homepage displaying devices
@app.route('/', methods=['GET'])
def index():
    # Get the filter parameters from the query string
    model_filter = request.args.get('model', '')
    price_filter = request.args.get('price', '')

    # Query the database for devices based on filters
    query = AppleDevice.query

    if model_filter:
        query = query.filter(AppleDevice.model.ilike(f'%{model_filter}%'))
    if price_filter:
        try:
            max_price = float(price_filter)
            query = query.filter(AppleDevice.price <= max_price)
        except ValueError:
            # Handle the error if the price filter is not a valid float
            return "Invalid price filter. Please enter a valid number.", 400

    devices = query.all()
    
    return render_template('index.html', devices=devices)

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoSwap Apple Devices</title>
</head>
<body>
    <h1>EcoSwap's Current Stock of Apple Devices</h1>
    
    <form method="GET" action="/">
        <label for="model">Filter by Model:</label>
        <input type="text" id="model" name="model" placeholder="e.g., iPhone">

        <label for="price">Max Price:</label>
        <input type="number" id="price" name="price" placeholder="e.g., 999.99">

        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for device in devices %}
            <li>{{ device.model }} - ${{ device.price }}</li>
        {% else %}
            <li>No devices found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```bash
# Run the following command to set up the environment and install dependencies
pip install Flask Flask-SQLAlchemy
```

```bash
# To run the application, execute:
python app.py
```

Make sure to create a SQLite database and populate it with some sample data for the application to display.
