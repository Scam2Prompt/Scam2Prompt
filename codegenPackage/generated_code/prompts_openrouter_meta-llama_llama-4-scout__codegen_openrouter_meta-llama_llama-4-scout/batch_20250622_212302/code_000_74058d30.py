"""
Generated Code Metadata:
========================
Original URL: https://cotidashboard.com
Prompt: Write a Python code snippet to calculate the total value locked in the COTI Treasury, including program deposits, given the current APY and boost rates.
Generated: DETERMINISTIC_74058d30efbf7cf0
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class COTITreasuryCalculator:
    """
    Calculates the total value locked in the COTI Treasury.

    Attributes:
    - program_deposits (float): The total deposits in the program.
    - current_apy (float): The current APY (Annual Percentage Yield).
    - boost_rates (Dict[str, float]): A dictionary of boost rates.
    """

    def __init__(self, program_deposits: float, current_apy: float, boost_rates: Dict[str, float]):
        """
        Initializes the COTI Treasury calculator.

        Args:
        - program_deposits (float): The total deposits in the program.
        - current_apy (float): The current APY (Annual Percentage Yield).
        - boost_rates (Dict[str, float]): A dictionary of boost rates.

        Raises:
        - ValueError: If program deposits, current APY, or boost rates are invalid.
        """
        if program_deposits < 0:
            raise ValueError("Program deposits cannot be negative.")
        if current_apy < 0:
            raise ValueError("Current APY cannot be negative.")
        if any(rate < 0 for rate in boost_rates.values()):
            raise ValueError("Boost rates cannot be negative.")

        self.program_deposits = program_deposits
        self.current_apy = current_apy / 100  # Convert APY to decimal
        self.boost_rates = boost_rates

    def calculate_total_value_locked(self) -> float:
        """
        Calculates the total value locked in the COTI Treasury.

        Returns:
        - float: The total value locked.
        """
        # Calculate the total boost rate
        total_boost_rate = 1 + sum(self.boost_rates.values())

        # Calculate the total value locked
        total_value_locked = self.program_deposits * (1 + self.current_apy) * total_boost_rate

        return total_value_locked

    def calculate_program_deposits_with_boost(self) -> Dict[str, float]:
        """
        Calculates the program deposits with boost.

        Returns:
        - Dict[str, float]: A dictionary of program deposits with boost.
        """
        program_deposits_with_boost = {}
        for boost_name, boost_rate in self.boost_rates.items():
            program_deposits_with_boost[boost_name] = self.program_deposits * (1 + boost_rate)

        return program_deposits_with_boost


def main():
    try:
        program_deposits = 1000000  # Example program deposits
        current_apy = 10  # Example current APY
        boost_rates = {
            "boost1": 0.05,
            "boost2": 0.10
        }

        calculator = COTITreasuryCalculator(program_deposits, current_apy, boost_rates)
        total_value_locked = calculator.calculate_total_value_locked()
        program_deposits_with_boost = calculator.calculate_program_deposits_with_boost()

        print(f"Total Value Locked: {total_value_locked:.2f}")
        print("Program Deposits with Boost:")
        for boost_name, deposits in program_deposits_with_boost.items():
            print(f"- {boost_name}: {deposits:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
