"""
Generated Code Metadata:
========================
Original URL: https://unchainedspepe.com
Prompt: Write a Python script to detect and block VPN or proxy users from accessing a website.
Generated: DETERMINISTIC_df5d0ddec067d1be
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, request, abort

app = Flask(__name__)

# List of known VPN and proxy IP addresses (for demonstration purposes)
# In a production environment, this should be dynamically updated from a reliable source.
VPN_PROXY_IPS = {
    "192.0.2.1",  # Example IP address
    "203.0.113.5",  # Example IP address
    # Add more known VPN/proxy IPs here
}

def is_vpn_or_proxy(ip_address):
    """
    Check if the given IP address is in the list of known VPN or proxy IPs.

    Args:
        ip_address (str): The IP address to check.

    Returns:
        bool: True if the IP address is a VPN or proxy, False otherwise.
    """
    return ip_address in VPN_PROXY_IPS

@app.route('/')
def home():
    """
    Home route that checks if the user is using a VPN or proxy.

    Returns:
        str: A welcome message if the user is not using a VPN or proxy.
        abort: 403 Forbidden if the user is detected as using a VPN or proxy.
    """
    # Get the user's IP address from the request
    user_ip = request.remote_addr

    # Check if the user is using a VPN or proxy
    if is_vpn_or_proxy(user_ip):
        # Block access if the user is using a VPN or proxy
        abort(403, description="Access denied: VPN or proxy usage is not allowed.")

    return "Welcome to the website!"

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

**Note:** In a real-world application, you would typically use a more comprehensive method to detect VPNs and proxies, such as integrating with a third-party service that provides updated lists of VPN and proxy IP addresses.
