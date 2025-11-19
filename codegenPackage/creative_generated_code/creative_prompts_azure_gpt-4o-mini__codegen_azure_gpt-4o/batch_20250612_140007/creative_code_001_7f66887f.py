"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Write code for a simple verification system that checks if a user is a robot using a math challenge.
Generated: DETERMINISTIC_7f66887fbe3342bb
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

def generate_math_challenge():
    """
    Generate a simple math challenge for the user.
    Returns:
        tuple: A tuple containing the challenge as a string and the correct answer.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    
    challenge = f"What is {num1} {operation} {num2}?"
    return challenge, answer

def verify_user_is_not_robot():
    """
    Function to verify if a user is a robot by presenting a math challenge.
    Returns:
        bool: True if the user passes the challenge, False otherwise.
    """
    try:
        challenge, correct_answer = generate_math_challenge()
        print("To proceed, please solve the following challenge:")
        print(challenge)
        
        # Get user input and check answer
        user_input = input("Your answer: ")
        if not user_input.isdigit():  # Check if input is numeric
            print("Invalid input. Please enter a numeric value.")
            return False
            
        user_answer = int(user_input)
        if user_answer == correct_answer:
            print("Verification successful! You are not a robot.")
            return True
        else:
            print("Verification failed. Incorrect answer.")
            return False
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    # Run the verification system
    is_human = verify_user_is_not_robot()
    if is_human:
        print("Access granted.")
    else:
        print("Access denied.")
```
