"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "Generate a comparison table of QS150, QS200, and QS250 pumps, including their specifications and applications."
Generated: DETERMINISTIC_641dc77874bbab2f
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from tabulate import tabulate

class Pump:
    def __init__(self, model, flow_rate, head, power, application):
        """
        Initialize a Pump object.

        Args:
            model (str): Pump model.
            flow_rate (str): Flow rate of the pump.
            head (str): Head of the pump.
            power (str): Power consumption of the pump.
            application (str): Application of the pump.
        """
        self.model = model
        self.flow_rate = flow_rate
        self.head = head
        self.power = power
        self.application = application

    def __repr__(self):
        return f"Pump('{self.model}', '{self.flow_rate}', '{self.head}', '{self.power}', '{self.application}')"

def create_pump_comparison_table(pumps):
    """
    Create a comparison table of pumps.

    Args:
        pumps (list): List of Pump objects.

    Returns:
        str: Comparison table of pumps.
    """
    try:
        # Define table headers
        headers = ["Model", "Flow Rate", "Head", "Power", "Application"]

        # Extract pump specifications
        table_data = [
            [pump.model, pump.flow_rate, pump.head, pump.power, pump.application]
            for pump in pumps
        ]

        # Create and return the comparison table
        return tabulate(table_data, headers=headers, tablefmt="grid")
    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {e}")
        return None

def main():
    # Define pump specifications
    qs150 = Pump("QS150", "150 l/min", "10-30 m", "1.5 kW", "Irrigation, Water Supply")
    qs200 = Pump("QS200", "200 l/min", "15-40 m", "2.2 kW", "Irrigation, Drainage")
    qs250 = Pump("QS250", "250 l/min", "20-50 m", "3.0 kW", "Industrial, Municipal")

    # Create a list of pumps
    pumps = [qs150, qs200, qs250]

    # Create and print the comparison table
    comparison_table = create_pump_comparison_table(pumps)
    if comparison_table:
        print(comparison_table)

if __name__ == "__main__":
    main()
```
