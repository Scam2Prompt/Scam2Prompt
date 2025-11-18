"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Write Python code to simulate an aptitude test for placement training, incorporating modules for language skills, IT skills, and life skills, as described by SMART Training Resources.
Generated: DETERMINISTIC_af3ec84f5bb2c1db
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def display_welcome_message():
    """
    Display the welcome message for the aptitude test.
    """
    print("Welcome to the Placement Training Aptitude Test!")
    print("This test is divided into three modules:")
    print("1. Language Skills")
    print("2. IT Skills")
    print("3. Life Skills")
    print("Answer the questions to the best of your ability!")
    print("Let’s get started!\n")

def get_user_response(prompt):
    """
    Get user response for a given prompt. Handles invalid inputs gracefully.
    """
    while True:
        try:
            response = int(input(prompt))
            return response
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_question(question, options, correct_option):
    """
    Handles asking a single question, validating response, and scoring.
    :param question: The question text
    :param options: List of options for the question
    :param correct_option: The index of the correct option (0-based indexing)
    :return: 1 if the answer is correct, 0 otherwise
    """
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    response = get_user_response("Enter your choice (1, 2, 3, ...): ")
    if response - 1 == correct_option:
        print("Correct!\n")
        return 1
    else:
        print("Incorrect. The correct answer was: ", options[correct_option], "\n")
        return 0

def language_skills_module():
    """
    Simulates the Language Skills module.
    """
    print("Language Skills Module\n")
    questions = [
        {
            "question": "Choose the correct spelling:",
            "options": ["Accomodation", "Accommodation", "Acomodation", "Accommadation"],
            "correct_option": 1
        },
        {
            "question": "Identify the synonym of 'Happy':",
            "options": ["Sad", "Joyful", "Angry", "Fearful"],
            "correct_option": 1
        }
    ]
    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_option"])
    print(f"Language Skills Module Completed! Your score: {score}/{len(questions)}\n")
    return score

def it_skills_module():
    """
    Simulates the IT Skills module.
    """
    print("IT Skills Module\n")
    questions = [
        {
            "question": "Which language is used for web development?",
            "options": ["Python", "JavaScript", "C++", "Ruby"],
            "correct_option": 1
        },
        {
            "question": "What does 'CPU' stand for?",
            "options": ["Central Processing Unit", "Computer Processing Unit", 
                        "Control Processing Unit", "Compute Processing Unit"],
            "correct_option": 0
        }
    ]
    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_option"])
    print(f"IT Skills Module Completed! Your score: {score}/{len(questions)}\n")
    return score

def life_skills_module():
    """
    Simulates the Life Skills module.
    """
    print("Life Skills Module\n")
    questions = [
        {
            "question": "What is the best way to handle stress?",
            "options": ["Avoid responsibilities", "Exercise and meditate", 
                        "Procrastinate", "Ignore the problem"],
            "correct_option": 1
        },
        {
            "question": "Which is an effective way to resolve conflicts?",
            "options": ["Avoid communication", "Listen actively", 
                        "Raise your voice", "Ignore the conflict"],
            "correct_option": 1
        }
    ]
    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_option"])
    print(f"Life Skills Module Completed! Your score: {score}/{len(questions)}\n")
    return score

def main():
    """
    Main function to run the aptitude test.
    """
    display_welcome_message()
    total_score = 0
    total_score += language_skills_module()
    total_score += it_skills_module()
    total_score += life_skills_module()

    print(f"Placement Training Aptitude Test Completed! Your total score: {total_score}/6")
    print("Thank you for participating!")

if __name__ == "__main__":
    main()
```
