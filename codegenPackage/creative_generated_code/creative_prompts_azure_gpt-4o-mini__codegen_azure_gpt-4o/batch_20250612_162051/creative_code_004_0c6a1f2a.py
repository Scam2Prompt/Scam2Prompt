"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Describe how to implement a delivery tracking system for Watpac Chemicals' products, ensuring it covers all states mentioned on their website.
Generated: DETERMINISTIC_0c6a1f2a893a061a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a delivery tracking system. It uses a RESTful API structure with Flask, which is suitable for tracking deliveries across multiple states.

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory storage for demo purposes
delivery_data = {}  # Dictionary to store delivery information

# List of states mentioned on Watpac Chemicals' website (replace with actual states)
SUPPORTED_STATES = [
    "New South Wales", "Queensland", "Victoria", "Tasmania", "South Australia",
    "Western Australia", "Northern Territory", "Australian Capital Territory"
]

@app.route('/deliveries', methods=['POST'])
def create_delivery():
    """
    Endpoint to create a new delivery record.
    Expected JSON format in request body:
    {
        "product_name": "Chemical Name",
        "destination_state": "State Name",
        "estimated_delivery_date": "YYYY-MM-DD"
    }
    """
    try:
        data = request.json

        # Validate input data
        product_name = data.get('product_name')
        destination_state = data.get('destination_state')
        estimated_delivery_date = data.get('estimated_delivery_date')

        if not product_name or not destination_state or not estimated_delivery_date:
            return jsonify({"error": "Missing required fields"}), 400

        if destination_state not in SUPPORTED_STATES:
            return jsonify({"error": f"State '{destination_state}' is not supported"}), 400

        # Generate a unique tracking ID
        tracking_id = str(uuid.uuid4())
        delivery_record = {
            "tracking_id": tracking_id,
            "product_name": product_name,
            "destination_state": destination_state,
            "status": "In Transit",
            "estimated_delivery_date": estimated_delivery_date,
            "created_at": datetime.datetime.utcnow().isoformat()
        }

        # Store the delivery record
        delivery_data[tracking_id] = delivery_record

        return jsonify({"message": "Delivery created successfully", "tracking_id": tracking_id}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/deliveries/<tracking_id>', methods=['GET'])
def get_delivery(tracking_id):
    """
    Endpoint to fetch delivery details by tracking ID.
    """
    try:
        delivery_record = delivery_data.get(tracking_id)

        if not delivery_record:
            return jsonify({"error": "Tracking ID not found"}), 404

        return jsonify(delivery_record), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/deliveries/<tracking_id>', methods=['PUT'])
def update_delivery_status(tracking_id):
    """
    Endpoint to update the status of a delivery.
    Expected JSON format in request body:
    {
        "status": "New Status"
    }
    """
    try:
        delivery_record = delivery_data.get(tracking_id)

        if not delivery_record:
            return jsonify({"error": "Tracking ID not found"}), 404

        data = request.json
        new_status = data.get("status")

        if not new_status:
            return jsonify({"error": "Missing 'status' field"}), 400

        # Update the delivery status
        delivery_record["status"] = new_status
        delivery_record["updated_at"] = datetime.datetime.utcnow().isoformat()
        delivery_data[tracking_id] = delivery_record

        return jsonify({"message": "Delivery status updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/deliveries', methods=['GET'])
def list_deliveries():
    """
    Endpoint to list all deliveries.
    """
    try:
        return jsonify(list(delivery_data.values())), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

### Instructions:
1. Install Flask using `pip install flask`.
2. Run the script and test the endpoints (`POST /deliveries`, `GET /deliveries/<tracking_id>`, etc.) using tools like Postman or curl.
3. Replace `SUPPORTED_STATES` with actual states provided by Watpac Chemicals' website.
