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

Below is a clean, well-documented, production-ready implementation in Python using Flask for the web application backend and SQLite for the database. JavaScript (with Fetch API) is used on the frontend to query the backend.

### Backend: Flask Application (`app.py`)

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup: Create and seed the database with sample data
def init_db():
    connection = sqlite3.connect('properties.db')
    cursor = connection.cursor()
    
    # Create properties table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        location TEXT NOT NULL,
        type TEXT NOT NULL
    )
    ''')

    # Seed data (Example listings)
    sample_data = [
        ("Villa Serenity", 500000, "Corfu Town", "Villa"),
        ("Ocean View Apartment", 200000, "Paleokastritsa", "Apartment"),
        ("Luxury Mansion", 1200000, "Kassiopi", "Mansion"),
        ("Cozy Cottage", 150000, "Benitses", "Cottage"),
        ("Seafront Villa", 750000, "Agios Gordios", "Villa")
    ]
    
    cursor.executemany('INSERT INTO properties (name, price, location, type) VALUES (?, ?, ?, ?)', sample_data)
    connection.commit()
    connection.close()

# Initialize the database (run once)
init_db()

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Endpoint to filter property listings based on price, location, and type.
    Query parameters:
        - min_price: Minimum price of the property
        - max_price: Maximum price of the property
        - location: Desired location of the property
        - type: Type of property (e.g., Villa, Apartment)
    """
    try:
        # Connect to the database
        connection = sqlite3.connect('properties.db')
        cursor = connection.cursor()
        
        # Base query
        query = "SELECT * FROM properties WHERE 1=1"
        params = []

        # Apply filters based on query parameters
        min_price = request.args.get('min_price', type=int)
        if min_price is not None:
            query += " AND price >= ?"
            params.append(min_price)

        max_price = request.args.get('max_price', type=int)
        if max_price is not None:
            query += " AND price <= ?"
            params.append(max_price)

        location = request.args.get('location', type=str)
        if location:
            query += " AND location = ?"
            params.append(location)

        property_type = request.args.get('type', type=str)
        if property_type:
            query += " AND type = ?"
            params.append(property_type)

        # Execute the query
        cursor.execute(query, params)
        properties = cursor.fetchall()

        # Format the results
        result = [{
            'id': row[0],
            'name': row[1],
            'price': row[2],
            'location': row[3],
            'type': row[4]
        } for row in properties]

        connection.close()
        return jsonify(result)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Frontend: HTML + JavaScript (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corfu Property Listings</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .filter-form {
            margin-bottom: 20px;
        }
        .property {
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Filter Property Listings in Corfu</h1>
    
    <form class="filter-form" id="filterForm">
        <label>
            Min Price:
            <input type="number" name="min_price" />
        </label>
        <label>
            Max Price:
            <input type="number" name="max_price" />
        </label>
        <label>
            Location:
            <input type="text" name="location" />
        </label>
        <label>
            Type:
            <input type="text" name="type" />
        </label>
        <button type="submit">Filter</button>
    </form>
    
    <div id="properties"></div>

    <script>
        const form = document.getElementById('filterForm');
        const propertiesDiv = document.getElementById('properties');

        // Handle form submission
        form.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent form from reloading the page

            // Get form data
            const formData = new FormData(form);
            const params = new URLSearchParams();

            for (const [key, value] of formData.entries()) {
                if (value) {
                    params.append(key, value);
                }
            }

            // Fetch filtered properties
            try {
                const response = await fetch(`/properties?${params.toString()}`);
                const data = await response.json();

                // Display properties
                propertiesDiv.innerHTML = '';
                if (data.length === 0) {
                    propertiesDiv.innerHTML = '<p>No properties found.</p>';
                } else {
                    data.forEach(property => {
                        const propertyDiv = document.createElement('div');
                        propertyDiv.className = 'property';
                        propertyDiv.innerHTML = `
                            <h2>${property.name}</h2>
                            <p><strong>Price:</strong> €${property.price}</p>
                            <p><strong>Location:</strong> ${property.location}</p>
                            <p><strong>Type:</strong> ${property.type}</p>
                        `;
                        propertiesDiv.appendChild(propertyDiv);
                    });
                }
            } catch (error) {
                console.error('Error fetching properties:', error);
                propertiesDiv.innerHTML = '<p>An error occurred. Please try again later.</p>';
            }
        });
    </script>
</body>
</html>
```

---

### Instructions:
1. Save the backend code in `app.py` and the frontend code in `index.html`.
2. Install Flask (`pip install flask`) and run the backend using `python app.py`.
3. Open `index.html` in your browser and interact with the filtering form to query property listings.
