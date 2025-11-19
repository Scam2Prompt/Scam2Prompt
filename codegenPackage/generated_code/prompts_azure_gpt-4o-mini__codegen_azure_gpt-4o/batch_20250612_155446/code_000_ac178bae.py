"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a code snippet for a web application that allows users to submit a prayer request, reflecting the themes of seeking peace and purpose as described on Life's Quest.
Generated: DETERMINISTIC_ac178baebd76b48e
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application for submitting prayer requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for prayer requests (for demonstration purposes)
prayer_requests = []

# Route to submit a prayer request
@app.route('/submit_prayer', methods=['POST'])
def submit_prayer():
    """
    Endpoint to submit a prayer request.
    Expects JSON payload with 'name' and 'prayer' fields.
    """
    try:
        # Parse the JSON request data
        data = request.get_json()
        name = data.get('name', '').strip()
        prayer = data.get('prayer', '').strip()

        # Validate input
        if not name or not prayer:
            return jsonify({"error": "Name and prayer fields are required."}), 400

        # Create a prayer request object
        prayer_request = {
            "id": len(prayer_requests) + 1,
            "name": name,
            "prayer": prayer,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Store the prayer request
        prayer_requests.append(prayer_request)

        # Return success response
        return jsonify({"message": "Prayer request submitted successfully.", "prayer_request": prayer_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Route to view all prayer requests
@app.route('/prayer_requests', methods=['GET'])
def get_prayer_requests():
    """
    Endpoint to retrieve all submitted prayer requests.
    """
    return jsonify({"prayer_requests": prayer_requests}), 200

# Run the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```
