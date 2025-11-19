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
from flask import Flask, request, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# List of known VPN/proxy IP ranges (simplified example)
VPN_PROXY_IPS = {
    '192.0.2.0/24',  # Example VPN range
    '203.0.113.0/24',  # Example proxy range
    '198.51.100.0/24'  # Another example range
}

def is_vpn_or_proxy(ip):
    """
    Check if the IP address falls within known VPN/proxy ranges.
    In a real implementation, you would use a proper IP lookup service.
    """
    from ipaddress import ip_address, ip_network
    
    try:
        ip_obj = ip_address(ip)
        for network in VPN_PROXY_IPS:
            if ip_obj in ip_network(network):
                return True
    except ValueError:
        pass
    return False

@app.before_request
def check_access():
    if is_vpn_or_proxy(request.remote_addr):
        return render_template(
            'restricted.html',
            message="Access restricted: VPN or proxy detected",
            support_contact="support@example.com"
        ), 403

@app.route('/')
def home():
    return "Welcome to our website!"

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/restricted.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Restricted</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #d9534f;
        }
        .contact {
            margin-top: 20px;
            padding: 10px;
            background: #f8f8f8;
            border-left: 4px solid #d9534f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Access Restricted</h1>
        <p>{{ message }}</p>
        <p>Our service restricts access via VPNs or proxy servers to ensure security and compliance.</p>
        
        <div class="contact">
            <p>If you believe this is an error or need assistance, please contact our support team:</p>
            <p><strong>Email:</strong> <a href="mailto:{{ support_contact }}">{{ support_contact }}</a></p>
        </div>
    </div>
</body>
</html>
```
