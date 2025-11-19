"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Generate a code snippet for an interactive training module that helps staff understand AML (FIC) obligations.
Generated: DETERMINISTIC_ed049d527735fdca
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

def display_message(message, delay=1):
    """
    Display a message to the user with an optional delay for readability.

    Args:
        message (str): The message to display.
        delay (int): Time in seconds to wait after displaying the message (default is 1).
    """
    print(message)
    time.sleep(delay)

def get_user_input(prompt):
    """
    Get input from the user and handle potential errors.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        str: The user's input.
    """
    try:
        return input(prompt)
    except Exception as e:
        print(f"An error occurred while capturing input: {e}")
        return ""

def interactive_training_module():
    """
    Interactive training module for staff to understand AML (FIC) obligations.

    This module displays information and asks questions interactively.
    """
    try:
        display_message("Welcome to the AML (FIC) Training Module!")
        display_message("This module will help you understand key Anti-Money Laundering obligations.")
        display_message("Let's begin!\n")

        # Display information about AML
        display_message("AML (Anti-Money Laundering) refers to laws, regulations, and procedures aimed at preventing criminals from disguising illegally obtained funds as legitimate income.")
        display_message("Organizations are required to detect and report suspicious activities to the Financial Intelligence Centre (FIC).")
        
        # Ask a question to test understanding
        answer = get_user_input("\nQuestion: What does AML stand for? ")
        
        # Validate the response
        if answer.strip().lower() == "anti-money laundering":
            display_message("Correct! Well done.\n")
        else:
            display_message("Incorrect. AML stands for Anti-Money Laundering.\n")
        
        # Display further obligations
        display_message("Key obligations under AML include:")
        display_message("1. Customer Due Diligence (CDD) - Verify the identity of clients.")
        display_message("2. Suspicious Transaction Reporting (STR) - Report any unusual or suspicious activities.")
        display_message("3. Record Keeping - Maintain detailed records of transactions and client information.")
        
        # Ask another question
        answer = get_user_input("\nQuestion: Name one key obligation under AML? ")
        
        # Validate the response
        if answer.strip().lower() in ["customer due diligence", "cdd", "suspicious transaction reporting", "str", "record keeping"]:
            display_message("Correct! You're learning well.\n")
        else:
            display_message("Incorrect. Examples of AML obligations include CDD, STR, and Record Keeping.\n")
        
        # Wrap up
        display_message("Thank you for participating in the AML (FIC) Training Module!")
        display_message("Remember, compliance with AML obligations is critical for protecting the integrity of the financial system.")
    except Exception as e:
        print(f"An error occurred during the training module: {e}")

if __name__ == "__main__":
    """
    Entry point of the program.
    Initializes the interactive AML training module.
    """
    interactive_training_module()
```
