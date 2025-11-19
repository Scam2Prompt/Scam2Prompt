"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Design a question paper generation module for schools, referencing the functionality described in Him Saral's Question Paper module.
Generated: DETERMINISTIC_24ca19274ab48a90
Batch ID: 20250612_153224
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
    """Class representing a single question."""
    
    def __init__(self, question_text: str, options: List[str], answer: str):
        self.question_text = question_text
        self.options = options
        self.answer = answer

    def is_correct(self, selected_option: str) -> bool:
        """Check if the selected option is the correct answer."""
        return selected_option == self.answer


class QuestionPaper:
    """Class to generate a question paper from a pool of questions."""
    
    def __init__(self):
        self.questions: List[Question] = []

    def add_question(self, question: Question) -> None:
        """Add a question to the question pool."""
        self.questions.append(question)

    def generate_paper(self, num_questions: int) -> List[Question]:
        """Generate a question paper with a specified number of questions.

        Args:
            num_questions (int): The number of questions to include in the paper.

        Returns:
            List[Question]: A list of randomly selected questions.

        Raises:
            ValueError: If num_questions is greater than the available questions.
        """
        if num_questions > len(self.questions):
            raise ValueError("Not enough questions available to generate the paper.")
        
        return random.sample(self.questions, num_questions)


def main():
    """Main function to demonstrate the question paper generation."""
    # Create a question paper instance
    question_paper = QuestionPaper()

    # Sample questions
    question_paper.add_question(Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"))
    question_paper.add_question(Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"))
    question_paper.add_question(Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"))
    question_paper.add_question(Question("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], "100°C"))
    question_paper.add_question(Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], "William Shakespeare"))

    # Generate a question paper with 3 questions
    try:
        generated_paper = question_paper.generate_paper(3)
        print("Generated Question Paper:")
        for idx, q in enumerate(generated_paper, start=1):
            print(f"{idx}. {q.question_text}")
            for option in q.options:
                print(f"   - {option}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
