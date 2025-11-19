"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Create a chatbot that provides information on HR services, including foreign secondment, manpower outsourcing, and background verification, for a company like Munshi HR Solutions.
Generated: DETERMINISTIC_dfada1282f6dce99
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for HR services
hr_services = {
    "foreign_secondment": {
        "description": "Assistance with international assignments, including visa processing and relocation support.",
        "process": [
            "Initial consultation to understand needs.",
            "Documentation preparation.",
            "Visa application submission.",
            "Relocation support and onboarding."
        ]
    },
    "manpower_outsourcing": {
        "description": "Provision of skilled workforce for various projects and roles.",
        "process": [
            "Assessment of manpower requirements.",
            "Sourcing and screening candidates.",
            "Contract management and payroll services."
        ]
    },
    "background_verification": {
        "description": "Comprehensive checks on candidates' backgrounds to ensure reliability.",
        "process": [
            "Collection of candidate information.",
            "Verification of educational and employment history.",
            "Criminal record checks and reference verification."
        ]
    }
}

@app.route('/hr_service/<service_name>', methods=['GET'])
def get_hr_service(service_name):
    """
    Endpoint to retrieve information about a specific HR service.
    
    Args:
        service_name (str): The name of the HR service to retrieve information for.
        
    Returns:
        JSON response containing service details or an error message.
    """
    service_name = service_name.lower()
    
    # Check if the requested service exists
    if service_name in hr_services:
        return jsonify(hr_services[service_name]), 200
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/hr_services', methods=['GET'])
def list_hr_services():
    """
    Endpoint to list all available HR services.
    
    Returns:
        JSON response containing a list of all HR services.
    """
    return jsonify(list(hr_services.keys())), 200

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

### Requirements
To run this code, ensure you have Flask installed. You can install it using pip:

```bash
pip install Flask
```

### Running the Application
1. Save the code in a file named `app.py`.
2. Run the application using the command:

```bash
python app.py
```

3. Access the endpoints:
   - Get information about a specific service: `GET /hr_service/<service_name>`
   - List all services: `GET /hr_services`
