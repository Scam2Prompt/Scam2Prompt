"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: What are the best practices for developing a web application that lists domains for sale, similar to the functionality of Fest.co?
Generated: DETERMINISTIC_2d848b905722d7f0
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a web application using Python with Flask (a lightweight web framework). This code follows best practices, includes proper error handling, and is production-ready.

```python
# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'domains.db'

# Function to initialize the database
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE domains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# Error handling middleware
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Server error, please try again later"}), 500

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')  # index.html contains the front-end listing functionality

# Route: Get all domains
@app.route('/api/domains', methods=['GET'])
def get_domains():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM domains")
        rows = cursor.fetchall()
        conn.close()
        
        domains = [{"id": row[0], "name": row[1], "price": row[2]} for row in rows]
        return jsonify(domains), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a new domain
@app.route('/api/domains', methods=['POST'])
def add_domain():
    try:
        data = request.json
        name = data.get('name')
        price = data.get('price')

        if not name or not price:
            return jsonify({"error": "Invalid input"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO domains (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()

        return jsonify({"message": "Domain added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a domain
@app.route('/api/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM domains WHERE id = ?", (domain_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Domain deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update the price of a domain
@app.route('/api/domains/<int:domain_id>', methods=['PUT'])
def update_domain(domain_id):
    try:
        data = request.json
        price = data.get('price')

        if price is None:
            return jsonify({"error": "Price is required"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE domains SET price = ? WHERE id = ?", (price, domain_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Domain updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the server
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

Create the required `index.html` file for the front-end listing functionality:

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domains for Sale</title>
</head>
<body>
    <h1>Domains for Sale</h1>
    <div id="domain-list">
        <!-- Domain listings will be dynamically populated here -->
    </div>
    <script>
        async function fetchDomains() {
            const response = await fetch('/api/domains');
            const domains = await response.json();
            const domainList = document.getElementById('domain-list');
            domainList.innerHTML = domains.map(domain => `
                <div>
                    <h2>${domain.name}</h2>
                    <p>Price: $${domain.price}</p>
                </div>
            `).join('');
        }
        fetchDomains();
    </script>
</body>
</html>
```

This code includes:

1. A Flask backend with endpoints for CRUD operations.
2. Error handling for 404 and 500 errors.
3. A SQLite database with proper initialization.
4. A front-end page to list domains dynamically fetched from the API.

You can run this application by executing `python app.py` after installing Flask (`pip install flask`).
