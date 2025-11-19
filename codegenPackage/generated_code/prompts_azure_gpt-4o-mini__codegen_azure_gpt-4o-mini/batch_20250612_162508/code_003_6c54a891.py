"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a function that evaluates the quality of architectural designs based on criteria mentioned by Remas Engineering Consultants, such as creativity and problem-solving.
Generated: DETERMINISTIC_6c54a891ebe62f2f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArchitecturalDesignEvaluator:
    """
    A class to evaluate the quality of architectural designs based on specified criteria.
    """

    def __init__(self, creativity: int, problem_solving: int, functionality: int, sustainability: int):
        """
        Initializes the evaluator with criteria scores.

        :param creativity: Score for creativity (0-10)
        :param problem_solving: Score for problem-solving (0-10)
        :param functionality: Score for functionality (0-10)
        :param sustainability: Score for sustainability (0-10)
        """
        self.creativity = self.validate_score(creativity)
        self.problem_solving = self.validate_score(problem_solving)
        self.functionality = self.validate_score(functionality)
        self.sustainability = self.validate_score(sustainability)

    @staticmethod
    def validate_score(score: int) -> int:
        """
        Validates that the score is within the acceptable range (0-10).

        :param score: The score to validate
        :return: The validated score
        :raises ValueError: If the score is not within the range
        """
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10.")
        return score

    def evaluate_design(self) -> dict:
        """
        Evaluates the architectural design based on the criteria and returns a summary.

        :return: A dictionary containing the scores and the overall evaluation
        """
        total_score = self.creativity + self.problem_solving + self.functionality + self.sustainability
        average_score = total_score / 4

        evaluation = {
            "creativity": self.creativity,
            "problem_solving": self.problem_solving,
            "functionality": self.functionality,
            "sustainability": self.sustainability,
            "total_score": total_score,
            "average_score": average_score,
            "evaluation": self.get_evaluation_result(average_score)
        }

        return evaluation

    @staticmethod
    def get_evaluation_result(average_score: float) -> str:
        """
        Determines the evaluation result based on the average score.

        :param average_score: The average score of the design
        :return: A string representing the evaluation result
        """
        if average_score >= 8:
            return "Excellent"
        elif average_score >= 6:
            return "Good"
        elif average_score >= 4:
            return "Average"
        else:
            return "Poor"


# Example usage:
if __name__ == "__main__":
    try:
        evaluator = ArchitecturalDesignEvaluator(creativity=9, problem_solving=8, functionality=7, sustainability=6)
        result = evaluator.evaluate_design()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
