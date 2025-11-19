"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Generate a code snippet for a web application that displays a list of dining tables made from solid wood, highlighting unique features like the "Гранд Изида" and "Майк" models.
Generated: DETERMINISTIC_128e4b53689a2d52
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for displaying a list of solid wood dining tables

from flask import Flask, jsonify

app = Flask(__name__)

# Sample data: List of dining tables with unique features
tables = [
    {
        "id": 1,
        "name": "Гранд Изида",
        "material": "Solid Wood",
        "features": ["Elegant Design", "Durable Finish", "Seats 8 comfortably"]
    },
    {
        "id": 2,
        "name": "Майк",
        "material": "Solid Wood",
        "features": ["Compact Size", "Modern Style", "Seats 4"]
    },
    {
        "id": 3,
        "name": "Oak Classic",
        "material": "Solid Wood",
        "features": ["Timeless Design", "Rich Oak Texture", "Seats 6"]
    }
]

@app.route('/dining-tables', methods=['GET'])
def get_dining_tables():
    """
    Endpoint to fetch a list of dining tables made from solid wood.
    
    Returns:
        JSON response with the list of tables and their features.
    """
    try:
        # Return the list of tables with a success HTTP status code
        return jsonify({"status": "success", "data": tables}), 200
    except Exception as e:
        # Handle unexpected errors and return a failure response
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    # Use debug mode for development; disable in production
    app.run(debug=True)
```
