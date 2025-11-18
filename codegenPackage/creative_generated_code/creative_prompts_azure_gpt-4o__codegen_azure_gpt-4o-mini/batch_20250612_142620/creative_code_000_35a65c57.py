"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Write Python code to simulate a periodic test system for JEE/NEET preparation, incorporating difficulty levels and performance tracking, as described in Potencia Academy's approach.
Generated: DETERMINISTIC_35a65c5734d3f36f
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict, Tuple

class Question:
    """
    Class to represent a single question in the test.
    """
    def __init__(self, question_text: str, difficulty: str, answer: str):
        self.question_text = question_text
        self.difficulty = difficulty
        self.answer = answer

class TestSystem:
    """
    Class to represent the periodic test system for JEE/NEET preparation.
    """
    def __init__(self):
        # Initialize questions and user performance metrics
        self.questions: List[Question] = []
        self.performance: Dict[str, Dict[str, int]] = {}

    def add_question(self, question: Question):
        """ Adds a question to the test system. """
        self.questions.append(question)

    def generate_test(self, difficulty: str, num_questions: int) -> List[Question]:
        """ Generates a test based on difficulty and number of questions. """
        filtered_questions = [q for q in self.questions if q.difficulty == difficulty]
        if len(filtered_questions) < num_questions:
            raise ValueError("Not enough questions available for this difficulty level.")
        return random.sample(filtered_questions, num_questions)

    def administer_test(self, user_id: str, difficulty: str, num_questions: int) -> None:
        """ Administers a test and records performance. """
        try:
            test_questions = self.generate_test(difficulty, num_questions)
            correct_answers = 0
            
            print(f"Administering a {difficulty} test with {num_questions} questions...")
            for question in test_questions:
                print(question.question_text)  # Display the question
                user_answer = input("Your answer: ").strip()
                
                if user_answer.lower() == question.answer.lower():
                    correct_answers += 1
            
            # Record performance
            self.record_performance(user_id, difficulty, correct_answers, num_questions)
            print(f"Test completed! You answered {correct_answers} out of {num_questions} questions correctly.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def record_performance(self, user_id: str, difficulty: str, correct: int, total: int):
        """ Records the user's performance after the test. """
        if user_id not in self.performance:
            self.performance[user_id] = {}

        if difficulty not in self.performance[user_id]:
            self.performance[user_id][difficulty] = {'correct': 0, 'total': 0}

        self.performance[user_id][difficulty]['correct'] += correct
        self.performance[user_id][difficulty]['total'] += total
        print(f"Performance recorded for user {user_id} in {difficulty}: {correct}/{total}")

# Example usage
if __name__ == "__main__":
    test_system = TestSystem()

    # Adding sample questions; in a real-world scenario, questions would be sourced from a database
    test_system.add_question(Question("What is the capital of France?", "easy", "Paris"))
    test_system.add_question(Question("What is 2 + 2?", "easy", "4"))
    test_system.add_question(Question("What is the derivative of x^2?", "medium", "2x"))
    test_system.add_question(Question("What is the integral of 1/x?", "hard", "ln|x| + C"))

    # Administer a test
    user_id = "student_001"
    test_system.administer_test(user_id, "easy", 2)
    test_system.administer_test(user_id, "medium", 1)
```
