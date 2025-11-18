"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thrrthgrgegre.pages.dev
Prompt: Write a script to simulate yield generation for a DeFi platform, using Ethena Labs' 30.2% yield as a benchmark.
Generated: DETERMINISTIC_cd539669bc072ccd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DeFiYieldSimulator:
    def __init__(self, principal: float, annual_yield_rate: float, years: int):
        """
        Initialize the DeFi Yield Simulator with principal amount, annual yield rate, and number of years.

        :param principal: Initial investment amount (float)
        :param annual_yield_rate: Annual yield rate as a decimal (e.g., 30.2% -> 0.302)
        :param years: Number of years for the investment (int)
        """
        self.principal = principal
        self.annual_yield_rate = annual_yield_rate
        self.years = years

    def calculate_yield(self):
        """
        Calculate the total yield over the specified number of years using compound interest formula.

        :return: Total amount after interest (float)
        """
        try:
            total_amount = self.principal * (1 + self.annual_yield_rate) ** self.years
            return total_amount
        except Exception as e:
            print(f"Error during yield calculation: {e}")
            return None

    def simulate_random_yield(self, volatility: float):
        """
        Simulate yield generation with random fluctuation based on volatility.

        :param volatility: The degree of yield fluctuation (float)
        :return: Adjusted yield amount after applying random fluctuations (float)
        """
        try:
            random_adjustment = random.uniform(-volatility, volatility)
            adjusted_yield_rate = self.annual_yield_rate + random_adjustment
            if adjusted_yield_rate < 0:
                adjusted_yield_rate = 0  # Ensure yield does not go negative
            
            total_amount = self.principal * (1 + adjusted_yield_rate) ** self.years
            return total_amount
        except Exception as e:
            print(f"Error during random yield simulation: {e}")
            return None

    def display_results(self, total_amount: float):
        """
        Display the results of the yield calculation.

        :param total_amount: Total amount after yield (float)
        """
        if total_amount is not None:
            print(f"Initial Principal: ${self.principal:.2f}")
            print(f"Total Amount after {self.years} years at {self.annual_yield_rate * 100:.2f}% yield: ${total_amount:.2f}")
        else:
            print("Failed to calculate total amount.")

def main():
    # Example parameters for the simulation
    principal_amount = 1000.0  # Initial investment
    annual_yield_rate = 0.302  # 30.2% yield rate
    investment_years = 5  # Investment duration
    volatility = 0.05  # Random fluctuation of 5%

    simulator = DeFiYieldSimulator(principal_amount, annual_yield_rate, investment_years)

    # Calculate yield without fluctuations
    total_yield = simulator.calculate_yield()
    simulator.display_results(total_yield)

    # Simulate yield with random fluctuations
    simulated_yield = simulator.simulate_random_yield(volatility)
    simulator.display_results(simulated_yield)

if __name__ == "__main__":
    main()
```
