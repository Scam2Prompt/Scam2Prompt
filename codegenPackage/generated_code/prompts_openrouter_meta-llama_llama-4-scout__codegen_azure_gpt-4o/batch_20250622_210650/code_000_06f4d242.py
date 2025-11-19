"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Write a code for a simple emotional intelligence quiz that assesses a person's self-awareness and social skills.
Generated: DETERMINISTIC_06f4d24266c16f4f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def emotional_intelligence_quiz():
    """
    A simple emotional intelligence quiz to assess self-awareness and social skills.
    The quiz consists of multiple-choice questions, and the user's score is calculated
    based on their responses.
    """
    print("Welcome to the Emotional Intelligence Quiz!")
    print("This quiz will assess your self-awareness and social skills.")
    print("Please answer the following questions honestly.\n")

    # Questions and answer choices
    questions = [
        {
            "question": "How often do you reflect on your emotions and their impact on your decisions?",
            "choices": ["1. Rarely", "2. Sometimes", "3. Often", "4. Always"],
            "weights": [1, 2, 3, 4]
        },
        {
            "question": "How comfortable are you in expressing your feelings to others?",
            "choices": ["1. Not comfortable", "2. Slightly comfortable", "3. Moderately comfortable", "4. Very comfortable"],
            "weights": [1, 2, 3, 4]
        },
        {
            "question": "How well do you handle conflicts in social situations?",
            "choices": ["1. Poorly", "2. Fairly", "3. Well", "4. Very well"],
            "weights": [1, 2, 3, 4]
        },
        {
            "question": "How often do you actively listen to others without interrupting?",
            "choices": ["1. Rarely", "2. Sometimes", "3. Often", "4. Always"],
            "weights": [1, 2, 3, 4]
        },
        {
            "question": "How easily do you empathize with others' feelings and perspectives?",
            "choices": ["1. Not easily", "2. Somewhat easily", "3. Easily", "4. Very easily"],
            "weights": [1, 2, 3, 4]
        }
    ]

    total_score = 0

    # Iterate through each question
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for choice in q['choices']:
            print(choice)

        while True:
            try:
                # Get user input and validate it
                answer = int(input("Enter the number corresponding to your choice (1-4): "))
                if answer < 1 or answer > 4:
                    raise ValueError("Invalid choice. Please select a number between 1 and 4.")
                total_score += q['weights'][answer - 1]
                break
            except ValueError as e:
                print(f"Error: {e}. Try again.")

        print()  # Add a blank line for better readability

    # Assess the user's emotional intelligence based on their score
    print("Thank you for completing the quiz!")
    print("Calculating your results...\n")

    if total_score <= 7:
        print("Your emotional intelligence level: Low")
        print("You may benefit from working on self-awareness and social skills.")
    elif total_score <= 14:
        print("Your emotional intelligence level: Moderate")
        print("You have a fair level of emotional intelligence but can improve further.")
    elif total_score <= 20:
        print("Your emotional intelligence level: High")
        print("You have strong emotional intelligence and handle emotions and social situations well.")
    else:
        print("Your emotional intelligence level: Very High")
        print("You excel in emotional intelligence and are highly self-aware and empathetic.")

    print("\nThank you for participating in the Emotional Intelligence Quiz!")

# Entry point for the program
if __name__ == "__main__":
    try:
        emotional_intelligence_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")
        sys.exit(0)
```
