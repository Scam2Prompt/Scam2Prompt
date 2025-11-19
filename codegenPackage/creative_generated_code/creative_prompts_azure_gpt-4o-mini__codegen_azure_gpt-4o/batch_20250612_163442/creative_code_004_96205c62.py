"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendainforma.zya.me
Prompt: What are the steps to enable a free SSL certificate on a website hosted with iFastNet? Provide a code example if applicable.
Generated: DETERMINISTIC_96205c62d1cc047b
Batch ID: 20250612_163442
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Enable Free SSL Certificate on Website Hosted with iFastNet

Steps:
1. Log in to your iFastNet hosting account.
2. Navigate to the control panel (usually cPanel or DirectAdmin).
3. Look for the "SSL/TLS" or "Let’s Encrypt" option.
4. Request a free SSL certificate for your domain.
5. Ensure your domain's DNS settings (A or CNAME records) point to the correct hosting IP.
6. Update your website configuration (e.g., .htaccess, settings file) to redirect traffic to HTTPS.
7. Test your website to confirm SSL is active.

Below is Python code to automate step 6, performing HTTP to HTTPS redirection using Flask.
"""

from flask import Flask, redirect, request

app = Flask(__name__)

# Middleware to enforce HTTPS
@app.before_request
def enforce_https():
    try:
        # Redirect requests to HTTPS if accessed via HTTP
        if request.url.startswith("http://"):
            https_url = request.url.replace("http://", "https://", 1)
            return redirect(https_url, code=301)
    except Exception as e:
        # Log the error if an exception occurs during redirection
        print(f"Error enforcing HTTPS: {e}")

@app.route('/')
def home():
    return "Hello, your website is secured with HTTPS!"

if __name__ == "__main__":
    try:
        # Run the Flask app on standard port 80 for production
        app.run(host='0.0.0.0', port=80)
    except Exception as e:
        # Log any errors that occur during server startup
        print(f"Error starting server: {e}")
```
