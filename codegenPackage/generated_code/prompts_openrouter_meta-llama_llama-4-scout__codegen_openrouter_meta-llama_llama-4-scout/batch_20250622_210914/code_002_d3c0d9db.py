"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Develop a code snippet to calculate a company's competitiveness score based on Norbert Gabriel's management consulting approach.
Generated: DETERMINISTIC_d3c0d9db04dbf945
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# competitiveness_score.py

class CompetitivenessScoreCalculator:
    """
    Calculates a company's competitiveness score based on Norbert Gabriel's management consulting approach.

    The score is calculated based on the following factors:
    - Financial Situation (20%)
    - Market Position (20%)
    - Innovation Capability (20%)
    - Customer Satisfaction (20%)
    - Employee Competence (20%)
    """

    def __init__(self, financial_situation, market_position, innovation_capability, customer_satisfaction, employee_competence):
        """
        Initializes the calculator with the company's data.

        Args:
            financial_situation (float): Score between 0 and 1 representing the company's financial situation.
            market_position (float): Score between 0 and 1 representing the company's market position.
            innovation_capability (float): Score between 0 and 1 representing the company's innovation capability.
            customer_satisfaction (float): Score between 0 and 1 representing the company's customer satisfaction.
            employee_competence (float): Score between 0 and 1 representing the company's employee competence.
        """
        self.financial_situation = self._validate_score(financial_situation)
        self.market_position = self._validate_score(market_position)
        self.innovation_capability = self._validate_score(innovation_capability)
        self.customer_satisfaction = self._validate_score(customer_satisfaction)
        self.employee_competence = self._validate_score(employee_competence)

    def _validate_score(self, score):
        """
        Validates a score to ensure it's between 0 and 1.

        Args:
            score (float): The score to validate.

        Returns:
            float: The validated score.

        Raises:
            ValueError: If the score is not between 0 and 1.
        """
        if not 0 <= score <= 1:
            raise ValueError("Score must be between 0 and 1")
        return score

    def calculate_competitiveness_score(self):
        """
        Calculates the company's competitiveness score.

        Returns:
            float: The competitiveness score between 0 and 1.
        """
        weights = [0.2, 0.2, 0.2, 0.2, 0.2]
        scores = [
            self.financial_situation,
            self.market_position,
            self.innovation_capability,
            self.customer_satisfaction,
            self.employee_competence
        ]

        return sum(score * weight for score, weight in zip(scores, weights))


def main():
    try:
        calculator = CompetitivenessScoreCalculator(
            financial_situation=0.8,
            market_position=0.7,
            innovation_capability=0.9,
            customer_satisfaction=0.85,
            employee_competence=0.8
        )

        competitiveness_score = calculator.calculate_competitiveness_score()
        print(f"Competitiveness Score: {competitiveness_score:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
