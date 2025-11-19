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
# accounting_service_evaluator.py

class AccountingServiceEvaluator:
    """
    Evaluates the quality and cost-effectiveness of accounting services.

    Attributes:
        responsiveness (float): Responsiveness score (0-1)
        personalized_support (float): Personalized support score (0-1)
        cost (float): Cost of the accounting service
        industry_average_cost (float): Industry average cost of accounting service
    """

    def __init__(self, responsiveness, personalized_support, cost, industry_average_cost):
        """
        Initializes the AccountingServiceEvaluator.

        Args:
            responsiveness (float): Responsiveness score (0-1)
            personalized_support (float): Personalized support score (0-1)
            cost (float): Cost of the accounting service
            industry_average_cost (float): Industry average cost of accounting service

        Raises:
            ValueError: If scores are not between 0 and 1
            ValueError: If costs are not positive
        """
        if not (0 <= responsiveness <= 1 and 0 <= personalized_support <= 1):
            raise ValueError("Scores must be between 0 and 1")

        if cost <= 0 or industry_average_cost <= 0:
            raise ValueError("Costs must be positive")

        self.responsiveness = responsiveness
        self.personalized_support = personalized_support
        self.cost = cost
        self.industry_average_cost = industry_average_cost

    def calculate_quality_score(self):
        """
        Calculates the overall quality score.

        Returns:
            float: Quality score (0-1)
        """
        # Weighted average of responsiveness and personalized support scores
        return (0.6 * self.responsiveness) + (0.4 * self.personalized_support)

    def calculate_cost_effectiveness_score(self):
        """
        Calculates the cost-effectiveness score.

        Returns:
            float: Cost-effectiveness score (0-1)
        """
        # Ratio of industry average cost to service cost
        return min(self.industry_average_cost / self.cost, 1)

    def evaluate(self):
        """
        Evaluates the accounting service.

        Returns:
            dict: Evaluation results
        """
        quality_score = self.calculate_quality_score()
        cost_effectiveness_score = self.calculate_cost_effectiveness_score()

        return {
            "quality_score": quality_score,
            "cost_effectiveness_score": cost_effectiveness_score,
            "overall_score": (quality_score + cost_effectiveness_score) / 2
        }


def main():
    try:
        evaluator = AccountingServiceEvaluator(
            responsiveness=0.8,
            personalized_support=0.9,
            cost=1000.0,
            industry_average_cost=1200.0
        )

        evaluation_results = evaluator.evaluate()
        print("Evaluation Results:")
        for key, value in evaluation_results.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
