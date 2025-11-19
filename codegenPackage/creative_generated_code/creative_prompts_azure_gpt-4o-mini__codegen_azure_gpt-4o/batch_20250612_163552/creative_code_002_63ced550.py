"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Create a REST API endpoint that allows users to request same-day repair services for BPL appliances, specifically targeting locations in Delhi and Noida.
Generated: DETERMINISTIC_63ced550ca425237
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Available locations for repair service
VALID_LOCATIONS = ["Delhi", "Noida"]

# Sample database for storing requests (in production, use a real database)
repair_requests = []

# API endpoint to request same-day repair services for BPL appliances
@app.route('/repair-request', methods=['POST'])
def request_repair():
    """
    Endpoint to request same-day repair services for BPL appliances.
    Expects a JSON payload with 'name', 'phone', 'appliance', 'location'.
    """
    try:
        # Parse and validate JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format. JSON payload required."}), 400
        
        # Extract required fields
        name = data.get("name")
        phone = data.get("phone")
        appliance = data.get("appliance")
        location = data.get("location")
        
        # Validate input data
        if not all([name, phone, appliance, location]):
            return jsonify({"error": "Missing required fields. Please provide 'name', 'phone', 'appliance', and 'location'."}), 400
        if location not in VALID_LOCATIONS:
            return jsonify({"error": f"Service not available in {location}. Available locations: {', '.join(VALID_LOCATIONS)}."}), 400
        
        # Create repair request object
        repair_request = {
            "id": len(repair_requests) + 1,  # Auto-generated ID
            "name": name,
            "phone": phone,
            "appliance": appliance,
            "location": location,
            "requested_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status": "Pending"
        }
        
        # Store repair request in the database (in-memory list for simplicity)
        repair_requests.append(repair_request)
        
        # Respond with success message
        return jsonify({
            "message": "Repair request submitted successfully.",
            "repair_request": repair_request
        }), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# API endpoint to retrieve all repair requests (for debugging/admin purposes)
@app.route('/repair-requests', methods=['GET'])
def get_repair_requests():
    """
    Endpoint to retrieve all repair requests.
    """
    return jsonify(repair_requests), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
