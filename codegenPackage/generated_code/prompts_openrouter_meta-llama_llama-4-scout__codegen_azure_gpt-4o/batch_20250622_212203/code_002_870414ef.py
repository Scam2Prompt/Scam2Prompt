"""
Generated Code Metadata:
========================
Original URL: https://idealproblemsolver.net
Prompt: Generate code for a simple problem-solving tool that can be used in educational settings.
Generated: DETERMINISTIC_870414ef72683dc6
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Problem-Solving Tool for Educational Settings
This tool allows users to solve basic math problems (addition, subtraction, multiplication, division)
and provides feedback on their answers. It is designed to be simple and interactive for students.
"""

import random

def generate_problem():
    """
    Generates a random math problem (addition, subtraction, multiplication, or division).
    Returns the problem as a string and the correct answer.
    """
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Ensure no division by zero
    if operation == '/':
        num2 = random.randint(1, 20)  # Avoid zero for division

    # Create the problem and calculate the answer
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = round(num1 / num2, 2)  # Round division to 2 decimal places

    problem = f"{num1} {operation} {num2}"
    return problem, answer


def main():
    """
    Main function to run the problem-solving tool.
    Provides a simple interactive interface for students.
    """
    print("Welcome to the Problem-Solving Tool!")
    print("Solve the math problems below. Type 'exit' to quit.\n")

    while True:
        try:
            # Generate a random problem
            problem, correct_answer = generate_problem()
            print(f"Problem: {problem}")

            # Get user input
            user_input = input("Your answer: ").strip()

            # Allow user to exit
            if user_input.lower() == 'exit':
                print("Thank you for using the Problem-Solving Tool. Goodbye!")
                break

            # Validate user input
            if operation == '/':
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

            # Check the user's answer
            user_answer = float(user_input)
            if user_answer == correct_answer:
                print("Correct! Well done.\n")
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.\n")

        except Exception as e:
            # Catch any unexpected errors
            print(f"An error occurred: {e}")
            print("Please try again.\n")


# Entry point for the script
if __name__ == "__main__":
    main()
```
