"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the environmental impact of a construction project, factoring in metrics like hours worked and resources used, inspired by INARO S.A.S.'s focus on project optimization.
Generated: DETERMINISTIC_45328cf5a54939f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class ConstructionProjectImpactCalculator:
    """
    A class to calculate the environmental impact of a construction project 
    based on hours worked, resources used, and other metrics.
    """

    def __init__(self, hours_worked, resources_used):
        """
        Initializes the calculator with the project metrics.

        :param hours_worked: Total hours worked on the project (float).
        :param resources_used: Dictionary containing quantities of resources used (e.g., {"concrete": 1000, "steel": 500}).
        """
        self.hours_worked = hours_worked
        self.resources_used = resources_used

    def calculate_energy_consumption(self):
        """
        Calculates estimated energy consumption based on hours worked.
        Assumes an average energy consumption rate of 1.5 kWh/hour.

        :return: Total energy consumption in kWh (float).
        """
        average_energy_rate_per_hour = 1.5  # kWh
        return self.hours_worked * average_energy_rate_per_hour

    def calculate_resource_impact(self):
        """
        Calculates the environmental impact of resources used based on predefined impact factors.

        :return: Total resource impact score (float).
        """
        # Impact factors per unit for resources (arbitrary values for illustration)
        impact_factors = {
            "concrete": 0.5,  # per ton
            "steel": 2.0,     # per ton
            "wood": 0.3       # per ton
        }
        
        total_impact = 0
        for resource, quantity in self.resources_used.items():
            if resource in impact_factors:
                total_impact += quantity * impact_factors[resource]
            else:
                logging.warning(f"Unknown resource: {resource}. No impact factor available.")
        return total_impact

    def calculate_total_impact(self):
        """
        Combines energy consumption and resource impact into a single score.

        :return: Total environmental impact score (float).
        """
        energy_impact = self.calculate_energy_consumption()
        resource_impact = self.calculate_resource_impact()
        return energy_impact + resource_impact


def main():
    """
    Main function to execute the program logic.
    """
    # Enable logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Example project metrics
        hours_worked = 1200  # Example: 1200 hours worked
        resources_used = {
            "concrete": 1500,  # Example: 1500 tons of concrete
            "steel": 800,      # Example: 800 tons of steel
        }

        # Create an instance of the calculator
        calculator = ConstructionProjectImpactCalculator(hours_worked, resources_used)

        # Calculate impacts
        energy_consumption = calculator.calculate_energy_consumption()
        resource_impact = calculator.calculate_resource_impact()
        total_impact = calculator.calculate_total_impact()

        # Display results
        logging.info(f"Energy Consumption (kWh): {energy_consumption:.2f}")
        logging.info(f"Resource Impact Score: {resource_impact:.2f}")
        logging.info(f"Total Environmental Impact Score: {total_impact:.2f}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
