"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Create code to integrate a callback request form for an online store, similar to the "Заказать обратный звонок" feature on acula.com.ua.
Generated: DETERMINISTIC_529af18988d32907
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Simulated database storage (in production, replace with a real database)
callback_requests = []

@app.route('/request_callback', methods=['POST'])
def request_callback():
    """
    Endpoint to handle callback requests.

    Expected JSON input:
    {
        "name": "Customer Name",
        "phone": "123-456-7890"
    }
    """
    try:
        # Parse request JSON
        data = request.get_json()

        # Validate input presence
        if not data or 'name' not in data or 'phone' not in data:
            return jsonify({"error": "Missing required fields: name and phone"}), 400

        name = data['name'].strip()
        phone = data['phone'].strip()

        # Validate name (non-empty, only letters and spaces)
        if not re.match(r"^[a-zA-Z\s]+$", name):
            return jsonify({"error": "Invalid name. Only letters and spaces are allowed."}), 400

        # Validate phone number format (basic example, adjust as needed for country-specific formats)
        if not re.match(r"^\+?[0-9\s\-]{7,15}$", phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Store the callback request (in production, save to a database)
        callback_requests.append({"name": name, "phone": phone})
        
        return jsonify({"message": "Callback request successfully submitted."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/callback_requests', methods=['GET'])
def get_callback_requests():
    """
    Endpoint to retrieve all callback requests (Admin/Operator functionality).
    """
    return jsonify(callback_requests), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
