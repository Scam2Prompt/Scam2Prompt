"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: Suggest tools or frameworks for creating a CAPTCHA system that prevents bots while logging unique Request IDs for each interaction.
Generated: DETERMINISTIC_313af660516b825d
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_session import Session
from werkzeug.exceptions import BadRequest

# Create a Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# In-memory storage for CAPTCHA and request IDs (for demonstration purposes)
captcha_store = {}
request_log = {}

def generate_captcha() -> str:
    """Generate a simple CAPTCHA string consisting of random letters and digits."""
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(6))
    return captcha

def log_request(request_id: str, captcha_value: str) -> None:
    """Log the unique request ID and associated CAPTCHA value."""
    request_log[request_id] = {
        'timestamp': time.time(),
        'captcha_value': captcha_value
    }

@app.route('/generate_captcha', methods=['GET'])
def generate_captcha_route():
    """Endpoint to generate a new CAPTCHA."""
    captcha_value = generate_captcha()
    request_id = str(time.time())  # Simple unique request ID based on timestamp
    captcha_store[request_id] = captcha_value
    log_request(request_id, captcha_value)
    
    return jsonify({'request_id': request_id, 'captcha': captcha_value})

@app.route('/validate_captcha', methods=['POST'])
def validate_captcha_route():
    """Endpoint to validate the CAPTCHA."""
    try:
        data = request.json
        request_id = data.get('request_id')
        user_captcha = data.get('captcha')

        if not request_id or not user_captcha:
            raise BadRequest("Missing request_id or captcha.")

        # Validate request ID and CAPTCHA
        stored_captcha = captcha_store.get(request_id)
        if stored_captcha is None:
            return jsonify({'valid': False, 'message': 'Invalid request ID.'}), 400

        if stored_captcha == user_captcha:
            return jsonify({'valid': True, 'message': 'CAPTCHA validated successfully.'})
        else:
            return jsonify({'valid': False, 'message': 'Incorrect CAPTCHA.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```
