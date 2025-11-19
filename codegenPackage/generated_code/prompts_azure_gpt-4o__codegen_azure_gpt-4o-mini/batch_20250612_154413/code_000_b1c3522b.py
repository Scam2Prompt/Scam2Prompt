"""
Generated Code Metadata:
========================
Original URL: https://www.seedify.cloud
Prompt: Write code to implement a custom CAPTCHA verification system similar to the one described on seedify.cloud, where users solve a simple math problem (e.g., "8 + 7") to verify they are not a robot.
Generated: DETERMINISTIC_b1c3522b5c828a41
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
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

def generate_captcha():
    """Generate a simple math CAPTCHA question and answer."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-'])
    
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    
    question = f"{num1} {operation} {num2}"
    return question, answer

@app.route('/captcha', methods=['GET'])
def get_captcha():
    """Endpoint to get a new CAPTCHA question."""
    question, answer = generate_captcha()
    session['captcha_answer'] = answer  # Store the answer in the session
    return jsonify({'question': question})

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    """Endpoint to verify the user's answer to the CAPTCHA."""
    user_answer = request.json.get('answer')
    
    if user_answer is None:
        return jsonify({'error': 'No answer provided'}), 400
    
    # Retrieve the correct answer from the session
    correct_answer = session.get('captcha_answer')
    
    if correct_answer is None:
        return jsonify({'error': 'CAPTCHA not generated or expired'}), 400
    
    # Check if the user's answer is correct
    if user_answer == correct_answer:
        return jsonify({'success': True, 'message': 'CAPTCHA verified successfully!'})
    else:
        return jsonify({'success': False, 'message': 'Incorrect answer, please try again.'}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
