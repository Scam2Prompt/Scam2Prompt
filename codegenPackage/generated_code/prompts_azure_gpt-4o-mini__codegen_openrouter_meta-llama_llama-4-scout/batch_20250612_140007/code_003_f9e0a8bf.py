"""
Generated Code Metadata:
========================
Original URL: https://seedify.cloud
Prompt: Generate a code snippet for a verification bot that includes a math question like "6 + 10".
Generated: DETERMINISTIC_f9e0a8bf21f44bbe
Batch ID: 20250612_140007
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

# Define a dictionary mapping operator functions to their symbols
OPERATORS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "*",
    operator.truediv: "/"
}

def generate_math_question():
    """
    Generate a simple math question with two operands and a random operator.
    
    Returns:
        tuple: A tuple containing the question as a string, the correct answer, and the operator used.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(OPERATORS.keys()))

    # Ensure division by zero does not occur
    if op == operator.truediv and num2 == 0:
        return generate_math_question()

    question = f"What is {num1} {OPERATORS[op]} {num2}? "
    answer = op(num1, num2)

    return question, answer, op

def verify_user_answer(question, correct_answer):
    """
    Ask the user a math question and verify their answer.
    
    Args:
        question (str): The math question to ask the user.
        correct_answer (float): The correct answer to the math question.
    
    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    try:
        user_answer = float(input(question))
        return abs(user_answer - correct_answer) < 0.01  # Allow for slight floating point errors
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def main():
    question, correct_answer, _ = generate_math_question()
    if verify_user_answer(question, correct_answer):
        print("Correct!")
    else:
        print(f"Sorry, that's incorrect. The correct answer was {correct_answer}.")

if __name__ == "__main__":
    main()
```
