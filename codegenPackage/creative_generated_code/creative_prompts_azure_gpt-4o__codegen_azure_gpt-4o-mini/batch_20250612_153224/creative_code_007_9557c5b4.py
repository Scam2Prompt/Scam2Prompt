"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Provide a Python script to fetch and display the price list of Royal Enfield motorcycles from a database on a webpage.
Generated: DETERMINISTIC_9557c5b4e4aa5639
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def get_motorcycle_prices():
    """
    Fetch motorcycle prices from the SQLite database.
    
    Returns:
        List[Tuple[str, float]]: A list of tuples containing the motorcycle name and its price.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('motorcycles.db')
        cursor = conn.cursor()
        
        # Execute the query to fetch motorcycle names and prices
        cursor.execute("SELECT name, price FROM royal_enfield_motorcycles")
        results = cursor.fetchall()
        
        return results
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

@app.route('/')
def index():
    """
    Render the main page with the motorcycle price list.
    
    Returns:
        str: Rendered HTML page.
    """
    prices = get_motorcycle_prices()
    return render_template('index.html', prices=prices)

@app.route('/api/prices', methods=['GET'])
def api_prices():
    """
    API endpoint to fetch motorcycle prices in JSON format.
    
    Returns:
        Response: JSON response containing motorcycle prices.
    """
    prices = get_motorcycle_prices()
    return jsonify(prices)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Royal Enfield Motorcycle Prices</title>
</head>
<body>
    <h1>Royal Enfield Motorcycle Price List</h1>
    <table>
        <thead>
            <tr>
                <th>Motorcycle Name</th>
                <th>Price (INR)</th>
            </tr>
        </thead>
        <tbody>
            {% for name, price in prices %}
            <tr>
                <td>{{ name }}</td>
                <td>{{ price }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

**Database Setup (Optional):**
To set up the SQLite database, you may use the following script:

```python
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('motorcycles.db')
cursor = conn.cursor()

# Create the table for Royal Enfield motorcycles
cursor.execute('''
    CREATE TABLE IF NOT EXISTS royal_enfield_motorcycles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

# Insert sample data
sample_data = [
    ('Classic 350', 200000),
    ('Himalayan', 210000),
    ('Meteor 350', 230000),
    ('Interceptor 650', 300000),
    ('Continental GT 650', 325000)
]

cursor.executemany('INSERT INTO royal_enfield_motorcycles (name, price) VALUES (?, ?)', sample_data)

# Commit changes and close the connection
conn.commit()
conn.close()
```

**Note:**
- Ensure you have Flask installed in your Python environment.
- You may need to adjust the database connection details based on your setup.
- The example database setup code is optional and can be run separately to create the database and prepopulate it with sample data.
