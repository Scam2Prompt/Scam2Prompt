"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Write a Python script that uses cookies to manage user consent preferences for a web application, similar to the functionality described on the Masa website.
Generated: DETERMINISTIC_fe3f24c0b5b1ce4d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# HTML template for the consent banner
CONSENT_BANNER_HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent</title>
    <style>
        #consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            text-align: center;
            display: {display};
        }
    </style>
</head>
<body>
    <div id="consent-banner">
        <p>This website uses cookies to enhance the user experience. 
        <a href="/privacy-policy">Learn more</a>.</p>
        <button onclick="acceptCookies()">Accept</button>
        <button onclick="rejectCookies()">Reject</button>
    </div>
    <script>
        function acceptCookies() {
            document.cookie = "user_consent=accepted; path=/; max-age=31536000"; // 1 year
            location.reload();
        }
        function rejectCookies() {
            document.cookie = "user_consent=rejected; path=/; max-age=31536000"; // 1 year
            location.reload();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    # Check for user consent cookie
    consent = request.cookies.get('user_consent')
    
    # Determine if the consent banner should be displayed
    if consent is None:
        display = 'block'  # Show banner if no consent has been given
    else:
        display = 'none'   # Hide banner if consent has been given

    # Render the consent banner with the appropriate display style
    return render_template_string(CONSENT_BANNER_HTML.format(display=display))

@app.route('/privacy-policy')
def privacy_policy():
    # Placeholder for privacy policy page
    return "<h1>Privacy Policy</h1><p>Your privacy is important to us.</p>"

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Log the error and exit gracefully
        print(f"An error occurred: {e}")
```
