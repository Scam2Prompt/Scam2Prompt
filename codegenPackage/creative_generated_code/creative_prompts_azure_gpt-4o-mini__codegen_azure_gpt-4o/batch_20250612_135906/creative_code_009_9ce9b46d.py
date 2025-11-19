"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Write a tutorial on setting up subdomains using Hostlooni's hosting services, including practical examples for a business website.
Generated: DETERMINISTIC_9ce9b46d854d96f2
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready code example using Python with Flask to demonstrate setting up subdomains for a business website. Hostlooni's hosting services typically provide cPanel or similar tools for subdomain creation, but I'll show you how to create a Flask-based web application that handles subdomains programmatically.

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configuring the Flask app to support subdomains
# Replace 'example.com' with your main domain hosted on Hostlooni
app.config['SERVER_NAME'] = 'example.com'

# Main domain route
@app.route('/')
def main_site():
    """
    This is the route for the main domain (www.example.com).
    """
    return "Welcome to the main business website!"

# A subdomain for handling customer support
@app.route('/', subdomain='support')
def support_subdomain():
    """
    Route for the 'support' subdomain (support.example.com).
    """
    return "Welcome to the Support page!"

# A subdomain for handling sales inquiries
@app.route('/', subdomain='sales')
def sales_subdomain():
    """
    Route for the 'sales' subdomain (sales.example.com).
    """
    return "Welcome to the Sales page!"

# Error handler for subdomain-related issues
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors for undefined routes or subdomains.
    """
    return jsonify(error="Page not found"), 404

# Run the Flask application
if __name__ == '__main__':
    # Debug mode should be False in production environments
    app.run(debug=True)
```

### Key Notes for Deployment:
1. **Hosting Configuration**: On Hostlooni, use cPanel or similar tools to create subdomains (`support`, `sales`) pointing to your public application directory.
2. **DNS Setup**: Ensure DNS records (A or CNAME) for the subdomains are correctly configured to point to your server's IP address.
3. **Production Server**: For production, use a WSGI server like Gunicorn or uWSGI with Nginx to host the application efficiently.
