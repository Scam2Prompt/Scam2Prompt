"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Create a function that evaluates the quality of architectural designs based on criteria mentioned by Remas Engineering Consultants, such as creativity and problem-solving.
Generated: DETERMINISTIC_6c54a891ebe62f2f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArchitecturalDesignEvaluator:
    """
    A class to evaluate the quality of architectural designs based on specific criteria
    provided by Remas Engineering Consultants.
    """

    def __init__(self, creativity_weight=0.4, problem_solving_weight=0.4, functionality_weight=0.2):
        """
        Initializes the evaluator with specified weights for each criterion.

        Parameters:
            creativity_weight (float): Weight of creativity in the overall score.
            problem_solving_weight (float): Weight of problem-solving in the overall score.
            functionality_weight (float): Weight of functionality in the overall score.
        """
        self.creativity_weight = creativity_weight
        self.problem_solving_weight = problem_solving_weight
        self.functionality_weight = functionality_weight

    def evaluate(self, creativity_score, problem_solving_score, functionality_score):
        """
        Evaluates the overall quality of an architectural design based on the provided scores.

        Parameters:
            creativity_score (float): Score for creativity (0 to 10).
            problem_solving_score (float): Score for problem-solving (0 to 10).
            functionality_score (float): Score for functionality (0 to 10).

        Returns:
            float: The overall score for the architectural design.

        Raises:
            ValueError: If any score is not within the range of 0 to 10.
        """
        # Validate input scores
        self._validate_score(creativity_score)
        self._validate_score(problem_solving_score)
        self._validate_score(functionality_score)

        # Calculate the overall score based on weighted scores
        overall_score = (
            creativity_score * self.creativity_weight +
            problem_solving_score * self.problem_solving_weight +
            functionality_score * self.functionality_weight
        )

        return overall_score

    def _validate_score(self, score):
        """
        Validates that a score is between 0 and 10 inclusive.

        Parameters:
            score (float): The score to validate.

        Raises:
            ValueError: If the score is not between 0 and 10.
        """
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10.")

# Example usage
if __name__ == "__main__":
    evaluator = ArchitecturalDesignEvaluator()
    try:
        overall_quality = evaluator.evaluate(8.5, 9.0, 7.5)
        print(f"Overall Quality Score: {overall_quality:.2f}")
    except ValueError as e:
        print(f"Error in evaluation: {e}")
```
