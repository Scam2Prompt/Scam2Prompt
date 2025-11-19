"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: How can I implement a CAPTCHA verification system to ensure users are not robots in my web application?
Generated: DETERMINISTIC_a025e7b830ac6f8e
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Generate a random CAPTCHA string
def generate_captcha():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Store CAPTCHA data in-memory for simplicity (Consider using a more persistent storage for production)
captcha_store = {}

@app.route('/')
def index():
    """
    Serve the main page with a CAPTCHA challenge.
    """
    captcha = generate_captcha()
    session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    captcha_store[session_id] = captcha  # Store CAPTCHA for validation later
    return render_template('index.html', captcha=captcha, session_id=session_id)

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    """
    Verify the user-provided CAPTCHA against the stored CAPTCHA.
    """
    try:
        # Extract form data
        session_id = request.form.get('session_id')
        user_input = request.form.get('captcha_input')

        # Check if session_id exists
        if session_id not in captcha_store:
            return jsonify({"success": False, "message": "Invalid session ID."})

        # Verify the CAPTCHA
        if captcha_store[session_id] == user_input:
            del captcha_store[session_id]  # Remove CAPTCHA after successful validation
            return jsonify({"success": True, "message": "CAPTCHA verified successfully!"})
        else:
            return jsonify({"success": False, "message": "CAPTCHA verification failed."})

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=False)
```

### Templates (HTML)
#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPTCHA Verification</title>
</head>
<body>
    <h1>CAPTCHA Verification</h1>
    <form id="captcha-form" method="POST" action="/verify_captcha">
        <p><strong>CAPTCHA:</strong> {{ captcha }}</p>
        <input type="hidden" name="session_id" value="{{ session_id }}">
        <label for="captcha_input">Enter CAPTCHA:</label>
        <input type="text" id="captcha_input" name="captcha_input" required>
        <button type="submit">Verify</button>
    </form>
</body>
</html>
```
