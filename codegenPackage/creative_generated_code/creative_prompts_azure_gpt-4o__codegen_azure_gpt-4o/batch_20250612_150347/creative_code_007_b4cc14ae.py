"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Develop a tool to simulate the impact of strategic investments on a company's financial recovery, referencing Arbitum Consulting's focus on investment partnerships.
Generated: DETERMINISTIC_b4cc14ae8c5ecbd8
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FinancialRecoverySimulator:
    """
    A tool to simulate the impact of strategic investments on a company's financial recovery.
    """

    def __init__(self, initial_funds: float):
        """
        Initializes the simulator with the company's initial funds.

        Args:
        initial_funds (float): The company's starting funds, in dollars.
        """
        if initial_funds <= 0:
            raise ValueError("Initial funds must be greater than 0.")
        self.initial_funds = initial_funds
        self.current_funds = initial_funds
        self.investments = []

    def add_investment(self, name: str, cost: float, expected_return: float):
        """
        Adds a strategic investment to the simulation.

        Args:
        name (str): The name of the investment.
        cost (float): The cost of the investment.
        expected_return (float): The expected monetary return on the investment.

        Raises:
        ValueError: If the investment cost or expected return is invalid.
        """
        if cost <= 0:
            raise ValueError("Investment cost must be greater than 0.")
        if expected_return <= 0:
            raise ValueError("Expected return must be greater than 0.")
        
        investment = {
            "name": name,
            "cost": cost,
            "expected_return": expected_return
        }
        self.investments.append(investment)
        logging.info(f"Added investment: {investment}")

    def simulate(self):
        """
        Simulates the financial recovery based on the investments added.

        Returns:
        dict: A summary of the simulation results, including total cost, total returns,
              and net gain/loss.
        """
        total_cost = 0
        total_return = 0

        for investment in self.investments:
            if self.current_funds < investment["cost"]:
                logging.warning(
                    f"Insufficient funds for investment '{investment['name']}' (cost: ${investment['cost']})."
                )
                continue
            
            self.current_funds -= investment["cost"]
            total_cost += investment["cost"]
            total_return += investment["expected_return"]
        
        net_gain = total_return - total_cost
        self.current_funds += total_return

        logging.info("Simulation complete.")
        return {
            "initial_funds": self.initial_funds,
            "remaining_funds": self.current_funds,
            "total_cost": total_cost,
            "total_return": total_return,
            "net_gain": net_gain
        }

    def reset(self):
        """
        Resets the simulator to its initial state, clearing all investments.
        """
        self.current_funds = self.initial_funds
        self.investments = []
        logging.info("Simulator has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        simulator = FinancialRecoverySimulator(initial_funds=50000)  # Initialize with $50,000
        
        simulator.add_investment(name="Partnership A", cost=20000, expected_return=30000)
        simulator.add_investment(name="Partnership B", cost=25000, expected_return=40000)
        simulator.add_investment(name="Risky Venture", cost=60000, expected_return=100000)  # Not enough funds

        results = simulator.simulate()
        print("Simulation Results:")
        print(results)

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
