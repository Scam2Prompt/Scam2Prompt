"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cint.privacykeeper.cc
Prompt: Provide an example of using a library to manage privacy settings in a web application.
Generated: DETERMINISTIC_43edc069113783bf
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError
import logging

# Configure logging for debugging and production readiness
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Privacy Settings Schema for Validation
class PrivacySettingsSchema(Schema):
    allow_data_sharing = fields.Boolean(required=True)
    allow_email_notifications = fields.Boolean(required=True)
    allow_targeted_ads = fields.Boolean(required=True)

# Initialize schema instance
privacy_settings_schema = PrivacySettingsSchema()

# In-memory database to store user privacy settings (for demonstration purposes)
user_privacy_settings = {}

@app.route("/privacy-settings/<user_id>", methods=["GET"])
def get_privacy_settings(user_id):
    """
    Endpoint to get privacy settings for a specific user.
    """
    if user_id not in user_privacy_settings:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user_id": user_id, "settings": user_privacy_settings[user_id]}), 200

@app.route("/privacy-settings/<user_id>", methods=["POST"])
def update_privacy_settings(user_id):
    """
    Endpoint to update privacy settings for a specific user.
    """
    try:
        # Validate incoming request data
        data = privacy_settings_schema.load(request.json)
    except ValidationError as err:
        # Return validation error response
        return jsonify({"error": "Invalid data", "details": err.messages}), 400

    # Save validated data to the in-memory database
    user_privacy_settings[user_id] = data
    logging.info(f"Updated privacy settings for user {user_id}")
    return jsonify({"message": "Privacy settings updated successfully"}), 200

@app.route("/privacy-settings/<user_id>", methods=["DELETE"])
def delete_privacy_settings(user_id):
    """
    Endpoint to delete privacy settings for a specific user.
    """
    if user_id not in user_privacy_settings:
        return jsonify({"error": "User not found"}), 404
    
    # Remove user's privacy settings
    del user_privacy_settings[user_id]
    logging.info(f"Deleted privacy settings for user {user_id}")
    return jsonify({"message": "Privacy settings deleted successfully"}), 200

# Run the app if executed directly
if __name__ == "__main__":
    app.run(debug=True)
```
