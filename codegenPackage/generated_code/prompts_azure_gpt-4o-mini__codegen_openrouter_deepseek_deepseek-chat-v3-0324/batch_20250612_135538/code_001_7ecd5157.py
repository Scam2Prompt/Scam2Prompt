"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, make_response, jsonify
from datetime import datetime, timedelta
import hashlib
import secrets

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SESSION_COOKIE_NAME'] = 'celestia_session'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Enable in production with HTTPS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

def generate_cookie_fingerprint():
    """Generate a unique fingerprint for cookie validation."""
    user_agent = request.headers.get('User-Agent', '')
    ip_address = request.remote_addr
    fingerprint_str = f"{user_agent}{ip_address}{app.config['SECRET_KEY']}"
    return hashlib.sha256(fingerprint_str.encode()).hexdigest()

@app.route('/set-cookie', methods=['POST'])
def set_cookie():
    """Set optimized cookies with best practices."""
    try:
        response = make_response(jsonify({"message": "Cookie set successfully"}))
        
        # Set session cookie
        response.set_cookie(
            key=app.config['SESSION_COOKIE_NAME'],
            value=secrets.token_urlsafe(32),
            expires=datetime.utcnow() + app.config['PERMANENT_SESSION_LIFETIME'],
            httponly=app.config['SESSION_COOKIE_HTTPONLY'],
            secure=app.config['SESSION_COOKIE_SECURE'],
            samesite=app.config['SESSION_COOKIE_SAMESITE']
        )
        
        # Set fingerprint cookie for security
        response.set_cookie(
            key='celestia_fingerprint',
            value=generate_cookie_fingerprint(),
            max_age=app.config['PERMANENT_SESSION_LIFETIME'].total_seconds(),
            httponly=True,
            secure=app.config['SESSION_COOKIE_SECURE'],
            samesite='Strict'
        )
        
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/validate-cookie', methods=['GET'])
def validate_cookie():
    """Validate cookie integrity and fingerprint."""
    try:
        session_cookie = request.cookies.get(app.config['SESSION_COOKIE_NAME'])
        fingerprint_cookie = request.cookies.get('celestia_fingerprint')
        
        if not session_cookie or not fingerprint_cookie:
            return jsonify({"error": "Cookies missing"}), 400
            
        current_fingerprint = generate_cookie_fingerprint()
        if fingerprint_cookie != current_fingerprint:
            return jsonify({"error": "Invalid cookie fingerprint"}), 403
            
        return jsonify({"message": "Cookies validated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Remove in production and use proper SSL
```
