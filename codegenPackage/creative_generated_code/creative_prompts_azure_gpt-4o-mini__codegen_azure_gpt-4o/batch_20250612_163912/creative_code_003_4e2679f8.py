"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstbaptistnj.org
Prompt: Create an API that allows users to subscribe to a church newsletter, inspired by the subscription feature on the First Baptist Church website.
Generated: DETERMINISTIC_4e2679f8cc5e3e01
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a production-ready API in Python using the Flask framework:

```python
from flask import Flask, request, jsonify
import re
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# In-memory data store for subscribers
subscribers = {}

# Helper function to validate email format
def is_valid_email(email):
    # Regex for validating email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Error handling decorator for cleaner error responses
def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return wrapper

@app.route('/subscribe', methods=['POST'])
@error_handler
def subscribe():
    """
    Endpoint to subscribe users to the church newsletter.
    Request Body: 
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    Response:
    - Success: 200 OK with a success message.
    - Error: 400 Bad Request for validation errors.
    """
    data = request.json

    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email' in request body."}), 400

    name = data['name'].strip()
    email = data['email'].strip()

    if not name:
        return jsonify({"error": "Name cannot be empty."}), 400
    
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    # Check if the email is already subscribed
    if email in subscribers:
        return jsonify({"error": "Email is already subscribed."}), 400

    # Subscribe the user
    subscribers[email] = name
    return jsonify({"message": f"Successfully subscribed {name} to the newsletter!"}), 200

@app.route('/subscribers', methods=['GET'])
@error_handler
def get_subscribers():
    """
    Endpoint to retrieve the list of all subscribers.
    Response:
    - Success: 200 OK with a list of subscribers.
    """
    return jsonify({"subscribers": subscribers}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Install Flask to run this API: `pip install flask`
- Save this script as `app.py`, and run it using the command: `python app.py`.
- Access endpoints:
  - Subscribe: `POST /subscribe` with JSON `{"name": "John Doe", "email": "john@example.com"}`
  - Get subscribers: `GET /subscribers`
