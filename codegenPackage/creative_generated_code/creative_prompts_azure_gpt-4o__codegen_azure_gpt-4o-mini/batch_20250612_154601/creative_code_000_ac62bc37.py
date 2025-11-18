"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Write Python code to calculate the energy efficiency (A++) of an air conditioning system based on the specifications provided for the Gree Bora A4 Silver series on the Frigoterm website.
Generated: DETERMINISTIC_ac62bc37a77328e6
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirConditioner:
    """
    A class to represent an air conditioning system and calculate its energy efficiency (A++).
    """

    def __init__(self, cooling_capacity_kW, input_power_kW):
        """
        Initializes the AirConditioner instance.

        :param cooling_capacity_kW: The cooling capacity of the air conditioning unit in kW.
        :param input_power_kW: The input power of the air conditioning unit in kW.
        """
        self.cooling_capacity_kW = cooling_capacity_kW
        self.input_power_kW = input_power_kW

    def calculate_energy_efficiency(self):
        """
        Calculate the Energy Efficiency Ratio (EER) of the air conditioning system.

        :return: The EER value as a float, or raises ValueError if input values are invalid.
        """
        if self.input_power_kW <= 0:
            raise ValueError("Input power must be greater than zero.")
        if self.cooling_capacity_kW <= 0:
            raise ValueError("Cooling capacity must be greater than zero.")

        # Calculate the Energy Efficiency Ratio (EER)
        eer = self.cooling_capacity_kW / self.input_power_kW
        return eer

    def classify_efficiency(self):
        """
        Classify the air conditioning system based on its energy efficiency ratio.

        :return: A string indicating the efficiency classification (e.g., 'A++', 'A+', etc.).
        """
        eer = self.calculate_energy_efficiency()

        # Classify based on EER ranges (example values, update as per actual standards)
        if eer >= 4.0:
            return 'A++'
        elif 3.6 <= eer < 4.0:
            return 'A+'
        elif 3.2 <= eer < 3.6:
            return 'A'
        else:
            return 'B or lower'

def main():
    """
    Main function to execute the program logic.
    """
    try:
        # Example specifications for the Gree Bora A4 Silver series
        cooling_capacity = 3.5  # in kW
        input_power = 0.9       # in kW

        # Create an AirConditioner instance
        ac_unit = AirConditioner(cooling_capacity, input_power)

        # Calculate EER and classify efficiency
        efficiency_ratio = ac_unit.calculate_energy_efficiency()
        efficiency_classification = ac_unit.classify_efficiency()

        # Output the results
        print(f"Energy Efficiency Ratio (EER): {efficiency_ratio:.2f}")
        print(f"Energy Efficiency Classification: {efficiency_classification}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
