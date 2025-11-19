"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://al-afdel.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, referencing the unique offerings of the company mentioned in the content.
Generated: DETERMINISTIC_6d0d82dcd8076210
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for requesting home cleaning services

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data to represent unique offerings
UNIQUE_OFFERINGS = [
    {"id": 1, "name": "Eco-friendly Cleaning", "description": "Using sustainable, non-toxic materials."},
    {"id": 2, "name": "Deep Cleaning", "description": "Thorough cleaning for every nook and cranny."},
    {"id": 3, "name": "Pet-Friendly Cleaning", "description": "Specialized cleaning for homes with pets."},
]

# Mock database for storing requests
CLEANING_REQUESTS = []

@app.route('/offerings', methods=['GET'])
def get_offerings():
    """
    Endpoint to fetch unique offerings of the company.
    Returns:
        JSON list of unique offerings.
    """
    return jsonify({"offerings": UNIQUE_OFFERINGS}), 200

@app.route('/request-cleaning', methods=['POST'])
def request_cleaning():
    """
    Endpoint for users to request home cleaning services.
    Request Body:
        - name (str): Name of the user.
        - email (str): Email address of the user.
        - phone (str): Contact number.
        - offering_id (int): ID of the selected offering.
        - date (str): Requested date for cleaning (YYYY-MM-DD).
    Returns:
        JSON response confirming the request or error.
    """
    data = request.json

    # Basic validation of input data
    try:
        if not data.get('name') or not data.get('email') or not data.get('phone') or not data.get('offering_id') or not data.get('date'):
            return jsonify({"error": "All fields are required: name, email, phone, offering_id, date"}), 400

        # Validate date format
        requested_date = datetime.strptime(data['date'], '%Y-%m-%d')

        # Check if offering_id is valid
        offering = next((o for o in UNIQUE_OFFERINGS if o['id'] == data['offering_id']), None)
        if not offering:
            return jsonify({"error": "Invalid offering_id"}), 400

        # Create and store the cleaning request
        request_id = len(CLEANING_REQUESTS) + 1
        cleaning_request = {
            "id": request_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "offering": offering,
            "requested_date": requested_date.isoformat(),
            "status": "Pending"
        }
        CLEANING_REQUESTS.append(cleaning_request)

        return jsonify({"message": "Cleaning request created successfully", "request": cleaning_request}), 201
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/requests', methods=['GET'])
def get_requests():
    """
    Endpoint to fetch all cleaning requests.
    Returns:
        JSON list of cleaning requests.
    """
    return jsonify({"requests": CLEANING_REQUESTS}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

To use this code, simply install Flask (`pip install flask`), save the script in a file, and run the file. The API will be available at `http://127.0.0.1:5000/`.
