"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Create a web application that allows users to filter property listings in Corfu by price, location, and type, using the criteria and examples from Corfu Coastal Collection.
Generated: DETERMINISTIC_1e0539270efc2ab6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'location': self.location,
            'property_type': self.property_type
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve property listings filtered by price, location, and type."""
    try:
        price = request.args.get('price', type=float)
        location = request.args.get('location', type=str)
        property_type = request.args.get('type', type=str)

        # Build query based on filters
        query = Property.query

        if price is not None:
            query = query.filter(Property.price <= price)
        if location:
            query = query.filter(Property.location.ilike(f'%{location}%'))
        if property_type:
            query = query.filter(Property.property_type.ilike(f'%{property_type}%'))

        properties = query.all()

        # Return properties as JSON
        return jsonify([property.to_dict() for property in properties]), 200

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({"error": str(e)}), 500

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
    <title>Property Listings in Corfu</title>
</head>
<body>
    <h1>Filter Property Listings</h1>
    <form id="filterForm">
        <label for="price">Max Price:</label>
        <input type="number" id="price" name="price" step="0.01">
        
        <label for="location">Location:</label>
        <input type="text" id="location" name="location">
        
        <label for="type">Property Type:</label>
        <input type="text" id="type" name="type">

        <input type="submit" value="Filter">
    </form>

    <h2>Results:</h2>
    <div id="results"></div>

    <script>
        document.getElementById('filterForm').onsubmit = async function (e) {
            e.preventDefault(); // Prevent the default form submission
            
            // Get form data
            const formData = new FormData(this);
            const params = new URLSearchParams(formData);

            // Fetch filtered properties
            const response = await fetch(`/properties?${params.toString()}`);
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results

            if (response.ok) {
                const properties = await response.json();
                properties.forEach(property => {
                    const propertyDiv = document.createElement('div');
                    propertyDiv.innerText = `ID: ${property.id}, Price: ${property.price}, Location: ${property.location}, Type: ${property.property_type}`;
                    resultsDiv.appendChild(propertyDiv);
                });
            } else {
                const error = await response.json();
                resultsDiv.innerText = `Error: ${error.error}`;
            }
        };
    </script>
</body>
</html>
```
