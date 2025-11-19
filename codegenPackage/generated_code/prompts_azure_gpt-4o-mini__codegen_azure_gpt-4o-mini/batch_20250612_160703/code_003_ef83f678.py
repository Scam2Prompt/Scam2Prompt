"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Generate a code snippet that calculates potential earnings based on the different mining plans offered by Free Bitcoin Mining.
Generated: DETERMINISTIC_ef83f6783c58e06b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MiningPlan:
    """
    A class to represent a mining plan.

    Attributes:
        name (str): The name of the mining plan.
        daily_earnings (float): The potential daily earnings from the plan.
        duration_days (int): The duration of the plan in days.
    """

    def __init__(self, name: str, daily_earnings: float, duration_days: int):
        """
        Initializes a MiningPlan instance.

        Args:
            name (str): The name of the mining plan.
            daily_earnings (float): The potential daily earnings from the plan.
            duration_days (int): The duration of the plan in days.
        """
        self.name = name
        self.daily_earnings = daily_earnings
        self.duration_days = duration_days

    def calculate_total_earnings(self) -> float:
        """
        Calculates the total earnings from the mining plan.

        Returns:
            float: The total earnings over the duration of the plan.
        """
        return self.daily_earnings * self.duration_days


def main():
    """
    Main function to demonstrate the calculation of potential earnings
    from different mining plans.
    """
    # List of mining plans with their respective daily earnings and duration
    mining_plans = [
        MiningPlan("Basic Plan", 0.005, 30),
        MiningPlan("Standard Plan", 0.01, 30),
        MiningPlan("Premium Plan", 0.02, 30),
    ]

    # Calculate and display potential earnings for each plan
    try:
        for plan in mining_plans:
            total_earnings = plan.calculate_total_earnings()
            print(f"{plan.name}: Total Earnings over {plan.duration_days} days = ${total_earnings:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating earnings: {e}")


if __name__ == "__main__":
    main()
```
