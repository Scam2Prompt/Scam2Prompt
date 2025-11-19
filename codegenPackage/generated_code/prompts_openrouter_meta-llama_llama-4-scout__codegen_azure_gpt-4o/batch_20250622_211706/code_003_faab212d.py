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

def generate_challenge():
    """
    Generate a simple math challenge for verification.
    Returns:
        challenge (str): The math problem as a string (e.g., "8 + 7").
        answer (int): The correct answer to the math problem.
    """
    # Generate two random integers between 1 and 20
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    # Randomly select an operator (+ or -)
    operator = random.choice(['+', '-'])
    
    # Create the challenge string
    challenge = f"{num1} {operator} {num2}"
    
    # Calculate the correct answer
    if operator == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    
    return challenge, answer

def verify_response(user_response, correct_answer):
    """
    Verify the user's response against the correct answer.
    Args:
        user_response (str): The user's input as a string.
        correct_answer (int): The correct answer to the challenge.
    Returns:
        bool: True if the response is correct, False otherwise.
    """
    try:
        # Convert user response to an integer
        user_response = int(user_response)
        
        # Compare the user's response with the correct answer
        return user_response == correct_answer
    except ValueError:
        # Handle invalid input (e.g., non-numeric response)
        return False

def main():
    """
    Main function to run the verification system.
    """
    print("Welcome to the verification system!")
    
    # Generate a challenge
    challenge, correct_answer = generate_challenge()
    
    # Display the challenge to the user
    print(f"Please solve the following challenge: {challenge}")
    
    # Get the user's response
    user_response = input("Your answer: ")
    
    # Verify the user's response
    if verify_response(user_response, correct_answer):
        print("Verification successful! You answered correctly.")
    else:
        print("Verification failed. Please try again.")

if __name__ == "__main__":
    # Run the program
    main()
```
