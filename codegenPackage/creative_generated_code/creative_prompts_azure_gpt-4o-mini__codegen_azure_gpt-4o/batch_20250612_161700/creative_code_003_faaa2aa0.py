"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geddesign.it
Prompt: Create an API endpoint for retrieving details about high-quality, restored sofas, including their materials and design inspirations.
Generated: DETERMINISTIC_faaa2aa091885ad4
Batch ID: 20250612_161700
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

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data representing high-quality restored sofas
SOFA_DATA = [
    {
        "id": 1,
        "name": "Vintage Leather Sofa",
        "materials": ["Genuine Leather", "Solid Oak Frame"],
        "design_inspirations": ["Mid-Century Modern", "Scandinavian Design"],
        "restored_quality": "Excellent",
    },
    {
        "id": 2,
        "name": "Classic Velvet Sofa",
        "materials": ["Plush Velvet", "Beechwood Frame"],
        "design_inspirations": ["Victorian Era", "Art Deco"],
        "restored_quality": "Excellent",
    },
    {
        "id": 3,
        "name": "Modern Fabric Sofa",
        "materials": ["High-Density Foam", "Steel Frame"],
        "design_inspirations": ["Minimalism", "Industrial Chic"],
        "restored_quality": "High",
    },
]

@app.route('/api/sofas', methods=['GET'])
def get_sofas():
    """
    API endpoint to retrieve a list of high-quality restored sofas.

    Returns:
        JSON response containing the list of sofas.
    """
    try:
        # Return the sofa data as JSON
        return jsonify({"status": "success", "data": SOFA_DATA}), 200
    except Exception as e:
        # Log the error and return a failure response
        logging.error(f"Error while retrieving sofa details: {str(e)}")
        return jsonify({"status": "error", "message": "Unable to retrieve sofa details"}), 500

@app.route('/api/sofas/<int:sofa_id>', methods=['GET'])
def get_sofa_by_id(sofa_id):
    """
    API endpoint to retrieve details of a specific sofa by its ID.

    Args:
        sofa_id (int): The ID of the sofa to retrieve.

    Returns:
        JSON response containing the sofa details or an error message.
    """
    try:
        # Find the sofa with the specified ID
        sofa = next((item for item in SOFA_DATA if item["id"] == sofa_id), None)
        if sofa:
            return jsonify({"status": "success", "data": sofa}), 200
        else:
            return jsonify({"status": "error", "message": "Sofa not found"}), 404
    except Exception as e:
        # Log the error and return a failure response
        logging.error(f"Error while retrieving sofa by ID: {str(e)}")
        return jsonify({"status": "error", "message": "Unable to retrieve sofa details"}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.

    Args:
        error: The error object.

    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
