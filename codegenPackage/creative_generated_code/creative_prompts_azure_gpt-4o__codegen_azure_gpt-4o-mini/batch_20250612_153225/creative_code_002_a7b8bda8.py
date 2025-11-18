"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Create a script to simulate the reduction in CO₂ emissions achieved by using solar panels, based on the data and goals outlined by Soltec Solutions.
Generated: DETERMINISTIC_a7b8bda8a7341690
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SolarPanelEmissionsSimulator:
    def __init__(self, emission_factor: float, annual_solar_output: float):
        """
        Initializes the simulation with the given parameters.
        
        :param emission_factor: The CO₂ emission factor in kg CO₂/kWh for traditional energy sources
        :param annual_solar_output: The annual output of solar panels in kWh
        """
        self.emission_factor = emission_factor
        self.annual_solar_output = annual_solar_output

    def calculate_emissions_reduction(self) -> float:
        """
        Calculates the reduction in CO₂ emissions achieved by using solar panels.
        
        :return: The reduction in CO₂ emissions in kg
        """
        # Calculate the emissions reduction
        emissions_reduction = self.annual_solar_output * self.emission_factor
        return emissions_reduction

    def simulate(self, years: int) -> pd.DataFrame:
        """
        Simulates the CO₂ emissions reduction over a specified number of years.
        
        :param years: The number of years to simulate
        :return: A DataFrame containing the emissions reduction for each year
        """
        if years <= 0:
            raise ValueError("The number of years must be a positive integer.")

        # Create a DataFrame to hold the simulation results
        results = {
            "Year": [],
            "Emissions Reduction (kg CO₂)": []
        }

        for year in range(1, years + 1):
            reduction = self.calculate_emissions_reduction()
            results["Year"].append(year)
            results["Emissions Reduction (kg CO₂)"].append(reduction)

        return pd.DataFrame(results)


def main():
    try:
        # Example parameters
        emission_factor = 0.5  # kg CO₂/kWh for traditional energy
        annual_solar_output = 10000  # kWh produced by solar panels annually

        # Create an instance of the simulator
        simulator = SolarPanelEmissionsSimulator(emission_factor, annual_solar_output)

        # Simulate for 10 years
        years_to_simulate = 10
        emissions_reduction_df = simulator.simulate(years_to_simulate)

        # Output the results
        print(emissions_reduction_df)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
