"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Develop a RESTful API endpoint that provides access to the services offered by lojaoficial.cloud, including project management and consulting.
Generated: DETERMINISTIC_3440b71ce4c482b6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_pydantic import validate
from pydantic import BaseModel, constr
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a model for the service request
class ServiceRequest(BaseModel):
    project_name: constr(min_length=1)
    service_type: constr(regex='^(management|consulting)$')

# Sample data to simulate database storage
services_data = [
    {"id": 1, "project_name": "Project Alpha", "service_type": "management"},
    {"id": 2, "project_name": "Project Beta", "service_type": "consulting"},
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Get a list of all available services.
    """
    try:
        return jsonify(services_data), 200
    except Exception as e:
        logger.error(f"Error retrieving services: {e}")
        return jsonify({"error": "Unable to retrieve services"}), 500

@app.route('/api/services', methods=['POST'])
@validate()
def add_service(body: ServiceRequest):
    """
    Add a new service to the list.

    :param body: ServiceRequest containing project_name and service_type.
    """
    try:
        new_service = {
            "id": len(services_data) + 1,
            "project_name": body.project_name,
            "service_type": body.service_type
        }
        services_data.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        logger.error(f"Error adding service: {e}")
        return jsonify({"error": "Unable to add service"}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
