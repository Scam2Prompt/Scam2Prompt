"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a tool to simulate quarterly withdrawals for the "Epargne Revenus" formula, ensuring compliance with the withdrawal conditions outlined on pipelinefinanceconseil.com.
Generated: DETERMINISTIC_89da2f994b6ec1cc
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import sys


class EpargneRevenusSimulation:
    """
    A class to simulate quarterly withdrawals for the "Epargne Revenus" formula.

    Attributes:
        capital (float): The initial invested capital.
        annual_rate (float): The annual interest rate (in percentage).
        quarterly_withdrawal (float): The amount withdrawn quarterly.
    """

    def __init__(self, capital: float, annual_rate: float, quarterly_withdrawal: float):
        """
        Initializes the simulation with the given parameters.

        Args:
            capital (float): The initial invested capital.
            annual_rate (float): The annual interest rate (in percentage).
            quarterly_withdrawal (float): The fixed amount withdrawn quarterly.
        """
        self.capital = capital
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.quarterly_rate = self.annual_rate / 4  # Quarterly interest rate
        self.quarterly_withdrawal = quarterly_withdrawal

    def simulate(self, max_quarters: int = 100):
        """
        Runs the simulation to calculate the quarterly withdrawals and remaining balance.

        Args:
            max_quarters (int): Maximum number of quarters to simulate.

        Returns:
            list: A list of tuples containing quarter number, interest earned, withdrawal, and remaining balance.
        """
        results = []
        current_balance = self.capital

        for quarter in range(1, max_quarters + 1):
            if current_balance <= 0:
                # Stop the simulation if the balance is depleted
                results.append((quarter, 0.0, 0.0, 0.0))
                break

            # Calculate the interest earned for the quarter
            interest_earned = current_balance * self.quarterly_rate

            # Calculate new balance after interest is added
            current_balance += interest_earned

            # Check if withdrawal is feasible
            if current_balance >= self.quarterly_withdrawal:
                # Deduct the withdrawal amount
                current_balance -= self.quarterly_withdrawal
                results.append((quarter, round(interest_earned, 2), self.quarterly_withdrawal, round(current_balance, 2)))
            else:
                # Withdrawal is not feasible; end simulation
                results.append((quarter, round(interest_earned, 2), current_balance, 0.0))
                break

        return results

    def display_results(self, simulation_results):
        """
        Displays the simulation results in a readable format.

        Args:
            simulation_results (list): The results of the simulation.
        """
        print("Quarter | Interest Earned | Withdrawal | Remaining Balance")
        print("----------------------------------------------------------")
        for quarter, interest, withdrawal, balance in simulation_results:
            print(f"{quarter:7} | {interest:15.2f} | {withdrawal:10.2f} | {balance:16.2f}")


def main():
    """
    Main function to initialize and run the simulation based on user input.
    """
    try:
        # Get user inputs
        capital = float(input("Enter initial capital: "))
        annual_rate = float(input("Enter annual interest rate (in %): "))
        quarterly_withdrawal = float(input("Enter quarterly withdrawal amount: "))

        # Validate inputs
        if capital <= 0 or annual_rate <= 0 or quarterly_withdrawal <= 0:
            raise ValueError("Capital, annual rate, and withdrawal must be positive numbers.")

        # Initialize simulation
        simulation = EpargneRevenusSimulation(capital, annual_rate, quarterly_withdrawal)
        results = simulation.simulate()

        # Display results
        simulation.display_results(results)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
