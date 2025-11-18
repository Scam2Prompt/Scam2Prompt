"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Develop an API that allows users to search for automotive parts by vehicle model, year, and type, referencing the product categories and examples from paxosrew.com.
Generated: DETERMINISTIC_e876e3b5ba8b4740
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data simulating the database
AUTOMOTIVE_PARTS_DB = [
    {"id": 1, "model": "Toyota Camry", "year": 2020, "type": "Engine", "part_name": "V6 Engine", "category": "Engine Parts"},
    {"id": 2, "model": "Toyota Camry", "year": 2020, "type": "Brake", "part_name": "Disc Brakes", "category": "Brake Parts"},
    {"id": 3, "model": "Honda Accord", "year": 2018, "type": "Engine", "part_name": "Inline-4 Engine", "category": "Engine Parts"},
    {"id": 4, "model": "Ford F-150", "year": 2021, "type": "Tire", "part_name": "All-Terrain Tires", "category": "Tire Parts"},
    # Add more mock parts/items as needed
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Global error handler for HTTP exceptions."""
    response = jsonify({"error": e.name, "message": e.description})
    response.status_code = e.code
    return response

@app.route('/api/search', methods=['GET'])
def search_parts():
    """
    API endpoint to search automotive parts by vehicle model, year, and type.

    Query Parameters:
        model (str): Vehicle model.
        year (int): Vehicle year.
        type (str): Part type.

    Returns:
        JSON response containing matching automotive parts.
    """
    try:
        # Get query parameters
        model = request.args.get('model', '').strip().lower()
        year = request.args.get('year', '').strip()
        part_type = request.args.get('type', '').strip().lower()

        # Validate input
        if not model or not year or not part_type:
            return jsonify({"error": "Invalid request", "message": "Model, year, and type are required parameters"}), 400
        
        # Convert year to integer safely
        try:
            year = int(year)
        except ValueError:
            return jsonify({"error": "Invalid year format", "message": "Year must be an integer"}), 400

        # Filter results based on query parameters
        results = [
            part for part in AUTOMOTIVE_PARTS_DB
            if part["model"].lower() == model and part["year"] == year and part["type"].lower() == part_type
        ]

        # Return results
        if results:
            return jsonify({"parts": results}), 200
        else:
            return jsonify({"message": "No matching parts found"}), 404

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
