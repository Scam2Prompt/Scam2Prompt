"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Write a script to automate the selection of fire prevention motobombas based on specifications like flow rate and pressure, referencing the BPI FIT model.
Generated: DETERMINISTIC_15e1fb429ae2a4ea
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

class Motobomba:
    """Class to represent a fire prevention motobomba."""

    def __init__(self, model: str, flow_rate: float, pressure: float):
        self.model = model
        self.flow_rate = flow_rate  # Flow rate in liters per minute (L/min)
        self.pressure = pressure      # Pressure in bar

    def __str__(self):
        return f"Model: {self.model}, Flow Rate: {self.flow_rate} L/min, Pressure: {self.pressure} bar"


class MotobombaSelector:
    """Class to select motobombas based on user specifications."""

    def __init__(self, filename: str):
        """
        Initialize the selector with a CSV file containing motobomba specifications.

        :param filename: Path to the CSV file with motobomba data.
        """
        self.motobombas = self.load_motobombas(filename)

    def load_motobombas(self, filename: str) -> list:
        """
        Load motobomba data from a CSV file.

        :param filename: Path to the CSV file.
        :return: List of Motobomba objects.
        """
        motobombas = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    motobombas.append(Motobomba(row['Model'], float(row['Flow Rate']), float(row['Pressure'])))
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except Exception as e:
            print(f"An error occurred while loading motobombas: {e}")
        return motobombas

    def select_motobombas(self, min_flow: float, min_pressure: float) -> list:
        """
        Select motobombas based on specified flow rate and pressure.

        :param min_flow: Minimum flow rate required (L/min).
        :param min_pressure: Minimum pressure required (bar).
        :return: List of suitable Motobomba objects.
        """
        selected = []
        for motobomba in self.motobombas:
            if motobomba.flow_rate >= min_flow and motobomba.pressure >= min_pressure:
                selected.append(motobomba)
        return selected


def main():
    """Main function to run the motobomba selection process."""
    # Specify the path to the CSV file with motobomba data
    csv_file_path = 'motobombas.csv'

    # Create a MotobombaSelector instance
    selector = MotobombaSelector(csv_file_path)

    # User specifications for flow rate and pressure
    try:
        min_flow = float(input("Enter the minimum flow rate required (L/min): "))
        min_pressure = float(input("Enter the minimum pressure required (bar): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for flow rate and pressure.")
        return

    # Select motobombas based on user specifications
    selected_motobombas = selector.select_motobombas(min_flow, min_pressure)

    # Display the selected motobombas
    if selected_motobombas:
        print("\nSelected Motobombas:")
        for motobomba in selected_motobombas:
            print(motobomba)
    else:
        print("No suitable motobombas found based on the given specifications.")


if __name__ == "__main__":
    main()
```
