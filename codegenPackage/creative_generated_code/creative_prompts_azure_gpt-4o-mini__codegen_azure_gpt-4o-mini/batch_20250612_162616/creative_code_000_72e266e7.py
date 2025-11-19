"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-fuelnetwork.app
Prompt: How can I implement security measures in my web application to prevent phishing attacks like those flagged by Cloudflare?
Generated: DETERMINISTIC_72e266e72091ce94
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, flash
import re
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key for production

# Configure logging
logging.basicConfig(level=logging.INFO)

# Regex pattern for validating URLs
URL_PATTERN = re.compile(r'^(https?://)?(www\.)?([a-z0-9-]+\.[a-z]{2,})(/.*)?$')


def is_valid_url(url):
    """
    Validate if the given URL is in a correct format.
    """
    return URL_PATTERN.match(url)


def log_suspicious_activity(ip_address, url):
    """
    Log suspicious activity for review.
    """
    logging.warning(f'Suspicious activity detected from IP: {ip_address}, URL: {url}')


@app.route('/')
def home():
    """Render the homepage."""
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    """
    Handle form submission, validate and sanitize input to prevent phishing.
    Redirect to success or error page based on validation.
    """
    url = request.form.get('url')
    ip_address = request.remote_addr  # Get the user's IP address

    # Validate the URL format
    if not is_valid_url(url):
        log_suspicious_activity(ip_address, url)
        flash('Invalid URL format. Please check and try again.', 'danger')
        return redirect(url_for('home'))

    # TODO: Add additional checks (e.g., check against known phishing domains)

    # If the URL is valid, proceed with the intended operation
    flash('URL submitted successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        logging.error(f'Error starting the server: {e}')
```

### Note:
- Ensure you have Flask installed in your Python environment (`pip install Flask`).
- This code implements basic URL validation and logs suspicious activity. You can expand upon this with more advanced security measures as required.
