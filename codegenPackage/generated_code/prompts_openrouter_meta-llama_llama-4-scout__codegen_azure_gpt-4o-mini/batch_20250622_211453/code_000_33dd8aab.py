"""
Generated Code Metadata:
========================
Original URL: https://etherpool.org
Prompt: Implement a CAPTCHA verification system using Python and the Flask framework that checks for unusual activity from IP addresses.
Generated: DETERMINISTIC_33dd8aabd4e9a53b
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import string
import time
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# In-memory storage for IP address activity
ip_activity = defaultdict(list)

# CAPTCHA form
class CaptchaForm(FlaskForm):
    captcha = StringField('CAPTCHA', validators=[DataRequired()])
    submit = SubmitField('Submit')

def generate_captcha():
    """Generate a random CAPTCHA string."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route('/captcha', methods=['GET', 'POST'])
def captcha():
    """Serve the CAPTCHA verification page."""
    form = CaptchaForm()
    ip_address = request.remote_addr

    # Generate a new CAPTCHA if it's a GET request
    if request.method == 'GET':
        captcha_value = generate_captcha()
        session['captcha'] = captcha_value
        return jsonify({'captcha': captcha_value})

    # Handle form submission
    if form.validate_on_submit():
        # Check if the submitted CAPTCHA matches the session CAPTCHA
        if form.captcha.data == session.get('captcha'):
            # Reset IP activity on successful CAPTCHA
            ip_activity[ip_address] = []
            return jsonify({'message': 'CAPTCHA verified successfully!'}), 200
        else:
            # Log unusual activity
            log_unusual_activity(ip_address)
            return jsonify({'message': 'CAPTCHA verification failed!'}), 400

    return jsonify({'message': 'Invalid form submission!'}), 400

def log_unusual_activity(ip_address):
    """Log unusual activity for the given IP address."""
    current_time = time.time()
    ip_activity[ip_address].append(current_time)

    # Keep only the last 10 minutes of activity
    ip_activity[ip_address] = [t for t in ip_activity[ip_address] if current_time - t < 600]

    # If there are more than 5 requests in the last 10 minutes, flag as unusual
    if len(ip_activity[ip_address]) > 5:
        print(f"Unusual activity detected from IP: {ip_address}")

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'message': 'Internal server error!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
