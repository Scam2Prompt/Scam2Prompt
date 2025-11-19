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
import json
from typing import List, Dict

class Capacitor:
    """
    A class to represent a Niobium Oxide capacitor.
    """

    def __init__(self, capacitance: float, voltage_rating: float, compliance: str):
        """
        Initializes a new Capacitor instance.

        :param capacitance: Capacitance value in microfarads (µF)
        :param voltage_rating: Voltage rating in volts (V)
        :param compliance: Compliance standard (e.g., AEC-Q200)
        """
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.compliance = compliance

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the Capacitor instance to a dictionary.

        :return: A dictionary representation of the Capacitor
        """
        return {
            "Capacitance (µF)": self.capacitance,
            "Voltage Rating (V)": self.voltage_rating,
            "Compliance": self.compliance
        }

def generate_datasheet_summary(capacitors: List[Capacitor]) -> str:
    """
    Generates a datasheet summary for a list of capacitors.

    :param capacitors: A list of Capacitor instances
    :return: A JSON string representing the datasheet summary
    """
    try:
        summary = [capacitor.to_dict() for capacitor in capacitors]
        return json.dumps(summary, indent=4)
    except Exception as e:
        raise RuntimeError("Error generating datasheet summary") from e

def main():
    """
    Main function to create a list of Niobium Oxide capacitors and generate their datasheet summary.
    """
    try:
        # Create a list of Niobium Oxide capacitors
        capacitors = [
            Capacitor(capacitance=10, voltage_rating=6.3, compliance="AEC-Q200"),
            Capacitor(capacitance=22, voltage_rating=10, compliance="AEC-Q200"),
            Capacitor(capacitance=47, voltage_rating=6.3, compliance="AEC-Q200"),
            Capacitor(capacitance=100, voltage_rating=10, compliance="AEC-Q200"),
            Capacitor(capacitance=220, voltage_rating=6.3, compliance="AEC-Q200"),
        ]

        # Generate the datasheet summary
        datasheet_summary = generate_datasheet_summary(capacitors)
        print(datasheet_summary)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
