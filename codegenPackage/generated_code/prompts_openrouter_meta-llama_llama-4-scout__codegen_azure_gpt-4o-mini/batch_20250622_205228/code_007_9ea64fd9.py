"""
Generated Code Metadata:
========================
Original URL: https://rocketspool.github.io
Prompt: Develop a code example for calculating the ROI for a node operator in the Rocket Pool network.
Generated: DETERMINISTIC_9ea64fd95c2f1515
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NodeOperatorROI:
    """
    A class to calculate the Return on Investment (ROI) for a node operator in the Rocket Pool network.
    """

    def __init__(self, initial_investment: float, rewards_earned: float, operational_costs: float):
        """
        Initializes the NodeOperatorROI with the necessary parameters.

        :param initial_investment: The initial amount invested in the node operation.
        :param rewards_earned: The total rewards earned from operating the node.
        :param operational_costs: The total operational costs incurred during the operation.
        """
        if initial_investment < 0 or rewards_earned < 0 or operational_costs < 0:
            raise ValueError("Initial investment, rewards earned, and operational costs must be non-negative.")

        self.initial_investment = initial_investment
        self.rewards_earned = rewards_earned
        self.operational_costs = operational_costs

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        ROI is calculated using the formula:
        ROI = (Total Rewards - Total Costs) / Initial Investment

        :return: The ROI as a percentage.
        """
        total_costs = self.initial_investment + self.operational_costs
        if total_costs == 0:
            raise ZeroDivisionError("Total costs cannot be zero when calculating ROI.")

        roi = (self.rewards_earned - total_costs) / total_costs * 100
        return roi

    def display_roi(self):
        """
        Displays the calculated ROI in a user-friendly format.
        """
        try:
            roi = self.calculate_roi()
            print(f"The Return on Investment (ROI) for the node operator is: {roi:.2f}%")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error calculating ROI: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the NodeOperatorROI with example values
        node_operator = NodeOperatorROI(initial_investment=1000.0, rewards_earned=1500.0, operational_costs=200.0)
        
        # Display the ROI
        node_operator.display_roi()
    except Exception as e:
        print(f"An error occurred: {e}")
```
