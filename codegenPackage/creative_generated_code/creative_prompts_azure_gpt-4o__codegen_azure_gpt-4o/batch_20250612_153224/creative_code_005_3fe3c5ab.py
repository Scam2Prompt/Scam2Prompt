"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Develop a program to compare the cost savings of switching to photovoltaic solar energy for businesses, using the advantages highlighted by Nexe Energetic.
Generated: DETERMINISTIC_3fe3c5abfa42b4dc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SolarCostComparison:
    """
    This class handles the computation and comparison of solar energy savings.
    """

    def __init__(self, current_energy_cost, solar_installation_cost, annual_solar_energy_savings, years):
        """
        Initialize the SolarCostComparison object with the required inputs.

        :param current_energy_cost: Annual energy cost without solar (in USD)
        :param solar_installation_cost: One-time cost of solar installation (in USD)
        :param annual_solar_energy_savings: Annual savings with solar energy (in USD)
        :param years: The period of comparison in years
        """
        self.current_energy_cost = current_energy_cost
        self.solar_installation_cost = solar_installation_cost
        self.annual_solar_energy_savings = annual_solar_energy_savings
        self.years = years

    def calculate_total_cost_without_solar(self):
        """
        Calculate the total cost of energy without solar over the specified period.

        :return: Total cost without solar (in USD)
        """
        return self.current_energy_cost * self.years

    def calculate_total_cost_with_solar(self):
        """
        Calculate the total cost of energy with solar over the specified period.

        :return: Total cost with solar (in USD)
        """
        return self.solar_installation_cost + (self.current_energy_cost - self.annual_solar_energy_savings) * self.years

    def calculate_savings(self):
        """
        Calculate the cost savings from switching to solar energy.

        :return: Cost savings (in USD)
        """
        return self.calculate_total_cost_without_solar() - self.calculate_total_cost_with_solar()

    def print_comparison(self):
        """
        Print a detailed comparison of costs and savings.
        """
        without_solar = self.calculate_total_cost_without_solar()
        with_solar = self.calculate_total_cost_with_solar()
        savings = self.calculate_savings()

        print("\n--- Solar Energy Cost Comparison ---")
        print(f"Total cost over {self.years} years without solar: ${without_solar:,}")
        print(f"Total cost over {self.years} years with solar: ${with_solar:,}")
        print(f"Total savings by switching to solar: ${savings:,}")
        print("-------------------------------------")


def main():
    """
    Main function to execute the solar cost comparison program.
    """
    try:
        # Collect user input
        current_energy_cost = float(input("Enter your annual energy cost (in USD): "))
        solar_installation_cost = float(input("Enter the one-time solar installation cost (in USD): "))
        annual_solar_energy_savings = float(input("Enter the annual savings with solar energy (in USD): "))
        years = int(input("Enter the number of years to compare: "))

        # Validate input
        if current_energy_cost < 0 or solar_installation_cost < 0 or annual_solar_energy_savings < 0 or years <= 0:
            raise ValueError("All input values must be positive.")

        # Perform comparison
        comparison = SolarCostComparison(current_energy_cost, solar_installation_cost, annual_solar_energy_savings, years)
        comparison.print_comparison()

    except ValueError as e:
        print(f"Error: {e}. Please provide valid input values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Solar Cost Comparison Tool!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
```
