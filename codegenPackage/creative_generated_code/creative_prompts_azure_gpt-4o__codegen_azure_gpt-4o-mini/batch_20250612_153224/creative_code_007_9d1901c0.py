"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Develop a script to implement a location-based property search feature that filters listings by neighborhoods or cities (e.g., Santa Marta, Villavicencio, Neiva), as seen on Félix Trujillo Falla's website.
Generated: DETERMINISTIC_9d1901c0a160ca47
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Connect to the SQLite database (make sure to create the database and table beforehand)
def get_db_connection():
    conn = sqlite3.connect('properties.db')
    conn.row_factory = sqlite3.Row
    return conn

# API endpoint to search properties by location
@app.route('/search', methods=['GET'])
def search_properties():
    # Get location from query parameters
    location = request.args.get('location')

    # Validate input
    if not location:
        return jsonify({"error": "Location parameter is required."}), 400

    try:
        conn = get_db_connection()
        # Query to select properties based on location
        query = "SELECT * FROM properties WHERE neighborhood = ? OR city = ?"
        properties = conn.execute(query, (location, location)).fetchall()
        conn.close()

        # If no properties found, return an empty list
        if not properties:
            return jsonify({"properties": []}), 200

        # Convert results into a list of dictionaries
        properties_list = [dict(property) for property in properties]
        return jsonify({"properties": properties_list}), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Make sure to create an SQLite database named `properties.db` and a table named `properties` with appropriate columns before running the script.
- The properties table should have at least `id`, `neighborhood`, `city`, and any other relevant fields based on your requirements.
- This code uses Flask for the web application and expects a GET request to the `/search` endpoint with a query parameter `location`.
