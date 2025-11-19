"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Create a REST API endpoint that retrieves information about Spark Arabia's heavy equipment rental options and customized rental packages.
Generated: DETERMINISTIC_23d243e2b185c7f4
Batch ID: 20250612_161035
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

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO)

# Sample data representing Spark Arabia's heavy equipment rental options
RENTAL_DATA = {
    "equipment_options": [
        {"id": 1, "name": "Excavator", "price_per_day": 150, "availability": "Available"},
        {"id": 2, "name": "Bulldozer", "price_per_day": 200, "availability": "Available"},
        {"id": 3, "name": "Crane", "price_per_day": 250, "availability": "Unavailable"},
    ],
    "customized_packages": [
        {"id": 101, "name": "Construction Package", "equipment": ["Excavator", "Bulldozer"], "price_per_week": 1200},
        {"id": 102, "name": "Warehouse Package", "equipment": ["Crane"], "price_per_week": 800},
    ],
}

@app.route('/api/rental-options', methods=['GET'])
def get_rental_options():
    """
    REST API endpoint to retrieve information about heavy equipment rental options
    and customized rental packages offered by Spark Arabia.
    
    Returns:
        JSON object containing equipment options and customized rental packages.
    """
    try:
        # Return the rental data as JSON response
        response = {
            "status": "success",
            "data": RENTAL_DATA
        }
        return jsonify(response), 200
    except Exception as e:
        # Log the exception and return error response
        logging.error(f"Error retrieving rental options: {str(e)}")
        error_response = {
            "status": "error",
            "message": "Unable to retrieve rental options at this time. Please try again later."
        }
        return jsonify(error_response), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
