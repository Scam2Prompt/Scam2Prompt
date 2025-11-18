"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duolingo.wiki
Prompt: Develop a program that simulates the steps outlined on the Duolingo Super membership page for copying and submitting a Duolingo username or email.
Generated: DETERMINISTIC_e8763dc8a2b59e95
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pyperclip  # Importing pyperclip to handle clipboard operations
import re  # Importing re for regex operations
import sys  # Importing sys for exiting the program gracefully

def get_duolingo_username_or_email():
    """
    Prompts the user to enter their Duolingo username or email.
    
    Returns:
        str: The entered username or email.
    """
    username_or_email = input("Please enter your Duolingo username or email: ")
    return username_or_email.strip()

def validate_input(user_input):
    """
    Validates the format of the username or email.

    Args:
        user_input (str): The username or email to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Simple regex for validating email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, user_input):
        return True
    elif len(user_input) > 0:  # Username should not be empty
        return True
    return False

def copy_to_clipboard(user_input):
    """
    Copies the validated username or email to the clipboard.

    Args:
        user_input (str): The username or email to copy.
    """
    try:
        pyperclip.copy(user_input)
        print("Successfully copied to clipboard!")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def main():
    """
    Main function that executes the program logic.
    """
    # Get user input
    user_input = get_duolingo_username_or_email()

    # Validate the input
    if not validate_input(user_input):
        print("Invalid input. Please enter a valid Duolingo username or email.")
        sys.exit(1)  # Exit with an error code

    # Copy the validated input to the clipboard
    copy_to_clipboard(user_input)

if __name__ == "__main__":
    main()  # Execute the main function
```

Make sure to install the `pyperclip` module before running the code by executing `pip install pyperclip` in your terminal.
