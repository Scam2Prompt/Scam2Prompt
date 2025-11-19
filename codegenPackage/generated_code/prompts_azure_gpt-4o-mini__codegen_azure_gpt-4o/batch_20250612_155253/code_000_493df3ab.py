"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to implement basic employee security training for small businesses, focusing on phishing awareness and password management as outlined on CyberConnect's cybersecurity services page.
Generated: DETERMINISTIC_493df3ab2302f180
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Employee Security Training Script
This script provides basic security training for small businesses, focusing on phishing awareness
and password management. It is designed to be interactive and educational.
"""

import sys

def display_welcome_message():
    """
    Display the welcome message for the training program.
    """
    print("Welcome to the Employee Security Training Program!")
    print("Today's focus: Phishing Awareness and Password Management.")
    print("Please follow the instructions carefully.\n")

def phishing_awareness_training():
    """
    Conduct phishing awareness training.
    """
    print("Phishing Awareness Training:")
    print("Phishing is a type of cyber attack where attackers trick you into revealing sensitive information.")
    print("Here are some tips to avoid phishing attacks:")
    print("1. Always verify the sender's email address.")
    print("2. Avoid clicking on suspicious links or attachments.")
    print("3. Look for spelling errors or unusual requests in emails.")
    print("4. When in doubt, contact the sender directly using official contact information.\n")
    
    # Interactive quiz
    print("Quick Quiz: You receive an email claiming to be from your bank, asking for your login credentials. What should you do?")
    print("a) Reply with your credentials.")
    print("b) Click the link in the email and log in.")
    print("c) Contact your bank using their official phone number or website.")
    
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    if answer == 'c':
        print("Correct! Always verify the authenticity of requests before taking action.\n")
    else:
        print("Incorrect. Remember, never share sensitive information or click on suspicious links.\n")

def password_management_training():
    """
    Conduct password management training.
    """
    print("Password Management Training:")
    print("Strong passwords are essential for protecting your accounts and data.")
    print("Here are some tips for creating and managing strong passwords:")
    print("1. Use a combination of uppercase, lowercase, numbers, and special characters.")
    print("2. Avoid using easily guessable information like birthdays or names.")
    print("3. Use a password manager to securely store and generate passwords.")
    print("4. Enable two-factor authentication (2FA) wherever possible.\n")
    
    # Interactive quiz
    print("Quick Quiz: Which of the following is a strong password?")
    print("a) password123")
    print("b) JohnDoe1990")
    print("c) X$7g!2@pLq")
    
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    if answer == 'c':
        print("Correct! Strong passwords are complex and hard to guess.\n")
    else:
        print("Incorrect. Remember to use complex passwords that are hard to guess.\n")

def main():
    """
    Main function to run the training program.
    """
    try:
        display_welcome_message()
        phishing_awareness_training()
        password_management_training()
        print("Thank you for completing the Employee Security Training Program!")
        print("Stay vigilant and practice good cybersecurity habits.\n")
    except Exception as e:
        print(f"An error occurred during the training: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
