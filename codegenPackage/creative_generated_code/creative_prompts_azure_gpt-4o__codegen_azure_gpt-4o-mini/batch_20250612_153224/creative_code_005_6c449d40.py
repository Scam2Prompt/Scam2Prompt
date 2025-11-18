"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Create a program to manage cookie consent preferences for a smart home system, inspired by the privacy and cookie management features described on vigilanciadomotica.es.
Generated: DETERMINISTIC_6c449d40eff2b6ed
Batch ID: 20250612_153224
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

app = Flask(__name__)

# Define consent options
CONSENT_OPTIONS = {
    "analytics": "Allow analytics cookies",
    "functional": "Allow functional cookies",
    "marketing": "Allow marketing cookies"
}

# Load or initialize cookie consent preferences
def load_preferences():
    try:
        with open('cookie_consent.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {option: False for option in CONSENT_OPTIONS.keys()}

# Save cookie consent preferences to file
def save_preferences(preferences):
    with open('cookie_consent.json', 'w') as file:
        json.dump(preferences, file)

# Route to get current consent preferences
@app.route('/consent', methods=['GET'])
def get_consent():
    """Get current cookie consent preferences."""
    preferences = load_preferences()
    return jsonify(preferences)

# Route to update consent preferences
@app.route('/consent', methods=['POST'])
def update_consent():
    """Update cookie consent preferences."""
    preferences = load_preferences()
    data = request.json

    # Validate incoming data
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data format"}), 400
    for key in data:
        if key not in CONSENT_OPTIONS:
            return jsonify({"error": f"Invalid consent option: {key}"}), 400

    # Update preferences and save to file
    preferences.update({key: data[key] for key in data if key in preferences})
    save_preferences(preferences)
    return jsonify(preferences), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
