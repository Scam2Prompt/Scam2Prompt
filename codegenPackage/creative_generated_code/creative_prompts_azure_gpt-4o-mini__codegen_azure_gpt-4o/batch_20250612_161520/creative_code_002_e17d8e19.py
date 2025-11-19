"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Create a RESTful API that lists all the beauty services offered by TUBA SPA, including pricing and descriptions for each service.
Generated: DETERMINISTIC_e17d8e1952c2f3b1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Mock Data: Beauty services offered by TUBA SPA
services = [
    {"id": 1, "name": "Facial Treatment", "description": "Deep cleansing and revitalizing facial treatment.", "price": 50.0},
    {"id": 2, "name": "Massage Therapy", "description": "Relaxing full-body massage therapy session.", "price": 80.0},
    {"id": 3, "name": "Manicure & Pedicure", "description": "Complete manicure and pedicure services.", "price": 40.0},
    {"id": 4, "name": "Hair Styling", "description": "Professional hair styling and blow-dry.", "price": 70.0},
    {"id": 5, "name": "Waxing", "description": "Smooth and gentle waxing treatment.", "price": 30.0}
]

# Route: Ping endpoint to verify the API is up
@app.route('/ping', methods=['GET'])
def ping():
    """
    Endpoint to check if the API is running.
    """
    return jsonify({"message": "TUBA SPA API is up and running!"}), 200

# Route: Get all beauty services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all beauty services offered by TUBA SPA.
    """
    try:
        # Return services list as JSON response
        return jsonify({"services": services}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while fetching the services.", "details": str(e)}), 500

# Route: Get a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Endpoint to retrieve a single beauty service by its ID.
    """
    try:
        # Find the service with the matching ID
        service = next((s for s in services if s["id"] == service_id), None)
        if service:
            return jsonify({"service": service}), 200
        else:
            # Service not found
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while fetching the service.", "details": str(e)}), 500

# Route: Add a new service (for demonstration purposes)
@app.route('/services', methods=['POST'])
def add_service():
    """
    Endpoint to add a new beauty service.
    """
    try:
        # Extract service data from request body
        new_service = request.get_json()
        if not new_service or not all(key in new_service for key in ("name", "description", "price")):
            return jsonify({"error": "Invalid service data. Please provide 'name', 'description', and 'price'."}), 400
        
        # Generate a new ID and add the service to the list
        new_id = max(s["id"] for s in services) + 1
        new_service["id"] = new_id
        services.append(new_service)
        
        return jsonify({"message": "Service added successfully!", "service": new_service}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while adding the service.", "details": str(e)}), 500

# Main: Run the Flask application
if __name__ == '__main__':
    # Run the app on localhost port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```
