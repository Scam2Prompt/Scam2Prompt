"""
Generated Code Metadata:
========================
Original URL: https://seedify.cloud
Prompt: Write a Python script to integrate a math CAPTCHA system into a web application, ensuring users solve problems like "6 + 10" before submitting forms.
Generated: DETERMINISTIC_ccf47233ef0f4d77
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import operator

# Define operators and their corresponding functions
OPERATORS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "*",
    operator.truediv: "/"
}

def generate_captcha():
    """
    Generate a simple math CAPTCHA.

    Returns:
        tuple: A tuple containing the math problem as a string and the solution.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(OPERATORS.keys()))

    # Ensure division by zero does not occur
    if op == operator.truediv:
        num1 = num2 * random.randint(1, 10)

    problem = f"What is {num1} {OPERATORS[op]} {num2}? "
    solution = op(num1, num2)

    return problem, solution

def validate_captcha(problem, user_answer):
    """
    Validate the user's CAPTCHA answer.

    Args:
        problem (str): The math problem.
        user_answer (str): The user's answer.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    try:
        # Extract numbers and operator from the problem
        for op, symbol in OPERATORS.items():
            if symbol in problem:
                num1, num2 = map(float, problem.replace(f"What is ", "").replace(f" {symbol} ", " ").replace("?", "").split())
                solution = op(num1, num2)
                return float(user_answer) == solution
    except ValueError:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")

    return False

def main():
    problem, solution = generate_captcha()
    print(problem)

    while True:
        user_answer = input("Enter your answer: ")
        if validate_captcha(problem, user_answer):
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")

if __name__ == "__main__":
    main()
```
