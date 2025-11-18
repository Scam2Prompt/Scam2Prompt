"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtch.pro
Prompt: Recommend libraries or APIs for integrating Telegram login functionality into a web application, ensuring secure handling of user data.
Generated: DETERMINISTIC_e3cf9d0c3eb73650
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to implement Telegram login functionality into a web application
using Flask (a Python web framework) and the `hmac` library for secure data validation.

Dependencies:
- Flask: Install via `pip install flask`
- Python `hmac` (standard library) for secure data validation of incoming Telegram data
"""

from flask import Flask, request, jsonify
import hmac
import hashlib
import time

app = Flask(__name__)

# Replace these with your bot's credentials
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_BOT_SECRET_KEY = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()

def validate_telegram_login_data(data):
    """
    Validates the data received from the Telegram login widget.
    This ensures the data is authentic and has not been tampered with.
    
    Args:
        data (dict): The data received from Telegram.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    try:
        # Extract the hash from the data
        provided_hash = data.pop('hash', None)
        if not provided_hash:
            return False
        
        # Sort the keys and prepare the data string
        data_check_string = '\n'.join(f"{key}={value}" for key, value in sorted(data.items()))
        
        # Generate the HMAC-SHA256 hash based on the data string
        calculated_hash = hmac.new(TELEGRAM_BOT_SECRET_KEY, data_check_string.encode(), hashlib.sha256).hexdigest()
        
        # Compare the calculated hash with the provided hash
        return hmac.compare_digest(calculated_hash, provided_hash)
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error during Telegram data validation: {e}")
        return False

@app.route('/telegram-login', methods=['POST'])
def telegram_login():
    """
    API endpoint to handle Telegram login callback.

    Expects a JSON payload from the Telegram login widget.
    """
    try:
        # Parse the incoming JSON data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid payload"}), 400
        
        # Validate the Telegram login data
        if not validate_telegram_login_data(data):
            return jsonify({"error": "Invalid or tampered data"}), 403

        # Ensure the data has not expired (optional but recommended)
        auth_date = int(data.get("auth_date", 0))
        current_time = int(time.time())
        if current_time - auth_date > 86400:  # 24 hours expiration
            return jsonify({"error": "Login data expired"}), 403

        # At this point, the login is valid. You can now use the user info.
        user_id = data.get("id")
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        # Return success response
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name
            }
        })
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error during login: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
```

_NOTE_: Replace `your_telegram_bot_token` with the token for your Telegram bot. Make sure your web application is served over HTTPS in production, as Telegram requires secure endpoints for its login widget.
