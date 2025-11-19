"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newmoly.pages.dev
Prompt: How can I create a registration system for the B1 and B2 series NFT drops on the Molly Gateway?
Generated: DETERMINISTIC_b23cf6760e2b8d77
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation for a simple NFT registration system using Python and Flask:

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database substitute
registrations = {
    "B1": [],
    "B2": []
}

# Error handling middleware for better production readiness
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": "Something went wrong"}), 500

# Route to register for NFT drop
@app.route('/register', methods=['POST'])
def register():
    try:
        # Parse JSON input
        data = request.get_json()

        # Validate required fields
        if not data or 'user_id' not in data or 'series' not in data:
            return jsonify({"error": "Invalid input", "message": "user_id and series are required"}), 400

        user_id = data['user_id']
        series = data['series'].upper()

        # Validate series
        if series not in registrations.keys():
            return jsonify({"error": "Invalid series", "message": f"Series must be one of: {', '.join(registrations.keys())}"}), 400

        # Check if user is already registered
        if any(reg['user_id'] == user_id for reg in registrations[series]):
            return jsonify({"message": "User is already registered for this series"}), 200

        # Generate unique registration ID
        registration_id = str(uuid.uuid4())

        # Register user for the series
        registrations[series].append({"registration_id": registration_id, "user_id": user_id})

        return jsonify({
            "message": f"Successfully registered for series {series}",
            "registration_id": registration_id
        }), 201

    except Exception as e:
        return jsonify({"error": "An error occurred during registration", "message": str(e)}), 500

# Route to fetch registrations for a series
@app.route('/registrations/<series>', methods=['GET'])
def get_registrations(series):
    try:
        series = series.upper()

        # Validate series
        if series not in registrations.keys():
            return jsonify({"error": "Invalid series", "message": f"Series must be one of: {', '.join(registrations.keys())}"}), 404

        return jsonify({
            "series": series,
            "registrations": registrations[series]
        }), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while fetching registrations", "message": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True)
```

### How to Use:
1. **Register for a series**: Send a POST request to `/register` with JSON payload `{"user_id": "user123", "series": "B1"}`.
2. **View registrations**: Send a GET request to `/registrations/B1` or `/registrations/B2`.

### Features:
- Error handling for invalid input and internal server errors.
- Registration ID is generated uniquely for each user using `uuid`.
- Checks for duplicate registrations.
- Validates against supported series (`B1`, `B2`).
