"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfreespin.com
Prompt: Create a script that validates a code entered by the user for accessing the TONfreespin.com event.
Generated: DETERMINISTIC_c412365ddb3e7c36
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_code(code):
    """
    Validates the access code for the TONfreespin.com event.
    
    Args:
        code (str): The access code entered by the user.
    
    Returns:
        bool: True if the code is valid, False otherwise.
    """
    
    # Define the regex pattern for a valid code: 
    # - Must be 8 characters long
    # - Must contain at least one uppercase letter
    # - Must contain at least one lowercase letter
    # - Must contain at least one digit
    # - Must contain at least one special character from the set !@#$%^&*()
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()]).{8}$')
    
    # Check if the provided code matches the pattern
    if pattern.match(code):
        return True
    else:
        return False

def main():
    """
    Main function to execute the code validation process.
    """
    try:
        user_code = input("Please enter your access code for TONfreespin.com event: ")
        
        # Validate the entered code
        if validate_code(user_code):
            print("Access code is valid. You may proceed to the event.")
        else:
            print("Invalid access code. Please check the requirements and try again.")
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
