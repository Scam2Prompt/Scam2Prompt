"""
Generated Code Metadata:
========================
Original URL: https://up7sd.eth-drop.top
Prompt: Design a basic API for managing privacy and terms of service updates for a software application, inspired by Google's approach.
Generated: DETERMINISTIC_7d972a58e33b8732
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for privacy and terms updates
updates = {
    "privacy_policy": [],
    "terms_of_service": []
}

# Helper function to validate update data
def validate_update_data(data):
    if not isinstance(data, dict):
        return False, "Invalid data format. Expected JSON object."
    if "version" not in data or "content" not in data:
        return False, "Missing required fields: 'version' and 'content'."
    if not isinstance(data["version"], str) or not isinstance(data["content"], str):
        return False, "Fields 'version' and 'content' must be strings."
    return True, None

@app.route('/api/privacy_policy', methods=['GET', 'POST'])
def privacy_policy():
    if request.method == 'GET':
        # Return all privacy policy updates
        return jsonify(updates["privacy_policy"]), 200

    if request.method == 'POST':
        # Add a new privacy policy update
        data = request.get_json()
        is_valid, error_message = validate_update_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Add timestamp to the update
        update = {
            "version": data["version"],
            "content": data["content"],
            "timestamp": datetime.utcnow().isoformat()
        }
        updates["privacy_policy"].append(update)
        return jsonify({"message": "Privacy policy updated successfully.", "update": update}), 201

@app.route('/api/terms_of_service', methods=['GET', 'POST'])
def terms_of_service():
    if request.method == 'GET':
        # Return all terms of service updates
        return jsonify(updates["terms_of_service"]), 200

    if request.method == 'POST':
        # Add a new terms of service update
        data = request.get_json()
        is_valid, error_message = validate_update_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Add timestamp to the update
        update = {
            "version": data["version"],
            "content": data["content"],
            "timestamp": datetime.utcnow().isoformat()
        }
        updates["terms_of_service"].append(update)
        return jsonify({"message": "Terms of service updated successfully.", "update": update}), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
