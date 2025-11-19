"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpcoin.pages.dev
Prompt: What are the best practices for ensuring user verification to prevent bot access in APIs?
Generated: DETERMINISTIC_c426105081dfc005
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import hcaptcha
import logging

app = Flask(__name__)

# Configure logging for production use
logging.basicConfig(level=logging.INFO)

# Replace with your hCaptcha secret key
HCAPTCHA_SECRET_KEY = "your_hcaptcha_secret_key"

@app.route('/api/resource', methods=['POST'])
def resource_access():
    """
    API route to provide resource access after user verification.
    """
    try:
        # Extract the hCaptcha token from the request
        hcaptcha_token = request.json.get('hcaptcha_token')
        if not hcaptcha_token:
            return jsonify({"error": "hCaptcha token is missing"}), 400
        
        # Verify the hCaptcha response
        verification_response = verify_hcaptcha(hcaptcha_token)
        if not verification_response.get("success"):
            logging.warning("hCaptcha verification failed.")
            return jsonify({"error": "User verification failed"}), 403
        
        # If verification is successful, provide resource access
        logging.info("User verified successfully.")
        return jsonify({"message": "Resource access granted"}), 200
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

def verify_hcaptcha(hcaptcha_token):
    """
    Verify the hCaptcha token using hCaptcha's API.

    Args:
        hcaptcha_token (str): The hCaptcha token provided by the client.

    Returns:
        dict: The response from hCaptcha verification.
    """
    try:
        response = hcaptcha.verify(HCAPTCHA_SECRET_KEY, hcaptcha_token)
        return response
    except Exception as e:
        logging.error(f"Error during hCaptcha verification: {str(e)}")
        return {"success": False}

if __name__ == '__main__':
    # Run the server
    app.run(host='0.0.0.0', port=5000)
```

**Note**: You'll need to install Flask (`pip install flask`) for this code to work. Additionally, install hCaptcha's Python SDK (`pip install hcaptcha`) or replace the verification logic with your preferred method if the SDK is unavailable. Replace `your_hcaptcha_secret_key` with your actual hCaptcha secret key for production use.
