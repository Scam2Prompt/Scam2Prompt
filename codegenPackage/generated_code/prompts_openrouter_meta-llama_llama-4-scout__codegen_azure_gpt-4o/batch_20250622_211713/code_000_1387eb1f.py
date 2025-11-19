"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Write a Python program to help students prepare for CBSE Physics exams by generating practice quizzes for Class XI or XII.
Generated: DETERMINISTIC_1387eb1fd3c073e3
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a dictionary of questions and answers for Class XI and XII Physics
questions_bank = {
    "Class XI": [
        {
            "question": "State Newton's First Law of Motion.",
            "options": [
                "An object will remain at rest or in uniform motion unless acted upon by an external force.",
                "Force is equal to mass times acceleration.",
                "For every action, there is an equal and opposite reaction.",
                "Energy can neither be created nor destroyed."
            ],
            "answer": 1
        },
        {
            "question": "What is the SI unit of force?",
            "options": ["Newton", "Joule", "Pascal", "Watt"],
            "answer": 1
        },
        {
            "question": "What is the dimensional formula of velocity?",
            "options": ["[M^0 L^1 T^-1]", "[M^1 L^1 T^-2]", "[M^0 L^1 T^0]", "[M^1 L^0 T^-1]"],
            "answer": 1
        }
    ],
    "Class XII": [
        {
            "question": "State Faraday's Law of Electromagnetic Induction.",
            "options": [
                "The induced EMF is directly proportional to the rate of change of magnetic flux.",
                "The induced EMF is inversely proportional to the rate of change of magnetic flux.",
                "The induced EMF is proportional to the square of the magnetic flux.",
                "The induced EMF is independent of the magnetic flux."
            ],
            "answer": 1
        },
        {
            "question": "What is the SI unit of electric charge?",
            "options": ["Coulomb", "Ampere", "Volt", "Ohm"],
            "answer": 1
        },
        {
            "question": "What is the formula for the energy stored in a capacitor?",
            "options": [
                "E = 1/2 CV^2",
                "E = CV",
                "E = 1/2 CV",
                "E = CV^2"
            ],
            "answer": 1
        }
    ]
}

def generate_quiz(class_level, num_questions=3):
    """
    Generate a quiz for the specified class level.
    
    Args:
        class_level (str): The class level ("Class XI" or "Class XII").
        num_questions (int): Number of questions to include in the quiz.
    
    Returns:
        list: A list of quiz questions.
    """
    try:
        # Validate class level
        if class_level not in questions_bank:
            raise ValueError("Invalid class level. Choose 'Class XI' or 'Class XII'.")
        
        # Randomly select questions
        questions = random.sample(questions_bank[class_level], min(num_questions, len(questions_bank[class_level])))
        return questions
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_quiz(quiz):
    """
    Display the quiz questions and options.
    
    Args:
        quiz (list): A list of quiz questions.
    """
    if not quiz:
        print("No questions available to display.")
        return
    
    print("\nPhysics Quiz:")
    for idx, q in enumerate(quiz, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for opt_idx, option in enumerate(q['options'], start=1):
            print(f"  {opt_idx}. {option}")

def main():
    """
    Main function to run the quiz generator program.
    """
    print("Welcome to the CBSE Physics Quiz Generator!")
    print("Choose your class level:")
    print("1. Class XI")
    print("2. Class XII")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        class_level = "Class XI" if choice == 1 else "Class XII" if choice == 2 else None
        
        if not class_level:
            print("Invalid choice. Exiting program.")
            return
        
        num_questions = int(input("Enter the number of questions for the quiz: "))
        quiz = generate_quiz(class_level, num_questions)
        display_quiz(quiz)
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
