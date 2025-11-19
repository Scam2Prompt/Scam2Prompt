"""
Generated Code Metadata:
========================
Original URL: https://www.seedify.cloud
Prompt: Generate Python code for a CAPTCHA system that dynamically generates math problems for user verification, inspired by the example on seedify.cloud.
Generated: DETERMINISTIC_fced0caf350828cc
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Tuple, Optional
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, make_response, session
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a real secret key in production

# Configuration
CAPTCHA_EXPIRATION_MINUTES = 5
OPERATORS = ['+', '-', '*']
MAX_NUMBER = 10  # Maximum number for operands

class MathCaptcha:
    """
    A class to generate and validate math-based CAPTCHAs.
    """
    def __init__(self):
        self.captcha_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.operator = random.choice(OPERATORS)
        self.num1 = random.randint(1, MAX_NUMBER)
        self.num2 = random.randint(1, MAX_NUMBER)
        self.answer = self._calculate_answer()
        self.expires_at = self.created_at + timedelta(minutes=CAPTCHA_EXPIRATION_MINUTES)

    def _calculate_answer(self) -> int:
        """Calculate the correct answer for the math problem."""
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        else:
            raise ValueError("Invalid operator")

    def is_expired(self) -> bool:
        """Check if the CAPTCHA has expired."""
        return datetime.utcnow() > self.expires_at

    def to_dict(self) -> dict:
        """Return CAPTCHA data as a dictionary (excluding the answer)."""
        return {
            'captcha_id': self.captcha_id,
            'problem': f"{self.num1} {self.operator} {self.num2}",
            'expires_at': self.expires_at.isoformat()
        }

@app.route('/api/captcha/generate', methods=['GET'])
def generate_captcha():
    """Generate a new math CAPTCHA and store it in the session."""
    captcha = MathCaptcha()
    session['captcha'] = {
        'captcha_id': captcha.captcha_id,
        'answer': captcha.answer,
        'expires_at': captcha.expires_at.isoformat()
    }
    return jsonify(captcha.to_dict())

@app.route('/api/captcha/verify', methods=['POST'])
def verify_captcha():
    """Verify the user's answer to the CAPTCHA."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    captcha_id = data.get('captcha_id')
    user_answer = data.get('answer')

    if not captcha_id or not user_answer:
        return jsonify({'error': 'Missing captcha_id or answer'}), 400

    stored_captcha = session.get('captcha')
    if not stored_captcha or stored_captcha['captcha_id'] != captcha_id:
        return jsonify({'error': 'Invalid or expired CAPTCHA'}), 400

    try:
        user_answer = int(user_answer)
    except ValueError:
        return jsonify({'error': 'Answer must be an integer'}), 400

    expires_at = datetime.fromisoformat(stored_captcha['expires_at'])
    if datetime.utcnow() > expires_at:
        return jsonify({'error': 'CAPTCHA expired'}), 400

    if user_answer == stored_captcha['answer']:
        session.pop('captcha', None)  # Clear the CAPTCHA after successful verification
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Incorrect answer'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
