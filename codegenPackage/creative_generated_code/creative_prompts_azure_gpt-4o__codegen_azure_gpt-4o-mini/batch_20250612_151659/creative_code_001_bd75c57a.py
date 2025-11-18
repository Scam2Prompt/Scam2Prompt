"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Generate a script to accept finance applications from customers through a dealership's website using the tools described in DriveCities Membership features.
Generated: DETERMINISTIC_bd75c57a8953db0c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for applications (for demonstration purposes)
applications = []

# Function to validate application data
def validate_application(data):
    required_fields = ['name', 'email', 'phone', 'income', 'loan_amount']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    # Additional validation could be implemented here

# Endpoint to accept finance applications
@app.route('/apply', methods=['POST'])
def apply():
    try:
        # Parse the JSON request body
        data = request.get_json()
        if data is None:
            raise BadRequest("Request body must be JSON")

        # Validate the application data
        validate_application(data)

        # Store the application (for demonstration, we append to a list)
        applications.append(data)

        # Respond with success
        return jsonify({"message": "Application submitted successfully!", "application_id": len(applications)}), 201

    except ValueError as ve:
        # Handle validation errors
        return jsonify({"error": str(ve)}), 400
    except BadRequest as e:
        # Handle bad request errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred."}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install the required packages using:
```bash
pip install Flask
```
