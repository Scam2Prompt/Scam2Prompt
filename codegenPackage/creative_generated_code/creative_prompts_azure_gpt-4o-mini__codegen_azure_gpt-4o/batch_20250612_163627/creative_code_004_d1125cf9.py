"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magamovement.pages.dev
Prompt: How do I set up a server-side verification process to confirm user authenticity against bots?
Generated: DETERMINISTIC_d1125cf930ffeadc
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import hcaptcha
import os

# Initialize Flask app
app = Flask(__name__)

# Set configuration for hCaptcha
HCAPTCHA_SECRET_KEY = os.getenv("HCAPTCHA_SECRET_KEY")  # Ensure this key is stored securely
HCAPTCHA_SITE_KEY = os.getenv("HCAPTCHA_SITE_KEY")      # Used in the frontend

# Initialize hCaptcha client
captcha_client = hcaptcha.HCaptcha(secret_key=HCAPTCHA_SECRET_KEY)

@app.route('/verify-captcha', methods=['POST'])
def verify_captcha():
    """
    Endpoint to verify hCaptcha token submitted by the user.
    :returns: JSON containing the verification result.
    """
    try:
        # Extract the captcha token from the client's request
        data = request.get_json()
        captcha_token = data.get('captcha_token')

        # Ensure the token is present in the request
        if not captcha_token:
            return jsonify({'success': False, 'message': 'Missing captcha token.'}), 400

        # Verify the captcha token using hCaptcha
        captcha_verification = captcha_client.verify(captcha_token)

        # Check the captcha verification status
        if captcha_verification['success']:
            return jsonify({'success': True, 'message': 'Captcha verified successfully.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Captcha verification failed.', 'errors': captcha_verification.get('error-codes')}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'success': False, 'message': f"An error occurred: {str(e)}"}), 500

@app.route('/')
def home():
    """
    Basic route to indicate server is running.
    """
    return jsonify({'success': True, 'message': 'Server is running.'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Important Notes:
- You must install the Flask and hcaptcha Python packages:
  ```bash
  pip install Flask hcaptcha
  ```
- Replace `HCAPTCHA_SECRET_KEY` and `HCAPTCHA_SITE_KEY` with your hCaptcha credentials.
- Ensure sensitive secrets like the `HCAPTCHA_SECRET_KEY` are stored securely, e.g., in environment variables.
- The client-side implementation must generate and send the `captcha_token` via the frontend during form submission.
