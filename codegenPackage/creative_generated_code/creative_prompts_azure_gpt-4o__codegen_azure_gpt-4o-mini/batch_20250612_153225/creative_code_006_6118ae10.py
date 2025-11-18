"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Create a function to estimate the environmental impact reduction for businesses using renting solutions that promote energy efficiency and renewable energy, as described by Innova Renting.
Generated: DETERMINISTIC_6118ae109580e080
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnvironmentalImpactEstimator:
    """
    A class to estimate the environmental impact reduction for businesses using renting solutions that promote
    energy efficiency and renewable energy.
    """

    def __init__(self, energy_saved: float, emissions_factor: float, renewable_energy_factor: float):
        """
        Initializes the estimator with required parameters.

        Args:
            energy_saved (float): The amount of energy saved by using renting solutions (in kWh).
            emissions_factor (float): The emissions factor for the energy source (in kg CO2 per kWh).
            renewable_energy_factor (float): The proportion of energy that comes from renewable sources (0 to 1).
        """
        self.energy_saved = energy_saved
        self.emissions_factor = emissions_factor
        self.renewable_energy_factor = renewable_energy_factor

    def calculate_emissions_reduction(self) -> float:
        """
        Calculates the reduction in CO2 emissions.

        Returns:
            float: The estimated reduction in CO2 emissions (in kg).
        """
        try:
            # Calculate emissions reduction from energy savings
            emissions_reduction = self.energy_saved * self.emissions_factor * (1 - self.renewable_energy_factor)
            logging.info(f"Calculated emissions reduction: {emissions_reduction} kg CO2")
            return emissions_reduction
        except Exception as e:
            logging.error(f"Error calculating emissions reduction: {e}")
            raise

    def calculate_energy_cost_savings(self, cost_per_kwh: float) -> float:
        """
        Calculates the cost savings associated with the energy saved.

        Args:
            cost_per_kwh (float): The cost of energy per kWh.

        Returns:
            float: The estimated cost savings (in currency).
        """
        try:
            # Calculate cost savings from energy savings
            cost_savings = self.energy_saved * cost_per_kwh
            logging.info(f"Calculated cost savings: {cost_savings} currency units")
            return cost_savings
        except Exception as e:
            logging.error(f"Error calculating cost savings: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the EnvironmentalImpactEstimator
    try:
        estimator = EnvironmentalImpactEstimator(energy_saved=10000, emissions_factor=0.5, renewable_energy_factor=0.3)
        emissions_reduction = estimator.calculate_emissions_reduction()
        cost_savings = estimator.calculate_energy_cost_savings(cost_per_kwh=0.12)

        print(f"Estimated CO2 emissions reduction: {emissions_reduction} kg")
        print(f"Estimated cost savings: {cost_savings} currency units")
    except Exception as e:
        logging.error(f"Error in the main execution block: {e}")
```
