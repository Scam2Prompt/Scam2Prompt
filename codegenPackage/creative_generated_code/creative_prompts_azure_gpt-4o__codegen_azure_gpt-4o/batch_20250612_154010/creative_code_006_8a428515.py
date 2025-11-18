"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Generate a script to restrict access to the VEMP Hunt campaign for users from the USA, UK, and Canada, as per the terms and conditions.
Generated: DETERMINISTIC_8a428515b9813cf0
Batch ID: 20250612_154010
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

# Initialize the Flask application
app = Flask(__name__)

# Define the list of restricted countries
RESTRICTED_COUNTRIES = {"USA", "UK", "Canada"}

@app.route('/vemp-hunt-access', methods=['GET'])
def restrict_access():
    """
    Endpoint to restrict access to the VEMP Hunt campaign based on user's country.
    """
    try:
        # Simulated user country retrieval from request headers (e.g., GeoIP middleware or headers)
        user_country = request.headers.get('X-Country', None)
        
        if not user_country:
            # If country information is missing, return an error response
            return jsonify({
                "success": False,
                "message": "Access denied: Unable to determine user's country."
            }), 400

        # Check if the country is in the restricted list
        if user_country in RESTRICTED_COUNTRIES:
            # Deny access for restricted countries
            return jsonify({
                "success": False,
                "message": f"Access denied: Users from {user_country} are restricted from participating in the VEMP Hunt campaign."
            }), 403
        
        # Allow access for other countries
        return jsonify({
            "success": True,
            "message": "Access granted: You can participate in the VEMP Hunt campaign."
        }), 200

    except Exception as e:
        # Handle unexpected server errors gracefully
        return jsonify({
            "success": False,
            "message": f"An error occurred while processing your request: {str(e)}"
        }), 500

# Run the Flask app
if __name__ == "__main__":
    # Host Flask app on localhost and default port 5000
    app.run(host="0.0.0.0", port=5000)
```
