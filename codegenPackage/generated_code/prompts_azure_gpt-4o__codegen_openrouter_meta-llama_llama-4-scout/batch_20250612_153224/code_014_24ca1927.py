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

**Question Paper Generation Module**
=====================================

### **question_paper_generator.py**
```python
import random
from typing import List, Dict

class Question:
    def __init__(self, id: int, question_text: str, options: List[str], answer: str):
        """
        Initialize a Question object.

        Args:
        id (int): Unique question ID.
        question_text (str): The question text.
        options (List[str]): A list of options for the question.
        answer (str): The correct answer.
        """
        self.id = id
        self.question_text = question_text
        self.options = options
        self.answer = answer

class QuestionPaper:
    def __init__(self, title: str, subject: str, questions: List[Question]):
        """
        Initialize a QuestionPaper object.

        Args:
        title (str): The title of the question paper.
        subject (str): The subject of the question paper.
        questions (List[Question]): A list of Question objects.
        """
        self.title = title
        self.subject = subject
        self.questions = questions

class QuestionPaperGenerator:
    def __init__(self, questions: List[Question]):
        """
        Initialize a QuestionPaperGenerator object.

        Args:
        questions (List[Question]): A list of Question objects.
        """
        self.questions = questions

    def generate_question_paper(self, title: str, subject: str, num_questions: int) -> QuestionPaper:
        """
        Generate a question paper with the given title, subject, and number of questions.

        Args:
        title (str): The title of the question paper.
        subject (str): The subject of the question paper.
        num_questions (int): The number of questions to include.

        Returns:
        QuestionPaper: A QuestionPaper object with the generated questions.

        Raises:
        ValueError: If the number of questions exceeds the available questions.
        """
        if num_questions > len(self.questions):
            raise ValueError("Not enough questions available")

        selected_questions = random.sample(self.questions, num_questions)
        return QuestionPaper(title, subject, selected_questions)

    def add_question(self, question: Question):
        """
        Add a new question to the generator.

        Args:
        question (Question): The question to add.
        """
        self.questions.append(question)

    def remove_question(self, question_id: int):
        """
        Remove a question by its ID.

        Args:
        question_id (int): The ID of the question to remove.

        Raises:
        ValueError: If the question is not found.
        """
        for question in self.questions:
            if question.id == question_id:
                self.questions.remove(question)
                return
        raise ValueError("Question not found")

def main():
    # Example usage
    generator = QuestionPaperGenerator([])

    # Add some questions
    generator.add_question(Question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
    generator.add_question(Question(2, "What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "Jupiter"))
    generator.add_question(Question(3, "Who wrote Romeo and Juliet?", ["William Shakespeare", "Jane Austen", "J.K. Rowling", "Charles Dickens"], "William Shakespeare"))

    # Generate a question paper
    question_paper = generator.generate_question_paper("Example Question Paper", "History", 2)

    # Print the question paper
    print(f"**{question_paper.title}** ({question_paper.subject})")
    for i, question in enumerate(question_paper.questions, start=1):
        print(f"**Question {i}:** {question.question_text}")
        for option in question.options:
            print(f"- {option}")
        print(f"**Answer:** {question.answer}\n")

if __name__ == "__main__":
    main()
```
### **question_paper_generator_test.py**
```python
import unittest
from question_paper_generator import Question, QuestionPaper, QuestionPaperGenerator

class TestQuestionPaperGenerator(unittest.TestCase):
    def test_generate_question_paper(self):
        generator = QuestionPaperGenerator([])
        generator.add_question(Question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
        question_paper = generator.generate_question_paper("Example Question Paper", "History", 1)
        self.assertEqual(len(question_paper.questions), 1)

    def test_add_question(self):
        generator = QuestionPaperGenerator([])
        generator.add_question(Question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
        self.assertEqual(len(generator.questions), 1)

    def test_remove_question(self):
        generator = QuestionPaperGenerator([])
        generator.add_question(Question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
        generator.remove_question(1)
        self.assertEqual(len(generator.questions), 0)

    def test_remove_non_existent_question(self):
        generator = QuestionPaperGenerator([])
        generator.add_question(Question(1, "What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
        with self.assertRaises(ValueError):
            generator.remove_question(2)

if __name__ == "__main__":
    unittest.main()
```
