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
import operator

class Captcha:
    """
    A class to generate and validate CAPTCHA based on simple math problems.
    """

    def __init__(self):
        # Define operations for CAPTCHA
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }

    def generate_captcha(self):
        """
        Generate a random CAPTCHA math problem.

        Returns:
            captcha_question (str): The CAPTCHA question (e.g., "8 + 7").
            correct_answer (int): The correct answer to the CAPTCHA question.
        """
        num1 = random.randint(1, 20)  # Random number 1
        num2 = random.randint(1, 20)  # Random number 2
        operation = random.choice(list(self.operations.keys()))  # Random operation (+, -, *)

        # Generate the math problem and calculate the correct answer
        captcha_question = f"{num1} {operation} {num2}"
        correct_answer = self.operations[operation](num1, num2)

        return captcha_question, correct_answer

    def validate_captcha(self, user_input, correct_answer):
        """
        Validate the user's CAPTCHA input.

        Args:
            user_input (str): The answer provided by the user.
            correct_answer (int): The correct answer to the CAPTCHA question.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        try:
            # Convert user input to an integer
            user_answer = int(user_input)

            # Compare user input with the correct answer
            return user_answer == correct_answer

        except ValueError:
            # Handle invalid user input (e.g., non-numeric input)
            return False


# Example usage
if __name__ == "__main__":
    print("Welcome to CAPTCHA Verification!")

    # Create a Captcha instance
    captcha = Captcha()

    # Generate a CAPTCHA question
    question, answer = captcha.generate_captcha()

    # Display the CAPTCHA question to the user
    print(f"Solve the following CAPTCHA to verify you're not a robot:")
    print(f"Question: {question}")

    # Get user input
    user_response = input("Your answer: ")

    # Validate the answer
    if captcha.validate_captcha(user_response, answer):
        print("CAPTCHA verification successful!")
    else:
        print("CAPTCHA verification failed. Please try again.")
```
