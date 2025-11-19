"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write Python code to simulate a timed ENEM-style exam with multiple-choice questions, incorporating TRI (Item Response Theory) scoring methodology as described in the Maratona do ENEM approach.
Generated: DETERMINISTIC_a67fec48f7e628e8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict

class Question:
    """Represents a multiple-choice question."""
    
    def __init__(self, question: str, options: List[str], correct_answer: int, difficulty: float, discrimination: float):
        """
        Initializes a Question object.

        Args:
        - question (str): The question text.
        - options (List[str]): A list of possible answers.
        - correct_answer (int): The index of the correct answer in the options list.
        - difficulty (float): The difficulty parameter of the question (b in TRI).
        - discrimination (float): The discrimination parameter of the question (a in TRI).
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.discrimination = discrimination

class Exam:
    """Simulates a timed ENEM-style exam."""
    
    def __init__(self, questions: List[Question], time_limit: int):
        """
        Initializes an Exam object.

        Args:
        - questions (List[Question]): A list of Question objects.
        - time_limit (int): The time limit for the exam in minutes.
        """
        self.questions = questions
        self.time_limit = time_limit * 60  # Convert minutes to seconds

    def administer_exam(self) -> Dict[str, float]:
        """
        Administers the exam and returns the results.

        Returns:
        - A dictionary with the student's score and response times.
        """
        score = 0
        response_times = {}
        start_time = time.time()

        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {question.question}")
            for j, option in enumerate(question.options):
                print(f"{j+1}. {option}")

            while True:
                try:
                    response = int(input("Enter the number of your answer: ")) - 1
                    if response < 0 or response >= len(question.options):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid response. Please enter a valid number.")

            response_time = time.time()
            if response == question.correct_answer:
                score += self.tri_score(question, response)
            response_times[f"Question {i+1}"] = response_time - start_time
            start_time = time.time()

            if time.time() - start_time > self.time_limit:
                print("\nTime's up!")
                break

        return {"score": score, "response_times": response_times}

    @staticmethod
    def tri_score(question: Question, response: int) -> float:
        """
        Calculates the TRI score for a given question and response.

        Args:
        - question (Question): The Question object.
        - response (int): The student's response.

        Returns:
        - The TRI score.
        """
        # Simulate a latent trait (theta) for the student
        theta = random.normalvariate(0, 1)

        # Calculate the probability of a correct response using the 2PL model
        probability = 1 / (1 + pow(2.71828, -question.discrimination * (theta - question.difficulty)))

        # If the response is correct, add the probability to the score
        if response == question.correct_answer:
            return probability
        else:
            return 0


# Example usage
if __name__ == "__main__":
    questions = [
        Question("What is the capital of Brazil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"], 2, 0.5, 1.0),
        Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], 2, 0.3, 1.2),
        Question("Who wrote 'To Kill a Mockingbird'?", ["F. Scott Fitzgerald", "Harper Lee", "Jane Austen", "J.K. Rowling"], 1, 0.7, 0.8),
    ]

    exam = Exam(questions, 10)  # 10-minute time limit
    results = exam.administer_exam()
    print(f"\nFinal Score: {results['score']:.2f}")
    print("Response Times:")
    for question, response_time in results["response_times"].items():
        print(f"{question}: {response_time:.2f} seconds")
```
