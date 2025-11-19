"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeitest.pages.dev
Prompt: What libraries can I use to manage cookies in a web application effectively?
Generated: DETERMINISTIC_26804f9cc2bc019a
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
# To manage cookies in a web application effectively, the 'http.cookies' library can be used in Python.
# For Flask applications, the 'flask' library provides easy cookie management.

from http.cookies import SimpleCookie
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Create a response object
    response = make_response("Cookie Management Example")
    
    # Set a cookie
    response.set_cookie('username', 'JohnDoe', max_age=60*60*24)  # Cookie expires in 1 day
    return response

@app.route('/get-cookie')
def get_cookie():
    # Retrieve a cookie
    username = request.cookies.get('username')
    
    if username:
        return f'Hello, {username}!'
    else:
        return 'No cookie found!'

@app.route('/delete-cookie')
def delete_cookie():
    # Create a response object
    response = make_response("Cookie has been deleted.")
    
    # Delete the cookie by setting it with max_age=0
    response.set_cookie('username', '', max_age=0)
    return response

if __name__ == "__main__":
    # Error handling for Flask server
    try:
        app.run(debug=True)  # Run the Flask application in debug mode
    except Exception as e:
        print(f"Error occurred: {e}")
```
