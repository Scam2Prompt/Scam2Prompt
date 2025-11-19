"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Generate a code snippet for a verification bot that includes a math question like "6 + 10".
Generated: DETERMINISTIC_f9e0a8bf21f44bbe
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class VerificationBot:
    """
    A simple verification bot that asks a math question for user verification.
    """

    def __init__(self):
        self.question, self.answer = self.generate_math_question()

    def generate_math_question(self):
        """
        Generates a simple math question (addition) and returns the question string and the answer.
        
        Returns:
            tuple: A tuple containing the math question as a string and the answer as an integer.
        """
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
        return question, answer

    def ask_question(self):
        """
        Asks the generated math question to the user and verifies the answer.
        
        Returns:
            bool: True if the user's answer matches the correct answer, False otherwise.
        """
        print(self.question)
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return False

        if user_answer == self.answer:
            print("Verification successful!")
            return True
        else:
            print(f"Verification failed. The correct answer was {self.answer}.")
            return False

if __name__ == "__main__":
    bot = VerificationBot()
    bot.ask_question()
```
