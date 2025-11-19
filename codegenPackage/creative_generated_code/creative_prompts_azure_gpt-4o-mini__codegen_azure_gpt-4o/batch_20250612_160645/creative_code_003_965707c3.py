"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Develop an API that allows users to submit renovation requests to Панам, including details like room size, type of renovation, and desired materials.
Generated: DETERMINISTIC_965707c3180fea13
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for renovation requests (for the purposes of this example)
renovation_requests = []

# Define valid renovation types and materials
VALID_RENOVATION_TYPES = {"painting", "flooring", "plumbing", "electrical"}
VALID_MATERIALS = {"wood", "ceramic", "marble", "metal", "plastic"}

@app.route('/submit-renovation', methods=['POST'])
def submit_renovation_request():
    """
    API endpoint to submit a renovation request.
    Request payload should include:
      - room_size (float): Size of the room in square meters.
      - renovation_type (str): Type of renovation.
      - materials (list of str): List of desired materials.
    Returns:
      JSON response with status and message.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid or missing JSON payload"}), 400
        
        # Extract and validate fields
        room_size = data.get("room_size")
        renovation_type = data.get("renovation_type")
        materials = data.get("materials")
        
        if not isinstance(room_size, (int, float)) or room_size <= 0:
            return jsonify({"status": "error", "message": "Invalid room size"}), 400
        
        if renovation_type not in VALID_RENOVATION_TYPES:
            return jsonify({"status": "error", "message": f"Invalid renovation type. Valid types are: {', '.join(VALID_RENOVATION_TYPES)}"}), 400
        
        if not isinstance(materials, list) or not all(material in VALID_MATERIALS for material in materials):
            return jsonify({"status": "error", "message": f"Invalid materials. Valid materials are: {', '.join(VALID_MATERIALS)}"}), 400
        
        # Save the renovation request
        request_id = len(renovation_requests) + 1
        renovation_request = {
            "id": request_id,
            "room_size": room_size,
            "renovation_type": renovation_type,
            "materials": materials
        }
        renovation_requests.append(renovation_request)
        
        # Log the request
        logging.info(f"Renovation request submitted: {renovation_request}")
        
        # Return success response
        return jsonify({"status": "success", "message": "Renovation request submitted successfully", "request_id": request_id}), 201
    
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error handling renovation request: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

@app.route('/renovation-requests', methods=['GET'])
def get_renovation_requests():
    """
    API endpoint to retrieve all submitted renovation requests.
    Returns:
      JSON response with a list of renovation requests.
    """
    return jsonify({"status": "success", "renovation_requests": renovation_requests}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
