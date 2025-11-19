"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a script that models the impact of quarterly withdrawals on a savings plan with a variable average rate of 9.24%, reflecting the features of Pipeline Finance Conseil.
Generated: DETERMINISTIC_7420d2b7251b9fb9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class SavingsPlanSimulator:
    """
    A class to simulate the impact of quarterly withdrawals on a savings plan
    with a variable average rate of return.
    """

    def __init__(self, initial_balance: float, annual_rate: float = 0.0924):
        """
        Initialize the savings plan simulator.

        Args:
            initial_balance (float): Initial savings balance.
            annual_rate (float): Average annual rate of return (default: 9.24%).
        """
        self.initial_balance = initial_balance
        self.annual_rate = annual_rate
        self.quarterly_rate = (1 + annual_rate) ** (1/4) - 1

    def simulate(
        self,
        quarters: int,
        quarterly_withdrawal: float,
        rate_variability: float = 0.02
    ) -> Tuple[List[float], List[float]]:
        """
        Simulate the savings plan over a number of quarters with withdrawals.

        Args:
            quarters (int): Number of quarters to simulate.
            quarterly_withdrawal (float): Amount withdrawn each quarter.
            rate_variability (float): Variability in quarterly rate (default: 2%).

        Returns:
            Tuple[List[float], List[float]]: (balance_history, rate_history)
        """
        if not isinstance(quarters, int) or quarters <= 0:
            raise ValueError("Quarters must be a positive integer.")
        if quarterly_withdrawal < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if rate_variability < 0 or rate_variability > 1:
            raise ValueError("Rate variability must be between 0 and 1.")

        balance_history = []
        rate_history = []
        current_balance = self.initial_balance

        for _ in range(quarters):
            # Apply variable rate
            variable_rate = self.quarterly_rate + np.random.uniform(
                -rate_variability/4, rate_variability/4
            )
            current_balance *= (1 + variable_rate)
            
            # Apply withdrawal
            if current_balance >= quarterly_withdrawal:
                current_balance -= quarterly_withdrawal
            else:
                current_balance = 0  # Account is depleted

            balance_history.append(current_balance)
            rate_history.append(variable_rate * 4)  # Annualize for reporting

            if current_balance <= 0:
                break  # Stop simulation if balance is depleted

        return balance_history, rate_history

    def plot_simulation(
        self,
        balance_history: List[float],
        rate_history: List[float],
        title: str = "Savings Plan Simulation"
    ) -> None:
        """
        Plot the simulation results.

        Args:
            balance_history (List[float]): Historical balance data.
            rate_history (List[float]): Historical rate data.
            title (str): Plot title.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot balance
        ax1.plot(balance_history, label='Account Balance', color='blue')
        ax1.set_title(f"{title} - Balance Over Time")
        ax1.set_ylabel('Balance ($)')
        ax1.grid(True)
        ax1.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        
        # Plot rates
        ax2.plot(rate_history, label='Annualized Rate', color='green')
        ax2.set_title("Rate Variability")
        ax2.set_ylabel('Annual Rate')
        ax2.set_xlabel('Quarters')
        ax2.grid(True)
        ax2.axhline(y=self.annual_rate, color='red', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        simulator = SavingsPlanSimulator(initial_balance=100000)
        balances, rates = simulator.simulate(
            quarters=40,  # 10 years
            quarterly_withdrawal=5000,
            rate_variability=0.02
        )
        simulator.plot_simulation(balances, rates)
    except Exception as e:
        print(f"Error during simulation: {e}")
```
