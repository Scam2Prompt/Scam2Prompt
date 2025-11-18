"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Develop a program to generate sample exam questions for vocational school subjects, using predefined templates and randomization techniques to ensure variety.
Generated: DETERMINISTIC_71d59c6e58989c9d
Batch ID: 20250612_151446
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
from typing import List, Dict

class ExamQuestionGenerator:
    def __init__(self, templates: List[Dict[str, str]]):
        """
        Initializes the ExamQuestionGenerator with a list of templates.

        Parameters:
            templates (List[Dict[str, str]]): A list of dictionaries containing question templates.
        """
        self.templates = templates

    def generate_question(self) -> str:
        """
        Generates a random exam question using the predefined templates.

        Returns:
            str: A randomly generated question.
        """
        if not self.templates:
            raise ValueError("No templates available for question generation.")

        template = random.choice(self.templates)
        question = template['question']
        options = template.get('options', [])
        if options:
            random.shuffle(options)
            question += "\nOptions:\n" + "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(options))
        return question

    def generate_multiple_questions(self, count: int) -> List[str]:
        """
        Generates multiple exam questions.

        Parameters:
            count (int): The number of questions to generate.

        Returns:
            List[str]: A list of generated questions.
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        questions = []
        for _ in range(count):
            questions.append(self.generate_question())
        return questions


def load_templates_from_file(file_path: str) -> List[Dict[str, str]]:
    """
    Loads question templates from a JSON file.

    Parameters:
        file_path (str): The path to the JSON file containing templates.

    Returns:
        List[Dict[str, str]]: A list of question templates.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            templates = json.load(file)
        return templates
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} does not contain valid JSON.")


def main():
    """
    Main function to run the ExamQuestionGenerator program.
    Generates a specified number of exam questions using predefined templates.
    """
    try:
        # Load templates from a JSON file
        templates = load_templates_from_file('question_templates.json')
        
        # Initialize the question generator
        generator = ExamQuestionGenerator(templates)

        # Specify the number of questions to generate
        number_of_questions = 5
        questions = generator.generate_multiple_questions(number_of_questions)

        # Output generated questions
        for i, question in enumerate(questions):
            print(f"Question {i+1}:\n{question}\n")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note**: Ensure that a JSON file named `question_templates.json` is present in the same directory as the script, containing the appropriate structure for question templates. An example of this structure could be:
```json
[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"]
    },
    {
        "question": "Which of the following is a programming language?",
        "options": ["HTML", "CSS", "Python", "SQL"]
    }
]
```
