"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unchainedspepe.com
Prompt: What are the security reasons for restricting access to websites for VPN or proxy users?
Generated: DETERMINISTIC_6068262395ead1ee
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that demonstrates how to restrict access to a website for VPN or proxy users. This is a simplified example that checks the IP address against a known list of VPN/proxy IP ranges (commonly provided by third-party services).

```python
import ipaddress
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of known VPN/proxy IP ranges (example data, in practice this would be fetched from a reliable source)
vpn_proxy_ip_ranges = [
    "192.168.100.0/24",  # Example VPN range
    "10.10.0.0/16",      # Example proxy range
    "172.16.5.0/24"      # Another example range
]

def is_vpn_or_proxy(ip_address):
    """
    Checks if the given IP address matches any known VPN/proxy IP ranges.
    
    Args:
        ip_address (str): The IP address to check.
    
    Returns:
        bool: True if the IP address belongs to a VPN/proxy range, False otherwise.
    """
    try:
        ip = ipaddress.ip_address(ip_address)
        for range in vpn_proxy_ip_ranges:
            if ip in ipaddress.ip_network(range):
                return True
        return False
    except ValueError:
        # Handle invalid IP address formats gracefully
        return False

@app.route('/')
def home():
    """
    Main route for the website. Restricts access if the user is identified as a VPN/proxy user.
    """
    client_ip = request.remote_addr  # Get the client's IP address from the request
    if is_vpn_or_proxy(client_ip):
        # Return a 403 Forbidden response if the client's IP is detected as VPN/proxy
        return jsonify({"error": "Access Denied: VPN or Proxy use detected."}), 403
    
    return jsonify({"message": "Welcome to the website!"})

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 Internal Server Error.
    """
    return jsonify({"error": "An internal server error occurred."}), 500

@app.errorhandler(404)
def not_found_error(e):
    """
    Custom error handler for 404 Not Found.
    """
    return jsonify({"error": "Resource not found."}), 404

if __name__ == '__main__':
    # Run the Flask application (debug mode should be disabled in production)
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Instructions:
1. Install Flask if not already installed: `pip install flask`
2. Save this code in a file, e.g., `app.py`.
3. Run the application: `python app.py`.
4. Test the behavior by sending requests from different IPs, including IPs in the `vpn_proxy_ip_ranges` list.

Security note: In production, use third-party services or APIs to maintain accurate lists of VPN/proxy IPs and ensure thorough testing to avoid false positives.
