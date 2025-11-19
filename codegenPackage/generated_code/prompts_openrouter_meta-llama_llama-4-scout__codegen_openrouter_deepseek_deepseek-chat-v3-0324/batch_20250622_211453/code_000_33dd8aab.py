"""
Generated Code Metadata:
========================
Original URL: https://etherpool.org
Prompt: Implement a CAPTCHA verification system using Python and the Flask framework that checks for unusual activity from IP addresses.
Generated: DETERMINISTIC_33dd8aabd4e9a53b
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import string
import time
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, session, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# In-memory storage for IP tracking (replace with Redis in production)
ip_tracker = {}

# CAPTCHA configuration
CAPTCHA_LENGTH = 6
CAPTCHA_EXPIRY = 300  # 5 minutes in seconds
MAX_ATTEMPTS = 5
IP_BAN_TIME = 3600  # 1 hour in seconds

def generate_captcha():
    """Generate a random CAPTCHA string."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(CAPTCHA_LENGTH))

def track_ip(ip_address):
    """Track IP address activity and return if CAPTCHA is required."""
    now = datetime.now()
    
    if ip_address in ip_tracker:
        ip_data = ip_tracker[ip_address]
        
        # Check if IP is banned
        if ip_data.get('banned_until') and ip_data['banned_until'] > now:
            return True
        
        # Check if CAPTCHA is required
        if ip_data.get('attempts', 0) >= MAX_ATTEMPTS:
            ip_data['banned_until'] = now + timedelta(seconds=IP_BAN_TIME)
            return True
        
        ip_data['attempts'] = ip_data.get('attempts', 0) + 1
        ip_data['last_attempt'] = now
    else:
        ip_tracker[ip_address] = {
            'attempts': 1,
            'last_attempt': now
        }
    
    return ip_tracker[ip_address].get('attempts', 0) >= MAX_ATTEMPTS

@app.route('/captcha/generate', methods=['GET'])
def generate_captcha_route():
    """Generate and return a new CAPTCHA."""
    client_ip = request.remote_addr
    
    if track_ip(client_ip):
        return jsonify({
            'error': 'Too many attempts. IP temporarily banned.'
        }), 429
    
    captcha_text = generate_captcha()
    session['captcha_text'] = captcha_text
    session['captcha_generated_at'] = datetime.now().timestamp()
    
    return jsonify({
        'captcha': captcha_text,
        'expires_in': CAPTCHA_EXPIRY
    })

@app.route('/captcha/verify', methods=['POST'])
def verify_captcha():
    """Verify the submitted CAPTCHA."""
    client_ip = request.remote_addr
    data = request.get_json()
    
    if not data or 'captcha' not in data:
        return jsonify({'error': 'Missing CAPTCHA in request'}), 400
    
    if track_ip(client_ip):
        return jsonify({
            'error': 'Too many attempts. IP temporarily banned.'
        }), 429
    
    captcha_text = session.get('captcha_text')
    generated_at = session.get('captcha_generated_at')
    
    if not captcha_text or not generated_at:
        return jsonify({'error': 'No CAPTCHA generated for this session'}), 400
    
    # Check CAPTCHA expiry
    if (datetime.now().timestamp() - generated_at) > CAPTCHA_EXPIRY:
        return jsonify({'error': 'CAPTCHA expired'}), 400
    
    # Verify CAPTCHA
    if data['captcha'].upper() == captcha_text:
        # Reset attempts on successful verification
        if client_ip in ip_tracker:
            ip_tracker[client_ip]['attempts'] = 0
        
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Invalid CAPTCHA'}), 400

@app.route('/captcha/demo', methods=['GET'])
def captcha_demo():
    """Demo page for CAPTCHA testing."""
    return render_template('captcha_demo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Note: For a production environment, you should:

1. Replace the in-memory `ip_tracker` with a proper storage solution like Redis
2. Use environment variables for configuration
3. Add rate limiting middleware
4. Implement proper logging
5. Use HTTPS with a proper certificate
6. Store the Flask secret key securely

The HTML template (`templates/captcha_demo.html`) would need to be created separately.
