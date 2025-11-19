"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Write a Python script that uses cookies to manage user consent preferences for a web application, similar to the functionality described on the Masa website.
Generated: DETERMINISTIC_fe3f24c0b5b1ce4d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, make_response, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

# HTML template for the consent banner
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Cookie Consent Example</title>
</head>
<body>
    <div id="consent-banner" style="display: {{ 'none' if consent else 'block' }}; background: #f8d7da; padding: 20px; position: fixed; bottom: 0; width: 100%;">
        <p>This website uses cookies to enhance user experience. Do you consent to the use of cookies?</p>
        <button onclick="setConsent(true)">Accept</button>
        <button onclick="setConsent(false)">Decline</button>
    </div>
    
    <script>
        function setConsent(value) {
            document.cookie = "user_consent=" + value + "; path=/; max-age=" + (60 * 60 * 24 * 365) + ";";
            location.reload();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Render the main page and check user consent preference."""
    consent = get_user_consent()
    return render_template_string(HTML_TEMPLATE, consent=consent)

def get_user_consent():
    """Retrieve user consent from cookies.
    
    Returns:
        bool: True if consent is given, False if declined, None if not set.
    """
    consent_cookie = request.cookies.get('user_consent')
    if consent_cookie is None:
        return None
    return consent_cookie.lower() == 'true'

if __name__ == '__main__':
    # Run the Flask web application
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        # Log error in case of an issue with running the application
        print(f"Error starting the server: {e}")
```
