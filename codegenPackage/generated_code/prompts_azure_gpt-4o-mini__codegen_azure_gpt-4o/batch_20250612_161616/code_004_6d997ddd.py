"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I create a nutritional education program for schools that incorporates the guidelines provided by It's Cool Foods for promoting healthy eating among children?
Generated: DETERMINISTIC_6d997ddd58d34489
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Nutritional Education Program for Schools

This program incorporates guidelines provided by It's Cool Foods to promote healthy eating among children.
It includes interactive lessons, quizzes, and meal planning activities to educate students about nutrition.
"""

import json
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NutritionalEducationProgram:
    """
    A class to represent the nutritional education program.
    """

    def __init__(self, guidelines_file):
        """
        Initialize the program with guidelines from It's Cool Foods.

        :param guidelines_file: Path to the JSON file containing nutritional guidelines.
        """
        self.guidelines = self.load_guidelines(guidelines_file)
        self.lessons = []
        self.quizzes = []
        self.meal_plans = []

    def load_guidelines(self, file_path):
        """
        Load nutritional guidelines from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing guidelines.
        """
        try:
            with open(file_path, 'r') as file:
                guidelines = json.load(file)
                logging.info("Guidelines successfully loaded.")
                return guidelines
        except FileNotFoundError:
            logging.error("Guidelines file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON file.")
            raise

    def create_lessons(self):
        """
        Create interactive lessons based on the guidelines.
        """
        try:
            for topic in self.guidelines.get("topics", []):
                lesson = {
                    "title": topic["title"],
                    "content": topic["content"],
                    "activity": topic.get("activity", "Discussion")
                }
                self.lessons.append(lesson)
            logging.info("Lessons successfully created.")
        except KeyError as e:
            logging.error(f"Missing key in guidelines: {e}")
            raise

    def create_quizzes(self):
        """
        Create quizzes to test students' knowledge of healthy eating.
        """
        try:
            for quiz in self.guidelines.get("quizzes", []):
                self.quizzes.append(quiz)
            logging.info("Quizzes successfully created.")
        except KeyError as e:
            logging.error(f"Missing key in guidelines: {e}")
            raise

    def create_meal_plans(self):
        """
        Create sample meal plans for students based on the guidelines.
        """
        try:
            for plan in self.guidelines.get("meal_plans", []):
                self.meal_plans.append(plan)
            logging.info("Meal plans successfully created.")
        except KeyError as e:
            logging.error(f"Missing key in guidelines: {e}")
            raise

    def display_program(self):
        """
        Display the complete program including lessons, quizzes, and meal plans.
        """
        print("\nNutritional Education Program")
        print("\nLessons:")
        for lesson in self.lessons:
            print(f"- {lesson['title']}: {lesson['content']} (Activity: {lesson['activity']})")

        print("\nQuizzes:")
        for quiz in self.quizzes:
            print(f"- {quiz['question']} (Options: {', '.join(quiz['options'])})")

        print("\nMeal Plans:")
        for plan in self.meal_plans:
            print(f"- {plan['name']}: {', '.join(plan['items'])}")

def main():
    """
    Main function to run the nutritional education program.
    """
    try:
        # Path to the JSON file containing guidelines
        guidelines_file = "its_cool_foods_guidelines.json"

        # Initialize the program
        program = NutritionalEducationProgram(guidelines_file)

        # Create lessons, quizzes, and meal plans
        program.create_lessons()
        program.create_quizzes()
        program.create_meal_plans()

        # Display the program
        program.display_program()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
