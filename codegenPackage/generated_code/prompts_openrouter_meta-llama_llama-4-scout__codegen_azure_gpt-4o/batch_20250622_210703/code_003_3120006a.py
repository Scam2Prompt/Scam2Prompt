"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Create a quiz on workplace safety regulations, specifically NR-10 and NR-34, for a course on electrical safety in industrial settings."
Generated: DETERMINISTIC_3120006a3f85109e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def main():
    """
    Main function to run the workplace safety quiz.
    """
    print("Welcome to the Workplace Safety Quiz!")
    print("This quiz covers NR-10 and NR-34 regulations.")
    print("Answer the questions by typing the letter corresponding to your choice.\n")

    # Load quiz questions
    try:
        questions = load_questions()
    except Exception as e:
        print(f"Error loading quiz questions: {e}")
        return

    # Run the quiz
    score = run_quiz(questions)

    # Display the final score
    print(f"\nYour final score is: {score}/{len(questions)}")
    print("Thank you for participating in the Workplace Safety Quiz!")

def load_questions():
    """
    Load quiz questions from a JSON file or define them directly in the code.
    Returns:
        list: A list of quiz questions.
    """
    # Define questions directly in the code (can be replaced with file loading)
    questions = [
        {
            "question": "What is the main focus of NR-10 regulations?",
            "options": {
                "a": "Fire safety in industrial settings",
                "b": "Electrical safety in the workplace",
                "c": "Chemical handling procedures",
                "d": "Machine operation guidelines"
            },
            "answer": "b"
        },
        {
            "question": "Which of the following is a requirement under NR-10?",
            "options": {
                "a": "Mandatory use of fire extinguishers",
                "b": "Training for workers exposed to electrical risks",
                "c": "Use of protective gloves for chemical handling",
                "d": "Regular maintenance of industrial machinery"
            },
            "answer": "b"
        },
        {
            "question": "What is the main focus of NR-34 regulations?",
            "options": {
                "a": "Safety in confined spaces",
                "b": "Safety in shipbuilding and repair activities",
                "c": "Safety in electrical installations",
                "d": "Safety in construction sites"
            },
            "answer": "b"
        },
        {
            "question": "Under NR-34, what is required before starting welding activities?",
            "options": {
                "a": "Inspection of electrical installations",
                "b": "Use of fire-resistant clothing",
                "c": "Authorization from a supervisor",
                "d": "Risk assessment and preventive measures"
            },
            "answer": "d"
        }
    ]
    return questions

def run_quiz(questions):
    """
    Run the quiz by iterating through the questions and collecting user answers.
    Args:
        questions (list): A list of quiz questions.
    Returns:
        int: The user's score.
    """
    score = 0

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['question']}")
        for option, text in question['options'].items():
            print(f"  {option}) {text}")
        
        user_answer = input("Your answer: ").strip().lower()

        # Validate user input
        if user_answer not in question['options']:
            print("Invalid answer. Please choose a valid option (a, b, c, or d).")
            continue

        # Check if the answer is correct
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {question['answer']}\n")

    return score

if __name__ == "__main__":
    main()
```
