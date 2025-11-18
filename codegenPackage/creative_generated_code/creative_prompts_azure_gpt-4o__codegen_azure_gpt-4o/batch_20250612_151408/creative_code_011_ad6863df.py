"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Develop a Python program to simulate Engel live bait cooler aeration performance, including parameters for water volume and aerator pump specifications.
Generated: DETERMINISTIC_ad6863df14833719
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class EngelBaitCooler:
    """
    Class to simulate Engel live bait cooler aeration performance.

    Attributes:
        water_volume (float): Volume of water in the cooler (in liters).
        pump_flow_rate (float): Flow rate of the aerator pump (in liters per minute).
        oxygen_transfer_rate (float): Rate at which oxygen is transferred into the water (in mg/L/min).
    """
    def __init__(self, water_volume, pump_flow_rate, oxygen_transfer_rate):
        """
        Initialize the Engel bait cooler simulation parameters.

        Args:
            water_volume (float): Volume of water in the cooler (in liters).
            pump_flow_rate (float): Flow rate of the aerator pump (in liters per minute).
            oxygen_transfer_rate (float): Oxygen transfer efficiency (in mg/L/min).
        """
        if water_volume <= 0:
            raise ValueError("Water volume must be greater than zero.")
        if pump_flow_rate <= 0:
            raise ValueError("Pump flow rate must be greater than zero.")
        if oxygen_transfer_rate <= 0:
            raise ValueError("Oxygen transfer rate must be greater than zero.")

        self.water_volume = water_volume
        self.pump_flow_rate = pump_flow_rate
        self.oxygen_transfer_rate = oxygen_transfer_rate

    def calculate_dissolved_oxygen(self, time_minutes):
        """
        Calculate the dissolved oxygen level in the water after a given time.

        Args:
            time_minutes (float): Time for which the aerator runs (in minutes).

        Returns:
            float: Dissolved oxygen level in the water (in mg/L).
        """
        if time_minutes < 0:
            raise ValueError("Time must be non-negative.")

        # Formula to calculate dissolved oxygen: 
        # dissolved_oxygen = oxygen_transfer_rate * time_minutes
        dissolved_oxygen = self.oxygen_transfer_rate * time_minutes

        # Simulate saturation limit (e.g., assume max dissolved oxygen is 10 mg/L)
        max_dissolved_oxygen = 10.0
        return min(dissolved_oxygen, max_dissolved_oxygen)

    def simulate_aeration(self, time_minutes):
        """
        Simulate the aeration process and provide performance metrics.

        Args:
            time_minutes (float): Time for which the aerator runs (in minutes).

        Returns:
            dict: Simulation results including dissolved oxygen and aerator performance.
        """
        dissolved_oxygen = self.calculate_dissolved_oxygen(time_minutes)
        oxygen_added = dissolved_oxygen * self.water_volume  # Total oxygen added (in mg)

        return {
            "time_minutes": time_minutes,
            "water_volume": self.water_volume,
            "pump_flow_rate": self.pump_flow_rate,
            "oxygen_transfer_rate": self.oxygen_transfer_rate,
            "dissolved_oxygen": dissolved_oxygen,
            "oxygen_added": oxygen_added
        }

def main():
    """
    Main function to simulate Engel live bait cooler aeration performance.
    """
    try:
        # Input parameters for simulation
        water_volume = float(input("Enter water volume in liters: "))
        pump_flow_rate = float(input("Enter pump flow rate in liters per minute: "))
        oxygen_transfer_rate = float(input("Enter oxygen transfer rate in mg/L/min: "))
        time_minutes = float(input("Enter aeration time in minutes: "))

        # Create an instance of EngelBaitCooler
        cooler = EngelBaitCooler(water_volume, pump_flow_rate, oxygen_transfer_rate)

        # Perform simulation
        results = cooler.simulate_aeration(time_minutes)

        # Display results
        print("\nSimulation Results:")
        for key, value in results.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
