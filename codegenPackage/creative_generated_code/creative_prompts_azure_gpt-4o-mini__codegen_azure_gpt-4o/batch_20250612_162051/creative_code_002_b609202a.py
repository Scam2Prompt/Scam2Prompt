"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Generate a code snippet for a web application that allows users to request cleaning services, similar to the comprehensive services offered by شمس المملكة.
Generated: DETERMINISTIC_b609202a1f94fe16
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A simple Flask-based web application for requesting cleaning services.

from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for service requests (for demonstration purposes)
service_requests = []

@app.route('/')
def home():
    """
    Render the homepage where users can request cleaning services.
    """
    return render_template('index.html')

@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint for processing cleaning service requests.
    Accepts JSON payload with user details and cleaning preferences.
    """
    try:
        # Parse request JSON data
        data = request.get_json()
        
        # Extract and validate user details
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        service_type = data.get('service_type')

        # Validate required fields
        if not all([name, email, phone, address, service_type]):
            return jsonify({"error": "All fields (name, email, phone, address, service_type) are required."}), 400
        
        # Validate email address format
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if not re.match(email_regex, email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate phone number format (example for international phone numbers)
        phone_regex = r'^\+?[1-9]\d{1,14}$'
        if not re.match(phone_regex, phone):
            return jsonify({"error": "Invalid phone number format."}), 400

        # Process and store the request
        service_request = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "service_type": service_type
        }
        service_requests.append(service_request)

        return jsonify({"message": "Service request submitted successfully!", "data": service_request}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/requests', methods=['GET'])
def get_requests():
    """
    Endpoint to retrieve all submitted cleaning service requests.
    """
    return jsonify({"service_requests": service_requests}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### `templates/index.html` (Frontend HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaning Services</title>
</head>
<body>
    <h1>Request Cleaning Services</h1>
    <form id="serviceRequestForm">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="address">Address:</label><br>
        <input type="text" id="address" name="address" required><br><br>

        <label for="service_type">Service Type:</label><br>
        <select id="service_type" name="service_type" required>
            <option value="general_cleaning">General Cleaning</option>
            <option value="deep_cleaning">Deep Cleaning</option>
            <option value="move_in_out_cleaning">Move In/Out Cleaning</option>
        </select><br><br>

        <button type="button" onclick="submitRequest()">Submit Request</button>
    </form>

    <script>
        async function submitRequest() {
            const form = document.getElementById('serviceRequestForm');
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/request-service', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                alert(result.message || result.error);
            } catch (error) {
                alert('An error occurred while submitting the request.');
            }
        }
    </script>
</body>
</html>
```
