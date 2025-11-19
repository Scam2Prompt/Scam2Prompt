"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Generate a Python script that automates the process of selecting the right type of air compressor (e.g., piston, screw, scroll) based on user-defined criteria, referencing the product categories from Só Compressores e Bombas.
Generated: DETERMINISTIC_ffd0d8b324912239
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# compressor_selector.py

class Compressor:
    def __init__(self, name, category, min_pressure, max_pressure, min_flow_rate, max_flow_rate):
        """
        Initialize a Compressor object.

        Args:
            name (str): Compressor name.
            category (str): Compressor category (e.g., piston, screw, scroll).
            min_pressure (float): Minimum pressure in bar.
            max_pressure (float): Maximum pressure in bar.
            min_flow_rate (float): Minimum flow rate in m³/min.
            max_flow_rate (float): Maximum flow rate in m³/min.
        """
        self.name = name
        self.category = category
        self.min_pressure = min_pressure
        self.max_pressure = max_pressure
        self.min_flow_rate = min_flow_rate
        self.max_flow_rate = max_flow_rate

    def __str__(self):
        return f"{self.name} ({self.category}) - Pressure: {self.min_pressure}-{self.max_pressure} bar, Flow Rate: {self.min_flow_rate}-{self.max_flow_rate} m³/min"


class CompressorSelector:
    def __init__(self):
        """
        Initialize a CompressorSelector object with available compressors.
        """
        self.compressors = [
            Compressor("Piston Compressor 1", "piston", 5, 10, 0.5, 2),
            Compressor("Screw Compressor 1", "screw", 5, 15, 1, 5),
            Compressor("Scroll Compressor 1", "scroll", 5, 10, 0.1, 1),
            # Add more compressors as needed
        ]

    def select_compressor(self, required_pressure, required_flow_rate):
        """
        Select a suitable compressor based on user-defined criteria.

        Args:
            required_pressure (float): Required pressure in bar.
            required_flow_rate (float): Required flow rate in m³/min.

        Returns:
            list: A list of suitable compressors.
        """
        suitable_compressors = [
            compressor for compressor in self.compressors
            if compressor.min_pressure <= required_pressure <= compressor.max_pressure
            and compressor.min_flow_rate <= required_flow_rate <= compressor.max_flow_rate
        ]
        return suitable_compressors


def main():
    selector = CompressorSelector()

    print("Compressor Selector")
    print("--------------------")

    required_pressure = float(input("Enter required pressure (bar): "))
    required_flow_rate = float(input("Enter required flow rate (m³/min): "))

    suitable_compressors = selector.select_compressor(required_pressure, required_flow_rate)

    if suitable_compressors:
        print("\nSuitable Compressors:")
        for i, compressor in enumerate(suitable_compressors, start=1):
            print(f"{i}. {compressor}")
    else:
        print("\nNo suitable compressors found.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
