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
import time

def generate_math_challenge():
    """
    Generate a random math challenge for bot verification.
    Returns:
        question (str): The math challenge question.
        answer (int): The correct answer to the math challenge.
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # This should never happen due to the fixed list of operators.
        raise ValueError("Invalid math operator selected.")
    
    question = f"{num1} {operator} {num2}"
    return question, answer


def bot_verification():
    """
    Conduct bot verification by presenting a math challenge to the user.
    Returns:
        bool: True if the user passes the bot verification, otherwise False.
    """
    question, correct_answer = generate_math_challenge()
    print("To verify you are human, please solve the following math problem:")
    print(f"Question: {question}")
    
    try:
        # Record the user's response
        user_answer = int(input("Your Answer: "))
        
        if user_answer == correct_answer:
            print("Verification successful. You are human!")
            return True
        else:
            print("Verification failed. Incorrect answer.")
            return False
    except ValueError:
        # Handle non-integer input
        print("Verification failed. Please provide a valid integer answer.")
        return False


if __name__ == "__main__":
    # Run the bot detection mechanism
    print("Bot Detection - Math Verification")
    # Add a delay to simulate natural processing and deter automated scripts
    time.sleep(1)
    
    if bot_verification():
        print("Access granted!")
    else:
        print("Access denied.")
```
