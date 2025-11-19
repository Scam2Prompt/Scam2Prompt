"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Develop a program to generate sample exam questions for vocational school subjects, using predefined templates and randomization techniques to ensure variety.
Generated: DETERMINISTIC_71d59c6e58989c9d
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class ExamQuestionGenerator:
    def __init__(self, templates_file):
        """
        Initializes the ExamQuestionGenerator with a set of templates.

        :param templates_file: Path to the JSON file containing question templates.
        """
        self.templates = self.load_templates(templates_file)

    def load_templates(self, templates_file):
        """
        Loads question templates from a JSON file.

        :param templates_file: Path to the JSON file.
        :return: List of question templates.
        """
        try:
            with open(templates_file, 'r') as file:
                templates = json.load(file)
                return templates
        except FileNotFoundError:
            raise Exception(f"Templates file not found: {templates_file}")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON from the file: {templates_file}")

    def generate_question(self):
        """
        Generates a random exam question based on the loaded templates.

        :return: A string containing a randomly generated question.
        """
        if not self.templates:
            raise Exception("No templates available to generate questions.")

        template = random.choice(self.templates)
        question = self.fill_template(template)
        return question

    def fill_template(self, template):
        """
        Fills in the template with random values.

        :param template: A dictionary containing the template structure.
        :return: A filled question string.
        """
        question = template['question']
        for placeholder, value in template['variables'].items():
            question = question.replace(f"{{{{ {placeholder} }}}}", random.choice(value))
        return question

def main():
    """
    Main function to run the exam question generator.
    """
    templates_file = 'question_templates.json'  # Path to the JSON file with templates
    generator = ExamQuestionGenerator(templates_file)

    try:
        for _ in range(5):  # Generate 5 random questions
            print(generator.generate_question())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Sample JSON Template (question_templates.json):**
```json
[
    {
        "question": "What is the capital of {{{{ country }}}}?",
        "variables": {
            "country": ["France", "Germany", "Italy", "Spain"]
        }
    },
    {
        "question": "Explain the process of {{{{ process }}}}.",
        "variables": {
            "process": ["photosynthesis", "combustion", "electrolysis"]
        }
    },
    {
        "question": "What are the main components of a {{{{ system }}}}?",
        "variables": {
            "system": ["computer", "ecosystem", "electrical circuit"]
        }
    }
]
```
