"""
Generated Code Metadata:
========================
Original URL: https://news18network.com
Prompt: Generate a list of interview questions based on the article about common interview questions on News18Network.com, and provide a code snippet to simulate a mock interview.
Generated: DETERMINISTIC_342eb9268cd51da4
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MockInterview:
    def __init__(self):
        # List of common interview questions
        self.questions = [
            "Tell me about yourself.",
            "What are your greatest strengths?",
            "What are your weaknesses?",
            "Why do you want to work here?",
            "Where do you see yourself in five years?",
            "Describe a challenging situation and how you overcame it.",
            "Why should we hire you?",
            "What is your salary expectation?",
            "How do you handle stress and pressure?",
            "Do you have any questions for us?"
        ]

    def get_random_question(self):
        """Selects a random question from the list."""
        return random.choice(self.questions)

    def conduct_interview(self, num_questions=5):
        """
        Conducts a mock interview by asking a specified number of random questions.
        
        Args:
            num_questions (int): The number of questions to ask during the interview.
        """
        if num_questions <= 0:
            raise ValueError("Number of questions must be greater than zero.")
        
        print("Welcome to the Mock Interview!\n")
        for i in range(num_questions):
            question = self.get_random_question()
            print(f"Question {i + 1}: {question}\n")
            input("Your answer: ")  # Simulate user input for the answer
            print()  # Print a newline for better readability

        print("Thank you for participating in the mock interview!")

if __name__ == "__main__":
    try:
        # Create an instance of MockInterview
        interview = MockInterview()
        # Conduct a mock interview with 5 questions
        interview.conduct_interview(num_questions=5)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
