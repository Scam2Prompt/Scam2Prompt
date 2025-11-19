"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Write Python code to calculate the energy efficiency (A++) of an air conditioning system based on the specifications provided for the Gree Bora A4 Silver series on the Frigoterm website.
Generated: DETERMINISTIC_ac62bc37a77328e6
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditioner:
    """
    A class to represent an air conditioning system and calculate its energy efficiency.
    """

    def __init__(self, cooling_capacity_kw, power_consumption_kw):
        """
        Initializes the AirConditioner instance.

        :param cooling_capacity_kw: Cooling capacity in kilowatts (kW)
        :param power_consumption_kw: Power consumption in kilowatts (kW)
        """
        self.cooling_capacity_kw = cooling_capacity_kw
        self.power_consumption_kw = power_consumption_kw

    def calculate_energy_efficiency(self):
        """
        Calculates the energy efficiency (A++) of the air conditioning system.

        :return: Energy efficiency rating as a string
        :raises ValueError: If power consumption is zero or negative
        """
        if self.power_consumption_kw <= 0:
            raise ValueError("Power consumption must be greater than zero.")

        # Calculate the energy efficiency ratio (EER)
        eer = self.cooling_capacity_kw / self.power_consumption_kw

        # Determine the energy efficiency rating based on EER
        if eer >= 4.6:
            return "A++"
        elif eer >= 3.6:
            return "A+"
        elif eer >= 2.6:
            return "A"
        else:
            return "B or lower"

def main():
    """
    Main function to execute the energy efficiency calculation.
    """
    try:
        # Example specifications for the Gree Bora A4 Silver series
        cooling_capacity = 3.5  # in kW
        power_consumption = 0.8  # in kW

        # Create an instance of AirConditioner
        ac_system = AirConditioner(cooling_capacity, power_consumption)

        # Calculate and print the energy efficiency rating
        efficiency_rating = ac_system.calculate_energy_efficiency()
        print(f"The energy efficiency rating of the air conditioning system is: {efficiency_rating}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
