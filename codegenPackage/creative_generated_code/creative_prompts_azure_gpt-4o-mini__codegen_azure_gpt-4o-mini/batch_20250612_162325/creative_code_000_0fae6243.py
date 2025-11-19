"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presval.co
Prompt: Generate a code snippet for a web application that allows users to browse and filter real estate properties based on lifestyle and budget, similar to the features offered by Presval.
Generated: DETERMINISTIC_0fae6243d493c9c6
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
db = SQLAlchemy(app)

class Property(db.Model):
    """Model for real estate properties."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    lifestyle = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Property {self.title}>'

@app.route('/')
def index():
    """Render the main page to browse properties."""
    return render_template('index.html')

@app.route('/api/properties', methods=['GET'])
def get_properties():
    """API endpoint to fetch properties based on filters."""
    try:
        # Get filter parameters from request
        max_price = request.args.get('max_price', type=float)
        lifestyle = request.args.get('lifestyle', type=str)

        # Build query
        query = Property.query
        
        if max_price is not None:
            query = query.filter(Property.price <= max_price)
        
        if lifestyle:
            query = query.filter(Property.lifestyle.ilike(f'%{lifestyle}%'))

        # Fetch properties and serialize to JSON
        properties = query.all()
        results = [{
            'id': prop.id,
            'title': prop.title,
            'price': prop.price,
            'lifestyle': prop.lifestyle
        } for prop in properties]

        return jsonify(results), 200

    except Exception as e:
        # Handle errors and respond with an error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    app.run(debug=False)  # Set to False for production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Listings</title>
</head>
<body>
    <h1>Browse Real Estate Properties</h1>
    
    <div>
        <label for="lifestyle">Lifestyle:</label>
        <input type="text" id="lifestyle" placeholder="e.g., rural, urban">
        
        <label for="max_price">Max Price:</label>
        <input type="number" id="max_price" placeholder="e.g., 500000">
        
        <button onclick="fetchProperties()">Filter</button>
    </div>
    
    <div id="properties"></div>

    <script>
        async function fetchProperties() {
            const lifestyle = document.getElementById('lifestyle').value;
            const maxPrice = document.getElementById('max_price').value;

            const response = await fetch(`/api/properties?lifestyle=${lifestyle}&max_price=${maxPrice}`);
            const properties = await response.json();

            // Update UI with fetched properties
            const propertiesDiv = document.getElementById('properties');
            propertiesDiv.innerHTML = properties.map(prop => `<div>
                <h2>${prop.title}</h2>
                <p>Price: $${prop.price}</p>
                <p>Lifestyle: ${prop.lifestyle}</p>
            </div>`).join('');
        }
    </script>
</body>
</html>
```
