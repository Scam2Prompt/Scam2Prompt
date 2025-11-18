"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Generate a script to calculate the return on investment (ROI) for MinerLab's "Elite" and "Ultimate" mining plans for Dogecoin and Litecoin.
Generated: DETERMINISTIC_fc96ead70bff7132
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MiningPlan:
    """
    Class to represent a mining plan with its characteristics and methods to calculate ROI.
    """

    def __init__(self, name, investment, daily_profit, days):
        """
        Initializes a MiningPlan instance.

        :param name: str - Name of the mining plan
        :param investment: float - Initial investment in the mining plan
        :param daily_profit: float - Expected daily profit from the mining plan
        :param days: int - Number of days to calculate ROI
        """
        self.name = name
        self.investment = investment
        self.daily_profit = daily_profit
        self.days = days
        
    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI).

        :return: float - The ROI as a percentage
        """
        if self.investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        if self.days <= 0:
            raise ValueError("Days must be greater than zero.")
        
        total_profit = self.daily_profit * self.days
        roi = (total_profit - self.investment) / self.investment * 100
        return roi


def main():
    """
    Main function to execute the ROI calculations for MinerLab's mining plans.
    """
    plans = [
        MiningPlan("Elite - Dogecoin", investment=1000, daily_profit=20, days=30),
        MiningPlan("Ultimate - Dogecoin", investment=2000, daily_profit=50, days=30),
        MiningPlan("Elite - Litecoin", investment=1000, daily_profit=25, days=30),
        MiningPlan("Ultimate - Litecoin", investment=2000, daily_profit=60, days=30),
    ]
    
    for plan in plans:
        try:
            roi = plan.calculate_roi()
            print(f"{plan.name} - ROI: {roi:.2f}%")
        except ValueError as e:
            print(f"Error calculating ROI for {plan.name}: {e}")


if __name__ == "__main__":
    main()
```
