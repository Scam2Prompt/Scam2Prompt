"""
Generated Code Metadata:
========================
Original URL: https://unchainedspepe.com
Prompt: Generate code to display a custom access restricted page for users accessing a website through a VPN or proxy, including a message and a support contact.
Generated: DETERMINISTIC_bd88099e4348e7a7
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Custom HTML template for the access restricted page
RESTRICTED_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Restricted</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        h1 { color: red; }
        p { font-size: 18px; }
    </style>
</head>
<body>
    <h1>Access Restricted</h1>
    <p>It seems you are trying to access this site through a VPN or proxy.</p>
    <p>Please disable your VPN or proxy and try again.</p>
    <p>If you need assistance, contact support at: <a href="mailto:support@example.com">support@example.com</a></p>
</body>
</html>
"""

def is_using_vpn_or_proxy(ip_address):
    """
    Check if the user is accessing the site through a VPN or proxy.
    This is a placeholder function. In a real application, you would implement
    logic to check the IP address against a database of known VPN/proxy IPs.
    
    :param ip_address: The IP address of the user
    :return: True if the IP is from a VPN or proxy, False otherwise
    """
    # Placeholder logic for demonstration purposes
    # In production, replace this with actual VPN/proxy detection logic
    return ip_address.startswith("192.168.")  # Example condition

@app.route('/')
def index():
    """
    Main route for the application. Checks if the user is using a VPN or proxy
    and displays the restricted access page if they are.
    
    :return: Rendered HTML page
    """
    user_ip = request.remote_addr  # Get the user's IP address
    if is_using_vpn_or_proxy(user_ip):
        return render_template_string(RESTRICTED_PAGE_TEMPLATE)
    
    return "<h1>Welcome to the website!</h1>"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)  # Run the Flask app
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
