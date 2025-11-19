"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pineappledex.org
Prompt: Generate a code example that demonstrates how to handle human verification in a web application, inspired by the methods used on PineappleDex.
Generated: DETERMINISTIC_32d8dab5dc7967e8
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template_string, jsonify
import random, string

app = Flask(__name__)

# Generate a random CAPTCHA string
def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# In-memory storage for CAPTCHA values (simplified for demonstration)
# In production, you would use a more robust storage method (e.g., a database or cache system)
captcha_store = {}

@app.route('/')
def index():
    """
    Render the home page with a CAPTCHA for human verification.
    """
    captcha = generate_captcha()
    session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    captcha_store[session_id] = captcha
    
    # Render a simple form with a CAPTCHA challenge
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Human Verification</title>
    </head>
    <body>
        <h1>Human Verification</h1>
        <form action="/verify" method="post">
            <p>Please enter the following CAPTCHA:</p>
            <p><strong>{{ captcha }}</strong></p>
            <input type="hidden" name="session_id" value="{{ session_id }}">
            <input type="text" name="captcha_input" placeholder="Enter CAPTCHA" required>
            <button type="submit">Verify</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(html_template, captcha=captcha, session_id=session_id)

@app.route('/verify', methods=['POST'])
def verify():
    """
    Verify the CAPTCHA submitted by the user.
    """
    session_id = request.form.get('session_id')
    captcha_input = request.form.get('captcha_input')
    
    if not session_id or not captcha_input:
        return jsonify({"error": "Invalid request. Missing required fields."}), 400
    
    # Retrieve the original CAPTCHA
    original_captcha = captcha_store.get(session_id)
    if not original_captcha:
        return jsonify({"error": "Session not found or expired."}), 400
    
    # Validate the CAPTCHA
    if captcha_input.strip().upper() == original_captcha:
        del captcha_store[session_id]  # Cleanup to prevent reuse
        return jsonify({"message": "Human verification successful!"}), 200
    else:
        return jsonify({"error": "CAPTCHA verification failed."}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
