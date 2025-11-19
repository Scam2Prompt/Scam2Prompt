"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Develop a tool to simulate the impact of strategic investments on a company's financial recovery, referencing Arbitum Consulting's focus on investment partnerships.
Generated: DETERMINISTIC_b4cc14ae8c5ecbd8
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple

class FinancialRecoverySimulator:
    """
    A tool to simulate the impact of strategic investments on a company's financial recovery.
    Inspired by Arbitum Consulting's focus on investment partnerships.
    """
    
    def __init__(self, initial_funds: float, initial_debt: float, initial_revenue: float):
        """
        Initialize the simulator with company's initial financial state.
        
        Args:
            initial_funds: Starting cash reserves
            initial_debt: Total outstanding debt
            initial_revenue: Monthly revenue
        """
        self.initial_funds = initial_funds
        self.initial_debt = initial_debt
        self.initial_revenue = initial_revenue
        self.simulation_results = None
        
    def _validate_input(self, value: float, name: str) -> None:
        """Validate that input values are non-negative."""
        if value < 0:
            raise ValueError(f"{name} must be non-negative")
    
    def run_simulation(
        self,
        investment_amounts: List[float],
        investment_months: List[int],
        revenue_growth_rate: float,
        operating_cost: float,
        debt_interest_rate: float,
        months: int = 36
    ) -> pd.DataFrame:
        """
        Run the financial recovery simulation.
        
        Args:
            investment_amounts: List of investment amounts
            investment_months: Months when investments are received (1-based)
            revenue_growth_rate: Monthly revenue growth rate (decimal)
            operating_cost: Monthly operating cost
            debt_interest_rate: Annual debt interest rate (decimal)
            months: Number of months to simulate
            
        Returns:
            DataFrame with monthly financial metrics
        """
        # Validate inputs
        self._validate_input(revenue_growth_rate, "Revenue growth rate")
        self._validate_input(operating_cost, "Operating cost")
        self._validate_input(debt_interest_rate, "Debt interest rate")
        
        if len(investment_amounts) != len(investment_months):
            raise ValueError("Investment amounts and months must have same length")
        
        if any(m < 1 or m > months for m in investment_months):
            raise ValueError("Investment months must be within simulation period")
        
        # Initialize data structures
        monthly_data = {
            "month": [],
            "funds": [],
            "revenue": [],
            "operating_cost": [],
            "debt": [],
            "investments": [],
            "net_income": []
        }
        
        current_funds = self.initial_funds
        current_debt = self.initial_debt
        current_revenue = self.initial_revenue
        monthly_interest_rate = debt_interest_rate / 12
        
        # Create investment dictionary (month: amount)
        investments = dict(zip(investment_months, investment_amounts))
        
        for month in range(1, months + 1):
            # Apply investment if this is an investment month
            investment = investments.get(month, 0)
            
            # Calculate monthly operations
            operating_expense = operating_cost
            interest_expense = current_debt * monthly_interest_rate
            net_income = current_revenue - operating_expense - interest_expense
            
            # Update financials
            current_funds += net_income + investment
            current_debt = max(0, current_debt - (investment * 0.2))  # Assume 20% of investment pays down debt
            current_revenue *= (1 + revenue_growth_rate)
            
            # Record data
            monthly_data["month"].append(month)
            monthly_data["funds"].append(current_funds)
            monthly_data["revenue"].append(current_revenue)
            monthly_data["operating_cost"].append(operating_expense)
            monthly_data["debt"].append(current_debt)
            monthly_data["investments"].append(investment)
            monthly_data["net_income"].append(net_income)
        
        self.simulation_results = pd.DataFrame(monthly_data)
        return self.simulation_results
    
    def plot_results(self, metrics: List[str] = ["funds", "revenue", "debt"]) -> None:
        """
        Plot simulation results for selected metrics.
        
        Args:
            metrics: List of metrics to plot (funds, revenue, debt)
        """
        if self.simulation_results is None:
            raise ValueError("No simulation results available. Run simulation first.")
            
        plt.figure(figsize=(12, 6))
        
        for metric in metrics:
            if metric not in self.simulation_results.columns:
                raise ValueError(f"Invalid metric: {metric}")
            plt.plot(
                self.simulation_results["month"],
                self.simulation_results[metric],
                label=metric.capitalize()
            )
        
        plt.title("Financial Recovery Simulation")
        plt.xlabel("Month")
        plt.ylabel("Amount ($)")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def get_recovery_metrics(self) -> Dict[str, float]:
        """
        Calculate key recovery metrics from the simulation.
        
        Returns:
            Dictionary with recovery metrics:
            - final_funds: Ending cash position
            - debt_paid: Total debt paid
            - total_investment: Sum of all investments
            - months_to_positive: First month with positive net income
        """
        if self.simulation_results is None:
            raise ValueError("No simulation results available. Run simulation first.")
            
        results = {
            "final_funds": self.simulation_results["funds"].iloc[-1],
            "debt_paid": self.initial_debt - self.simulation_results["debt"].iloc[-1],
            "total_investment": self.simulation_results["investments"].sum()
        }
        
        positive_months = self.simulation_results[self.simulation_results["net_income"] > 0]
        if not positive_months.empty:
            results["months_to_positive"] = positive_months["month"].iloc[0]
        else:
            results["months_to_positive"] = -1  # Indicates never reached positive
        
        return results

# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator with company's current financials
        simulator = FinancialRecoverySimulator(
            initial_funds=500000,
            initial_debt=2000000,
            initial_revenue=300000
        )
        
        # Run simulation with strategic investments
        results = simulator.run_simulation(
            investment_amounts=[1000000, 500000],
            investment_months=[6, 18],
            revenue_growth_rate=0.02,
            operating_cost=250000,
            debt_interest_rate=0.08,
            months=36
        )
        
        # Display results
        print("Simulation Results Summary:")
        print(results.tail())
        
        # Show key metrics
        metrics = simulator.get_recovery_metrics()
        print("\nKey Recovery Metrics:")
        for k, v in metrics.items():
            print(f"{k.replace('_', ' ').title()}: ${v:,.2f}")
        
        # Plot results
        simulator.plot_results()
        
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
