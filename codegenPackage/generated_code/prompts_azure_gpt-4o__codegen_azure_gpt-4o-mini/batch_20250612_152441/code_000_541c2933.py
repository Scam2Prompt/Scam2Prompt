"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Write a Python script to simulate the energy efficiency benefits of UPVC windows and doors, referencing the features described on the Dexodoor website.
Generated: DETERMINISTIC_541c29339af63ca5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class UPVCWindowDoor:
    """
    A class to simulate the energy efficiency benefits of UPVC windows and doors.
    """

    def __init__(self, insulation_rating, air_leakage, solar_gain):
        """
        Initializes the UPVCWindowDoor instance with insulation rating, air leakage, and solar gain.

        :param insulation_rating: The insulation rating of the window/door (higher is better).
        :param air_leakage: The air leakage rate (lower is better).
        :param solar_gain: The solar gain coefficient (higher is better).
        """
        self.insulation_rating = insulation_rating
        self.air_leakage = air_leakage
        self.solar_gain = solar_gain

    def calculate_energy_savings(self, outside_temp, inside_temp, hours):
        """
        Calculates the energy savings based on temperature difference and time.

        :param outside_temp: The outside temperature in degrees Celsius.
        :param inside_temp: The desired inside temperature in degrees Celsius.
        :param hours: The number of hours to simulate.
        :return: Estimated energy savings in kWh.
        """
        try:
            # Calculate temperature difference
            temp_difference = inside_temp - outside_temp
            
            # Calculate energy savings based on insulation rating and air leakage
            energy_loss = (temp_difference / self.insulation_rating) * (1 + self.air_leakage)
            energy_savings = energy_loss * hours
            
            # Adjust savings based on solar gain
            energy_savings *= (1 + self.solar_gain)

            return round(energy_savings, 2)

        except ZeroDivisionError:
            print("Error: Insulation rating cannot be zero.")
            return 0.0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0.0

def main():
    """
    Main function to simulate the energy efficiency benefits of UPVC windows and doors.
    """
    # Example parameters for UPVC windows and doors
    insulation_rating = 3.0  # Higher is better
    air_leakage = 0.1        # Lower is better
    solar_gain = 0.3         # Higher is better

    # Create an instance of UPVCWindowDoor
    upvc_window_door = UPVCWindowDoor(insulation_rating, air_leakage, solar_gain)

    # Simulate energy savings
    outside_temp = random.uniform(-10, 30)  # Random outside temperature
    inside_temp = 20                         # Desired inside temperature
    hours = 24                               # Number of hours

    # Calculate energy savings
    energy_savings = upvc_window_door.calculate_energy_savings(outside_temp, inside_temp, hours)

    # Output the results
    print(f"Outside Temperature: {outside_temp:.2f} °C")
    print(f"Inside Temperature: {inside_temp} °C")
    print(f"Estimated Energy Savings over {hours} hours: {energy_savings} kWh")

if __name__ == "__main__":
    main()
```
