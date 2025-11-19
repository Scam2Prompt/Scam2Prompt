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

def generate_math_question():
    """
    Generate a random math question (addition).
    Returns a tuple containing the question string and the correct answer.
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = f"{num1} + {num2}"
    answer = num1 + num2
    return question, answer

def verify_user():
    """
    Function to verify the user by asking a math question.
    Ensures correct input handling and provides feedback based on user response.
    """
    try:
        # Generate a random math question
        question, correct_answer = generate_math_question()
        print("Verification Required: Solve the following math question.")
        print(f"Question: {question}")
        
        # Prompt user for their answer
        user_input = input("Your Answer: ")
        
        # Validate user input
        if not user_input.isdigit():
            print("Invalid input. Please enter a numeric value.")
            return False
        
        user_answer = int(user_input)
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Verification successful. Welcome!")
            return True
        else:
            print("Verification failed. Please try again.")
            return False
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    # Start the verification process
    verify_user()
```
