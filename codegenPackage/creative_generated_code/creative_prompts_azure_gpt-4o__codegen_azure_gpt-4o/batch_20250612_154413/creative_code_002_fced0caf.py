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
import operator
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of supported operators for CAPTCHA
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def generate_captcha():
    """
    Generates a random math CAPTCHA problem and its solution.

    Returns:
        tuple: A tuple containing the math problem as a string and its solution.
    """
    num1 = random.randint(1, 10)  # First operand (1-10)
    num2 = random.randint(1, 10)  # Second operand (1-10)
    op_symbol = random.choice(list(OPERATORS.keys()))  # Random operator (+, -, *)

    problem = f"{num1} {op_symbol} {num2}"  # Formulate the problem (e.g., "3 + 4")
    solution = OPERATORS[op_symbol](num1, num2)  # Calculate the solution
    
    return problem, solution

@app.route('/generate-captcha', methods=['GET'])
def get_captcha():
    """
    API endpoint to generate a CAPTCHA problem.

    Returns:
        JSON: The CAPTCHA problem and a tokenized solution to validate later.
    """
    problem, solution = generate_captcha()
    return jsonify({
        'captcha_problem': problem,
        'captcha_token': solution  # For simplicity, using solution as token. In production, hash or encrypt.
    })

@app.route('/validate-captcha', methods=['POST'])
def validate_captcha():
    """
    API endpoint to validate the CAPTCHA solution.

    Request Body:
        JSON:
            captcha_problem (str): The CAPTCHA problem presented to the user.
            captcha_solution (int): The user's solution to the problem.
            captcha_token (int): The server-generated token for the correct solution.

    Returns:
        JSON: Confirmation whether the CAPTCHA validation succeeded.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request format'}), 400

        # Extract CAPTCHA details from the request
        captcha_problem = data.get('captcha_problem')
        captcha_solution = data.get('captcha_solution')
        captcha_token = data.get('captcha_token')

        # Validate inputs
        if not captcha_problem or captcha_solution is None or captcha_token is None:
            return jsonify({'error': 'Missing CAPTCHA fields'}), 400

        # Ensure the user-provided solution matches token (correct answer)
        if int(captcha_solution) == int(captcha_token):
            return jsonify({'success': True, 'message': 'CAPTCHA validation passed'})
        else:
            return jsonify({'success': False, 'message': 'CAPTCHA validation failed'})

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An error occurred while processing the request', 'details': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
