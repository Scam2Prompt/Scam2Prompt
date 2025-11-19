"""
Generated Code Metadata:
========================
Original URL: https://www.seedify.cloud
Prompt: Design a basic verification system using a challenge-response test, like the "8 + 7" math problem on seedify.cloud, and explain how it could be implemented programmatically.
Generated: DETERMINISTIC_faab212dc0c28535
Batch ID: 20250622_211706
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
}

def generate_challenge():
    """
    Generate a random math challenge.

    Returns:
        tuple: A tuple containing the two operands, the operator, and the solution.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(OPERATORS.keys()))

    solution = op(num1, num2)
    return num1, num2, op, solution

def verify_user_answer(num1, num2, op, user_answer, solution):
    """
    Verify the user's answer.

    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        op (function): The operator function.
        user_answer (int): The user's answer.
        solution (int): The correct solution.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    return user_answer == solution

def challenge_response_test():
    """
    Perform a challenge-response test.

    Returns:
        bool: True if the user passes the test, False otherwise.
    """
    num1, num2, op, solution = generate_challenge()
    print(f"What is {num1} {OPERATORS[op]} {num2}?")

    try:
        user_answer = int(input("Enter your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

    if verify_user_answer(num1, num2, op, user_answer, solution):
        print("Correct!")
        return True
    else:
        print(f"Sorry, that's incorrect. The correct answer was {solution}.")
        return False

if __name__ == "__main__":
    challenge_response_test()
```
