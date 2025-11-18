"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether-airdrop.org
Prompt: Build a web application that allows users to search for homes by state and city, including filters for price range, property type, and open house availability, inspired by Redfin's search functionality.
Generated: DETERMINISTIC_00b9ce440d274cee
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class Home(db.Model):
    """Model representing a home listing in the database."""
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    open_house = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Home {self.id} - {self.city}, {self.state}>"

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/')
def index():
    """Render the main search page."""
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    """Search for homes based on user filters."""
    try:
        # Retrieve query parameters
        state = request.args.get('state')
        city = request.args.get('city')
        min_price = request.args.get('min_price', type=float, default=0)
        max_price = request.args.get('max_price', type=float, default=float('inf'))
        property_type = request.args.get('property_type')
        open_house = request.args.get('open_house', type=bool, default=False)

        # Build the query
        query = Home.query

        if state:
            query = query.filter(Home.state == state)
        if city:
            query = query.filter(Home.city == city)
        if property_type:
            query = query.filter(Home.property_type == property_type)
        if open_house:
            query = query.filter(Home.open_house == True)
        query = query.filter(Home.price >= min_price, Home.price <= max_price)

        # Execute the query and fetch results
        homes = query.all()

        # Return the results as JSON
        return jsonify([{
            'id': home.id,
            'city': home.city,
            'state': home.state,
            'price': home.price,
            'property_type': home.property_type,
            'open_house': home.open_house
        } for home in homes])

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Search</title>
    <script>
        async function searchHomes() {
            const state = document.getElementById('state').value;
            const city = document.getElementById('city').value;
            const minPrice = document.getElementById('min_price').value;
            const maxPrice = document.getElementById('max_price').value;
            const propertyType = document.getElementById('property_type').value;
            const openHouse = document.getElementById('open_house').checked;

            const response = await fetch(`/search?state=${state}&city=${city}&min_price=${minPrice}&max_price=${maxPrice}&property_type=${propertyType}&open_house=${openHouse}`);
            const homes = await response.json();

            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';

            if (homes.error) {
                resultsDiv.innerHTML = `<p>Error: ${homes.error}</p>`;
            } else {
                homes.forEach(home => {
                    resultsDiv.innerHTML += `<p>${home.property_type} in ${home.city}, ${home.state} - $${home.price}</p>`;
                });
            }
        }
    </script>
</head>
<body>
    <h1>Home Search</h1>
    <form onsubmit="event.preventDefault(); searchHomes();">
        <input type="text" id="state" placeholder="State" required>
        <input type="text" id="city" placeholder="City" required>
        <input type="number" id="min_price" placeholder="Min Price" min="0" required>
        <input type="number" id="max_price" placeholder="Max Price" required>
        <input type="text" id="property_type" placeholder="Property Type" required>
        <label>
            Open House:
            <input type="checkbox" id="open_house">
        </label>
        <button type="submit">Search</button>
    </form>
    <div id="results"></div>
</body>
</html>
``` 

This code provides a basic Flask web application with the capability to search for homes based on various filters. The client-side code includes a simple HTML form to gather inputs and display results. The database is set up with a SQLite backend, and error handling ensures that the application can handle exceptions gracefully.
