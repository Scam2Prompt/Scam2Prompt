"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Develop a RESTful API endpoint that allows users to schedule package pickups with a logistics provider, inspired by the services of Spedition Steinhübl.
Generated: DETERMINISTIC_548ed6ef152457b1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a RESTful API endpoint in Python using the Flask framework. This code meets all the requested requirements.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for scheduled pickups (simulating a database)
scheduled_pickups = {}

# Helper function to validate pickup data
def validate_pickup_data(data):
    required_fields = ['name', 'address', 'email', 'pickup_date', 'pickup_time']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Field '{field}' is required and cannot be empty."
    try:
        # Validate pickup_date and pickup_time
        datetime.strptime(data['pickup_date'], "%Y-%m-%d")
        datetime.strptime(data['pickup_time'], "%H:%M")
    except ValueError:
        return False, "Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time."
    return True, None

@app.route('/schedule-pickup', methods=['POST'])
def schedule_pickup():
    """
    API Endpoint to schedule a package pickup.
    Request Body:
    {
        "name": "John Doe",
        "address": "123 Example St",
        "email": "johndoe@example.com",
        "pickup_date": "2023-10-15",
        "pickup_time": "14:00"
    }
    Response:
    - Success: Returns the pickup ID and confirmation message.
    - Error: Returns error message with appropriate HTTP status code.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON."}), 400

        # Validate input data
        is_valid, validation_error = validate_pickup_data(data)
        if not is_valid:
            return jsonify({"error": validation_error}), 400

        # Generate a unique ID for the pickup
        pickup_id = str(uuid.uuid4())

        # Store the pickup details in memory (simulating database storage)
        scheduled_pickups[pickup_id] = {
            "name": data['name'],
            "address": data['address'],
            "email": data['email'],
            "pickup_date": data['pickup_date'],
            "pickup_time": data['pickup_time'],
            "created_at": datetime.utcnow().isoformat(),
        }

        # Send success response
        return jsonify({
            "pickup_id": pickup_id,
            "message": "Pickup scheduled successfully."
        }), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/scheduled-pickups', methods=['GET'])
def get_scheduled_pickups():
    """
    API Endpoint to retrieve all scheduled pickups.
    Response:
    - Success: Returns a list of all scheduled pickups.
    """
    return jsonify(scheduled_pickups), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Install Flask if not already installed:
   ```
   pip install flask
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Test the endpoints using tools like `curl`, Postman, or any REST client.
