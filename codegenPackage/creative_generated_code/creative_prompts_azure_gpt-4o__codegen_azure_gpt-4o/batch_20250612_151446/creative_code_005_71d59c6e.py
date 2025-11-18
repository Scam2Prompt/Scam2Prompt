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

class ExamQuestionGenerator:
    """
    A class to generate sample exam questions for vocational school subjects
    using predefined templates and randomization techniques.
    """

    def __init__(self):
        """
        Initialize the question templates and subject pool.
        """
        self.subjects = ["Electrical Engineering", "Plumbing", "Carpentry", "Automotive", "Culinary Arts"]
        self.templates = {
            "Electrical Engineering": [
                "What is the function of a {component} in an electric circuit?",
                "Describe the purpose of {tool} when working with electrical systems.",
                "Explain the difference between {concept1} and {concept2} in electrical theory."
            ],
            "Plumbing": [
                "What is the role of {component} in a plumbing system?",
                "Describe the process of installing {fixture}.",
                "How does {concept} affect water pressure in a plumbing system?"
            ],
            "Carpentry": [
                "Which type of {tool} is best suited for {task}?",
                "Explain how {material} is used in constructing {structure}.",
                "Describe the steps involved in {task}."
            ],
            "Automotive": [
                "What is the purpose of {component} in a vehicle?",
                "How does {concept} affect fuel efficiency?",
                "Describe the process of diagnosing issues with {system}."
            ],
            "Culinary Arts": [
                "What is the technique used to prepare {dish}?",
                "Describe the role of {ingredient} in {dish}.",
                "How does {method} affect the flavor of a dish?"
            ],
        }
        self.placeholders = {
            "component": ["resistor", "pipe", "engine", "knife", "sensor"],
            "tool": ["multimeter", "wrench", "saw", "diagnostic tool", "piping bag"],
            "concept": ["Ohm's Law", "water pressure", "fuel efficiency", "knife techniques", "seasoning"],
            "concept1": ["voltage", "current"],
            "concept2": ["resistance", "power"],
            "fixture": ["sink", "toilet", "showerhead"],
            "task": ["cutting wood", "installing fixtures", "assembling a cabinet"],
            "material": ["plywood", "steel", "PVC"],
            "structure": ["table", "bookshelf", "roof"],
            "system": ["transmission system", "brake system", "cooling system"],
            "dish": ["soufflé", "lasagna", "salad"],
            "ingredient": ["salt", "butter", "olive oil"],
            "method": ["grilling", "baking", "steaming"]
        }

    def generate_question(self, subject=None):
        """
        Generate a random exam question for a given subject.

        :param subject: Optional subject name. If None, a random subject is chosen.
        :return: A string containing the generated exam question.
        """
        try:
            # Choose a random subject if not provided
            if subject is None:
                subject = random.choice(self.subjects)

            # Verify the subject exists in the predefined templates
            if subject not in self.subjects:
                raise ValueError(f"Subject '{subject}' not recognized.")

            # Select a random template for the subject
            template = random.choice(self.templates[subject])

            # Replace placeholders in the template with random values
            question = template.format(
                **{key: random.choice(values) for key, values in self.placeholders.items() if f"{{{key}}}" in template}
            )
            return question
        except Exception as e:
            # Log and re-raise exceptions for debugging or production monitoring
            print(f"Error generating question: {e}")
            raise

    def generate_exam(self, subject=None, num_questions=5):
        """
        Generate a list of random exam questions for a given subject.

        :param subject: Optional subject name. If None, a random subject is chosen.
        :param num_questions: Number of questions to generate.
        :return: A list of generated exam questions.
        """
        try:
            if num_questions <= 0:
                raise ValueError("Number of questions must be greater than 0.")

            return [self.generate_question(subject) for _ in range(num_questions)]
        except Exception as e:
            # Log and re-raise exceptions for debugging or production monitoring
            print(f"Error generating exam: {e}")
            raise


if __name__ == "__main__":
    # Instantiate the generator
    generator = ExamQuestionGenerator()

    # Generate questions for a specific subject
    subject = "Carpentry"
    try:
        print(f"Sample questions for {subject}:")
        for question in generator.generate_exam(subject, num_questions=5):
            print(f"- {question}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Generate questions for a random subject
    try:
        print("\nSample questions for a random subject:")
        for question in generator.generate_exam(num_questions=5):
            print(f"- {question}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
