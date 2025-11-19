"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Generate a script to restrict access to the VEMP Hunt campaign for users from the USA, UK, and Canada, as per the terms and conditions.
Generated: DETERMINISTIC_8a428515b9813cf0
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from functools import wraps
from flask import Flask, request, jsonify, abort
import pycountry

app = Flask(__name__)

# List of restricted countries (ISO Alpha-2 codes)
RESTRICTED_COUNTRIES = {'US', 'GB', 'CA'}

def get_country_from_ip(ip_address):
    """
    Get country code from IP address using a geolocation service.
    In production, replace with a proper geolocation API or library.
    This is a mock implementation for demonstration.
    """
    # NOTE: In a real application, use a proper IP geolocation service like:
    # - MaxMind GeoIP
    # - ipapi.co
    # - IP2Location
    # This is just a mock that returns US for demonstration
    return 'US'  # Mock response - always returns US for testing

def restrict_countries(view_function):
    """
    Decorator to restrict access based on user's country.
    """
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        # Get client IP (consider X-Forwarded-For if behind proxy)
        client_ip = request.remote_addr
        
        try:
            country_code = get_country_from_ip(client_ip)
            
            # Check if country is restricted
            if country_code in RESTRICTED_COUNTRIES:
                abort(403, description="Access to this campaign is restricted in your country.")
                
            return view_function(*args, **kwargs)
            
        except Exception as e:
            # Log the error in production
            app.logger.error(f"Error checking country restriction: {str(e)}")
            abort(500, description="An error occurred while processing your request.")
    
    return wrapper

@app.route('/vemp-hunt', methods=['GET'])
@restrict_countries
def vemp_hunt_campaign():
    """
    Main endpoint for the VEMP Hunt campaign.
    Only accessible to users from non-restricted countries.
    """
    return jsonify({
        'status': 'success',
        'message': 'Welcome to the VEMP Hunt campaign!'
    })

@app.errorhandler(403)
def forbidden_error(error):
    return jsonify({
        'status': 'error',
        'message': error.description
    }), 403

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'status': 'error',
        'message': error.description
    }), 500

if __name__ == '__main__':
    app.run(debug=True)
```
