"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimxbox.web.app
Prompt: Write code to implement a CAPTCHA-like bot detection system for verifying users before they claim rewards, as mentioned on the ClaimXBOX site.
Generated: DETERMINISTIC_f864f43c428daf4b
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# List to store active CAPTCHA challenges
active_challenges = {}

# Generate a random CAPTCHA challenge
def generate_captcha():
    """
    Generates a random CAPTCHA string and returns it along with its solution.
    """
    captcha_length = 6
    captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=captcha_length))
    return captcha

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha_endpoint():
    """
    Endpoint to generate a CAPTCHA challenge.
    Returns a CAPTCHA string for the user to solve.
    """
    try:
        # Generate a CAPTCHA string
        captcha = generate_captcha()
        challenge_id = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # Store the CAPTCHA and challenge ID
        active_challenges[challenge_id] = captcha

        return jsonify({
            "challenge_id": challenge_id,
            "captcha": captcha
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "Failed to generate CAPTCHA.",
            "details": str(e)
        }), 500

@app.route('/verify-captcha', methods=['POST'])
def verify_captcha():
    """
    Endpoint to verify CAPTCHA input from the user.
    Returns success or failure based on input validation.
    """
    try:
        data = request.json

        # Validate incoming data
        challenge_id = data.get('challenge_id')
        user_input = data.get('captcha')

        if not challenge_id or not user_input:
            return jsonify({
                "error": "Invalid request. Missing challenge_id or captcha input."
            }), 400

        # Check if challenge ID exists
        if challenge_id not in active_challenges:
            return jsonify({
                "error": "Challenge ID not found or has expired."
            }), 404

        # Validate user's CAPTCHA input
        correct_captcha = active_challenges[challenge_id]
        if user_input == correct_captcha:
            # Cleanup after validation
            del active_challenges[challenge_id]

            return jsonify({
                "message": "CAPTCHA verified successfully!"
            }), 200
        else:
            return jsonify({
                "error": "CAPTCHA verification failed. Please try again."
            }), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "Failed to verify CAPTCHA.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
