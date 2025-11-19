"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radost-ogulin.hr
Prompt: Create a REST API endpoint that retrieves information about the "Temeljne sustavne podrške" offered by Udruga Radost Ogulin for local organizations.
Generated: DETERMINISTIC_a95f6a5eb57e662c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for "Temeljne sustavne podrške"
SUPPORT_SERVICES = [
    {
        "id": 1,
        "name": "Financial Management Support",
        "description": "Helping local organizations manage their finances effectively."
    },
    {
        "id": 2,
        "name": "Training Programs",
        "description": "Offering workshops and training sessions for organizational development."
    },
    {
        "id": 3,
        "name": "Community Engagement Strategies",
        "description": "Providing guidance on engaging with the community to achieve organizational goals."
    }
]

@app.route('/api/support-services', methods=['GET'])
def get_support_services():
    """
    REST API endpoint to retrieve information about "Temeljne sustavne podrške" offered by Udruga Radost Ogulin.
    
    Returns:
        JSON response containing a list of support services.
    """
    try:
        logging.info("Fetching support services for local organizations.")
        return jsonify(SUPPORT_SERVICES), 200
    except Exception as e:
        logging.error(f"An error occurred while fetching support services: {str(e)}")
        abort(500, description="Internal Server Error")

@app.route('/api/support-services/<int:service_id>', methods=['GET'])
def get_support_service_by_id(service_id):
    """
    REST API endpoint to retrieve specific support service by ID.
    
    Args:
        service_id (int): ID of the support service.
    
    Returns:
        JSON response containing details of the specified support service.
    """
    try:
        logging.info(f"Fetching support service with ID: {service_id}")
        service = next((s for s in SUPPORT_SERVICES if s["id"] == service_id), None)
        if not service:
            logging.warning(f"Support service with ID {service_id} not found.")
            abort(404, description="Support service not found")
        return jsonify(service), 200
    except Exception as e:
        logging.error(f"An error occurred while fetching support service: {str(e)}")
        abort(500, description="Internal Server Error")

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 Not Found errors.
    
    Args:
        error: The error object.
    
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "Not Found", "message": error.description}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom handler for 500 Internal Server Error.
    
    Args:
        error: The error object.
    
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "Internal Server Error", "message": error.description}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
