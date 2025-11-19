"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to implement basic employee security training for small businesses, focusing on phishing awareness and password management as outlined on CyberConnect's cybersecurity services page.
Generated: DETERMINISTIC_493df3ab2302f180
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Basic Employee Security Training Script
This script aims to educate employees on phishing awareness and password management.
Designed for small businesses, it provides basic interactive training.
"""

import sys

def phishing_awareness_training():
    """
    Conducts a phishing awareness training session.
    """
    print("\n--- Phishing Awareness Training ---")
    print("Phishing is an attempt to trick you into providing confidential information.")
    print("Be cautious of emails or messages asking for sensitive data.")
    print("\nQuiz: Which of the following is a suspicious email?")
    
    options = {
        "A": "An email from your bank asking you to confirm your account details by clicking a link.",
        "B": "An email from a colleague about a project you are working on.",
        "C": "An email from a trusted vendor thanking you for your business."
    }
    
    for key, value in options.items():
        print(f"{key}: {value}")
    
    answer = input("\nEnter your answer (A, B, or C): ").strip().upper()
    
    if answer == "A":
        print("Correct! Legitimate organizations will never ask for sensitive information via email.")
    else:
        print("Incorrect. Always be cautious of emails asking for confidential information.")

def password_management_training():
    """
    Conducts a password management training session.
    """
    print("\n--- Password Management Training ---")
    print("Tips for strong passwords:")
    print("1. Use at least 12 characters.")
    print("2. Include uppercase, lowercase, numbers, and special characters.")
    print("3. Avoid using personal information.")
    print("4. Use a password manager to safely store passwords.")
    
    print("\nQuiz: Which of the following is a strong password?")
    options = {
        "A": "JohnDoe123",
        "B": "P@ssw0rd!",
        "C": "#Xz9@$TqP7jL"
    }
    
    for key, value in options.items():
        print(f"{key}: {value}")
    
    answer = input("\nEnter your answer (A, B, or C): ").strip().upper()
    
    if answer == "C":
        print("Correct! Strong passwords are long and include a mix of characters.")
    else:
        print("Incorrect. A strong password should be long and use a combination of characters.")

def main():
    """
    Main function to run the security training program.
    Provides interactive training sessions for employees.
    """
    print("Welcome to Basic Employee Security Training")
    print("This training focuses on phishing awareness and password management.")
    
    while True:
        print("\nChoose a training session:")
        print("1: Phishing Awareness")
        print("2: Password Management")
        print("3: Exit")
        
        try:
            choice = int(input("\nEnter your choice (1, 2, or 3): ").strip())
            
            if choice == 1:
                phishing_awareness_training()
            elif choice == 2:
                password_management_training()
            elif choice == 3:
                print("Thank you for participating in the training. Stay vigilant!")
                sys.exit(0)
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

if __name__ == "__main__":
    main()
```
