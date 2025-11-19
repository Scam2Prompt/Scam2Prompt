"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write code to generate a datasheet summary for Niobium Oxide capacitors, including voltage ratings up to 10Vr, high capacitance values, and AEC-Q200 compliance, as described on the KYOCERA AVX website.
Generated: DETERMINISTIC_52c104c1bc53b8a0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class NiobiumOxideCapacitor:
    """
    Represents a Niobium Oxide capacitor.
    """

    def __init__(self, part_number, voltage_rating, capacitance, tolerance, esr, operating_temperature):
        """
        Initializes a NiobiumOxideCapacitor object.

        Args:
            part_number (str): The part number of the capacitor.
            voltage_rating (float): The voltage rating of the capacitor in volts.
            capacitance (float): The capacitance value of the capacitor in microfarads.
            tolerance (str): The tolerance of the capacitor (e.g., ±20%).
            esr (float): The equivalent series resistance of the capacitor in milliohms.
            operating_temperature (str): The operating temperature range of the capacitor (e.g., -55°C to 125°C).
        """
        self.part_number = part_number
        self.voltage_rating = voltage_rating
        self.capacitance = capacitance
        self.tolerance = tolerance
        self.esr = esr
        self.operating_temperature = operating_temperature

    def __str__(self):
        return f"Part Number: {self.part_number}\nVoltage Rating: {self.voltage_rating}V\nCapacitance: {self.capacitance}μF\nTolerance: {self.tolerance}\nESR: {self.esr}mΩ\nOperating Temperature: {self.operating_temperature}"

def generate_datasheet_summary(capacitors):
    """
    Generates a datasheet summary for a list of Niobium Oxide capacitors.

    Args:
        capacitors (list[NiobiumOxideCapacitor]): A list of NiobiumOxideCapacitor objects.

    Returns:
        pd.DataFrame: A pandas DataFrame summarizing the capacitors.
    """
    data = []
    for capacitor in capacitors:
        data.append({
            "Part Number": capacitor.part_number,
            "Voltage Rating (V)": capacitor.voltage_rating,
            "Capacitance (μF)": capacitor.capacitance,
            "Tolerance": capacitor.tolerance,
            "ESR (mΩ)": capacitor.esr,
            "Operating Temperature": capacitor.operating_temperature,
            "AEC-Q200 Compliant": "Yes"  # Assuming all capacitors are AEC-Q200 compliant
        })

    df = pd.DataFrame(data)
    return df

def main():
    try:
        # Define capacitors
        capacitors = [
            NiobiumOxideCapacitor("NOJ227M10R", 10, 220, "+/-20%", 35, "-55°C to 125°C"),
            NiobiumOxideCapacitor("NOJ337M06R", 6.3, 330, "+/-20%", 25, "-55°C to 125°C"),
            NiobiumOxideCapacitor("NOJ476M04R", 4, 47, "+/-20%", 150, "-55°C to 125°C"),
        ]

        # Filter capacitors with voltage ratings up to 10V and high capacitance values
        filtered_capacitors = [c for c in capacitors if c.voltage_rating <= 10 and c.capacitance >= 47]

        # Generate datasheet summary
        df = generate_datasheet_summary(filtered_capacitors)

        # Print datasheet summary
        print(df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
