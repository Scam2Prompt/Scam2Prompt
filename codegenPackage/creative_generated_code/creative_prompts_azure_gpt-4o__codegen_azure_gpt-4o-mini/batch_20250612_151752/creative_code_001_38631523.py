"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Generate a Python script to implement a bot detection mechanism that includes a math-based verification step, similar to "6 + 10."
Generated: DETERMINISTIC_38631523a57e5b4d
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BotDetection:
    def __init__(self):
        """Initialize the bot detection mechanism."""
        self.question, self.answer = self.generate_math_question()

    def generate_math_question(self):
        """Generate a simple math question for verification."""
        # Generate two random numbers between 1 and 20
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        # Create the question and calculate the answer
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
        return question, answer

    def verify_answer(self, user_answer):
        """Verify the user's answer against the correct answer."""
        try:
            # Ensure the user answer is an integer
            user_answer = int(user_answer)
        except ValueError:
            raise ValueError("Invalid input: Please enter a numeric value.")

        # Check if the answer is correct
        if user_answer == self.answer:
            return True
        else:
            return False

def main():
    """Main function to run the bot detection mechanism."""
    bot_detection = BotDetection()
    
    print(bot_detection.question)  # Display the math question
    
    user_input = input("Please enter your answer: ")
    
    try:
        # Verify the user's answer
        if bot_detection.verify_answer(user_input):
            print("Verification successful: You are not a bot.")
        else:
            print("Verification failed: Please try again.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
