"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Provide code to model the environmental benefits of clean energy adoption in rural Kenya, as described in Sauti Kenya's briquette-making initiative.
Generated: DETERMINISTIC_a6e351401b48eed3
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CleanEnergyModel:
    """
    A class to model the environmental benefits of clean energy adoption.
    Specifically tailored for the Sauti Kenya briquette-making initiative.
    """

    def __init__(self, community_name, annual_energy_consumption, briquette_emission_factor, charcoal_emission_factor):
        """
        Initialize the model with community details and energy parameters.

        :param community_name: Name of the rural community being modeled.
        :param annual_energy_consumption: Annual energy consumption in tons.
        :param briquette_emission_factor: Emission factor for briquettes (kg CO2 / ton).
        :param charcoal_emission_factor: Emission factor for charcoal (kg CO2 / ton).
        """
        self.community_name = community_name
        self.annual_energy_consumption = annual_energy_consumption
        self.briquette_emission_factor = briquette_emission_factor
        self.charcoal_emission_factor = charcoal_emission_factor

    def calculate_emission_savings(self):
        """
        Calculate the annual emission savings when switching from charcoal to briquettes.

        :return: Emission savings in kilograms of CO2.
        """
        charcoal_emissions = self.annual_energy_consumption * self.charcoal_emission_factor
        briquette_emissions = self.annual_energy_consumption * self.briquette_emission_factor
        emission_savings = charcoal_emissions - briquette_emissions

        return emission_savings

    def generate_report(self):
        """
        Generate a report summarizing the environmental benefits.

        :return: A dictionary with the calculated emission savings and related details.
        """
        try:
            emission_savings = self.calculate_emission_savings()
            report = {
                "community_name": self.community_name,
                "annual_energy_consumption": self.annual_energy_consumption,
                "charcoal_emission_factor": self.charcoal_emission_factor,
                "briquette_emission_factor": self.briquette_emission_factor,
                "emission_savings_kg_CO2": emission_savings
            }
            return report
        except Exception as e:
            print(f"Error generating report: {e}")
            return None


def save_report_to_file(report, file_name):
    """
    Save the environmental benefits report to a JSON file.

    :param report: The report dictionary containing data about emissions savings.
    :param file_name: The name of the file to save the report.
    """
    try:
        with open(file_name, 'w') as file:
            json.dump(report, file, indent=4)
        print(f"Report saved successfully to {file_name}")
    except Exception as e:
        print(f"Error saving report to file: {e}")


# Example usage
if __name__ == "__main__":
    # Parameters for the Sauti Kenya initiative
    community_name = "Rural Kenya Community"
    annual_energy_consumption = 1000  # tons
    briquette_emission_factor = 50   # kg CO2 / ton
    charcoal_emission_factor = 150   # kg CO2 / ton

    # Create the model object
    model = CleanEnergyModel(community_name, annual_energy_consumption, briquette_emission_factor, charcoal_emission_factor)

    # Generate the report
    report = model.generate_report()

    # Save the report to a file
    if report:
        save_report_to_file(report, "environmental_benefits_report.json")
```
