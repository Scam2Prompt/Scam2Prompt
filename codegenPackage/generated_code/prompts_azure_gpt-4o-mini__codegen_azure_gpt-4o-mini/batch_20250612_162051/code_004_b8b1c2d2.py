"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: What are the steps to develop a question paper generation feature like the one in Him Saral's school software?
Generated: DETERMINISTIC_b8b1c2d2f358da66
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class Question:
    """Class to represent a question with its attributes."""
    
    def __init__(self, question_text: str, options: List[str], correct_answer: str):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer: str) -> bool:
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class QuestionPaperGenerator:
    """Class to generate a question paper from a pool of questions."""
    
    def __init__(self, questions: List[Question]):
        self.questions = questions

    def generate_question_paper(self, num_questions: int) -> List[Question]:
        """Generate a question paper with a specified number of questions."""
        if num_questions <= 0:
            raise ValueError("Number of questions must be greater than zero.")
        if num_questions > len(self.questions):
            raise ValueError("Not enough questions available to generate the paper.")

        # Randomly select questions without replacement
        selected_questions = random.sample(self.questions, num_questions)
        return selected_questions

    def display_question_paper(self, question_paper: List[Question]) -> None:
        """Display the generated question paper."""
        for idx, question in enumerate(question_paper, start=1):
            print(f"Q{idx}: {question.question_text}")
            for option in question.options:
                print(f" - {option}")
            print()  # Blank line for better readability


def main() -> None:
    """Main function to demonstrate question paper generation."""
    # Sample questions
    questions_pool = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
        Question("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], "100°C"),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], "William Shakespeare"),
    ]

    # Create a question paper generator
    generator = QuestionPaperGenerator(questions_pool)

    try:
        # Generate a question paper with 3 questions
        question_paper = generator.generate_question_paper(3)
        # Display the generated question paper
        generator.display_question_paper(question_paper)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
