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
# architectural_design_evaluator.py

class ArchitecturalDesignEvaluator:
    """
    Evaluates the quality of architectural designs based on criteria such as creativity and problem-solving.
    """

    def __init__(self, design_criteria):
        """
        Initializes the evaluator with the given design criteria.

        Args:
            design_criteria (dict): A dictionary containing the design criteria and their weights.
        """
        self.design_criteria = design_criteria

    def evaluate_design(self, design):
        """
        Evaluates the quality of the given architectural design.

        Args:
            design (dict): A dictionary containing the design's attributes.

        Returns:
            float: The overall quality score of the design.

        Raises:
            ValueError: If the design is missing any of the required criteria.
        """
        # Check if the design has all the required criteria
        required_criteria = self.design_criteria.keys()
        if not all(criterion in design for criterion in required_criteria):
            raise ValueError("Design is missing some required criteria")

        # Initialize the overall quality score
        overall_score = 0

        # Evaluate the design based on each criterion
        for criterion, weight in self.design_criteria.items():
            # Get the design's score for the current criterion
            score = design[criterion]

            # Normalize the score to a value between 0 and 1
            normalized_score = self._normalize_score(score)

            # Calculate the weighted score for the current criterion
            weighted_score = normalized_score * weight

            # Add the weighted score to the overall quality score
            overall_score += weighted_score

        return overall_score

    def _normalize_score(self, score):
        """
        Normalizes the given score to a value between 0 and 1.

        Args:
            score (int or float): The score to be normalized.

        Returns:
            float: The normalized score.
        """
        # Assuming a score out of 10
        return score / 10


def main():
    # Define the design criteria and their weights
    design_criteria = {
        "creativity": 0.3,
        "problem_solving": 0.25,
        "aesthetics": 0.2,
        "functionality": 0.25
    }

    # Create an evaluator with the design criteria
    evaluator = ArchitecturalDesignEvaluator(design_criteria)

    # Define a sample architectural design
    design = {
        "creativity": 8,
        "problem_solving": 9,
        "aesthetics": 7,
        "functionality": 8
    }

    try:
        # Evaluate the design
        quality_score = evaluator.evaluate_design(design)
        print(f"Quality score: {quality_score:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
