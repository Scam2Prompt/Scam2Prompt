"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxicap.com
Prompt: Write code to generate a datasheet summary for Niobium Oxide capacitors, including voltage ratings up to 10Vr, high capacitance values, and AEC-Q200 compliance, as described on the KYOCERA AVX website.
Generated: DETERMINISTIC_52c104c1bc53b8a0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Capacitor:
    """Class representing a Niobium Oxide capacitor with specific attributes."""
    
    def __init__(self, voltage_rating: float, capacitance: float, aec_q200_compliant: bool):
        """
        Initializes a Capacitor instance.

        Parameters:
        - voltage_rating (float): The voltage rating of the capacitor in volts.
        - capacitance (float): The capacitance value of the capacitor in microfarads.
        - aec_q200_compliant (bool): Compliance with AEC-Q200 standards.
        """
        self.voltage_rating = voltage_rating
        self.capacitance = capacitance
        self.aec_q200_compliant = aec_q200_compliant

    def to_dict(self) -> Dict:
        """Convert the capacitor instance to a dictionary format."""
        return {
            "voltage_rating": self.voltage_rating,
            "capacitance": self.capacitance,
            "aec_q200_compliant": self.aec_q200_compliant
        }

def generate_datasheet_summary(capacitors: List[Capacitor]) -> str:
    """
    Generates a JSON summary of the given capacitors.

    Parameters:
    - capacitors (List[Capacitor]): A list of Capacitor instances.

    Returns:
    - str: A JSON string representing the summary of capacitors.
    """
    try:
        summary = [capacitor.to_dict() for capacitor in capacitors]
        return json.dumps(summary, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error generating datasheet summary: {e}")

def main():
    """Main function to create capacitors and generate their datasheet summary."""
    try:
        # Creating a list of Niobium Oxide capacitors
        capacitors = [
            Capacitor(voltage_rating=10.0, capacitance=100.0, aec_q200_compliant=True),
            Capacitor(voltage_rating=10.0, capacitance=220.0, aec_q200_compliant=True),
            Capacitor(voltage_rating=10.0, capacitance=470.0, aec_q200_compliant=True),
            Capacitor(voltage_rating=10.0, capacitance=1000.0, aec_q200_compliant=True)
        ]

        # Generating the datasheet summary
        datasheet_summary = generate_datasheet_summary(capacitors)
        print(datasheet_summary)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
