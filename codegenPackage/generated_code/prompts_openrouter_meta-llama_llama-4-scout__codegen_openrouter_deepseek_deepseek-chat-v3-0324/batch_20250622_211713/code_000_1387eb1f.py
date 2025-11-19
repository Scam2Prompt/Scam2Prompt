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
from typing import Dict, List, Tuple, Optional

class PhysicsQuizGenerator:
    """
    A class to generate practice quizzes for CBSE Physics exams (Class XI or XII).
    The quiz consists of multiple-choice questions (MCQs) with options.
    """

    def __init__(self):
        self.questions_xi = {
            "Units and Measurements": [
                {
                    "question": "Which of the following is a derived unit?",
                    "options": ["Kilogram", "Second", "Newton", "Ampere"],
                    "answer": "Newton"
                },
                {
                    "question": "The dimensional formula for force is:",
                    "options": ["[MLT⁻²]", "[ML²T⁻²]", "[MLT⁻¹]", "[M⁰L⁰T⁻¹]"],
                    "answer": "[MLT⁻²]"
                }
            ],
            "Motion in a Straight Line": [
                {
                    "question": "The slope of a velocity-time graph represents:",
                    "options": ["Displacement", "Acceleration", "Distance", "Speed"],
                    "answer": "Acceleration"
                }
            ]
        }

        self.questions_xii = {
            "Electric Charges and Fields": [
                {
                    "question": "The SI unit of electric flux is:",
                    "options": ["N/C", "N·m²/C", "V/m", "C/m²"],
                    "answer": "N·m²/C"
                }
            ],
            "Current Electricity": [
                {
                    "question": "Ohm's Law relates current, voltage, and:",
                    "options": ["Resistance", "Capacitance", "Inductance", "Power"],
                    "answer": "Resistance"
                }
            ]
        }

    def generate_quiz(self, class_level: str, topic: Optional[str] = None, num_questions: int = 5) -> List[Dict]:
        """
        Generate a quiz based on class level and optional topic.
        
        Args:
            class_level (str): 'XI' or 'XII'
            topic (str, optional): Specific topic to focus on. Defaults to None (random topics).
            num_questions (int): Number of questions in the quiz. Defaults to 5.
            
        Returns:
            List[Dict]: List of question dictionaries with 'question', 'options', and 'answer'.
            
        Raises:
            ValueError: If class_level is not 'XI' or 'XII' or if num_questions is invalid.
        """
        if class_level.upper() not in ['XI', 'XII']:
            raise ValueError("Class level must be 'XI' or 'XII'")
        
        if num_questions <= 0:
            raise ValueError("Number of questions must be positive")
            
        question_pool = self.questions_xi if class_level.upper() == 'XI' else self.questions_xii
        
        if topic:
            if topic not in question_pool:
                raise ValueError(f"Topic '{topic}' not found for Class {class_level}")
            questions = question_pool[topic]
        else:
            questions = [q for topic_questions in question_pool.values() for q in topic_questions]
            
        if num_questions > len(questions):
            raise ValueError(f"Only {len(questions)} questions available for the selected criteria")
            
        return random.sample(questions, num_questions)

    def take_quiz(self, quiz: List[Dict]) -> Tuple[int, int]:
        """
        Administer the quiz to the user and return the score.
        
        Args:
            quiz (List[Dict]): List of question dictionaries.
            
        Returns:
            Tuple[int, int]: (correct_answers, total_questions)
        """
        correct = 0
        for i, q in enumerate(quiz, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")
                
            while True:
                try:
                    choice = int(input("Your answer (enter option number): "))
                    if 1 <= choice <= len(q['options']):
                        break
                    print(f"Please enter a number between 1 and {len(q['options'])}")
                except ValueError:
                    print("Please enter a valid number")
                    
            if q['options'][choice - 1] == q['answer']:
                correct += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is: {q['answer']}")
                
        return correct, len(quiz)

def main():
    """Main function to interact with the user and run the quiz."""
    print("Welcome to CBSE Physics Quiz Generator!")
    generator = PhysicsQuizGenerator()
    
    while True:
        try:
            class_level = input("Enter class level (XI/XII): ").upper()
            topic = input("Enter topic (press Enter for random): ").strip() or None
            num_questions = int(input("Number of questions (default 5): ") or 5)
            
            quiz = generator.generate_quiz(class_level, topic, num_questions)
            print(f"\nStarting your {class_level} Physics quiz ({len(quiz)} questions)...")
            
            correct, total = generator.take_quiz(quiz)
            print(f"\nQuiz completed! Score: {correct}/{total} ({correct/total*100:.1f}%)")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nQuiz aborted.")
            break
            
        another = input("\nTake another quiz? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
```
