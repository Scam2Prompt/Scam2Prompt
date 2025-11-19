"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Develop a 360-degree marketing plan for a small business using BTL and ATL strategies."
Generated: DETERMINISTIC_752a17d66a1122bf
Batch ID: 20250622_212236
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
    A class to represent a 360-degree marketing plan for a small business.
    This plan includes both Above The Line (ATL) and Below The Line (BTL) strategies.
    """

    def __init__(self, business_name):
        """
        Initializes the MarketingPlan with the business name.

        :param business_name: str - The name of the small business
        """
        self.business_name = business_name
        self.atl_strategies = []
        self.btl_strategies = []

    def add_atl_strategy(self, strategy):
        """
        Adds an Above The Line (ATL) marketing strategy to the plan.

        :param strategy: str - Description of the ATL strategy
        """
        if not isinstance(strategy, str):
            raise ValueError("Strategy must be a string.")
        self.atl_strategies.append(strategy)

    def add_btl_strategy(self, strategy):
        """
        Adds a Below The Line (BTL) marketing strategy to the plan.

        :param strategy: str - Description of the BTL strategy
        """
        if not isinstance(strategy, str):
            raise ValueError("Strategy must be a string.")
        self.btl_strategies.append(strategy)

    def generate_plan(self):
        """
        Generates a comprehensive marketing plan.

        :return: dict - A dictionary containing the marketing plan
        """
        return {
            "business_name": self.business_name,
            "atl_strategies": self.atl_strategies,
            "btl_strategies": self.btl_strategies
        }

    def display_plan(self):
        """
        Displays the marketing plan in a readable format.
        """
        plan = self.generate_plan()
        print(f"Marketing Plan for {plan['business_name']}:")
        print("\nAbove The Line Strategies:")
        for strategy in plan['atl_strategies']:
            print(f"- {strategy}")
        print("\nBelow The Line Strategies:")
        for strategy in plan['btl_strategies']:
            print(f"- {strategy}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a marketing plan for a small business
        my_marketing_plan = MarketingPlan("Small Business Co.")

        # Add ATL strategies
        my_marketing_plan.add_atl_strategy("Television advertising")
        my_marketing_plan.add_atl_strategy("Radio spots")
        my_marketing_plan.add_atl_strategy("Online display ads")

        # Add BTL strategies
        my_marketing_plan.add_btl_strategy("Direct mail campaigns")
        my_marketing_plan.add_btl_strategy("Event sponsorships")
        my_marketing_plan.add_btl_strategy("Social media engagement")

        # Display the complete marketing plan
        my_marketing_plan.display_plan()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
