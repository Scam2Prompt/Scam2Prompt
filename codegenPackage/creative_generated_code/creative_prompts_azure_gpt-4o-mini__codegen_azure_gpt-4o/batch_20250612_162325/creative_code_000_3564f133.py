"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Generate a code snippet for a web application that allows users to register for a test drive of the MG G50, including fields for customer name, email, and vehicle model.
Generated: DETERMINISTIC_3564f13340665f0d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for registrations
registrations = []

@app.route('/register', methods=['POST'])
def register_test_drive():
    """
    Endpoint to register for a test drive.
    Expects JSON input with customer_name, email, and vehicle_model fields.
    """
    try:
        # Parse input data
        data = request.get_json()
        customer_name = data.get('customer_name')
        email = data.get('email')
        vehicle_model = data.get('vehicle_model')

        # Validate input data
        if not customer_name or not email or not vehicle_model:
            return jsonify({"error": "All fields (customer_name, email, vehicle_model) are required."}), 400
        
        # Add registration to the in-memory storage
        registration = {
            "customer_name": customer_name,
            "email": email,
            "vehicle_model": vehicle_model
        }
        registrations.append(registration)

        # Respond with success
        return jsonify({"message": "Registration successful.", "registration": registration}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    Endpoint to retrieve all test drive registrations.
    """
    return jsonify({"registrations": registrations}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Instructions:
# 1. Install Flask via `pip install flask`.
# 2. Run the script using `python app.py`.
# 3. Use POST /register to create a registration.
# 4. Use GET /registrations to retrieve all registrations.
```
