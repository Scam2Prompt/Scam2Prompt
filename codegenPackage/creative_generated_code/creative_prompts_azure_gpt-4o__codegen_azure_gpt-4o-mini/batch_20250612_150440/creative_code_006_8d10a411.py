"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Develop a program that calculates the ROI for running a node in Rocket Pool's network, factoring in commissions earned and staking rewards.
Generated: DETERMINISTIC_8d10a4110c31d656
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NodeROI:
    """
    A class to calculate the Return on Investment (ROI) for running a node 
    in Rocket Pool's network based on staking rewards and commissions earned.
    """

    def __init__(self, initial_investment: float, annual_staking_reward: float, 
                 annual_commission: float, operational_cost: float):
        """
        Initializes the NodeROI with the required parameters.
        
        :param initial_investment: Initial amount invested in the node (in ETH).
        :param annual_staking_reward: Annual staking rewards expected (in ETH).
        :param annual_commission: Annual commissions earned from users (in ETH).
        :param operational_cost: Annual operational costs (in ETH).
        """
        if initial_investment < 0 or annual_staking_reward < 0 or \
           annual_commission < 0 or operational_cost < 0:
            raise ValueError("All financial inputs must be non-negative.")

        self.initial_investment = initial_investment
        self.annual_staking_reward = annual_staking_reward
        self.annual_commission = annual_commission
        self.operational_cost = operational_cost

    def calculate_roi(self) -> float:
        """
        Calculates the ROI for the node.
        
        :return: The ROI as a percentage.
        """
        # Calculate total income
        total_income = self.annual_staking_reward + self.annual_commission
        
        # Calculate net profit
        net_profit = total_income - self.operational_cost
        
        # Calculate ROI
        if self.initial_investment > 0:
            roi = (net_profit / self.initial_investment) * 100
        else:
            raise ZeroDivisionError("Initial investment cannot be zero.")

        return roi

if __name__ == "__main__":
    try:
        # Example inputs for the NodeROI calculation
        initial_investment = 10.0  # in ETH
        annual_staking_reward = 2.0  # in ETH
        annual_commission = 1.0  # in ETH
        operational_cost = 0.5  # in ETH

        # Create an instance of NodeROI
        node_roi = NodeROI(initial_investment, annual_staking_reward, 
                           annual_commission, operational_cost)

        # Calculate and print the ROI
        roi = node_roi.calculate_roi()
        print(f"The ROI for the node is: {roi:.2f}%")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Calculation error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
