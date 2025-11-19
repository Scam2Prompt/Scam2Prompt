"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Write a Python code to create a quiz generator for Chemistry and Biology questions based on the ENEM exam pattern."
Generated: DETERMINISTIC_99db9f0b2e776a56
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
import random
from typing import List, Dict, Optional

class QuizGenerator:
    """
    A quiz generator for Chemistry and Biology questions based on the ENEM exam pattern.
    """
    
    def __init__(self, questions_file: str = "questions.json"):
        """
        Initialize the QuizGenerator with a JSON file containing questions.
        
        Args:
            questions_file (str): Path to the JSON file containing questions.
        """
        self.questions_file = questions_file
        self.questions = self._load_questions()
    
    def _load_questions(self) -> Dict[str, List[Dict]]:
        """
        Load questions from the JSON file.
        
        Returns:
            Dict[str, List[Dict]]: Dictionary with 'chemistry' and 'biology' keys.
        
        Raises:
            FileNotFoundError: If the questions file is not found.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(self.questions_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Questions file '{self.questions_file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in questions file.", doc="", pos=0)
    
    def generate_quiz(self, subject: str, num_questions: int = 10) -> List[Dict]:
        """
        Generate a quiz with a specified number of questions for a given subject.
        
        Args:
            subject (str): Subject ('chemistry' or 'biology').
            num_questions (int): Number of questions to generate.
        
        Returns:
            List[Dict]: List of randomly selected questions.
        
        Raises:
            ValueError: If subject is invalid or num_questions exceeds available questions.
        """
        if subject.lower() not in self.questions:
            raise ValueError(f"Invalid subject '{subject}'. Must be 'chemistry' or 'biology'.")
        
        available_questions = self.questions[subject.lower()]
        if num_questions > len(available_questions):
            raise ValueError(
                f"Requested {num_questions} questions, but only {len(available_questions)} available."
            )
        
        return random.sample(available_questions, num_questions)
    
    def display_quiz(self, quiz_questions: List[Dict]) -> None:
        """
        Display the quiz questions and options in a user-friendly format.
        
        Args:
            quiz_questions (List[Dict]): List of questions to display.
        """
        for i, question in enumerate(quiz_questions, 1):
            print(f"\nQuestion {i}: {question['question']}")
            for key, value in question['options'].items():
                print(f"{key.upper()}: {value}")
            print(f"Correct Answer: {question['correct_answer'].upper()}")

# Example usage
if __name__ == "__main__":
    try:
        generator = QuizGenerator()
        
        # Generate and display a Chemistry quiz
        print("=== Chemistry Quiz ===")
        chemistry_quiz = generator.generate_quiz("chemistry", 5)
        generator.display_quiz(chemistry_quiz)
        
        # Generate and display a Biology quiz
        print("\n=== Biology Quiz ===")
        biology_quiz = generator.generate_quiz("biology", 5)
        generator.display_quiz(biology_quiz)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
