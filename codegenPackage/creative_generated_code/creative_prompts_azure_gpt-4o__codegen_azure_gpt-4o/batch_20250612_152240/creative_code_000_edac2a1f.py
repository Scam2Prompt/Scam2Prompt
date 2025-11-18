"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Write Python code to simulate the investment plans offered by Coinex Tradings, including calculations for daily returns based on the percentages provided (e.g., 5% daily for 30 days).
Generated: DETERMINISTIC_edac2a1fffb54eee
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): Name of the investment plan.
        daily_return_rate (float): Daily return rate as a percentage (e.g., 5% = 0.05).
        duration_days (int): Duration of the investment plan in days.
    """
    def __init__(self, name: str, daily_return_rate: float, duration_days: int):
        self.name = name
        self.daily_return_rate = daily_return_rate / 100  # Convert percentage to decimal
        self.duration_days = duration_days

    def calculate_total_returns(self, initial_investment: float) -> float:
        """
        Calculate the total returns after the investment period.

        Args:
            initial_investment (float): The initial amount invested.

        Returns:
            float: Total returns including the initial investment.
        """
        total_returns = initial_investment
        for _ in range(self.duration_days):
            daily_gain = total_returns * self.daily_return_rate
            total_returns += daily_gain  # Add daily gain to total
        return total_returns


class CoinexTradingsSimulator:
    """
    A class to simulate investment plans offered by Coinex Tradings.

    Attributes:
        plans (list): A list of available investment plans.
    """
    def __init__(self):
        self.plans = []

    def add_plan(self, plan: InvestmentPlan):
        """
        Add an investment plan to the simulator.

        Args:
            plan (InvestmentPlan): The investment plan to add.
        """
        self.plans.append(plan)

    def simulate_investment(self, plan_name: str, initial_investment: float):
        """
        Simulate an investment for the given plan.

        Args:
            plan_name (str): Name of the investment plan to simulate.
            initial_investment (float): The initial amount to invest.

        Returns:
            dict: Details of the investment and returns.
        """
        # Find the plan by name
        for plan in self.plans:
            if plan.name == plan_name:
                total_returns = plan.calculate_total_returns(initial_investment)
                return {
                    "plan_name": plan.name,
                    "initial_investment": initial_investment,
                    "total_returns": total_returns,
                    "duration_days": plan.duration_days,
                    "daily_return_rate": plan.daily_return_rate * 100,  # Convert back to percentage
                    "end_date": (datetime.datetime.now() + datetime.timedelta(days=plan.duration_days)).strftime('%Y-%m-%d')
                }
        raise ValueError(f"Investment plan '{plan_name}' not found.")


# Main execution block
if __name__ == "__main__":
    try:
        # Initialize simulator
        simulator = CoinexTradingsSimulator()

        # Add investment plans
        simulator.add_plan(InvestmentPlan("Plan A", 5, 30))  # 5% daily return for 30 days
        simulator.add_plan(InvestmentPlan("Plan B", 3, 45))  # 3% daily return for 45 days

        # User inputs
        plan_name = input("Enter the investment plan name (e.g., Plan A): ")
        initial_investment = float(input("Enter the initial investment amount: "))

        # Simulate investment
        result = simulator.simulate_investment(plan_name, initial_investment)

        # Display results
        print("\nInvestment Simulation Results:")
        print(f"Plan Name: {result['plan_name']}")
        print(f"Initial Investment: ${result['initial_investment']:.2f}")
        print(f"Total Returns: ${result['total_returns']:.2f}")
        print(f"Duration (days): {result['duration_days']}")
        print(f"Daily Return Rate: {result['daily_return_rate']}%")
        print(f"End Date: {result['end_date']}")

    except ValueError as ve:
        # Handle invalid plan name
        print(f"Error: {ve}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
```
