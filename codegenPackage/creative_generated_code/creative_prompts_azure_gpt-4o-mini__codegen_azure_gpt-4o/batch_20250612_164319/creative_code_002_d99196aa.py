"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-application5.pages.dev
Prompt: What are the best practices for managing cookies in a web application?
Generated: DETERMINISTIC_d99196aa7f8117f4
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask Example: Managing Cookies in a Web Application
# This script demonstrates best practices for managing cookies securely.

from flask import Flask, request, make_response

app = Flask(__name__)

# Set a secret key for secure cookies
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    """
    Endpoint to demonstrate cookie management.
    Sets a secure, HTTP-only cookie for the user.
    """
    response = make_response("Welcome to the web application!")
    
    # Set cookie with security best practices
    # Key points:
    #  - Secure flag ensures cookie is sent only via HTTPS.
    #  - HttpOnly flag prevents JavaScript access to the cookie.
    #  - SameSite flag mitigates CSRF vulnerabilities.
    response.set_cookie(
        key="session_id", 
        value="unique_session_identifier",
        max_age=3600,  # Cookie expiry time in seconds (1 hour)
        secure=True,  # Cookie only accessible via HTTPS
        httponly=True,  # Prevent JavaScript access
        samesite='Strict'  # Prevent CSRF attacks
    )
    return response

@app.route('/get-cookie')
def get_cookie():
    """
    Endpoint to retrieve a cookie value.
    Includes error handling if the cookie does not exist.
    """
    session_id = request.cookies.get("session_id")
    if session_id:
        return f"Cookie value: {session_id}"
    else:
        return "No session cookie found.", 404

@app.route('/delete-cookie')
def delete_cookie():
    """
    Endpoint to delete a cookie.
    Provides users with an option to clear their session.
    """
    response = make_response("Session cookie cleared.")
    response.delete_cookie("session_id")
    return response

# Error Handling Example
@app.errorhandler(500)
def internal_error(error):
    """
    Generic error handler for internal server errors.
    Provide a friendly error message and log the error for debugging.
    """
    return "An internal error occurred. Please try again later.", 500

if __name__ == '__main__':
    # Run the Flask application in debug mode (set to False in production)
    app.run(debug=True)
```
