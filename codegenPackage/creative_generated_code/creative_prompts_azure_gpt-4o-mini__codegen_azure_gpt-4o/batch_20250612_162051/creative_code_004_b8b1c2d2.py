"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: What are the steps to develop a question paper generation feature like the one in Him Saral's school software?
Generated: DETERMINISTIC_b8b1c2d2f358da66
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a question paper generation feature, following your requirements:

```python
import random
import json

class QuestionPaperGenerator:
    def __init__(self, question_bank_file):
        """
        Initializes the QuestionPaperGenerator with the provided question bank file.
        :param question_bank_file: Path to the JSON file containing the question bank.
        """
        self.question_bank_file = question_bank_file
        self.question_bank = self.load_question_bank()

    def load_question_bank(self):
        """
        Loads questions from a JSON file.
        :return: A dictionary with questions categorized by subject and type.
        """
        try:
            with open(self.question_bank_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Question bank file '{self.question_bank_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in question bank file.")

    def generate_question_paper(self, subject, num_questions, question_types=None):
        """
        Generates a question paper based on the specified criteria.
        :param subject: Subject for which the question paper is needed.
        :param num_questions: Total number of questions required in the paper.
        :param question_types: List of question types to include (optional).
        :return: A list of selected questions.
        """
        if subject not in self.question_bank:
            raise ValueError(f"Subject '{subject}' not found in question bank.")

        questions_pool = self.question_bank[subject]
        if question_types:
            # Filter questions by specified types
            questions_pool = [q for q in questions_pool if q['type'] in question_types]

        if len(questions_pool) < num_questions:
            raise ValueError("Insufficient questions available to generate the paper.")

        # Randomly select the requested number of questions
        return random.sample(questions_pool, num_questions)

    @staticmethod
    def format_question_paper(questions):
        """
        Formats the selected questions into a readable question paper format.
        :param questions: List of selected questions.
        :return: Formatted question paper as a string.
        """
        formatted_paper = "Question Paper\n"
        formatted_paper += "-" * 50 + "\n"
        for i, question in enumerate(questions, start=1):
            formatted_paper += f"{i}. {question['text']} ({question['type']})\n"
        return formatted_paper


def main():
    """
    Main function to demonstrate the question paper generation.
    """
    # Path to the JSON file containing the question bank
    question_bank_file = "question_bank.json"

    try:
        # Initialize the generator
        generator = QuestionPaperGenerator(question_bank_file)

        # Parameters for question paper generation
        subject = "Math"
        num_questions = 5
        question_types = ["MCQ", "Short Answer"]  # Optional filtering by types

        # Generate the question paper
        questions = generator.generate_question_paper(subject, num_questions, question_types)

        # Format and display the question paper
        formatted_paper = generator.format_question_paper(questions)
        print(formatted_paper)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

### Notes about the code:
1. The question bank is expected to be provided in a JSON file (`question_bank.json`) with a structure similar to:

```json
{
  "Math": [
    {"text": "What is 2+2?", "type": "MCQ"},
    {"text": "Solve for x: 3x + 2 = 11", "type": "Short Answer"},
    {"text": "What is the square root of 16?", "type": "MCQ"}
  ],
  "Science": [
    {"text": "Describe the water cycle.", "type": "Essay"},
    {"text": "What is the chemical symbol for water?", "type": "Short Answer"}
  ]
}
```

2. Proper error handling is included to account for missing files, invalid JSON structures, and insufficient questions.
