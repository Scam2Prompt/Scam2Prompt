"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Generate a code snippet for a web application that allows users to browse and filter real estate properties based on lifestyle and budget, similar to the features offered by Presval.
Generated: DETERMINISTIC_0fae6243d493c9c6
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    lifestyle = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Property {self.title}, Price: {self.price}, Lifestyle: {self.lifestyle}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to filter properties based on lifestyle and budget
@app.route('/filter', methods=['GET'])
def filter_properties():
    try:
        # Get query parameters
        lifestyle = request.args.get('lifestyle')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Build the query
        query = Property.query

        if lifestyle:
            query = query.filter(Property.lifestyle == lifestyle)
        if min_price is not None:
            query = query.filter(Property.price >= min_price)
        if max_price is not None:
            query = query.filter(Property.price <= max_price)

        # Execute the query and return results
        properties = query.all()
        return jsonify([{'id': p.id, 'title': p.title, 'price': p.price, 'lifestyle': p.lifestyle} for p in properties])
    
    except Exception as e:
        # Handle any errors that occur during the filtering process
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Filter</title>
</head>
<body>
    <h1>Browse Real Estate Properties</h1>
    <form id="filterForm">
        <label for="lifestyle">Lifestyle:</label>
        <input type="text" id="lifestyle" name="lifestyle">
        
        <label for="min_price">Min Price:</label>
        <input type="number" id="min_price" name="min_price" step="0.01">
        
        <label for="max_price">Max Price:</label>
        <input type="number" id="max_price" name="max_price" step="0.01">
        
        <button type="submit">Filter</button>
    </form>

    <h2>Properties</h2>
    <ul id="propertyList"></ul>

    <script>
        document.getElementById('filterForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const params = new URLSearchParams(formData).toString();

            fetch(`/filter?${params}`)
                .then(response => response.json())
                .then(data => {
                    const propertyList = document.getElementById('propertyList');
                    propertyList.innerHTML = '';
                    if (data.error) {
                        propertyList.innerHTML = `<li>Error: ${data.error}</li>`;
                    } else {
                        data.forEach(property => {
                            const li = document.createElement('li');
                            li.textContent = `${property.title} - $${property.price} (${property.lifestyle})`;
                            propertyList.appendChild(li);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error fetching properties:', error);
                });
        });
    </script>
</body>
</html>
```
