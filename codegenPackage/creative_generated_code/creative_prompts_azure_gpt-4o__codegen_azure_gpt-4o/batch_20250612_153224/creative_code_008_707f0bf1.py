"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-share.pages.dev
Prompt: Generate code to collect anonymous site visitation data using cookies, as described in the Privacy Notice section of the webpage.
Generated: DETERMINISTIC_707f0bf12654a7be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.cookies import SimpleCookie
from flask import Flask, request, make_response
import json
import datetime

app = Flask(__name__)

# Set up a function to generate a unique visitor ID
def generate_visitor_id():
    return f"visitor-{datetime.datetime.utcnow().timestamp()}"

# Function to collect and store anonymous visitation data
def collect_visitation_data(visitor_id):
    visitation_data = {
        "visitor_id": visitor_id,
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }

    # Here, store visitation_data in a secure database or log file.
    # For demonstration purposes, we'll print it to the console.
    print(json.dumps(visitation_data))  # Replace this with database storage.

@app.route("/")
def home():
    # Check if the visitor has a cookie
    visitor_id = request.cookies.get("visitor_id")

    if not visitor_id:
        # Generate a new visitor ID if none exists
        visitor_id = generate_visitor_id()

        # Create a response object and set a cookie
        response = make_response("<h1>Welcome to the site!</h1>")
        response.set_cookie("visitor_id", visitor_id, httponly=True, secure=True, samesite="Lax")
    else:
        # Create a response object without setting a new cookie
        response = make_response("<h1>Welcome back!</h1>")

    # Collect anonymous visitation data
    collect_visitation_data(visitor_id)

    # Return the response
    return response


# Error handling route for any unhandled errors
@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>Internal Server Error</h1>", 500


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False for production use
```
