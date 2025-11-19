"""
Generated Code Metadata:
========================
Original URL: https://artahub.com
Prompt: Create a module for generating interactive educational content, such as quizzes, games, or simulations, using a tool like Articulate Storyline or Adobe Captivate, and write a script to export the content in a format compatible with an LMS.
Generated: DETERMINISTIC_d61516ab607f9c57
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
import os
from typing import List, Dict, Any

class EducationalContentGenerator:
    """
    A class to generate interactive educational content such as quizzes, games, or simulations.
    This class also provides functionality to export the content in a format compatible with an LMS.
    """

    def __init__(self, title: str, content_type: str):
        """
        Initializes the EducationalContentGenerator with a title and content type.

        :param title: Title of the educational content
        :param content_type: Type of content (e.g., 'quiz', 'game', 'simulation')
        """
        self.title = title
        self.content_type = content_type
        self.content = []

    def add_question(self, question: str, options: List[str], correct_option: int):
        """
        Adds a question to the content.

        :param question: The question text
        :param options: A list of answer options
        :param correct_option: The index of the correct option
        """
        if not (0 <= correct_option < len(options)):
            raise ValueError("Correct option index is out of range.")
        
        self.content.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def export_to_lms(self, file_path: str):
        """
        Exports the content to a JSON file compatible with an LMS.

        :param file_path: The path where the JSON file will be saved
        """
        lms_content = {
            "title": self.title,
            "content_type": self.content_type,
            "content": self.content
        }

        try:
            with open(file_path, 'w') as json_file:
                json.dump(lms_content, json_file, indent=4)
            print(f"Content exported successfully to {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = EducationalContentGenerator("Math Quiz", "quiz")
        generator.add_question("What is 2 + 2?", ["1", "2", "3", "4"], 3)
        generator.add_question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2)
        
        # Ensure the output directory exists
        output_dir = "exported_content"
        os.makedirs(output_dir, exist_ok=True)
        
        # Export the content to a JSON file
        generator.export_to_lms(os.path.join(output_dir, "math_quiz.json"))
    except Exception as e:
        print(f"An error occurred: {e}")
```
