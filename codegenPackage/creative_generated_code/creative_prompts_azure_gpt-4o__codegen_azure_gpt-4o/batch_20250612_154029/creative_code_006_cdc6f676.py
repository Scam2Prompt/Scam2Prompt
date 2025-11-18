"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Develop a script to restrict access to the HAGGIS Hunt campaign for users from specific jurisdictions, as outlined in the legal terms on the website.
Generated: DETERMINISTIC_cdc6f67614d60d52
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from geoip import geolite2
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of restricted jurisdictions (country codes) based on legal terms
RESTRICTED_JURISDICTIONS = {'US', 'CA', 'AU', 'CN'}

def is_access_allowed(ip_address):
    """
    Checks if the IP address belongs to a restricted jurisdiction.
    
    Args:
        ip_address (str): IP address of the user.
        
    Returns:
        bool: True if access is allowed, False otherwise.
    """
    try:
        # Lookup the user's geographical location using the IP address
        match = geolite2.lookup(ip_address)
        if match and match.country:
            return match.country not in RESTRICTED_JURISDICTIONS
        else:
            return False  # Default to no access if location cannot be determined
    except Exception as e:
        # Log the exception (production systems should use logging libraries)
        print(f"Error determining access for IP {ip_address}: {e}")
        return False  # Deny access if an error occurs

@app.route('/haggis-hunt', methods=['GET'])
def haggis_hunt_access():
    """
    Endpoint to handle access requests for the HAGGIS Hunt campaign.
    Restricts access for users from specific jurisdictions.
    """
    # Extract the user's IP address from the request
    ip_address = request.remote_addr

    # Validate if the IP address format is correct (basic validation)
    if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip_address):
        return jsonify({"error": "Invalid IP address."}), 400

    # Check if access is allowed based on the IP address location
    if is_access_allowed(ip_address):
        return jsonify({"message": "Access granted. Enjoy the HAGGIS Hunt campaign!"}), 200
    else:
        return jsonify({"error": "Access restricted based on your jurisdiction."}), 403

if __name__ == '__main__':
    # Run the Flask app on localhost
    app.run(host='0.0.0.0', port=5000)
```
