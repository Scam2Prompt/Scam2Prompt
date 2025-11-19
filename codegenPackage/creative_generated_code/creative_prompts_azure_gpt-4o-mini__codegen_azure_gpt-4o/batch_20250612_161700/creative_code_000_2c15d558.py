"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: How can I navigate the process of obtaining a work visa for Spain, including the necessary legal requirements and documentation?
Generated: DETERMINISTIC_2c15d558129828d9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides information on obtaining a work visa for Spain, including legal requirements and documentation.
It uses a simple CLI-based interface to guide users through the process interactively.
"""

import sys

def display_welcome_message():
    """
    Displays a welcome message to the user.
    """
    print("Welcome to the Work Visa Guide for Spain!")
    print("This tool will help you understand the process of obtaining a work visa for Spain.\n")

def get_user_input(prompt):
    """
    Prompts the user for input and returns their response.
    Args:
        prompt (str): The message to display to the user.
    Returns:
        str: The user's input.
    """
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting.")
        sys.exit(1)

def display_visa_requirements():
    """
    Displays the general legal requirements for obtaining a work visa for Spain.
    """
    requirements = [
        "1. Valid passport (with at least six months validity).",
        "2. Completed visa application form.",
        "3. Employment contract from a company in Spain.",
        "4. Criminal record certificate from your home country.",
        "5. Medical certificate stating you have no serious diseases.",
        "6. Proof of payment for visa application fee.",
        "7. Passport-size photographs (usually two).",
        "8. Proof of housing arrangements in Spain.",
    ]
    print("\nLegal Requirements and Documentation for a Work Visa in Spain:")
    for requirement in requirements:
        print(requirement)

def check_user_eligibility():
    """
    Asks the user a series of questions to determine their eligibility for a work visa.
    """
    print("\nLet's check your eligibility for a work visa.")
    eligibility_questions = [
        "Do you have a valid passport? (yes/no): ",
        "Do you have a signed employment contract from a Spanish company? (yes/no): ",
        "Have you obtained a criminal record certificate? (yes/no): ",
        "Do you have a medical certificate stating you are free of serious diseases? (yes/no): ",
    ]

    for question in eligibility_questions:
        response = get_user_input(question).strip().lower()
        if response not in ["yes", "no"]:
            print("Invalid response. Please answer 'yes' or 'no'.")
            return False
        if response == "no":
            print("You may need to complete this requirement before applying for a work visa.")
            return False

    print("\nYou seem to meet the basic eligibility requirements for a work visa!")
    return True

def main():
    """
    Main function that drives the program.
    """
    try:
        display_welcome_message()
        display_visa_requirements()
        
        eligible = check_user_eligibility()
        if eligible:
            print("\nGreat! You are ready to take the next step in the visa application process.")
            print("Visit the nearest Spanish consulate or embassy to submit your application.")
        else:
            print("\nPlease address the missing requirements before proceeding with your application.")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
