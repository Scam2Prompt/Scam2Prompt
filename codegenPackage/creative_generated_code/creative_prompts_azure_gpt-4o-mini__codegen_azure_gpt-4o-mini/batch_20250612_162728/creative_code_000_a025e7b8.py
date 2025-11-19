"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: How can I implement a CAPTCHA verification system to ensure users are not robots in my web application?
Generated: DETERMINISTIC_a025e7b830ac6f8e
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# captcha_service.py

import random
import string
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

def generate_captcha(length=6):
    """Generate a random CAPTCHA string of given length."""
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

@app.route('/captcha', methods=['GET'])
def get_captcha():
    """Endpoint to generate and return a new CAPTCHA."""
    captcha = generate_captcha()
    session['captcha'] = captcha  # Store CAPTCHA in session for verification
    return jsonify({'captcha': captcha})

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    """Endpoint to verify the submitted CAPTCHA against the stored session value."""
    user_captcha = request.json.get('captcha', '')
    
    # Check if CAPTCHA exists in the session
    if 'captcha' not in session:
        return jsonify({'error': 'No CAPTCHA generated'}), 400
    
    # Compare user input with stored CAPTCHA
    if user_captcha == session['captcha']:
        # Clear the CAPTCHA from session upon successful verification
        session.pop('captcha', None)
        return jsonify({'success': 'CAPTCHA verified successfully'}), 200
    else:
        return jsonify({'error': 'Invalid CAPTCHA'}), 400

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
```

### Requirements:
- Install Flask if not already installed: `pip install Flask`
- Replace `'your_secret_key'` with a strong secret key for session management.
- Use this in a secure environment to ensure proper handling of user sessions and data.
