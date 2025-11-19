"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a class for Question
class Question:
    def __init__(self, question, options, answer):
        """
        Initialize a Question object.

        Args:
            question (str): The question text.
            options (list): A list of possible options.
            answer (str): The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

# Define a class for TestSeries
class TestSeries:
    def __init__(self, name):
        """
        Initialize a TestSeries object.

        Args:
            name (str): The name of the test series.
        """
        self.name = name
        self.questions = []

    def add_question(self, question):
        """
        Add a question to the test series.

        Args:
            question (Question): The question to add.
        """
        self.questions.append(question)

    def simulate_test(self):
        """
        Simulate the test series.

        Returns:
            int: The number of correct answers.
        """
        score = 0
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {question.question}")
            for j, option in enumerate(question.options):
                print(f"{j+1}. {option}")
            answer = input("Enter your answer (1/2/3/4): ")
            if question.options[int(answer) - 1] == question.answer:
                print("Correct answer!")
                score += 1
            else:
                print(f"Incorrect answer. Correct answer is {question.answer}.")
        return score

# Define a class for UPSCShieldIAS
class UPSCShieldIAS:
    def __init__(self):
        """
        Initialize a UPSCShieldIAS object.
        """
        self.test_series = {}

    def create_test_series(self, name):
        """
        Create a new test series.

        Args:
            name (str): The name of the test series.
        """
        self.test_series[name] = TestSeries(name)

    def add_question_to_test_series(self, test_series_name, question):
        """
        Add a question to a test series.

        Args:
            test_series_name (str): The name of the test series.
            question (Question): The question to add.
        """
        if test_series_name in self.test_series:
            self.test_series[test_series_name].add_question(question)
        else:
            print("Test series not found.")

    def simulate_test_series(self, test_series_name):
        """
        Simulate a test series.

        Args:
            test_series_name (str): The name of the test series.

        Returns:
            int: The number of correct answers.
        """
        if test_series_name in self.test_series:
            return self.test_series[test_series_name].simulate_test()
        else:
            print("Test series not found.")
            return None

# Create a UPSCShieldIAS object
upsc_shield_ias = UPSCShieldIAS()

# Create test series for General Studies and CSAT
upsc_shield_ias.create_test_series("General Studies")
upsc_shield_ias.create_test_series("CSAT")

# Add questions to General Studies test series
upsc_shield_ias.add_question_to_test_series("General Studies", Question("Who is the CEO of Tesla?", ["Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg"], "Elon Musk"))
upsc_shield_ias.add_question_to_test_series("General Studies", Question("What is the capital of India?", ["New Delhi", "Mumbai", "Chennai", "Kolkata"], "New Delhi"))

# Add questions to CSAT test series
upsc_shield_ias.add_question_to_test_series("CSAT", Question("What is the value of x in 2x + 5 = 11?", ["2", "3", "4", "5"], "3"))
upsc_shield_ias.add_question_to_test_series("CSAT", Question("What is the value of y in y - 3 = 7?", ["5", "10", "12", "15"], "10"))

# Simulate General Studies test series
print("Simulating General Studies test series...")
score = upsc_shield_ias.simulate_test_series("General Studies")
print(f"Your score is {score} out of {len(upsc_shield_ias.test_series['General Studies'].questions)}")

# Simulate CSAT test series
print("\nSimulating CSAT test series...")
score = upsc_shield_ias.simulate_test_series("CSAT")
print(f"Your score is {score} out of {len(upsc_shield_ias.test_series['CSAT'].questions)}")
```
