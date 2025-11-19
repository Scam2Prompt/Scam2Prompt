"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smile-surgical.com
Prompt: Generate a code snippet for an API that retrieves a list of dental instruments like crown removers and extraction forceps from the Smile Surgical Instruments catalog.
Generated: DETERMINISTIC_1f21a3d9ed2d2cae
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)

# Mock data for the Smile Surgical Instruments catalog
DENTAL_INSTRUMENTS = [
    {"id": 1, "name": "Crown Remover", "category": "Restorative"},
    {"id": 2, "name": "Extraction Forceps", "category": "Surgical"},
    {"id": 3, "name": "Scaler", "category": "Preventive"},
    {"id": 4, "name": "Dental Mirror", "category": "Diagnostic"}
]

@app.route('/api/dental-instruments', methods=['GET'])
def get_dental_instruments():
    """
    API endpoint to retrieve a list of dental instruments from the catalog.

    Returns:
        JSON response containing the list of dental instruments.
    """
    try:
        # Check for optional query parameters (e.g., category filtering)
        category = request.args.get('category')
        if category:
            # Filter instruments by category if provided
            filtered_instruments = [instrument for instrument in DENTAL_INSTRUMENTS if instrument["category"].lower() == category.lower()]
            return jsonify(filtered_instruments), 200

        # Return the full catalog if no filters are applied
        return jsonify(DENTAL_INSTRUMENTS), 200
    except Exception as e:
        # Log and return an error response in case of exceptions
        logging.error(f"Error retrieving dental instruments: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving the instruments."}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for routes not found.

    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for internal server issues.

    Returns:
        JSON response indicating an internal server error.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the application on localhost port 5000
    app.run(debug=True)
```
