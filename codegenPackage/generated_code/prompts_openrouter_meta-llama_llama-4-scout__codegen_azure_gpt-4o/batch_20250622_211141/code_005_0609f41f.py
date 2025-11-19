"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Design a certification program for artificial intelligence and machine learning using Python."
Generated: DETERMINISTIC_0609f41ff7d5b671
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Certification Program for Artificial Intelligence and Machine Learning
This program allows users to register for a certification, take a test, and receive a certificate
based on their performance. It uses Python's built-in features and follows best practices.
"""

import json
import random

# Constants
CERTIFICATION_PASS_THRESHOLD = 70  # Minimum percentage to pass the certification
CERTIFICATION_QUESTIONS = [
    {"question": "What is supervised learning?", "options": ["A", "B", "C", "D"], "answer": "A"},
    {"question": "Which algorithm is used for classification?", "options": ["A", "B", "C", "D"], "answer": "B"},
    {"question": "What is overfitting?", "options": ["A", "B", "C", "D"], "answer": "C"},
    {"question": "Which library is used for deep learning?", "options": ["A", "B", "C", "D"], "answer": "D"},
    {"question": "What is gradient descent?", "options": ["A", "B", "C", "D"], "answer": "A"},
]

# User database (in-memory for simplicity)
user_database = {}

# Function to register a user
def register_user():
    """
    Registers a new user for the certification program.
    """
    print("Welcome to the AI/ML Certification Program!")
    name = input("Enter your full name: ").strip()
    email = input("Enter your email address: ").strip()

    if email in user_database:
        print("Error: Email already registered.")
        return

    user_database[email] = {"name": name, "email": email, "score": None, "certificate": None}
    print(f"Registration successful! Welcome, {name}.")

# Function to take the test
def take_test(email):
    """
    Allows a registered user to take the certification test.
    """
    if email not in user_database:
        print("Error: User not found. Please register first.")
        return

    print("Starting the AI/ML Certification Test...")
    score = 0

    for question in CERTIFICATION_QUESTIONS:
        print("\n" + question["question"])
        print("Options:", ", ".join(question["options"]))
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == question["answer"]:
            score += 1

    percentage_score = (score / len(CERTIFICATION_QUESTIONS)) * 100
    user_database[email]["score"] = percentage_score

    if percentage_score >= CERTIFICATION_PASS_THRESHOLD:
        user_database[email]["certificate"] = f"Certificate of Completion for AI/ML (Score: {percentage_score:.2f}%)"
        print(f"Congratulations! You passed with a score of {percentage_score:.2f}%.")
    else:
        user_database[email]["certificate"] = None
        print(f"Unfortunately, you did not pass. Your score: {percentage_score:.2f}%.")

# Function to view certificate
def view_certificate(email):
    """
    Allows a user to view their certificate if they passed the test.
    """
    if email not in user_database:
        print("Error: User not found. Please register first.")
        return

    certificate = user_database[email]["certificate"]
    if certificate:
        print("\n" + certificate)
    else:
        print("No certificate available. Please take the test and pass to receive a certificate.")

# Main program loop
def main():
    """
    Main function to run the certification program.
    """
    while True:
        print("\nAI/ML Certification Program")
        print("1. Register")
        print("2. Take Test")
        print("3. View Certificate")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            register_user()
        elif choice == 2:
            email = input("Enter your registered email: ").strip()
            take_test(email)
        elif choice == 3:
            email = input("Enter your registered email: ").strip()
            view_certificate(email)
        elif choice == 4:
            print("Thank you for using the AI/ML Certification Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
