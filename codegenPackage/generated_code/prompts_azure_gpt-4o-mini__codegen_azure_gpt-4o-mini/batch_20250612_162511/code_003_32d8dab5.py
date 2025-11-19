"""
Generated Code Metadata:
========================
Original URL: https://pineappledex.org
Prompt: Generate a code example that demonstrates how to handle human verification in a web application, inspired by the methods used on PineappleDex.
Generated: DETERMINISTIC_32d8dab5dc7967e8
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

# In-memory store for verification codes (for demonstration purposes)
verification_codes = {}

def generate_verification_code(length=6):
    """Generate a random verification code of specified length."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/request_verification', methods=['POST'])
def request_verification():
    """Endpoint to request a verification code."""
    user_email = request.json.get('email')
    
    if not user_email:
        return jsonify({"error": "Email is required"}), 400

    # Generate a verification code
    code = generate_verification_code()
    verification_codes[user_email] = code

    # Here you would send the code to the user's email
    # For demonstration, we will just return it
    return jsonify({"message": "Verification code sent", "code": code}), 200

@app.route('/verify_code', methods=['POST'])
def verify_code():
    """Endpoint to verify the provided code."""
    user_email = request.json.get('email')
    user_code = request.json.get('code')

    if not user_email or not user_code:
        return jsonify({"error": "Email and code are required"}), 400

    # Check if the code matches the stored code
    if verification_codes.get(user_email) == user_code:
        # Code is valid, proceed with verification
        del verification_codes[user_email]  # Remove the code after successful verification
        return jsonify({"message": "Verification successful"}), 200
    else:
        return jsonify({"error": "Invalid verification code"}), 400

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Example</title>
</head>
<body>
    <h1>Human Verification</h1>
    <form id="verificationForm">
        <input type="email" id="email" placeholder="Enter your email" required>
        <button type="button" onclick="requestVerification()">Request Verification Code</button>
        <br>
        <input type="text" id="code" placeholder="Enter verification code" required>
        <button type="button" onclick="verifyCode()">Verify Code</button>
    </form>
    <div id="message"></div>

    <script>
        async function requestVerification() {
            const email = document.getElementById('email').value;
            const response = await fetch('/request_verification', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email })
            });
            const data = await response.json();
            document.getElementById('message').innerText = data.message || data.error;
        }

        async function verifyCode() {
            const email = document.getElementById('email').value;
            const code = document.getElementById('code').value;
            const response = await fetch('/verify_code', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, code })
            });
            const data = await response.json();
            document.getElementById('message').innerText = data.message || data.error;
        }
    </script>
</body>
</html>
```
