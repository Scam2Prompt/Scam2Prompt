"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: Generate Python code for a CAPTCHA system that dynamically generates math problems for user verification, inspired by the example on seedify.cloud.
Generated: DETERMINISTIC_fced0caf350828cc
Batch ID: 20250612_154413
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
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def generate_math_problem():
    """Generate a simple math problem with two random integers and an operator."""
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)

    # Handle division to avoid zero division error
    if operator == '/':
        num1 = num1 * num2  # Ensure num1 is divisible by num2

    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)  # Evaluate the answer of the problem

    return problem, answer

@app.route('/generate_captcha', methods=['GET'])
def generate_captcha():
    """Endpoint to generate a new CAPTCHA math problem."""
    try:
        problem, answer = generate_math_problem()
        session['captcha_answer'] = answer  # Store the answer in the session
        return jsonify({'problem': problem}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to generate CAPTCHA', 'message': str(e)}), 500

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    """Endpoint to verify the user's answer to the CAPTCHA."""
    user_answer = request.json.get('answer')
    
    try:
        correct_answer = session.get('captcha_answer')

        # Check if the user answer matches the correct answer
        if correct_answer is None:
            return jsonify({'error': 'No CAPTCHA generated or expired.'}), 400
        
        if user_answer == correct_answer:
            return jsonify({'result': 'CAPTCHA passed!'}), 200
        else:
            return jsonify({'result': 'CAPTCHA failed, try again!'}), 403
    except Exception as e:
        return jsonify({'error': 'Verification failed', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
