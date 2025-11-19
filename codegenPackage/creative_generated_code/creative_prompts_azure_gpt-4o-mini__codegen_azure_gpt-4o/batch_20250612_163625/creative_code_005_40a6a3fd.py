"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://02ip.ru
Prompt: What are the best practices for using IP Logger's consent collection feature to comply with GDPR regulations?
Generated: DETERMINISTIC_40a6a3fd3fa3767f
Batch ID: 20250612_163625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates best practices for collecting user consent when using an IP Logger feature to comply with GDPR regulations.
It assumes you are using a web framework like Flask to handle web requests. The code focuses on obtaining explicit user consent
before logging their IP address.
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Store user consents in memory for simplicity (use a database in production)
user_consents = {}

@app.route('/')
def home():
    """
    Render the consent page template.
    The template should explain why the user's IP is being logged and provide an opt-in mechanism.
    """
    return render_template('consent.html')  # Ensure you have a 'consent.html' file in the templates folder


@app.route('/consent', methods=['POST'])
def collect_consent():
    """
    Endpoint to collect user consent.
    Expects a POST request with a 'consent' parameter indicating whether the user agrees to log their IP.
    """
    try:
        user_id = request.form.get('user_id')  # Identify the user uniquely (e.g., via session or user account)
        consent = request.form.get('consent')  # User's consent choice, e.g., 'yes' or 'no'

        if not user_id or consent not in ['yes', 'no']:
            return jsonify({'error': 'Invalid input'}), 400

        # Store the consent status
        user_consents[user_id] = consent

        if consent == 'yes':
            ip_address = request.remote_addr  # Log the user's IP address
            # Do something with the IP address, such as saving it securely (e.g., in a database)
            return jsonify({'message': 'Consent granted. IP address logged.', 'ip_address': ip_address}), 200
        else:
            return jsonify({'message': 'Consent denied. IP address not logged.'}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500


@app.route('/consent-status', methods=['GET'])
def check_consent():
    """
    Endpoint to check the user's consent status.
    Expects a 'user_id' parameter in the request.
    """
    try:
        user_id = request.args.get('user_id')  # Identify the user uniquely

        if not user_id:
            return jsonify({'error': 'Invalid input'}), 400

        consent = user_consents.get(user_id, 'no')  # Default to 'no' if consent was never collected
        return jsonify({'user_id': user_id, 'consent': consent}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Additional Notes:
1. **HTML Template (`consent.html`)**:
   You need to create a consent.html file with clear language explaining the purpose of logging IP addresses, alongside a checkbox or button for users to opt-in or opt-out.

2. **Security**: Ensure secure storage of IP addresses and encrypt sensitive data if needed.

3. **Compliance**: Regularly review GDPR compliance requirements as they may evolve over time.
