"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Write code to implement a scoring system for ENEM mock exams based on TRI, ensuring accurate predictions of student performance, as described in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_dfbf0cd1ee0b3ac3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import math

class TRIScoringSystem:
    """
    A class to calculate scores for ENEM mock exams based on Item Response Theory (IRT) models.

    Attributes:
        difficulty_levels (list): List of difficulty levels (b) for each question.
        discrimination_levels (list): List of discrimination factors (a) for each question.
        guessing_factors (list): List of guessing probabilities (c) for each question.
    """

    def __init__(self, difficulties, discriminations, guessing_factors):
        """
        Initializes the TRIScoringSystem with the given parameters.
        Parameters:
            difficulties (list): Difficulty levels (b) for each question.
            discriminations (list): Discrimination factors (a) for each question.
            guessing_factors (list): Guessing probabilities (c) for each question.
        """
        if not (len(difficulties) == len(discriminations) == len(guessing_factors)):
            raise ValueError("All input lists must have the same length.")
        
        self.difficulty_levels = np.array(difficulties)
        self.discrimination_levels = np.array(discriminations)
        self.guessing_factors = np.array(guessing_factors)

    def probability_of_correct_response(self, theta, question_index):
        """
        Calculates the probability of a correct response for a given student (theta) to a specific question.
        Parameters:
            theta (float): The ability level of the student.
            question_index (int): Index of the question in the parameter lists.
        Returns:
            float: Probability of the student correctly answering the question.
        """
        a = self.discrimination_levels[question_index]
        b = self.difficulty_levels[question_index]
        c = self.guessing_factors[question_index]

        # Logistic model for IRT (three-parameter model)
        p = c + (1 - c) / (1 + math.exp(-a * (theta - b)))
        return p

    def calculate_score(self, responses, theta):
        """
        Calculates the total score for a student based on their responses and ability level (theta).
        Parameters:
            responses (list): List of binary responses (1 for correct, 0 for incorrect).
            theta (float): The ability level of the student.
        Returns:
            float: The calculated score for the student.
        """
        if len(responses) != len(self.difficulty_levels):
            raise ValueError("The number of responses must match the number of questions.")

        score = 0
        for i, response in enumerate(responses):
            p = self.probability_of_correct_response(theta, i)
            if response == 1:
                score += math.log(p)  # Log-likelihood for correct response
            elif response == 0:
                score += math.log(1 - p)  # Log-likelihood for incorrect response
            else:
                raise ValueError("Responses must be binary (0 or 1).")
        
        return score

# Example usage
if __name__ == "__main__":
    try:
        # Parameters for sample questions (difficulty, discrimination, guessing factor)
        difficulties = [0.5, 1.0, -0.5, 0.8]
        discriminations = [1.2, 0.8, 1.5, 1.0]
        guessing_factors = [0.25, 0.2, 0.3, 0.1]

        scoring_system = TRIScoringSystem(difficulties, discriminations, guessing_factors)

        # Mock responses and student ability level
        responses = [1, 0, 1, 1]  # 1 for correct, 0 for incorrect
        student_theta = 0.7  # Ability level

        # Calculate score
        score = scoring_system.calculate_score(responses, student_theta)
        print(f"Student's score: {score:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
