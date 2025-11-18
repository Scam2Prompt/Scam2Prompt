"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Create a Python script to simulate investment growth over time based on the wealth creation strategies mentioned on the Australia Wide Wealth Services website.
Generated: DETERMINISTIC_26e561554d369dd8
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

class InvestmentSimulator:
    """
    A class to simulate investment growth over time based on specific strategies.
    """

    def __init__(self, initial_investment, annual_rate_of_return, years):
        """
        Initialize the investment simulator with required parameters.
        
        :param initial_investment: Initial amount of money to invest.
        :param annual_rate_of_return: Expected annual rate of return (as a decimal).
        :param years: Number of years to simulate the investment growth.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if not (0 <= annual_rate_of_return <= 1):
            raise ValueError("Annual rate of return must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")

        self.initial_investment = initial_investment
        self.annual_rate_of_return = annual_rate_of_return
        self.years = years

    def calculate_growth(self):
        """
        Calculate the investment growth over the specified number of years.
        
        :return: A list of investment values at the end of each year.
        """
        growth_values = []
        for year in range(self.years + 1):
            future_value = self.initial_investment * (1 + self.annual_rate_of_return) ** year
            growth_values.append(future_value)
        return growth_values

    def plot_growth(self, growth_values):
        """
        Plot the investment growth over time.

        :param growth_values: A list of investment values to plot.
        """
        years = list(range(self.years + 1))
        plt.figure(figsize=(10, 5))
        plt.plot(years, growth_values, marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.grid(True)
        plt.xticks(years)
        plt.axhline(y=self.initial_investment, color='r', linestyle='--', label='Initial Investment')
        plt.legend()
        plt.show()


def main():
    """
    Main function to run the investment simulator.
    """
    try:
        # User input for simulation parameters
        initial_investment = float(input("Enter the initial investment amount ($): "))
        annual_rate_of_return = float(input("Enter the annual rate of return (as a percentage): ")) / 100
        years = int(input("Enter the number of years to simulate: "))

        # Create an instance of InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, annual_rate_of_return, years)

        # Calculate the growth of investment
        growth_values = simulator.calculate_growth()

        # Plot the results
        simulator.plot_growth(growth_values)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
