"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Develop a code snippet to restrict access to the platform for users from specific regions (e.g., USA, UK, Canada), as mentioned in the eligibility criteria for MELLSTROY Hunt.
Generated: DETERMINISTIC_29d878ebe837a9e8
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of restricted regions (ISO Country Codes for simplicity)
RESTRICTED_REGIONS = {"US", "GB", "CA"}  # USA, UK, Canada


def get_user_region(ip_address: str) -> str:
    """
    Mock function to get the region based on IP address.
    In production, use a GeoIP library or API (e.g., MaxMind, ipinfo.io).
    """
    geo_ip_database = {
        "192.168.1.1": "US",  # Example IP -> USA
        "192.168.1.2": "GB",  # Example IP -> UK
        "192.168.1.3": "CA",  # Example IP -> Canada
        "192.168.1.4": "IN",  # Example IP -> India
    }
    return geo_ip_database.get(ip_address, "UNKNOWN")


@app.route('/access', methods=['GET'])
def check_access():
    """
    Endpoint to check if a user can access the platform.
    """
    try:
        # Get the user's IP address (mocked here for demonstration purposes)
        user_ip = request.args.get('ip', '192.168.1.1')  # Default IP for testing
        
        # Determine the user's region
        region = get_user_region(user_ip)
        
        if region == "UNKNOWN":
            return jsonify({"message": "Unable to determine region.", "access_granted": False}), 400
        
        # Check if the region is restricted
        if region in RESTRICTED_REGIONS:
            return jsonify({"message": f"Access denied for users from {region}.", "access_granted": False}), 403
        
        # Grant access if the region is not restricted
        return jsonify({"message": "Access granted.", "access_granted": True}), 200
    
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
