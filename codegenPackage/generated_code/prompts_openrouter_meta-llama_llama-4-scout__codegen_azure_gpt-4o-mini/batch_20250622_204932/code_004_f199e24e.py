"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Develop a short algorithm to assess the quality and cost-effectiveness of accounting services, incorporating factors like responsiveness and personalized support."
Generated: DETERMINISTIC_f199e24e233a0860
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountingServiceAssessment:
    """
    A class to assess the quality and cost-effectiveness of accounting services.
    """

    def __init__(self, responsiveness, personalized_support, cost, quality):
        """
        Initializes the assessment parameters.

        :param responsiveness: A score (1-10) indicating the responsiveness of the service.
        :param personalized_support: A score (1-10) indicating the level of personalized support.
        :param cost: The cost of the accounting service.
        :param quality: A score (1-10) indicating the overall quality of the service.
        """
        self.responsiveness = self.validate_score(responsiveness)
        self.personalized_support = self.validate_score(personalized_support)
        self.cost = self.validate_cost(cost)
        self.quality = self.validate_score(quality)

    @staticmethod
    def validate_score(score):
        """
        Validates that the score is between 1 and 10.

        :param score: The score to validate.
        :return: The validated score.
        :raises ValueError: If the score is not between 1 and 10.
        """
        if not (1 <= score <= 10):
            raise ValueError("Score must be between 1 and 10.")
        return score

    @staticmethod
    def validate_cost(cost):
        """
        Validates that the cost is a positive number.

        :param cost: The cost to validate.
        :return: The validated cost.
        :raises ValueError: If the cost is not a positive number.
        """
        if cost <= 0:
            raise ValueError("Cost must be a positive number.")
        return cost

    def assess_service(self):
        """
        Assesses the service based on responsiveness, personalized support, cost, and quality.

        :return: A dictionary containing the assessment results.
        """
        score = (self.responsiveness + self.personalized_support + self.quality) / 3
        cost_effectiveness = score / self.cost

        assessment = {
            "average_score": score,
            "cost_effectiveness": cost_effectiveness,
            "recommendation": self.get_recommendation(cost_effectiveness)
        }
        return assessment

    @staticmethod
    def get_recommendation(cost_effectiveness):
        """
        Provides a recommendation based on cost-effectiveness.

        :param cost_effectiveness: The calculated cost-effectiveness score.
        :return: A recommendation string.
        """
        if cost_effectiveness > 1:
            return "Highly recommended"
        elif cost_effectiveness == 1:
            return "Recommended"
        else:
            return "Not recommended"


# Example usage
if __name__ == "__main__":
    try:
        service = AccountingServiceAssessment(responsiveness=8, personalized_support=9, cost=500, quality=7)
        assessment_result = service.assess_service()
        print(assessment_result)
    except ValueError as e:
        print(f"Error: {e}")
```
