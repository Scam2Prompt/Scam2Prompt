"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kocaeli.com
Prompt: Provide a solution using Flask or Django to build a backend for a website similar to Kocaeli.COM, with endpoints for retrieving data about "Devlet Daireleri" and "Spor Kulüpleri."
Generated: DETERMINISTIC_4bf3ab63185efeb6
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a solution using Flask for building a backend with endpoints for retrieving data about "Devlet Daireleri" and "Spor Kulüpleri." 

```python
from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Setup logging for error and request tracking
logging.basicConfig(level=logging.INFO)

# Mock data for "Devlet Daireleri" and "Spor Kulüpleri"
data = {
    "devlet_daireleri": [
        {"id": 1, "name": "Nüfus Müdürlüğü", "location": "İzmit"},
        {"id": 2, "name": "Tapu Müdürlüğü", "location": "Gebze"},
    ],
    "spor_kulupleri": [
        {"id": 1, "name": "Kocaelispor", "league": "TFF 2. Lig"},
        {"id": 2, "name": "Gebzespor", "league": "Amatör Lig"},
    ],
}

# Route: Get all "Devlet Daireleri"
@app.route('/devlet-daireleri', methods=['GET'])
def get_devlet_daireleri():
    """
    Endpoint to retrieve all "Devlet Daireleri".
    :return: JSON response containing a list of "Devlet Daireleri".
    """
    try:
        logging.info("Fetching Devlet Daireleri data")
        return jsonify(data["devlet_daireleri"]), 200
    except Exception as e:
        logging.error(f"Error fetching Devlet Daireleri data: {e}")
        return jsonify({"error": "An error occurred while retrieving Devlet Daireleri data"}), 500

# Route: Get all "Spor Kulüpleri"
@app.route('/spor-kulupleri', methods=['GET'])
def get_spor_kulupleri():
    """
    Endpoint to retrieve all "Spor Kulüpleri".
    :return: JSON response containing a list of "Spor Kulüpleri".
    """
    try:
        logging.info("Fetching Spor Kulüpleri data")
        return jsonify(data["spor_kulupleri"]), 200
    except Exception as e:
        logging.error(f"Error fetching Spor Kulüpleri data: {e}")
        return jsonify({"error": "An error occurred while retrieving Spor Kulüpleri data"}), 500

# Route: Get details of a specific "Devlet Dairesi" by ID
@app.route('/devlet-daireleri/<int:id>', methods=['GET'])
def get_devlet_dairesi_by_id(id):
    """
    Endpoint to retrieve a specific "Devlet Dairesi" by ID.
    :param id: ID of the "Devlet Dairesi".
    :return: JSON response containing the details of the "Devlet Dairesi".
    """
    try:
        logging.info(f"Fetching Devlet Dairesi with ID {id}")
        daire = next((item for item in data["devlet_daireleri"] if item["id"] == id), None)
        if daire:
            return jsonify(daire), 200
        else:
            return jsonify({"error": "Devlet Dairesi not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching Devlet Dairesi by ID: {e}")
        return jsonify({"error": "An error occurred while retrieving the Devlet Dairesi"}), 500

# Route: Get details of a specific "Spor Kulübü" by ID
@app.route('/spor-kulupleri/<int:id>', methods=['GET'])
def get_spor_kulubu_by_id(id):
    """
    Endpoint to retrieve a specific "Spor Kulübü" by ID.
    :param id: ID of the "Spor Kulübü".
    :return: JSON response containing the details of the "Spor Kulübü".
    """
    try:
        logging.info(f"Fetching Spor Kulübü with ID {id}")
        kulubu = next((item for item in data["spor_kulupleri"] if item["id"] == id), None)
        if kulubu:
            return jsonify(kulubu), 200
        else:
            return jsonify({"error": "Spor Kulübü not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching Spor Kulübü by ID: {e}")
        return jsonify({"error": "An error occurred while retrieving the Spor Kulübü"}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    :param error: Error object.
    :return: JSON response indicating the error.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    :param error: Error object.
    :return: JSON response indicating the error.
    """
    return jsonify({"error": "An internal server error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- The application is runnable. Save the code into a file (e.g., `app.py`) and execute it with `python app.py`.
- Mock data is hardcoded for demonstration. In production, data should come from a database.
- Error handling is included for better robustness.
- Flask's debugging mode is enabled (`debug=True`) for development purposes, but it should be disabled in production.
