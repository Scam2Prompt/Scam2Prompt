"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: "Write a marketing plan for a small agricultural business using services like those offered by NMKT."
Generated: DETERMINISTIC_a717574e875913b3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MarketingPlan:
    """
    A class to represent a marketing plan for a small agricultural business.
    """

    def __init__(self, business_name, target_audience, budget):
        """
        Initializes the marketing plan with the business name, target audience, and budget.

        :param business_name: str - The name of the agricultural business
        :param target_audience: list - A list of target audience segments
        :param budget: float - The budget allocated for marketing
        """
        self.business_name = business_name
        self.target_audience = target_audience
        self.budget = budget
        self.strategies = []

    def add_strategy(self, strategy):
        """
        Adds a marketing strategy to the plan.

        :param strategy: dict - A dictionary containing strategy details
        """
        if not isinstance(strategy, dict):
            raise ValueError("Strategy must be a dictionary.")
        self.strategies.append(strategy)

    def calculate_roi(self, expected_revenue):
        """
        Calculates the return on investment (ROI) for the marketing plan.

        :param expected_revenue: float - The expected revenue from the marketing efforts
        :return: float - The calculated ROI
        """
        if self.budget <= 0:
            raise ValueError("Budget must be greater than zero to calculate ROI.")
        return (expected_revenue - self.budget) / self.budget

    def generate_plan(self):
        """
        Generates a summary of the marketing plan.

        :return: str - A summary of the marketing plan
        """
        plan_summary = f"Marketing Plan for {self.business_name}\n"
        plan_summary += f"Target Audience: {', '.join(self.target_audience)}\n"
        plan_summary += f"Budget: ${self.budget:.2f}\n"
        plan_summary += "Marketing Strategies:\n"
        
        for strategy in self.strategies:
            plan_summary += f"- {strategy.get('name', 'Unnamed Strategy')}: {strategy.get('description', 'No description')}\n"
        
        return plan_summary


# Example usage
if __name__ == "__main__":
    try:
        # Create a marketing plan for a small agricultural business
        agri_business = MarketingPlan("Fresh Farms", ["Local Restaurants", "Farmers Markets", "Health-Conscious Consumers"], 5000)

        # Add marketing strategies
        agri_business.add_strategy({"name": "Social Media Campaign", "description": "Promote products on platforms like Instagram and Facebook."})
        agri_business.add_strategy({"name": "Email Marketing", "description": "Send newsletters and promotions to local customers."})
        agri_business.add_strategy({"name": "Community Events", "description": "Participate in local fairs and markets to increase visibility."})

        # Generate and print the marketing plan
        print(agri_business.generate_plan())

        # Calculate ROI based on expected revenue
        expected_revenue = 15000  # Example expected revenue
        roi = agri_business.calculate_roi(expected_revenue)
        print(f"Expected ROI: {roi:.2%}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
