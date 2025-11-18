"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code to create a gamified quiz about hardware and software, inspired by the interactive games on "Portal de Saltinho" for teaching computer science concepts.
Generated: DETERMINISTIC_8dbd1e7d71f3b02f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Function to display a welcome message
def display_welcome():
    print("Welcome to the Computer Science Concepts Quiz!")
    print("Test your knowledge of hardware and software in this interactive quiz!")
    print("Type the number corresponding to your answer and press Enter.")
    print("Let’s get started!\n")

# Function to load questions and answers
def load_questions():
    return [
        {
            "question": "What is the main function of the CPU?",
            "options": ["Execute instructions", "Store data", "Connect peripherals", "Transmit data"],
            "answer": 1
        },
        {
            "question": "Which device is considered an input device?",
            "options": ["Monitor", "Keyboard", "Printer", "Speaker"],
            "answer": 2
        },
        {
            "question": "Which type of software is used to manage hardware resources?",
            "options": ["Operating System", "Application Software", "Utility Software", "Driver Software"],
            "answer": 1
        },
        {
            "question": "Which of the following is volatile memory?",
            "options": ["Hard Drive", "RAM", "DVD", "Flash Drive"],
            "answer": 2
        },
        {
            "question": "Which represents a hardware component?",
            "options": ["Microsoft Word", "Google Chrome", "Motherboard", "Antivirus Software"],
            "answer": 3
        }
    ]

# Function to ask a question and get the user's answer
def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    while True:
        try:
            user_choice = int(input("Your answer (1-4): "))
            if user_choice < 1 or user_choice > 4:
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
            return user_choice
        except ValueError as e:
            print(e)

# Function to calculate the score at the end of the quiz
def calculate_score(questions, user_answers):
    score = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question["answer"]:
            score += 1
    return score

# Main function to run the quiz
def run_quiz():
    display_welcome()
    questions = load_questions()
    user_answers = []

    # Shuffle questions for a gamified experience
    random.shuffle(questions)

    # Loop through the questions
    for question in questions:
        user_answers.append(ask_question(question))
        print("\n")  # Add spacing between questions for better readability

    # Calculate score and display results
    score = calculate_score(questions, user_answers)
    print(f"Quiz complete! You scored {score}/{len(questions)}.")
    if score == len(questions):
        print("Excellent job! You're a computer science wizard!")
    elif score >= len(questions) * 0.75:
        print("Great work! You have a solid understanding!")
    else:
        print("Keep studying, and you'll get there!")

# Entry point for the script
if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz terminated. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
```
