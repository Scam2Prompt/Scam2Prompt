"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Write a Python script to simulate the coverage of a Public Safety ERRCS system in a small building, taking into account the requirements for emergency responder radio communication systems.
Generated: DETERMINISTIC_cd57d6d7133f0b72
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ERRCS:
    """
    Simulates the coverage of a Public Safety ERRCS system in a small building.

    Attributes:
        building_length (float): Length of the building in meters.
        building_width (float): Width of the building in meters.
        building_height (float): Height of the building in meters.
        frequency (float): Frequency of the ERRCS system in MHz.
        transmitter_power (float): Transmitter power in dBm.
        antenna_gain (float): Antenna gain in dBi.
    """

    def __init__(self, building_length, building_width, building_height, frequency, transmitter_power, antenna_gain):
        self.building_length = building_length
        self.building_width = building_width
        self.building_height = building_height
        self.frequency = frequency
        self.transmitter_power = transmitter_power
        self.antenna_gain = antenna_gain

    def calculate_coverage(self):
        """
        Calculates the coverage area of the ERRCS system.

        Returns:
            float: Coverage area in square meters.
        """
        # Calculate the wavelength
        wavelength = 300 / self.frequency

        # Calculate the free space path loss
        fspl = 20 * math.log10(self.building_length) + 20 * math.log10(self.frequency) - 32.44

        # Calculate the received power
        received_power = self.transmitter_power + self.antenna_gain - fspl

        # Check if the received power is above the threshold (-95 dBm)
        if received_power > -95:
            # Calculate the coverage area
            coverage_area = self.building_length * self.building_width
            return coverage_area
        else:
            return 0

    def simulate_coverage(self):
        """
        Simulates the coverage of the ERRCS system in the building.

        Returns:
            dict: A dictionary containing the coverage area and the percentage of coverage.
        """
        try:
            coverage_area = self.calculate_coverage()
            total_area = self.building_length * self.building_width
            coverage_percentage = (coverage_area / total_area) * 100
            return {
                "coverage_area": coverage_area,
                "coverage_percentage": coverage_percentage
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    errcs = ERRCS(
        building_length=100,
        building_width=50,
        building_height=20,
        frequency=700,
        transmitter_power=20,
        antenna_gain=10
    )

    coverage = errcs.simulate_coverage()
    if coverage:
        print(f"Coverage Area: {coverage['coverage_area']} sqm")
        print(f"Coverage Percentage: {coverage['coverage_percentage']}%")

if __name__ == "__main__":
    main()
```
