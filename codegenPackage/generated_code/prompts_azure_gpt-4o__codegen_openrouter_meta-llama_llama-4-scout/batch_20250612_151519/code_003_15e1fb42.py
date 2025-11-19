"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Write a script to automate the selection of fire prevention motobombas based on specifications like flow rate and pressure, referencing the BPI FIT model.
Generated: DETERMINISTIC_15e1fb429ae2a4ea
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_prevention_motobomba_selector.py

"""
Script to automate the selection of fire prevention motobombas based on specifications like flow rate and pressure,
referencing the BPI FIT model.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd

# Define the BPI FIT model data
class BPIFITModel:
    def __init__(self):
        # Sample BPI FIT model data (replace with actual data)
        self.model_data = pd.DataFrame({
            'Model': ['BPI-10', 'BPI-20', 'BPI-30', 'BPI-40', 'BPI-50'],
            'Flow Rate (m³/h)': [10, 20, 30, 40, 50],
            'Pressure (bar)': [5, 7, 9, 11, 13]
        })

    def get_compatible_motobombas(self, required_flow_rate, required_pressure):
        """
        Returns a list of compatible motobombas based on the required flow rate and pressure.

        Args:
            required_flow_rate (float): The required flow rate in m³/h.
            required_pressure (float): The required pressure in bar.

        Returns:
            list: A list of compatible motobomba models.
        """
        compatible_motobombas = self.model_data[
            (self.model_data['Flow Rate (m³/h)'] >= required_flow_rate) &
            (self.model_data['Pressure (bar)'] >= required_pressure)
        ]

        return compatible_motobombas


def main():
    try:
        # Initialize the BPI FIT model
        bpi_fit_model = BPIFITModel()

        # Get user input for required flow rate and pressure
        required_flow_rate = float(input("Enter the required flow rate (m³/h): "))
        required_pressure = float(input("Enter the required pressure (bar): "))

        # Get compatible motobombas
        compatible_motobombas = bpi_fit_model.get_compatible_motobombas(required_flow_rate, required_pressure)

        # Display results
        if not compatible_motobombas.empty:
            print("Compatible motobombas:")
            print(compatible_motobombas)
        else:
            print("No compatible motobombas found.")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
