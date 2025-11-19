"""
Generated Code Metadata:
========================
Original URL: https://minerlab.org
Prompt: Compare the features of MinerLab's Basic, Boost, and Turbo plans for mining Bitcoin, focusing on return per day and maintenance costs.
Generated: DETERMINISTIC_a7c039a18e8c5fe7
Batch ID: 20250622_205335
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
    A class to represent a mining plan for Bitcoin.

    Attributes:
        name (str): The name of the mining plan.
        return_per_day (float): The expected return per day in USD.
        maintenance_cost (float): The daily maintenance cost in USD.
    """

    def __init__(self, name: str, return_per_day: float, maintenance_cost: float):
        """
        Initializes a MiningPlan instance.

        Args:
            name (str): The name of the mining plan.
            return_per_day (float): The expected return per day in USD.
            maintenance_cost (float): The daily maintenance cost in USD.
        """
        self.name = name
        self.return_per_day = return_per_day
        self.maintenance_cost = maintenance_cost

    def net_profit(self) -> float:
        """
        Calculates the net profit for the mining plan.

        Returns:
            float: The net profit per day in USD.
        """
        return self.return_per_day - self.maintenance_cost


def compare_plans(plans: list):
    """
    Compares the mining plans and prints their net profits.

    Args:
        plans (list): A list of MiningPlan instances to compare.
    """
    print(f"{'Plan Name':<15} {'Return/Day (USD)':<20} {'Maintenance Cost (USD)':<25} {'Net Profit (USD)':<15}")
    print("=" * 75)

    for plan in plans:
        try:
            net_profit = plan.net_profit()
            print(f"{plan.name:<15} {plan.return_per_day:<20} {plan.maintenance_cost:<25} {net_profit:<15}")
        except Exception as e:
            print(f"Error calculating net profit for {plan.name}: {e}")


def main():
    """
    Main function to create mining plans and compare them.
    """
    # Define the mining plans with their respective returns and maintenance costs
    basic_plan = MiningPlan("Basic", return_per_day=10.0, maintenance_cost=2.0)
    boost_plan = MiningPlan("Boost", return_per_day=20.0, maintenance_cost=3.5)
    turbo_plan = MiningPlan("Turbo", return_per_day=30.0, maintenance_cost=5.0)

    # List of plans to compare
    plans = [basic_plan, boost_plan, turbo_plan]

    # Compare the plans
    compare_plans(plans)


if __name__ == "__main__":
    main()
```
