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

class ChallengeResponseVerification:
    def __init__(self):
        """Initialize the verification system."""
        self.challenge = None
        self.answer = None

    def generate_challenge(self):
        """Generate a simple math challenge."""
        # Generate two random numbers between 1 and 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.challenge = f"{num1} + {num2}"
        self.answer = num1 + num2
        return self.challenge

    def verify_response(self, user_response):
        """Verify the user's response against the correct answer.
        
        Args:
            user_response (int): The user's answer to the challenge.
        
        Returns:
            bool: True if the response is correct, False otherwise.
        """
        try:
            # Convert user response to integer
            user_response = int(user_response)
            return user_response == self.answer
        except ValueError:
            # Handle the case where the user response is not an integer
            print("Invalid input. Please enter a numeric value.")
            return False

def main():
    """Main function to run the verification system."""
    verifier = ChallengeResponseVerification()
    
    # Generate a challenge
    challenge = verifier.generate_challenge()
    print(f"Solve the challenge: {challenge}")

    # Get user response
    user_input = input("Your answer: ")

    # Verify the response
    if verifier.verify_response(user_input):
        print("Verification successful! You answered correctly.")
    else:
        print("Verification failed. Please try again.")

if __name__ == "__main__":
    main()
```
