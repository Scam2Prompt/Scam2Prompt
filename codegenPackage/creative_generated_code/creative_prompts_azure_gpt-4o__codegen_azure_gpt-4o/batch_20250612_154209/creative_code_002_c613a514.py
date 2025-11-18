"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-globale-maprimerenov.aides-gouv-fr.info
Prompt: Create a script to simulate the impact of installing a heat pump and insulation on energy bills, using the guidelines from Ma Prime Renov' 2024.
Generated: DETERMINISTIC_c613a5147c40d278
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class EnergyBillSimulator:
    """
    A class to simulate the impact of installing a heat pump and insulation 
    on energy bills, using guidelines similar to Ma Prime Renov' 2024.
    """

    def __init__(self, current_energy_bill, insulation_reduction_rate=0.25, heat_pump_efficiency_rate=0.40):
        """
        Initialize the simulator.

        :param current_energy_bill: Current monthly energy bill in euros.
        :param insulation_reduction_rate: Percentage reduction due to insulation (default: 25%).
        :param heat_pump_efficiency_rate: Percentage reduction due to heat pump (default: 40%).
        """
        self.current_energy_bill = current_energy_bill
        self.insulation_reduction_rate = insulation_reduction_rate
        self.heat_pump_efficiency_rate = heat_pump_efficiency_rate

    def calculate_energy_bill_after_insulation(self):
        """
        Calculates the energy bill after applying insulation.

        :return: Energy bill after insulation in euros.
        """
        return self.current_energy_bill * (1 - self.insulation_reduction_rate)

    def calculate_energy_bill_with_heat_pump(self, post_insulation_bill):
        """
        Calculates the energy bill after installing a heat pump.

        :param post_insulation_bill: Energy bill after insulation in euros.
        :return: Energy bill after heat pump installation in euros.
        """
        return post_insulation_bill * (1 - self.heat_pump_efficiency_rate)

    def simulate(self):
        """
        Simulates the impact of insulation and heat pump on the energy bill.

        :return: A dictionary containing the energy bill details.
        """
        try:
            post_insulation_bill = self.calculate_energy_bill_after_insulation()
            post_heat_pump_bill = self.calculate_energy_bill_with_heat_pump(post_insulation_bill)

            return {
                "current_energy_bill": round(self.current_energy_bill, 2),
                "post_insulation_bill": round(post_insulation_bill, 2),
                "post_heat_pump_bill": round(post_heat_pump_bill, 2),
                "total_savings": round(self.current_energy_bill - post_heat_pump_bill, 2),
            }
        except Exception as e:
            # Catch any unexpected errors during calculation
            print(f"Error during simulation: {e}")
            return None


if __name__ == "__main__":
    # Example usage of the Energy Bill Simulator
    try:
        # Input: Current monthly energy bill in euros
        current_energy_bill = float(input("Enter your current energy bill (€/month): "))

        # Initialize the simulator
        simulator = EnergyBillSimulator(current_energy_bill)

        # Run the simulation
        results = simulator.simulate()

        if results:
            print("\nSimulation Results:")
            print(f"Current Energy Bill: €{results['current_energy_bill']}/month")
            print(f"Energy Bill After Insulation: €{results['post_insulation_bill']}/month")
            print(f"Energy Bill After Heat Pump Installation: €{results['post_heat_pump_bill']}/month")
            print(f"Total Monthly Savings: €{results['total_savings']}/month")
        else:
            print("Could not complete the simulation due to an error.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the energy bill.")
```
