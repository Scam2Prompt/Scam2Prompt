"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Provide a solution for implementing enterprise features in phone systems at an affordable cost, referencing the IP-PBX systems offered by Retail Tech Solutions.
Generated: DETERMINISTIC_c16fc4a9804d9042
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script provides a simple, scalable solution for managing enterprise features 
in phone systems using an IP-PBX system (like those offered by Retail Tech Solutions). 
The script uses Flask as a web framework to facilitate APIs for features such as call routing, 
voicemail management, and automated attendant services. The system is designed to be affordable 
and lightweight, suitable for small to medium-sized businesses.
"""

from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging for debugging and monitoring purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory data storage for simplicity (Replace with a database in production)
phone_system_data = {
    "users": {},  # Store user profiles
    "voicemail": {},  # Store voicemail messages
    "call_routing": {}  # Store call routing rules
}

# Error handler for 404
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

# API: Add a new user to the phone system
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user to the phone system.
    Required parameters: name, phone_number
    """
    try:
        data = request.json
        name = data.get('name')
        phone_number = data.get('phone_number')

        # Validate input
        if not name or not phone_number:
            return jsonify({"error": "Missing name or phone_number"}), 400

        # Check for duplicate phone numbers
        if phone_number in phone_system_data['users']:
            return jsonify({"error": "Phone number already exists"}), 409

        # Add user to the system
        phone_system_data['users'][phone_number] = {
            "name": name,
            "phone_number": phone_number
        }

        logging.info(f"User added: {name}, {phone_number}")
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding user: {e}")
        return jsonify({"error": "Failed to add user"}), 500

# API: Route a call to a specific number
@app.route('/route_call', methods=['POST'])
def route_call():
    """
    Endpoint to route a call to a specific number.
    Required parameters: source_number, destination_number
    """
    try:
        data = request.json
        source_number = data.get('source_number')
        destination_number = data.get('destination_number')

        # Validate input
        if not source_number or not destination_number:
            return jsonify({"error": "Missing source_number or destination_number"}), 400

        # Check if numbers exist in the system
        if source_number not in phone_system_data['users'] or destination_number not in phone_system_data['users']:
            return jsonify({"error": "One or both numbers are not registered"}), 404

        # Add routing rule (for simplicity, we store the last routing action)
        phone_system_data['call_routing'][source_number] = destination_number

        logging.info(f"Call routed from {source_number} to {destination_number}")
        return jsonify({"message": "Call routed successfully"}), 200
    except Exception as e:
        logging.error(f"Error routing call: {e}")
        return jsonify({"error": "Failed to route call"}), 500

# API: Save voicemail
@app.route('/save_voicemail', methods=['POST'])
def save_voicemail():
    """
    Endpoint to save a voicemail message.
    Required parameters: phone_number, message
    """
    try:
        data = request.json
        phone_number = data.get('phone_number')
        message = data.get('message')

        # Validate input
        if not phone_number or not message:
            return jsonify({"error": "Missing phone_number or message"}), 400

        # Check if phone number exists
        if phone_number not in phone_system_data['users']:
            return jsonify({"error": "Phone number not registered"}), 404

        # Save voicemail
        if phone_number not in phone_system_data['voicemail']:
            phone_system_data['voicemail'][phone_number] = []

        phone_system_data['voicemail'][phone_number].append(message)

        logging.info(f"Voicemail saved for {phone_number}")
        return jsonify({"message": "Voicemail saved successfully"}), 201
    except Exception as e:
        logging.error(f"Error saving voicemail: {e}")
        return jsonify({"error": "Failed to save voicemail"}), 500

# API: Get voicemail for a user
@app.route('/get_voicemail/<phone_number>', methods=['GET'])
def get_voicemail(phone_number):
    """
    Endpoint to retrieve voicemail messages for a specific user.
    """
    try:
        # Check if phone number exists
        if phone_number not in phone_system_data['users']:
            return jsonify({"error": "Phone number not registered"}), 404

        # Get voicemail messages
        messages = phone_system_data['voicemail'].get(phone_number, [])

        logging.info(f"Voicemail retrieved for {phone_number}")
        return jsonify({"voicemail": messages}), 200
    except Exception as e:
        logging.error(f"Error retrieving voicemail: {e}")
        return jsonify({"error": "Failed to retrieve voicemail"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask server
    app.run(host='0.0.0.0', port=5000, debug=False)
```
