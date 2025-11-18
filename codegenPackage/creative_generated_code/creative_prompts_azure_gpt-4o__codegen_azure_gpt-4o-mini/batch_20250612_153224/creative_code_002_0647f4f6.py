"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Generate a script in Python to calculate the energy savings of using VinaRoy air blowers in wastewater treatment applications.
Generated: DETERMINISTIC_0647f4f61c311085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EnergySavingsCalculator:
    """
    A class to calculate energy savings from using VinaRoy air blowers 
    in wastewater treatment applications.
    """

    def __init__(self, old_blower_power, new_blower_power, operating_hours, days_per_year):
        """
        Initializes the EnergySavingsCalculator with the given parameters.

        :param old_blower_power: Power consumption of the old blower in kW
        :param new_blower_power: Power consumption of the new VinaRoy blower in kW
        :param operating_hours: Number of hours the blowers operate per day
        :param days_per_year: Number of days the blowers operate per year
        """
        self.old_blower_power = old_blower_power
        self.new_blower_power = new_blower_power
        self.operating_hours = operating_hours
        self.days_per_year = days_per_year

    def calculate_energy_savings(self):
        """
        Calculate the annual energy savings by replacing the old blower 
        with the new VinaRoy blower.

        :return: Annual energy savings in kWh
        """
        try:
            # Calculate the annual energy consumption for both blowers
            old_blower_energy = self.old_blower_power * self.operating_hours * self.days_per_year
            new_blower_energy = self.new_blower_power * self.operating_hours * self.days_per_year
            
            # Calculate energy savings
            energy_savings = old_blower_energy - new_blower_energy
            
            return energy_savings
        
        except Exception as e:
            print(f"Error occurred during calculation: {e}")
            return None

def main():
    """
    Main function to execute the energy savings calculation.
    """
    # Input parameters (these can also come from user input or config)
    old_blower_power = 15.0  # kW
    new_blower_power = 10.0   # kW
    operating_hours = 24       # hours per day
    days_per_year = 365       # days per year

    # Create an instance of the EnergySavingsCalculator
    calculator = EnergySavingsCalculator(old_blower_power, new_blower_power, operating_hours, days_per_year)

    # Calculate and print energy savings
    savings = calculator.calculate_energy_savings()
    
    if savings is not None:
        print(f"Annual energy savings from using VinaRoy air blowers: {savings:.2f} kWh")

if __name__ == "__main__":
    main()
```
