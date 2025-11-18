"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Develop a chatbot using Python that can assist users in finding BPL service centers near them and booking repair services for appliances like refrigerators and washing machines.
Generated: DETERMINISTIC_c212657ed9c9f3cc
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for BPL service centers
SERVICE_CENTERS = [
    {"id": 1, "name": "BPL Service Center A", "location": "New York", "services": ["Refrigerator", "Washing Machine"]},
    {"id": 2, "name": "BPL Service Center B", "location": "Los Angeles", "services": ["Refrigerator"]},
    {"id": 3, "name": "BPL Service Center C", "location": "Chicago", "services": ["Washing Machine"]},
]

# Function to find service centers based on user location
def find_service_centers(location):
    """Find service centers by location."""
    centers = [center for center in SERVICE_CENTERS if location.lower() in center["location"].lower()]
    return centers

# Function to book a service
def book_service(center_id, appliance_type):
    """Book a repair service at a given service center for a specific appliance."""
    # Simulating booking process (this should ideally interact with a real database)
    for center in SERVICE_CENTERS:
        if center['id'] == center_id and appliance_type in center['services']:
            return {"status": "success", "message": f"Service booked at {center['name']} for {appliance_type}."}
    return {"status": "error", "message": "Service center not found or service unavailable."}

@app.route('/find_centers', methods=['GET'])
def get_centers():
    """API endpoint to find service centers by location."""
    location = request.args.get('location')
    if not location:
        return jsonify({"status": "error", "message": "Location query parameter is required."}), 400
    
    centers = find_service_centers(location)
    
    if not centers:
        return jsonify({"status": "error", "message": "No service centers found for the specified location."}), 404
    
    return jsonify({"status": "success", "service_centers": centers}), 200

@app.route('/book_service', methods=['POST'])
def book_repair_service():
    """API endpoint to book a repair service."""
    data = request.get_json()
    center_id = data.get('center_id')
    appliance_type = data.get('appliance_type')
    
    if not center_id or not appliance_type:
        return jsonify({"status": "error", "message": "center_id and appliance_type are required."}), 400
    
    result = book_service(center_id, appliance_type)
    
    if result['status'] == 'error':
        return jsonify(result), 404
    
    return jsonify(result), 200

if __name__ == '__main__':
    # Running the Flask app
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```
