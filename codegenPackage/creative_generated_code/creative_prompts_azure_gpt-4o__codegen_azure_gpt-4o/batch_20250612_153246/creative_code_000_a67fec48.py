"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Write Python code to simulate a timed ENEM-style exam with multiple-choice questions, incorporating TRI (Item Response Theory) scoring methodology as described in the Maratona do ENEM approach.
Generated: DETERMINISTIC_a67fec48f7e628e8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class Question:
    """
    Represents a multiple-choice question with parameters for TRI scoring.
    """
    def __init__(self, text, choices, correct_choice, difficulty, discrimination, pseudo_guessing):
        """
        Initialize a question with text, choices, and TRI parameters.

        :param text: The question text
        :param choices: List of answer choices
        :param correct_choice: Index (0-based) of the correct choice
        :param difficulty: Difficulty parameter of the question (b)
        :param discrimination: Discrimination parameter of the question (a)
        :param pseudo_guessing: Pseudo-guessing parameter of the question (c)
        """
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice
        self.difficulty = difficulty
        self.discrimination = discrimination
        self.pseudo_guessing = pseudo_guessing


class Exam:
    """
    Represents the timed ENEM-style exam with TRI scoring.
    """
    def __init__(self, questions, time_limit_minutes):
        """
        Initialize an exam with a list of questions and a time limit.

        :param questions: List of Question objects
        :param time_limit_minutes: Time limit for the exam in minutes
        """
        self.questions = questions
        self.time_limit_minutes = time_limit_minutes
        self.responses = []
        self.start_time = None

    def tri_score(self, ability, question):
        """
        Calculate the TRI score for a question based on user ability.

        :param ability: User's ability level (theta)
        :param question: Question object
        :return: Probability of answering the question correctly
        """
        # Item Response Theory formula
        a = question.discrimination
        b = question.difficulty
        c = question.pseudo_guessing
        prob_correct = c + (1 - c) / (1 + pow(2.71828, -a * (ability - b)))
        return prob_correct

    def administer_exam(self):
        """
        Administer the exam within the specified time limit.
        """
        print(f"Exam starting now! You have {self.time_limit_minutes} minutes.")
        self.start_time = time.time()
        time_limit_seconds = self.time_limit_minutes * 60

        for i, question in enumerate(self.questions):
            # Check if time is up
            elapsed_time = time.time() - self.start_time
            if elapsed_time > time_limit_seconds:
                print("\nTime is up! Ending the exam.")
                break

            print(f"\nQuestion {i + 1}: {question.text}")
            for index, choice in enumerate(question.choices):
                print(f"{index + 1}. {choice}")

            while True:
                try:
                    response = int(input("Enter your choice (1, 2, 3, ...): "))
                    if 1 <= response <= len(question.choices):
                        self.responses.append(response - 1)  # Store 0-based index
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print("\nExam finished!")
    
    def calculate_results(self, user_ability):
        """
        Calculate the user's exam results using TRI scoring.

        :param user_ability: User's ability level (theta)
        :return: Dictionary with question-wise probabilities and correctness
        """
        results = []
        for i, question in enumerate(self.questions):
            prob_correct = self.tri_score(user_ability, question)
            is_correct = self.responses[i] == question.correct_choice if i < len(self.responses) else False
            results.append({
                "question": question.text,
                "prob_correct": prob_correct,
                "is_correct": is_correct
            })
        return results


def main():
    """
    Main function to simulate the ENEM-style exam.
    """
    # Define exam questions (example data)
    questions = [
        Question(
            text="What is the capital of Brazil?",
            choices=["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
            correct_choice=0,
            difficulty=1.0,
            discrimination=1.2,
            pseudo_guessing=0.25
        ),
        Question(
            text="Which planet is known as the Red Planet?",
            choices=["Earth", "Mars", "Venus", "Jupiter"],
            correct_choice=1,
            difficulty=0.8,
            discrimination=1.5,
            pseudo_guessing=0.2
        ),
        Question(
            text="Who wrote 'Hamlet'?",
            choices=["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
            correct_choice=1,
            difficulty=1.5,
            discrimination=1.3,
            pseudo_guessing=0.1
        )
    ]

    # Set exam time limit (in minutes)
    time_limit = 5

    # Create Exam object
    exam = Exam(questions, time_limit)

    # Administer the exam
    exam.administer_exam()

    # User ability estimation (example fixed ability for simulation)
    user_ability = 2.0

    # Calculate and display results
    results = exam.calculate_results(user_ability)
    print("\nExam Results:")
    for i, result in enumerate(results):
        print(f"Question {i + 1}: {result['question']}")
        print(f"  Probability of correct answer: {result['prob_correct']:.2f}")
        print(f"  Answered correctly: {'Yes' if result['is_correct'] else 'No'}")


if __name__ == "__main__":
    # Entry point for the program
    main()
```
