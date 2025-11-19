"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Develop a library for creating interactive environmental education modules, including features for gamification and progress tracking.
Generated: DETERMINISTIC_92dc30fae9f94590
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_education.py

class Module:
    """
    Represents an educational module with gamification features.
    """

    def __init__(self, title, description):
        """
        Initializes a new educational module.

        :param title: Title of the module
        :param description: Description of the module
        """
        self.title = title
        self.description = description
        self.questions = []
        self.progress = 0

    def add_question(self, question, correct_answer):
        """
        Adds a question to the module.

        :param question: The question text
        :param correct_answer: The correct answer for the question
        """
        self.questions.append({'question': question, 'correct_answer': correct_answer, 'user_answer': None})

    def answer_question(self, question_index, user_answer):
        """
        Records the user's answer to a question.

        :param question_index: Index of the question in the module
        :param user_answer: The user's answer
        """
        try:
            if question_index < 0 or question_index >= len(self.questions):
                raise IndexError("Question index out of range.")
            self.questions[question_index]['user_answer'] = user_answer
            if user_answer == self.questions[question_index]['correct_answer']:
                self.progress += 1
        except IndexError as e:
            print(f"Error: {e}")

    def get_progress(self):
        """
        Returns the user's progress as a percentage.

        :return: Progress percentage
        """
        if not self.questions:
            return 0
        return (self.progress / len(self.questions)) * 100

    def get_results(self):
        """
        Returns the results of the module including questions and user answers.

        :return: List of questions with user answers
        """
        return [{'question': q['question'], 'user_answer': q['user_answer'], 'correct_answer': q['correct_answer']}
                for q in self.questions]


class User:
    """
    Represents a user interacting with the educational modules.
    """

    def __init__(self, username):
        """
        Initializes a new user.

        :param username: The username of the user
        """
        self.username = username
        self.modules_completed = []

    def complete_module(self, module):
        """
        Marks a module as completed by the user.

        :param module: The module to be completed
        """
        self.modules_completed.append(module.title)

    def get_completed_modules(self):
        """
        Returns a list of completed modules.

        :return: List of completed module titles
        """
        return self.modules_completed


# Example usage
if __name__ == "__main__":
    # Create a new educational module
    module = Module("Climate Change Awareness", "Learn about the causes and effects of climate change.")

    # Add questions to the module
    module.add_question("What is the greenhouse effect?", "A natural process that warms the Earth.")
    module.add_question("What gas is primarily responsible for climate change?", "Carbon dioxide")

    # Create a user
    user = User("student123")

    # User answers questions
    module.answer_question(0, "A natural process that warms the Earth.")
    module.answer_question(1, "Carbon dioxide")

    # User completes the module
    user.complete_module(module)

    # Display progress and results
    print(f"Progress: {module.get_progress()}%")
    print("Results:", module.get_results())
    print("Completed Modules:", user.get_completed_modules())
```
