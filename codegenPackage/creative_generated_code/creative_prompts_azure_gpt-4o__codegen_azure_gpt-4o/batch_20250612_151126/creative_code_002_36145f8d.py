"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Generate code for a newsletter subscription form that adheres to GDPR compliance, inspired by the ALPS Foundation's email subscription system.
Generated: DETERMINISTIC_36145f8d3561b9cd
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# In-memory storage for subscribers (for demonstration purposes)
subscribers = []

# Regular expression for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# GDPR-compliant subscription form page
@app.route('/')
def subscription_form():
    # Render the subscription HTML form
    return render_template('subscription_form.html')

# Endpoint to handle form submission
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Parse form data
        email = request.form.get('email')
        consent = request.form.get('consent')

        # Validate email address
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email address'}), 400

        # Check if GDPR consent is provided
        if consent != 'on':
            return jsonify({'error': 'GDPR consent is required'}), 400

        # Check if email is already subscribed
        if email in subscribers:
            return jsonify({'error': 'This email is already subscribed'}), 400

        # Save the subscriber (for demonstration, storing in memory)
        subscribers.append(email)

        return jsonify({'message': 'Subscription successful'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# HTML template for the subscription form
@app.route('/subscription_form.html')
def subscription_form_html():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Newsletter Subscription</title>
    </head>
    <body>
        <h1>Subscribe to our Newsletter</h1>
        <form action="/subscribe" method="POST">
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            
            <label for="consent">
                <input type="checkbox" id="consent" name="consent" required>
                I agree to the processing of my personal data in accordance with the GDPR.
            </label><br><br>
            
            <button type="submit">Subscribe</button>
        </form>
    </body>
    </html>
    '''
    return html_content

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
