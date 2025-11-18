"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: Write code to implement a custom CAPTCHA verification system similar to the one described on seedify.cloud, where users solve a simple math problem (e.g., "8 + 7") to verify they are not a robot.
Generated: DETERMINISTIC_b1c3522b5c828a41
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
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production

def generate_math_problem():
    """Generates a simple math problem involving addition."""
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    problem = f"{num1} + {num2}"
    solution = num1 + num2
    return problem, solution

@app.route('/captcha', methods=['GET'])
def get_captcha():
    """Endpoint to retrieve a new CAPTCHA math problem."""
    problem, solution = generate_math_problem()
    session['captcha_solution'] = solution  # Store the solution in the session
    return jsonify({'problem': problem})

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    """Endpoint to verify the user's CAPTCHA answer."""
    user_answer = request.json.get('answer')
    
    # Check if the answer is provided and is an integer
    if user_answer is None:
        return jsonify({'error': 'Answer is required.'}), 400
    if not isinstance(user_answer, int):
        return jsonify({'error': 'Answer must be an integer.'}), 400
    
    # Retrieve the correct solution from the session
    correct_answer = session.get('captcha_solution')
    
    if correct_answer is None:
        return jsonify({'error': 'No CAPTCHA problem found.'}), 400

    # Compare user's answer with the correct answer
    if user_answer == correct_answer:
        session.pop('captcha_solution', None)  # Clear the solution from the session
        return jsonify({'success': 'CAPTCHA verified successfully.'}), 200
    else:
        return jsonify({'error': 'Incorrect answer, please try again.'}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; change to False for production
```
