"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-oasisprotocoi.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in the context of flagged sites?
Generated: DETERMINISTIC_be4ac2491276389c
Batch ID: 20250612_162601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Flask web application against phishing attacks

from flask import Flask, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

# Regular expression to validate URLs
URL_REGEX = re.compile(
    r'^(https?:\/\/)'  # Protocol (http or https)
    r'([a-zA-Z0-9.-]+)'  # Domain name
    r'(\.[a-zA-Z]{2,})$'  # Top-level domain (e.g., .com)
)

# List of flagged domains known for phishing
FLAGGED_DOMAINS = [
    "phishingsite.com",
    "malicious-site.net",
    "fake-login.org"
]

# Function to validate URLs
def is_safe_url(url):
    """
    Validate a URL to ensure its safety.
    Checks if the domain matches known flagged domains.
    """
    if not URL_REGEX.match(url):  # Validate URL format
        return False

    domain = url.split("://")[-1].split("/")[0].lower()
    if domain in FLAGGED_DOMAINS:  # Check against flagged domains
        return False

    return True


@app.route('/submit', methods=['POST'])
def submit_url():
    """
    Endpoint for submitting URLs.
    """
    try:
        # Extract URL from the POST request
        url = request.form.get("url", "").strip()

        # Validate the URL
        if not url or not is_safe_url(url):
            return "Invalid or unsafe URL detected.", 400

        # Process the safe URL (e.g., store or redirect)
        # Example: Redirect to the given URL after validation
        return redirect(url, code=302)

    except Exception as e:
        # Log the error and return a safe response
        app.logger.error(f"Error validating the URL: {e}")
        return "An error occurred while processing your request.", 500


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page to prevent phishing-related attacks 
    by showing friendly error messages instead of browser error pages.
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error page for graceful handling of server-side errors.
    """
    return render_template("500.html"), 500


if __name__ == '__main__':
    # Run the application securely
    # Example: Use HTTPS for deployment to prevent MITM (Man-in-the-Middle) attacks
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
```

### Notes:
- Replace `cert.pem` and `key.pem` with your actual certificate and key files for HTTPS.
- Consider integrating third-party services (like Google's Safe Browsing API) to dynamically detect malicious URLs.
- Regularly update `FLAGGED_DOMAINS` with known phishing sites from trusted sources to enhance security.
