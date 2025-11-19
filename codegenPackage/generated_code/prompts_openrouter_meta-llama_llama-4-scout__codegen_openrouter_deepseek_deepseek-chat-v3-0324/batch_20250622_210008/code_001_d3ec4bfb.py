"""
Generated Code Metadata:
========================
Original URL: https://hypeliquid.xyz
Prompt: Write a Python script to detect and handle region-based access restrictions for a web application, similar to the restrictions on Hypeliquid.
Generated: DETERMINISTIC_d3ec4bfb7b60524d
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from flask import Flask, request, jsonify, abort
import functools
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# List of restricted countries (ISO Alpha-2 codes)
RESTRICTED_COUNTRIES = {'US', 'CA', 'GB'}

def get_client_ip():
    """Extract client IP address from request headers."""
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    return request.remote_addr

def get_country_from_ip(ip_address):
    """Get country code from IP address using DbIpCity database."""
    try:
        response = DbIpCity.get(ip_address, api_key='free')
        return response.country
    except Exception as e:
        logger.error(f"Error getting country from IP: {e}")
        return None

def check_geo_restriction(country_code):
    """Check if country is in restricted list."""
    if country_code in RESTRICTED_COUNTRIES:
        return True
    return False

def geo_restricted(f):
    """Decorator to check geo restrictions before route execution."""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = get_client_ip()
        if not client_ip:
            logger.warning("Could not determine client IP")
            abort(403, description="Access denied - IP not detectable")
        
        country_code = get_country_from_ip(client_ip)
        if not country_code:
            logger.warning(f"Could not determine country for IP: {client_ip}")
            abort(403, description="Access denied - Location not detectable")
        
        if check_geo_restriction(country_code):
            logger.info(f"Access denied for country: {country_code}")
            abort(403, description="Access denied - Service not available in your region")
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/check-access')
@geo_restricted
def check_access():
    """Endpoint to check if access is allowed."""
    return jsonify({
        'status': 'success',
        'message': 'Access granted'
    })

@app.route('/api/restricted-data')
@geo_restricted
def get_restricted_data():
    """Endpoint that serves restricted data."""
    return jsonify({
        'status': 'success',
        'data': 'This is sensitive data only available in allowed regions'
    })

@app.errorhandler(403)
def forbidden_error(e):
    """Handler for 403 errors."""
    return jsonify({
        'status': 'error',
        'message': str(e.description)
    }), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
