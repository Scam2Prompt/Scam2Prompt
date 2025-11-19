"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: Write code to create a simple verification system that checks if a user is a robot using basic arithmetic like 8 + 7.
Generated: DETERMINISTIC_2ad48daecc61d0e1
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VerificationSystem:
    def __init__(self):
        """Initialize the verification system with a predefined question and answer."""
        self.question = "What is 8 + 7?"
        self.correct_answer = 15

    def ask_question(self):
        """Ask the verification question and get the user's answer."""
        print(self.question)
        try:
            user_answer = int(input("Your answer: "))
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def verify_user(self, user_answer):
        """Check if the user's answer is correct.

        Args:
            user_answer (int): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        if user_answer is None:
            return False
        return user_answer == self.correct_answer

    def run_verification(self):
        """Run the verification process."""
        print("Welcome to the Verification System!")
        user_answer = self.ask_question()
        if self.verify_user(user_answer):
            print("Verification successful. You are not a robot!")
        else:
            print("Verification failed. You might be a robot.")

if __name__ == "__main__":
    verification_system = VerificationSystem()
    verification_system.run_verification()
```
