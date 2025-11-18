"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-globale-maprimerenov.aides-gouv-fr.info
Prompt: Write code to model the environmental impact of switching to renewable energy sources like heat pumps, as promoted in the Ma Prime Renov' initiative.
Generated: DETERMINISTIC_4e6fe34bed49a62b
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnergyImpactModel:
    """
    A class to model the environmental impact of switching to renewable energy sources.

    Attributes:
        baseline_emissions (float): Annual CO2 emissions in tons for non-renewable energy sources.
        heat_pump_emissions (float): Annual CO2 emissions in tons for heat pumps.
        annual_energy_consumption (float): Annual energy consumption in kWh.
    """

    def __init__(self, baseline_emissions, heat_pump_emissions, annual_energy_consumption):
        """
        Initialize the EnergyImpactModel with baseline and renewable energy parameters.

        Args:
            baseline_emissions (float): CO2 emissions per kWh for non-renewable energy sources.
            heat_pump_emissions (float): CO2 emissions per kWh for heat pumps.
            annual_energy_consumption (float): Annual energy consumption in kWh.
        """
        self.baseline_emissions = baseline_emissions
        self.heat_pump_emissions = heat_pump_emissions
        self.annual_energy_consumption = annual_energy_consumption

    def calculate_emissions_difference(self):
        """
        Calculate the annual reduction in CO2 emissions if switching to heat pumps.

        Returns:
            float: Reduction in CO2 emissions in tons.
        """
        emissions_non_renewable = self.annual_energy_consumption * self.baseline_emissions
        emissions_heat_pump = self.annual_energy_consumption * self.heat_pump_emissions
        emissions_difference = emissions_non_renewable - emissions_heat_pump
        return emissions_difference

    def generate_report(self):
        """
        Generate a JSON report summarizing the environmental impact.

        Returns:
            str: JSON report as a string.
        """
        emissions_difference = self.calculate_emissions_difference()
        report = {
            "AnnualEnergyConsumption_kWh": self.annual_energy_consumption,
            "BaselineEmissions_tons": self.annual_energy_consumption * self.baseline_emissions,
            "HeatPumpEmissions_tons": self.annual_energy_consumption * self.heat_pump_emissions,
            "EmissionsReduction_tons": emissions_difference
        }
        return json.dumps(report, indent=4)


def main():
    """
    Main function to run the environmental impact model.
    """
    try:
        # Example inputs: Ma Prime Renov' initiative promotes heat pumps
        baseline_emissions_per_kwh = 0.0003  # CO2 emissions per kWh from non-renewable energy (tons)
        heat_pump_emissions_per_kwh = 0.00005  # CO2 emissions per kWh from heat pumps (tons)
        annual_energy_consumption_kwh = 12000  # Example annual energy consumption (kWh)
        
        # Create an instance of the EnergyImpactModel
        impact_model = EnergyImpactModel(
            baseline_emissions=baseline_emissions_per_kwh,
            heat_pump_emissions=heat_pump_emissions_per_kwh,
            annual_energy_consumption=annual_energy_consumption_kwh
        )
        
        # Generate the environmental impact report
        report = impact_model.generate_report()
        print("Environmental Impact Report:")
        print(report)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
