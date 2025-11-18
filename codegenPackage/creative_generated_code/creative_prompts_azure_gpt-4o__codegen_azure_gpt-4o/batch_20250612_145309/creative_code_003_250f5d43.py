"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haciendodestinos.com
Prompt: Create a program that simulates the economic impact of implementing T.R.E.S. tourism strategies in Argentina, as proposed by Haciendo Destinos.
Generated: DETERMINISTIC_250f5d431820b031
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class TourismStrategySimulator:
    """
    Simulates the economic impact of implementing T.R.E.S. (Tourism, Resources, Economy, Sustainability) 
    strategies in Argentina.
    """

    def __init__(self, initial_budget, growth_rate, sustainability_factor, years):
        """
        Initializes the simulation with key parameters.

        :param initial_budget: The initial budget allocated to tourism in millions of USD.
        :param growth_rate: Expected annual growth rate in tourism revenue due to T.R.E.S. strategies (percentage).
        :param sustainability_factor: Factor representing sustainability impact on long-term growth (0-1).
        :param years: Number of years to simulate.
        """
        self.initial_budget = initial_budget
        self.growth_rate = growth_rate
        self.sustainability_factor = sustainability_factor
        self.years = years

    def simulate(self):
        """
        Runs the simulation and returns the result as a list of yearly economic impact data.
        """
        results = []
        current_revenue = self.initial_budget

        # Simulate year-by-year results
        for year in range(1, self.years + 1):
            # Apply growth rate
            growth = current_revenue * (self.growth_rate / 100)

            # Adjust growth by sustainability factor
            adjusted_growth = growth * self.sustainability_factor

            # Update revenue for the year
            current_revenue += adjusted_growth

            # Simulate potential volatility due to external factors (random +/- 5%)
            volatility = random.uniform(-0.05, 0.05)
            current_revenue *= (1 + volatility)

            # Ensure revenue does not fall below zero
            current_revenue = max(0, current_revenue)

            # Store the result for this year
            results.append({
                "Year": year,
                "Revenue (in millions USD)": round(current_revenue, 2),
                "Growth (in millions USD)": round(adjusted_growth, 2),
                "Volatility Factor": round(volatility, 4)
            })

        return results

    def display_results(self, results):
        """
        Displays the simulation results in a readable format.

        :param results: List of yearly economic impact data.
        """
        print("\nEconomic Impact Simulation Results for T.R.E.S. Strategies in Argentina:")
        print("-" * 70)
        print(f"{'Year':<10}{'Revenue (M USD)':<20}{'Growth (M USD)':<20}{'Volatility':<10}")
        print("-" * 70)

        for result in results:
            print(f"{result['Year']:<10}{result['Revenue (in millions USD)']:<20}{result['Growth (in millions USD)']:<20}{result['Volatility Factor']:<10.4f}")

        print("-" * 70)


# Main function to execute the simulation
def main():
    """
    Entry point to the program. Initializes and runs the T.R.E.S. economic impact simulation.
    """
    try:
        # Input parameters for the simulation
        initial_budget = float(input("Enter the initial tourism budget (in millions USD): "))
        growth_rate = float(input("Enter the expected annual growth rate (as a percentage): "))
        sustainability_factor = float(input("Enter the sustainability factor (0-1): "))
        years = int(input("Enter the number of years to simulate: "))

        # Validate inputs
        if not (0 <= sustainability_factor <= 1):
            raise ValueError("Sustainability factor must be between 0 and 1.")
        if years <= 0:
            raise ValueError("Number of years must be a positive integer.")

        # Create simulator instance and run simulation
        simulator = TourismStrategySimulator(initial_budget, growth_rate, sustainability_factor, years)
        results = simulator.simulate()

        # Display results
        simulator.display_results(results)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
```
