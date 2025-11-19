"""
Generated Code Metadata:
========================
Original URL: https://tos.hyperliquidfndn.org
Prompt: Generate a code snippet for a user agreement system that requires acceptance of terms and conditions, similar to those outlined for the Hyper Foundation's HYPE event.
Generated: DETERMINISTIC_1ea96c1db47af850
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Sample terms and conditions
TERMS_AND_CONDITIONS = """
1. Acceptance of Terms
By participating in the HYPE event, you agree to abide by these terms and conditions.

2. Code of Conduct
Participants are expected to behave respectfully and professionally.

3. Liability
The organizers are not liable for any damages or losses incurred during the event.
"""

# In-memory storage for user agreements (for demonstration purposes)
user_agreements = {}

@app.route('/')
def index():
    """Render the main page with terms and conditions."""
    return render_template('index.html', terms=TERMS_AND_CONDITIONS)

@app.route('/accept', methods=['POST'])
def accept_terms():
    """Handle the acceptance of terms and conditions."""
    user_id = request.form.get('user_id')
    
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400

    # Store the user's acceptance
    user_agreements[user_id] = True
    return jsonify({"message": "Terms accepted successfully."}), 200

@app.route('/check/<user_id>', methods=['GET'])
def check_agreement(user_id):
    """Check if a user has accepted the terms and conditions."""
    accepted = user_agreements.get(user_id, False)
    return jsonify({"user_id": user_id, "accepted": accepted}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms and Conditions</title>
</head>
<body>
    <h1>Terms and Conditions</h1>
    <pre>{{ terms }}</pre>
    <form action="/accept" method="post">
        <input type="text" name="user_id" placeholder="Enter your User ID" required>
        <button type="submit">Accept Terms</button>
    </form>
</body>
</html>
```

### Notes:
- This code uses Flask, a lightweight web framework for Python.
- The terms and conditions are hardcoded for demonstration purposes.
- User agreements are stored in an in-memory dictionary for simplicity; consider using a database for production.
- Error handling is included for missing user IDs.
- The HTML template is included for rendering the terms and conditions.
