"""
Generated Code Metadata:
========================
Original URL: https://zenixglobaltrade.com
Prompt: Write code to simulate the investment growth over time for ZenixGlobaltrade's plans, including Starter, Classic, Professional, and Premium, with user-defined deposit amounts.
Generated: DETERMINISTIC_e6bf06e8a3da51e0
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from typing import List, Dict, Optional

class InvestmentPlan:
    """
    Represents an investment plan with its specific growth rate and duration.
    """
    def __init__(self, name: str, daily_growth_rate: float, duration_days: int):
        """
        Initialize the investment plan.
        
        Args:
            name: Name of the plan (e.g., "Starter")
            daily_growth_rate: Daily growth rate as a decimal (e.g., 0.01 for 1%)
            duration_days: Duration of the plan in days
        """
        self.name = name
        self.daily_growth_rate = daily_growth_rate
        self.duration_days = duration_days

class InvestmentSimulator:
    """
    Simulates investment growth over time for different plans.
    """
    def __init__(self):
        """
        Initialize the simulator with predefined investment plans.
        """
        self.plans = {
            "Starter": InvestmentPlan("Starter", 0.01, 30),
            "Classic": InvestmentPlan("Classic", 0.015, 60),
            "Professional": InvestmentPlan("Professional", 0.02, 90),
            "Premium": InvestmentPlan("Premium", 0.025, 120)
        }

    def calculate_growth(self, initial_amount: float, plan_name: str) -> List[float]:
        """
        Calculate the daily growth of the investment for the selected plan.
        
        Args:
            initial_amount: Initial deposit amount
            plan_name: Name of the investment plan
            
        Returns:
            List of daily balances over the plan duration
            
        Raises:
            ValueError: If the plan name is invalid or initial amount is negative
        """
        if initial_amount < 0:
            raise ValueError("Initial amount cannot be negative.")
        
        plan = self.plans.get(plan_name)
        if not plan:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {list(self.plans.keys())}")
        
        daily_balances = []
        current_balance = initial_amount
        
        for _ in range(plan.duration_days):
            current_balance *= (1 + plan.daily_growth_rate)
            daily_balances.append(current_balance)
            
        return daily_balances

    def simulate_investment(self, initial_amount: float, plan_name: str) -> Dict[str, float]:
        """
        Simulate an investment and return key metrics.
        
        Args:
            initial_amount: Initial deposit amount
            plan_name: Name of the investment plan
            
        Returns:
            Dictionary containing:
            - final_balance: Final balance after plan duration
            - total_growth: Total growth amount
            - growth_percentage: Percentage growth
            
        Raises:
            ValueError: If the plan name is invalid or initial amount is negative
        """
        daily_balances = self.calculate_growth(initial_amount, plan_name)
        
        if not daily_balances:
            return {}
            
        final_balance = daily_balances[-1]
        total_growth = final_balance - initial_amount
        growth_percentage = (total_growth / initial_amount) * 100
        
        return {
            "final_balance": final_balance,
            "total_growth": total_growth,
            "growth_percentage": growth_percentage
        }

    def plot_growth(self, initial_amount: float, plan_name: str) -> Optional[plt.Figure]:
        """
        Plot the investment growth over time.
        
        Args:
            initial_amount: Initial deposit amount
            plan_name: Name of the investment plan
            
        Returns:
            matplotlib Figure object if successful, None otherwise
        """
        try:
            daily_balances = self.calculate_growth(initial_amount, plan_name)
            plan = self.plans[plan_name]
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(range(1, plan.duration_days + 1), daily_balances)
            ax.set_title(f"Investment Growth: {plan.name} Plan")
            ax.set_xlabel("Day")
            ax.set_ylabel("Balance ($)")
            ax.grid(True)
            
            return fig
        except Exception as e:
            print(f"Error generating plot: {e}")
            return None

def main():
    """
    Main function to demonstrate the investment simulation.
    """
    simulator = InvestmentSimulator()
    
    print("ZenixGlobaltrade Investment Simulator")
    print("Available plans:")
    for plan_name in simulator.plans:
        print(f"- {plan_name}")
    
    try:
        initial_amount = float(input("Enter initial deposit amount: $"))
        if initial_amount <= 0:
            raise ValueError("Deposit amount must be positive.")
            
        plan_name = input("Select plan: ")
        if plan_name not in simulator.plans:
            raise ValueError("Invalid plan selected.")
            
        result = simulator.simulate_investment(initial_amount, plan_name)
        
        print("\nSimulation Results:")
        print(f"Initial Deposit: ${initial_amount:,.2f}")
        print(f"Plan: {plan_name}")
        print(f"Final Balance: ${result['final_balance']:,.2f}")
        print(f"Total Growth: ${result['total_growth']:,.2f}")
        print(f"Growth Percentage: {result['growth_percentage']:.2f}%")
        
        fig = simulator.plot_growth(initial_amount, plan_name)
        if fig:
            plt.show()
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
