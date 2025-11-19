"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Generate a Python script to visualize the buy-and-build model of acquiring and growing multiple youth mental healthcare firms.
Generated: DETERMINISTIC_5fefe917cb7abfb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class MentalHealthFirm:
    """
    A class to represent a mental healthcare firm.
    """

    def __init__(self, name, initial_value, growth_rate):
        """
        Initialize a new mental healthcare firm.

        :param name: str - The name of the firm.
        :param initial_value: float - The initial value of the firm.
        :param growth_rate: float - The annual growth rate of the firm (as a decimal).
        """
        self.name = name
        self.initial_value = initial_value
        self.growth_rate = growth_rate

    def value_over_years(self, years):
        """
        Calculate the value of the firm over a number of years.

        :param years: int - The number of years to project.
        :return: list - The projected values of the firm over the specified years.
        """
        return [self.initial_value * (1 + self.growth_rate) ** year for year in range(years + 1)]

def visualize_buy_and_build(firms, years):
    """
    Visualize the buy-and-build model of acquiring and growing multiple mental healthcare firms.

    :param firms: list - A list of MentalHealthFirm objects.
    :param years: int - The number of years to project.
    """
    plt.figure(figsize=(10, 6))

    # Generate a color map for the firms
    colors = plt.cm.viridis(np.linspace(0, 1, len(firms)))

    for firm, color in zip(firms, colors):
        values = firm.value_over_years(years)
        plt.plot(range(years + 1), values, label=firm.name, color=color)
    
    plt.title('Buy-and-Build Model: Growth of Mental Healthcare Firms')
    plt.xlabel('Years')
    plt.ylabel('Firm Value ($)')
    plt.xticks(range(years + 1))
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the visualization of the buy-and-build model.
    """
    try:
        # Define the firms with their initial values and growth rates
        firms = [
            MentalHealthFirm("Firm A", 1_000_000, 0.10),  # 10% growth
            MentalHealthFirm("Firm B", 500_000, 0.15),   # 15% growth
            MentalHealthFirm("Firm C", 750_000, 0.12)    # 12% growth
        ]

        # Define the number of years for projection
        years = 10

        # Visualize the growth of the firms
        visualize_buy_and_build(firms, years)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
