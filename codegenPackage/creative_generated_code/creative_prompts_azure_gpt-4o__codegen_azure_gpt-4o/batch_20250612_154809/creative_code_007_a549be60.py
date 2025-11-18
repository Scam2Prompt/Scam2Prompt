"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lair-fi-claim-reward.vercel.app
Prompt: Write a script to integrate the Lair Finance privacy notice functionality, ensuring cookies are handled according to user preferences (Allow or Decline).
Generated: DETERMINISTIC_a549be60457039c9
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from http.cookies import SimpleCookie
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

# Define the privacy notice HTML template
privacy_notice_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Notice</title>
</head>
<body>
    <h1>Privacy Notice</h1>
    <p>We use cookies to enhance your experience on our website. Please select your preference:</p>
    <form method="POST" action="/set-cookie-preference">
        <button type="submit" name="preference" value="allow">Allow Cookies</button>
        <button type="submit" name="preference" value="decline">Decline Cookies</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    """
    Main route to display content based on cookie preference.
    """
    # Check the user's cookie preference
    cookie = request.cookies.get('cookie_preference')
    if cookie == 'allow':
        return "<h1>Welcome! Cookies are enabled.</h1>"
    elif cookie == 'decline':
        return "<h1>Welcome! Cookies are disabled.</h1>"
    else:
        # If no preference is set, display the privacy notice
        return render_template("privacy_notice.html")

@app.route('/privacy-notice')
def privacy_notice():
    """
    Route to display the privacy notice page.
    """
    return privacy_notice_html

@app.route('/set-cookie-preference', methods=['POST'])
def set_cookie_preference():
    """
    Handle user preferences for cookies and set the appropriate cookie.
    """
    try:
        # Get user preference from the form submission
        preference = request.form.get('preference')
        if preference not in ['allow', 'decline']:
            return "Invalid preference.", 400

        # Create a response object and set the cookie
        response = make_response("<h1>Your preference has been saved!</h1>")
        response.set_cookie('cookie_preference', preference, max_age=30*24*60*60)  # Cookie valid for 30 days
        
        return response
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```
