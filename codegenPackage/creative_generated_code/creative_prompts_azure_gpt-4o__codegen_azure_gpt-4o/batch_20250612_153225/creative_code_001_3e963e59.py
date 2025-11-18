"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Generate a script to calculate the optimal configuration for solar panel installations using Growatt series systems and Enphase parallel systems, as described on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_3e963e591e8e2754
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class SolarPanelOptimizer:
    """
    Class to calculate the optimal configuration for solar panel installations
    using Growatt series systems and Enphase parallel systems.
    """

    def __init__(self, total_power_requirement, solar_panel_power, system_type):
        """
        Initialize the optimizer with required parameters.

        :param total_power_requirement: Total power requirement in kW (kilowatts).
        :param solar_panel_power: Power output of a single solar panel in kW.
        :param system_type: Type of system - 'Growatt' for series, 'Enphase' for parallel.
        """
        self.total_power_requirement = total_power_requirement
        self.solar_panel_power = solar_panel_power
        self.system_type = system_type.lower()

    def calculate_optimal_configuration(self):
        """
        Calculate the optimal number of solar panels and system configuration.

        :return: A dictionary with the configuration details.
        """
        try:
            # Calculate the number of panels required
            number_of_panels = math.ceil(self.total_power_requirement / self.solar_panel_power)

            if self.system_type == 'growatt':
                # Series system: Panels connected sequentially, system efficiency depends on weakest panel
                return {
                    "system_type": "Growatt (Series)",
                    "number_of_panels": number_of_panels,
                    "total_power_output": number_of_panels * self.solar_panel_power,
                    "notes": "Ensure all panels are similar and evenly exposed to sunlight for optimal performance."
                }
            elif self.system_type == 'enphase':
                # Parallel system: Panels operate independently, better for varying conditions
                return {
                    "system_type": "Enphase (Parallel)",
                    "number_of_panels": number_of_panels,
                    "total_power_output": number_of_panels * self.solar_panel_power,
                    "notes": "Best for installations with varying sunlight exposure levels between panels."
                }
            else:
                raise ValueError("Invalid system_type provided. Use 'Growatt' or 'Enphase'.")

        except Exception as e:
            return {
                "error": str(e),
                "message": "An error occurred while calculating the solar panel configuration."
            }

    @staticmethod
    def validate_inputs(total_power_requirement, solar_panel_power):
        """
        Validate the user inputs for total power requirement and solar panel power.

        :param total_power_requirement: Total power requirement in kW (kilowatts).
        :param solar_panel_power: Power output of a single solar panel in kW.
        :return: True if inputs are valid, False otherwise.
        """
        if total_power_requirement <= 0:
            raise ValueError("Total power requirement must be greater than 0.")
        if solar_panel_power <= 0:
            raise ValueError("Solar panel power must be greater than 0.")
        return True


if __name__ == "__main__":
    # Example user inputs
    try:
        total_power_requirement = float(input("Enter total power requirement in kW: "))
        solar_panel_power = float(input("Enter power output of a single solar panel in kW: "))
        system_type = input("Enter system type ('Growatt' for series or 'Enphase' for parallel): ")

        # Validate inputs
        SolarPanelOptimizer.validate_inputs(total_power_requirement, solar_panel_power)

        # Initialize optimizer and calculate configuration
        optimizer = SolarPanelOptimizer(total_power_requirement, solar_panel_power, system_type)
        optimal_configuration = optimizer.calculate_optimal_configuration()

        # Display configuration
        if "error" in optimal_configuration:
            print(f"Error: {optimal_configuration['error']}")
        else:
            print("\nOptimal Configuration:")
            for key, value in optimal_configuration.items():
                print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
