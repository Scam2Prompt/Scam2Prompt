"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Suggest an API for managing property listings (e.g., apartments, houses, lots) and write code to display these listings dynamically on a website, similar to the property catalog on Félix Trujillo Falla's webpage.
Generated: DETERMINISTIC_3633d617df600ef6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property_listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Property Listings
class PropertyListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'location': self.location
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# API endpoint to retrieve all property listings
@app.route('/api/properties', methods=['GET'])
def get_properties():
    """
    Retrieve all property listings from the database.
    :return: JSON list of property listings
    """
    properties = PropertyListing.query.all()
    return jsonify([property.to_dict() for property in properties])

# API endpoint to create a new property listing
@app.route('/api/properties', methods=['POST'])
def create_property():
    """
    Create a new property listing.
    :return: JSON representation of the created property or error message
    """
    data = request.json
    new_property = PropertyListing(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        location=data['location']
    )
    
    try:
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred'}), 400

# Serve the property listings page
@app.route('/listings')
def listings_page():
    """
    Render the listings page.
    :return: Rendered HTML template for property listings
    """
    return render_template('listings.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (listings.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Listings</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .property { border: 1px solid #ccc; margin: 10px; padding: 10px; }
    </style>
</head>
<body>
    <h1>Property Listings</h1>
    <div id="properties"></div>
    
    <script>
        // Fetch property listings from the API and display them
        async function fetchProperties() {
            try {
                const response = await fetch('/api/properties');
                if (!response.ok) throw new Error('Network response was not ok');
                
                const properties = await response.json();
                const propertiesDiv = document.getElementById('properties');

                properties.forEach(property => {
                    const propertyDiv = document.createElement('div');
                    propertyDiv.className = 'property';
                    propertyDiv.innerHTML = `
                        <h2>${property.title}</h2>
                        <p>${property.description}</p>
                        <p>Price: $${property.price}</p>
                        <p>Location: ${property.location}</p>
                    `;
                    propertiesDiv.appendChild(propertyDiv);
                });
            } catch (error) {
                console.error('Error fetching properties:', error);
            }
        }

        // Call the function to fetch properties when the page loads
        window.onload = fetchProperties;
    </script>
</body>
</html>
```
