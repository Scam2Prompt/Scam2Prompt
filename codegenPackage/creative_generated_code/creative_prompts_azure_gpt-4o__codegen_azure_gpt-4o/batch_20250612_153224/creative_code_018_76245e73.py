"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create Python code for a gamified quiz that tests knowledge of Microsoft Word shortcuts, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_76245e73c05bcdf2
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

# Define the quiz questions and answers
QUESTIONS = [
    {
        "question": "What is the shortcut to save a document in Microsoft Word?",
        "options": ["Ctrl + S", "Ctrl + C", "Ctrl + V", "Ctrl + P"],
        "answer": "Ctrl + S",
    },
    {
        "question": "How do you undo an action in Microsoft Word?",
        "options": ["Ctrl + U", "Ctrl + Z", "Ctrl + Y", "Ctrl + N"],
        "answer": "Ctrl + Z",
    },
    {
        "question": "What is the shortcut to paste content in Microsoft Word?",
        "options": ["Ctrl + C", "Ctrl + S", "Ctrl + P", "Ctrl + V"],
        "answer": "Ctrl + V",
    },
    {
        "question": "Which shortcut is used to print a document in Microsoft Word?",
        "options": ["Ctrl + P", "Ctrl + Q", "Ctrl + O", "Ctrl + S"],
        "answer": "Ctrl + P",
    },
    {
        "question": "How do you select all content in a Microsoft Word document?",
        "options": ["Ctrl + A", "Ctrl + E", "Ctrl + L", "Ctrl + T"],
        "answer": "Ctrl + A",
    },
]

def ask_question(question_data):
    """
    Displays a question, its options, and gets the user's answer.
    
    Args:
        question_data (dict): A dictionary containing the question, options, and correct answer.
    
    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        # Get user input and validate it
        user_choice = int(input("Enter the number of your answer: "))
        if user_choice < 1 or user_choice > len(question_data["options"]):
            print("Invalid choice. Please select a valid option.")
            return False
        
        # Check if the answer is correct
        selected_option = question_data["options"][user_choice - 1]
        if selected_option == question_data["answer"]:
            print("Correct!")
            return True
        else:
            print("Wrong! The correct answer was:", question_data["answer"])
            return False
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the options.")
        return False

def gamified_quiz():
    """
    Runs the gamified quiz on Microsoft Word shortcuts.
    """
    print("Welcome to the Microsoft Word Shortcuts Quiz!")
    print("Test your knowledge of Word shortcuts. Each correct answer earns you a point!")

    score = 0
    total_questions = len(QUESTIONS)
    
    # Randomize the order of questions
    random.shuffle(QUESTIONS)
    
    for question_data in QUESTIONS:
        if ask_question(question_data):
            score += 1
    
    # Display the final score
    print("\nQuiz Over!")
    print(f"Your final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent job! You nailed it!")
    elif score >= total_questions // 2:
        print("Good work! Keep practicing and you'll get even better!")
    else:
        print("Keep learning! Practice makes perfect!")

# Entry point for the program
if __name__ == "__main__":
    try:
        gamified_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")
```
