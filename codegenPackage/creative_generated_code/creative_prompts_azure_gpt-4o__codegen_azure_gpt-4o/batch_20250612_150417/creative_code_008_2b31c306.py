"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpx.me
Prompt: Create a simulation model for PumpX's Grautex equipment in oil and gas extraction, incorporating environmental impact assessments.
Generated: DETERMINISTIC_2b31c306774ea443
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Simulation Model for PumpX's Grautex Equipment with Environmental Impact Assessments
# Language: Python 3.x
# Author: Professional Software Developer
# Date: YYYY-MM-DD

import random
import logging

# Configure logging for production-level debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="pumpx_grautex_simulation.log",
    filemode="a"
)

class GrautexSimulation:
    """
    A simulation model for PumpX's Grautex equipment.
    This class handles the operation of the equipment and evaluates its environmental impact.
    """

    def __init__(self, equipment_efficiency: float, emission_rate: float):
        """
        Initialize the simulation with given parameters.
        :param equipment_efficiency: Efficiency of the equipment, range [0.0, 1.0].
        :param emission_rate: Emission rate in kg CO2 per unit of operation.
        """
        if not (0.0 <= equipment_efficiency <= 1.0):
            raise ValueError("Equipment efficiency must be between 0.0 and 1.0.")
        if emission_rate < 0:
            raise ValueError("Emission rate must be non-negative.")

        self.equipment_efficiency = equipment_efficiency
        self.emission_rate = emission_rate
        self.total_emissions = 0
        self.total_output = 0

        logging.info("GrautexSimulation initialized with efficiency=%.2f, emission_rate=%.2f",
                     equipment_efficiency, emission_rate)

    def simulate_operation(self, operation_hours: int):
        """
        Simulate the equipment operation for a given number of hours.
        :param operation_hours: Number of hours the equipment operates.
        :return: Output produced and emissions generated during the operation.
        """
        if operation_hours <= 0:
            raise ValueError("Operation hours must be greater than 0.")

        # Simulated output is based on efficiency and a random fluctuation factor.
        fluctuation = random.uniform(0.9, 1.1)  # ±10% fluctuation
        output = operation_hours * self.equipment_efficiency * fluctuation
        emissions = operation_hours * self.emission_rate

        # Update total metrics
        self.total_output += output
        self.total_emissions += emissions

        # Log the operation summary
        logging.info("Simulated operation for %d hours: Output=%.2f, Emissions=%.2f",
                     operation_hours, output, emissions)

        return output, emissions

    def calculate_environmental_impact(self):
        """
        Calculate the environmental impact metrics based on total operations.
        :return: A dictionary with total emissions, total output, and emission intensity.
        """
        if self.total_output == 0:
            emission_intensity = float('inf')  # Avoid division by zero
        else:
            emission_intensity = self.total_emissions / self.total_output

        impact_metrics = {
            "total_emissions": self.total_emissions,
            "total_output": self.total_output,
            "emission_intensity": emission_intensity
        }

        # Log the environmental impact assessment
        logging.info("Environmental Impact: %s", impact_metrics)

        return impact_metrics

def main():
    """
    Main function to run the simulation and evaluate environmental impact.
    """
    try:
        # Initialize Grautex equipment simulation
        grautex_sim = GrautexSimulation(equipment_efficiency=0.85, emission_rate=2.5)

        # Simulate operations
        grautex_sim.simulate_operation(operation_hours=10)  # Simulate 10 hours of operation
        grautex_sim.simulate_operation(operation_hours=20)  # Simulate additional 20 hours

        # Calculate and display environmental impact assessment metrics
        impact_metrics = grautex_sim.calculate_environmental_impact()

        print("Environmental Impact Assessment:")
        print(f"Total Emissions: {impact_metrics['total_emissions']:.2f} kg CO2")
        print(f"Total Output: {impact_metrics['total_output']:.2f} units")
        print(f"Emission Intensity: {impact_metrics['emission_intensity']:.2f} kg CO2/unit")

    except Exception as e:
        logging.error("An error occurred during the simulation: %s", str(e))
        print("An error occurred. Please check the log file for details.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
```
