"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waffles887.pages.dev
Prompt: What are the best practices for ensuring user verification against bots in web forms?
Generated: DETERMINISTIC_0f37d17bbfd396b0
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template_string, jsonify
import re
import random
import string
import time

app = Flask(__name__)

# Simple HTML form template with a CAPTCHA
form_template = """
<!doctype html>
<html>
<head>
    <title>User Verification Form</title>
</head>
<body>
    <h1>User Verification</h1>
    <form action="/submit" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>

        <label for="captcha">Solve: {{ captcha }}</label>
        <input type="text" id="captcha" name="captcha" required><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Generate a simple CAPTCHA (e.g., a math problem)
def generate_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return f"{num1} + {num2} = ?", num1 + num2

@app.route('/')
def index():
    captcha_text, captcha_answer = generate_captcha()
    # Store the correct answer for validation
    # In a real application, consider using session or database
    request.environ['captcha_answer'] = captcha_answer  
    return render_template_string(form_template, captcha=captcha_text)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    captcha_response = request.form.get('captcha')

    # Validate username format
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        return jsonify({"error": "Invalid username format. It should be 3-20 characters long and contain only letters, numbers, or underscores."}), 400

    # Validate CAPTCHA response against the stored answer
    try:
        correct_answer = request.environ['captcha_answer']
        if int(captcha_response) != correct_answer:
            return jsonify({"error": "Incorrect CAPTCHA answer."}), 400
        
        # CAPTCHA passed, proceed with processing
        return jsonify({"message": "User verified successfully!"}), 200

    except (ValueError, KeyError) as e:
        return jsonify({"error": "An error occurred during verification."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
