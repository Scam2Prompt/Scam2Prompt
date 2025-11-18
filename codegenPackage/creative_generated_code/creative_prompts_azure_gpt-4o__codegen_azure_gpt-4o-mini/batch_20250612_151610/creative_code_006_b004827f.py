"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Develop a program that evaluates whether a business concept is franchisable, using criteria such as scalability, operational efficiency, and market potential, as described by Franchise Teacher.
Generated: DETERMINISTIC_b004827ff61a296a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FranchiseEvaluation:
    """
    A class to evaluate if a business concept is viable for franchising
    based on scalability, operational efficiency, and market potential.
    """

    def __init__(self, scalability_score, operational_efficiency_score, market_potential_score):
        """
        Initializes the FranchiseEvaluation with scores for each criterion.

        :param scalability_score: A score from 0 to 10 representing scalability.
        :param operational_efficiency_score: A score from 0 to 10 representing operational efficiency.
        :param market_potential_score: A score from 0 to 10 representing market potential.
        """
        self.scalability_score = self.validate_score(scalability_score)
        self.operational_efficiency_score = self.validate_score(operational_efficiency_score)
        self.market_potential_score = self.validate_score(market_potential_score)

    def validate_score(self, score):
        """
        Validates that a score is within the acceptable range of 0 to 10.

        :param score: The score to validate.
        :return: Validated score.
        :raises ValueError: If the score is not within the range.
        """
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10.")
        return score

    def evaluate_franchisability(self):
        """
        Evaluates the franchisability of the business concept based on the criteria scores.

        :return: A string indicating whether the business concept is franchisable or not.
        """
        average_score = (self.scalability_score + 
                         self.operational_efficiency_score + 
                         self.market_potential_score) / 3

        # Define the threshold for a business to be considered franchisable
        threshold = 7

        if average_score >= threshold:
            return "The business concept is viable for franchising."
        else:
            return "The business concept is not viable for franchising."

# Example usage
if __name__ == "__main__":
    try:
        # Scores for scalability, operational efficiency, and market potential
        scalability = float(input("Enter scalability score (0-10): "))
        operational_efficiency = float(input("Enter operational efficiency score (0-10): "))
        market_potential = float(input("Enter market potential score (0-10): "))

        # Create a FranchiseEvaluation instance
        evaluation = FranchiseEvaluation(scalability, operational_efficiency, market_potential)

        # Evaluate and print the result
        result = evaluation.evaluate_franchisability()
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
```
