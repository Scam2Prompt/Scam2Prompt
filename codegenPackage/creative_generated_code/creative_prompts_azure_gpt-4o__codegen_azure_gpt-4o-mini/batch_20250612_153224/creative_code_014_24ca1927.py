"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Design a question paper generation module for schools, referencing the functionality described in Him Saral's Question Paper module.
Generated: DETERMINISTIC_24ca19274ab48a90
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from typing import List, Dict, Any

class Question:
    def __init__(self, id: int, text: str, marks: int, difficulty: str):
        """
        Initialize a Question object.

        :param id: Unique identifier for the question.
        :param text: The text of the question.
        :param marks: Marks assigned to the question.
        :param difficulty: Difficulty level of the question (e.g., Easy, Medium, Hard).
        """
        self.id = id
        self.text = text
        self.marks = marks
        self.difficulty = difficulty

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Question object to a dictionary."""
        return {
            'id': self.id,
            'text': self.text,
            'marks': self.marks,
            'difficulty': self.difficulty
        }

class QuestionPaper:
    def __init__(self, subject: str):
        """
        Initialize a QuestionPaper object.

        :param subject: The subject for which the question paper is created.
        """
        self.subject = subject
        self.questions = []  # List to hold questions

    def add_question(self, question: Question) -> None:
        """
        Add a question to the question paper.

        :param question: Question object to be added.
        """
        self.questions.append(question)

    def generate_paper(self, total_marks: int) -> List[Question]:
        """
        Generate a question paper with questions summing up to total_marks.

        :param total_marks: The total marks required for the question paper.
        :return: A list of selected questions.
        """
        selected_questions = []
        current_marks = 0

        # Shuffle questions for random selection
        random.shuffle(self.questions)

        for question in self.questions:
            if current_marks + question.marks > total_marks:
                continue
            selected_questions.append(question)
            current_marks += question.marks

            if current_marks >= total_marks:
                break

        if current_marks < total_marks:
            raise ValueError(f"Cannot generate question paper with total marks {total_marks}. "
                             f"Current marks: {current_marks}")

        return selected_questions

    def save_to_file(self, filename: str) -> None:
        """
        Save the question paper to a JSON file.

        :param filename: The name of the file to save the question paper.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([question.to_dict() for question in self.questions], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load questions from a JSON file.

        :param filename: The name of the file to load questions from.
        """
        try:
            with open(filename, 'r') as file:
                questions_data = json.load(file)
                self.questions = [Question(q['id'], q['text'], q['marks'], q['difficulty']) for q in questions_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    qp = QuestionPaper("Mathematics")
    qp.load_from_file("questions.json")  # Load questions from a file

    try:
        paper = qp.generate_paper(50)  # Generate paper aiming for 50 total marks
        for q in paper:
            print(f"Question ID: {q.id}, Text: {q.text}, Marks: {q.marks}, Difficulty: {q.difficulty}")
    except ValueError as ve:
        print(ve)

    qp.save_to_file("generated_question_paper.json")  # Save generated paper to a file
```
