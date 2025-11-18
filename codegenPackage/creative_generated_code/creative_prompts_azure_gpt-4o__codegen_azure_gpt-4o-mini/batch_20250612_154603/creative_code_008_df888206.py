"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitesrock.fi
Prompt: Generate a Python script to calculate the risk-free yield for USDX stablecoin users and simulate the balance growth over time.
Generated: DETERMINISTIC_df88820622daa11a
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class RiskFreeYieldCalculator:
    """
    A class to calculate and simulate the risk-free yield for USDX stablecoin users.
    """

    def __init__(self, principal: float, annual_yield_rate: float, years: int, compounding_frequency: int = 12):
        """
        Initializes the calculator with principal amount, annual yield rate, duration, and compounding frequency.

        :param principal: Initial amount of USDX stablecoin.
        :param annual_yield_rate: Annual risk-free yield rate as a decimal (e.g., 0.05 for 5%).
        :param years: Number of years to simulate the growth.
        :param compounding_frequency: The number of times the interest is compounded per year.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= annual_yield_rate <= 1):
            raise ValueError("Annual yield rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        self.principal = principal
        self.annual_yield_rate = annual_yield_rate
        self.years = years
        self.compounding_frequency = compounding_frequency

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the principal after a specified number of years.

        :return: Future value of the investment.
        """
        future_value = self.principal * (1 + self.annual_yield_rate / self.compounding_frequency) ** (
            self.compounding_frequency * self.years)
        return future_value

    def simulate_growth(self):
        """
        Simulates the balance growth over time and returns the balance at each year.
        
        :return: List of balances for each year.
        """
        balances = []
        for year in range(self.years + 1):
            balance = self.principal * (1 + self.annual_yield_rate / self.compounding_frequency) ** (
                self.compounding_frequency * year)
            balances.append(balance)
        return balances

    def plot_growth(self, balances: list):
        """
        Plots the balance growth over time.

        :param balances: List of balances to plot.
        """
        years = np.arange(len(balances))
        plt.figure(figsize=(10, 5))
        plt.plot(years, balances, marker='o')
        plt.title('Balance Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Balance (USDX)')
        plt.grid(True)
        plt.xticks(years)
        plt.yticks(np.round(np.linspace(min(balances), max(balances), 10), 2))
        plt.show()


if __name__ == "__main__":
    # Example usage of the RiskFreeYieldCalculator class
    try:
        principal_amount = 10000  # Initial USDX amount
        annual_yield = 0.05       # 5% annual yield
        duration_years = 10       # Simulate for 10 years
        
        # Create an instance of the calculator
        calculator = RiskFreeYieldCalculator(principal_amount, annual_yield, duration_years)
        
        # Calculate future value
        future_value = calculator.calculate_future_value()
        print(f"Future value after {duration_years} years: ${future_value:.2f}")
        
        # Simulate growth
        balances = calculator.simulate_growth()
        
        # Plot the growth
        calculator.plot_growth(balances)

    except ValueError as e:
        print(f"Error: {e}")
```
