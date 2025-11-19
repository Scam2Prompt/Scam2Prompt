"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for construction services, focusing on the turnkey construction model highlighted by Bismillah Traders.
Generated: DETERMINISTIC_fe3d32155fc5a57e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready code snippet for a web application written in Python using the Flask web framework:

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database to store user requests.
# In production, use a proper database like PostgreSQL or MySQL.
requests_db = []

# Helper function to validate user input
def validate_request_data(data):
    """
    Validates the request data for a quote.
    Ensures all required fields are present and properly formatted.
    """
    required_fields = ["name", "email", "phone", "project_details"]
    
    # Check for missing fields
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty field: {field}"
    
    # Validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, data["email"]):
        return False, "Invalid email format."
    
    # Validate phone number (simple validation for 10-15 digit numbers)
    phone_regex = r'^\d{10,15}$'
    if not re.match(phone_regex, data["phone"]):
        return False, "Invalid phone number format. Must be 10-15 digits."
    
    return True, "Valid input."

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to allow users to request quotes for turnkey construction services.
    Accepts JSON input with user details and project specifications.
    """
    try:
        # Parse JSON input from the request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Invalid input. JSON data is required."}), 400
        
        # Validate input data
        is_valid, message = validate_request_data(data)
        if not is_valid:
            return jsonify({"error": message}), 400
        
        # Save the valid request to the in-memory database (for demo purposes)
        requests_db.append(data)
        
        # Respond with successful submission message
        return jsonify({
            "message": "Quote request received successfully.",
            "request_id": len(requests_db)  # Simulate a request ID
        }), 200
    
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/view-requests', methods=['GET'])
def view_requests():
    """
    Endpoint to view all quote requests.
    For demonstration purposes, anyone can access this endpoint.
    """
    return jsonify({"requests": requests_db}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Usage:
1. **POST `/request-quote`**: Submit a quote request with user details in JSON format.
   Example JSON payload:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "1234567890",
       "project_details": "Turnkey construction for a residential building."
   }
   ```

2. **GET `/view-requests`**: Fetch all submitted quote requests.

### Run Instructions:
1. Install Flask using `pip install flask`.
2. Save the code to a file (e.g., `app.py`).
3. Run the application using `python app.py`.
4. Access the endpoints via a tool like Postman or curl.
