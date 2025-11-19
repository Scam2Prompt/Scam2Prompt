"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haciendodestinos.com
Prompt: Develop a program that simulates the employment growth potential of the tourism sector in Argentina, using the statistics and strategies from Haciendo Destinos as a foundation.
Generated: DETERMINISTIC_10c91c48be8a930d
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TourismEmploymentSimulator:
    """
    A class to simulate employment growth potential in the tourism sector in Argentina, 
    based on statistics and strategies from Haciendo Destinos.
    """

    def __init__(self, base_employment, growth_rate, years):
        """
        Initialize the simulator with base employment, growth rate, and simulation years.

        :param base_employment: (int) Current number of employees in the tourism sector
        :param growth_rate: (float) Expected annual growth rate (percentage as a decimal)
        :param years: (int) Number of years to simulate
        """
        self.base_employment = base_employment
        self.growth_rate = growth_rate
        self.years = years

    def simulate_growth(self):
        """
        Simulates employment growth over the specified number of years.

        :return: (list) A list of employment levels for each year
        """
        employment_projection = []
        current_employment = self.base_employment

        for year in range(1, self.years + 1):
            # Calculate employment projection for the year
            current_employment += current_employment * self.growth_rate
            employment_projection.append({
                'year': year,
                'employment': int(current_employment)  # Round to nearest integer
            })

        return employment_projection

    def save_results(self, filename):
        """
        Saves simulation results to a JSON file.

        :param filename: (str) File path to save the results
        """
        try:
            results = self.simulate_growth()
            with open(filename, 'w') as file:
                json.dump(results, file, indent=4)
            print(f"Results successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving results to file: {e}")

def main():
    """
    Main function to run the simulator.
    """
    print("Welcome to the Tourism Employment Growth Simulator!")
    
    # Get user inputs with error handling
    try:
        base_employment = int(input("Enter the current employment level in the tourism sector: "))
        growth_rate = float(input("Enter the expected annual growth rate (percentage as a decimal, e.g., 0.05 for 5%): "))
        years = int(input("Enter the number of years to simulate: "))
    except ValueError:
        print("Invalid input. Please ensure you enter numbers where required.")
        return

    # Ensure inputs are sensible
    if base_employment <= 0 or growth_rate <= 0 or years <= 0:
        print("All inputs must be positive numbers.")
        return

    # Initialize and run the simulator
    simulator = TourismEmploymentSimulator(base_employment, growth_rate, years)
    results = simulator.simulate_growth()

    # Display results
    print("\nSimulation Results:")
    for result in results:
        print(f"Year {result['year']}: Employment = {result['employment']}")

    # Save results to file
    save_option = input("Do you want to save the results to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        filename = input("Enter the filename (e.g., results.json): ").strip()
        simulator.save_results(filename)
    else:
        print("Results not saved.")

if __name__ == '__main__':
    main()
```
