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

class QuestionPaperGenerator:
    """
    A class for generating question papers for schools.

    Attributes:
        question_bank (list): A list of questions from which to generate papers.
    """
    def __init__(self, question_bank_path):
        """
        Initializes the QuestionPaperGenerator with a question bank.

        Args:
            question_bank_path (str): Path to the JSON file containing the question bank.
        """
        try:
            with open(question_bank_path, 'r') as file:
                self.question_bank = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Question bank file not found.")
        except json.JSONDecodeError:
            raise ValueError("Question bank file is not a valid JSON.")

    def generate_question_paper(self, num_questions, difficulty_levels):
        """
        Generates a question paper based on the number of questions and difficulty levels.

        Args:
            num_questions (int): Total number of questions in the paper.
            difficulty_levels (dict): Number of questions required for each difficulty level (e.g., {'easy': 5, 'medium': 3, 'hard': 2}).

        Returns:
            list: A list of questions representing the generated question paper.
        """
        paper = []

        try:
            # Ensure the number of requested questions matches the total questions
            if sum(difficulty_levels.values()) != num_questions:
                raise ValueError("The sum of difficulty levels does not match the total number of questions.")

            for level, count in difficulty_levels.items():
                # Filter questions by difficulty level
                questions_by_level = [q for q in self.question_bank if q['difficulty'] == level]

                # Ensure there are enough questions for the requested difficulty level
                if len(questions_by_level) < count:
                    raise ValueError(f"Not enough questions available for difficulty level: {level}")

                # Randomly select 'count' number of questions for the current difficulty level
                paper += random.sample(questions_by_level, count)

            return paper
        except ValueError as ve:
            print(f"Error: {ve}")
            return []

    def save_question_paper(self, paper, output_path):
        """
        Saves the generated question paper to a JSON file.

        Args:
            paper (list): The generated question paper.
            output_path (str): Path to save the question paper.
        """
        try:
            with open(output_path, 'w') as file:
                json.dump(paper, file, indent=4)
            print(f"Question paper saved successfully at {output_path}")
        except Exception as e:
            print(f"Error saving question paper: {e}")

# Example Usage
if __name__ == "__main__":
    # Path to the question bank JSON file
    question_bank_path = "question_bank.json"
    output_path = "generated_question_paper.json"

    # Create an instance of the generator
    generator = QuestionPaperGenerator(question_bank_path)

    # Define criteria for question paper generation
    num_questions = 10
    difficulty_levels = {'easy': 4, 'medium': 4, 'hard': 2}

    # Generate the question paper
    question_paper = generator.generate_question_paper(num_questions, difficulty_levels)

    if question_paper:
        # Save the generated question paper
        generator.save_question_paper(question_paper, output_path)
```

**Note:** Ensure that `question_bank.json` exists in the same directory as the script or update the file path accordingly. It should contain a list of questions, where each question is a dictionary with the following structure:
```json
[
    {"question": "What is 2 + 2?", "difficulty": "easy"},
    {"question": "Solve x^2 + 5x + 6 = 0.", "difficulty": "medium"},
    {"question": "Prove Fermat's Last Theorem.", "difficulty": "hard"}
]
```
