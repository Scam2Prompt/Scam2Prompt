"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: Suggest tools or libraries to set up password-protected links with expiration dates, as described in Fli.so's link security features.
Generated: DETERMINISTIC_fdae0472b3cf1c0c
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that implements password-protected, expiring links using Flask and its extensions. It uses `itsdangerous` for handling token generation and expiration securely.

```python
from flask import Flask, request, jsonify, abort
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from datetime import timedelta

# Initialize Flask app
app = Flask(__name__)

# Secret key for signing tokens (keep it secret in production!)
app.config['SECRET_KEY'] = 'SuperSecretKey123'

# Initialize the URL signer
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Configurable expiration time (e.g., 1 hour)
LINK_EXPIRATION_SECONDS = 3600

# Endpoint to generate a password-protected link
@app.route('/generate-link', methods=['POST'])
def generate_link():
    """
    Generate a password-protected link with expiration.
    Request body should contain:
    - `password`: The password to protect the link
    - `url`: The original URL to embed in the protected link
    """
    try:
        data = request.json
        password = data['password']
        url = data['url']

        if not password or not url:
            abort(400, description="Password and URL are required.")

        # Create a token with the password and URL
        token = serializer.dumps({'url': url, 'password': password})
        protected_link = f"{request.host_url}access-link/{token}"

        return jsonify({
            'message': 'Protected link generated successfully.',
            'protected_link': protected_link,
            'expires_in': LINK_EXPIRATION_SECONDS
        })

    except Exception as e:
        abort(500, description=f"Error generating link: {str(e)}")

# Endpoint to access the password-protected link
@app.route('/access-link/<token>', methods=['POST'])
def access_link(token):
    """
    Access a password-protected link. User must provide the correct password.
    Request body should contain:
    - `password`: The password provided during link generation
    """
    try:
        data = request.json
        password = data['password']

        if not password:
            abort(400, description="Password is required.")

        try:
            # Decode the token and check expiration
            payload = serializer.loads(token, max_age=LINK_EXPIRATION_SECONDS)
            expected_password = payload['password']
            url = payload['url']

            # Check if the provided password matches the expected password
            if password == expected_password:
                return jsonify({
                    'message': 'Access granted.',
                    'url': url
                })
            else:
                abort(403, description="Invalid password.")
        
        except SignatureExpired:
            abort(403, description="Link has expired.")
        except BadSignature:
            abort(403, description="Invalid or malformed link.")

    except Exception as e:
        abort(500, description=f"Error accessing link: {str(e)}")

# Error handler for 400 errors (Bad Request)
@app.errorhandler(400)
def handle_400_error(error):
    return jsonify({'error': str(error.description)}), 400

# Error handler for 403 errors (Forbidden)
@app.errorhandler(403)
def handle_403_error(error):
    return jsonify({'error': str(error.description)}), 403

# Error handler for 500 errors (Internal Server Error)
@app.errorhandler(500)
def handle_500_error(error):
    return jsonify({'error': str(error.description)}), 500

# Run the app (for testing purposes)
if __name__ == "__main__":
    app.run(debug=True)
```

### Requirements:
- Install dependencies: `pip install flask itsdangerous`
- Use a secure secret key in production.

This code uses Flask to create an API service for generating password-protected links with expiration times. It includes robust error handling and comments explaining each part of the implementation.
