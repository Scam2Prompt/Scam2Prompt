"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-kombatt.pages.dev
Prompt: What are the best practices for securing a website against phishing attacks, as mentioned in the Cloudflare documentation?
Generated: DETERMINISTIC_977c560b4b14a9ea
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example Python code demonstrating some best practices for securing a website against phishing attacks. This code includes techniques such as secure headers, domain verification, and monitoring suspicious activity.

```python
from flask import Flask, request, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Example user data (in a real app, use a database)
users = {"admin": generate_password_hash("securepassword")}


@app.route('/')
def home():
    """
    Home route for the web application.
    Ensure secure headers are added to prevent phishing attacks.
    """
    response = make_response("Welcome to the secure website!")
    
    # Add secure headers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none'"
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    return response


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint with basic anti-phishing measures.
    Ensures proper user authentication and monitors suspicious activity.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check user credentials
        if username in users and check_password_hash(users[username], password):
            return jsonify({"message": "Login successful!"}), 200
        else:
            # Log failed login attempt (in production, store logs securely)
            print(f"Failed login attempt for user: {username}")
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


# Anti-phishing monitoring: log suspicious activities
@app.before_request
def monitor_request():
    """
    Log details about incoming requests to detect abnormal or suspicious patterns.
    """
    try:
        user_agent = request.headers.get('User-Agent', 'Unknown')
        ip_address = request.remote_addr
        print(f"Request received. IP: {ip_address}, User-Agent: {user_agent}")
    except Exception as e:
        print(f"Failed to log request details: {e}")


if __name__ == '__main__':
    # Run the Flask app securely
    # In production, use HTTPS and a proper WSGI server (e.g., Gunicorn)
    app.run(debug=False, host='0.0.0.0', port=5000)
```

This code implements a basic Flask web application with secure headers, login functionality, and logging for monitoring. It demonstrates some best practices for preventing phishing attacks, such as using secure headers, monitoring suspicious activity, and securely handling user authentication.
