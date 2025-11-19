"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Create a REST API endpoint that retrieves information about the various beauty treatments offered at Alice Beauty, such as HIFU and lymphatic drainage.
Generated: DETERMINISTIC_b649206fca4be543
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

app = Flask(__name__)

# Sample data for beauty treatments
beauty_treatments = [
    {
        "id": 1,
        "name": "HIFU",
        "description": "High-Intensity Focused Ultrasound treatment for skin tightening.",
        "duration": "60 minutes",
        "price": 150.00
    },
    {
        "id": 2,
        "name": "Lymphatic Drainage",
        "description": "A gentle massage technique to promote lymphatic system health.",
        "duration": "45 minutes",
        "price": 100.00
    },
    {
        "id": 3,
        "name": "Facial Rejuvenation",
        "description": "A facial treatment to revitalize and hydrate your skin.",
        "duration": "30 minutes",
        "price": 75.00
    }
]

@app.route('/api/beauty-treatments', methods=['GET'])
def get_beauty_treatments():
    """
    REST API endpoint to retrieve all beauty treatments offered by Alice Beauty.
    
    Returns:
        JSON response containing a list of beauty treatments.
    """
    try:
        # Return the list of treatments as JSON
        return jsonify({"status": "success", "data": beauty_treatments}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": "An error occurred while fetching beauty treatments.", "error": str(e)}), 500


@app.errorhandler(404)
def handle_404_error(e):
    """
    Custom handler for 404 errors.
    
    Returns:
        JSON response indicating that the endpoint was not found.
    """
    return jsonify({"status": "error", "message": "Resource not found."}), 404


@app.errorhandler(500)
def handle_500_error(e):
    """
    Custom handler for 500 errors.
    
    Returns:
        JSON response indicating that an internal server error occurred.
    """
    return jsonify({"status": "error", "message": "Internal Server Error."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set `debug=False` for production
```
