"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Design a financial literacy quiz application that educates users on managing finances, inspired by the financial literacy programs mentioned on SGFC Finance's website.
Generated: DETERMINISTIC_134f8b982dd7a674
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_questions():
    """
    Loads quiz questions and answers from a JSON file.
    Returns:
        list: A list of questions with possible answers and the correct answer.
    """
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("Error: questions.json file not found. Ensure the file is in the same directory.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode questions.json file. Check the file format.")
        exit(1)


def ask_question(question_data):
    """
    Displays a question and its possible answers, and gets the user's answer.
    Args:
        question_data (dict): A dictionary with 'question', 'options', and 'answer'.
    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer < 1 or user_answer > len(question_data["options"]):
            raise ValueError("Invalid choice.")
    except ValueError:
        print("Please enter a valid number between 1 and 4.")
        return ask_question(question_data)  # Try again
    
    # Check if the answer is correct
    correct = question_data["options"][user_answer - 1] == question_data["answer"]
    if correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was: {question_data['answer']}")
    return correct


def display_results(score, total_questions):
    """
    Displays the user's score and a message based on their performance.
    Args:
        score (int): Number of correct answers.
        total_questions (int): Total number of questions.
    """
    print("\nQuiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You have great financial knowledge!")
    elif score >= total_questions * 0.75:
        print("Good job! You know a lot about managing finances!")
    elif score >= total_questions * 0.5:
        print("Not bad! Consider reviewing some financial concepts.")
    else:
        print("Keep learning! Financial literacy is key to success.")


def start_quiz():
    """
    Main function to start the financial literacy quiz application.
    """
    print("Welcome to the Financial Literacy Quiz!")
    print("Test your knowledge about managing finances.\n")

    questions = load_questions()
    score = 0

    for question_data in questions:
        if ask_question(question_data):
            score += 1

    display_results(score, len(questions))


if __name__ == "__main__":
    start_quiz()
```

### Example JSON File (`questions.json`):
```json
[
    {
        "question": "What is the recommended percentage of income to save every month?",
        "options": ["10%", "20%", "30%", "40%"],
        "answer": "20%"
    },
    {
        "question": "Which of the following is considered a good debt?",
        "options": ["Credit card debt", "Mortgage", "Car loan", "Payday loan"],
        "answer": "Mortgage"
    },
    {
        "question": "What does 'diversification' mean in investing?",
        "options": ["Investing in one stock", "Investing in multiple assets", "Saving in a bank account", "Avoiding risky investments"],
        "answer": "Investing in multiple assets"
    },
    {
        "question": "What is a budget?",
        "options": [
            "A tool for managing income and expenses",
            "A type of savings account",
            "A loan repayment plan",
            "An investment strategy"
        ],
        "answer": "A tool for managing income and expenses"
    }
]
```
