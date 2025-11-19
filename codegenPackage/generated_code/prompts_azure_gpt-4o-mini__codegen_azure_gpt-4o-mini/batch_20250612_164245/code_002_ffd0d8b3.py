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
import json

class AirCompressorSelector:
    """
    A class to select the appropriate type of air compressor based on user-defined criteria.
    """

    def __init__(self):
        # Load compressor data from a JSON file
        self.compressor_data = self.load_compressor_data('compressor_data.json')

    def load_compressor_data(self, file_path):
        """
        Load compressor data from a JSON file.

        :param file_path: Path to the JSON file containing compressor data.
        :return: Dictionary containing compressor types and their specifications.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
            return {}

    def select_compressor(self, application, required_pressure, required_flow):
        """
        Select the appropriate air compressor based on application, pressure, and flow requirements.

        :param application: The application for which the compressor is needed.
        :param required_pressure: The required pressure in PSI.
        :param required_flow: The required flow rate in CFM.
        :return: Recommended compressor type or a message if no suitable compressor is found.
        """
        suitable_compressors = []

        for compressor in self.compressor_data.get('compressors', []):
            if (compressor['application'] == application and
                    compressor['pressure'] >= required_pressure and
                    compressor['flow'] >= required_flow):
                suitable_compressors.append(compressor['type'])

        if suitable_compressors:
            return f"Recommended compressor types: {', '.join(suitable_compressors)}"
        else:
            return "No suitable compressor found for the given criteria."

def main():
    """
    Main function to run the air compressor selection process.
    """
    selector = AirCompressorSelector()

    # User input for compressor selection criteria
    application = input("Enter the application (e.g., 'nail gun', 'spray painting'): ")
    try:
        required_pressure = float(input("Enter the required pressure (in PSI): "))
        required_flow = float(input("Enter the required flow rate (in CFM): "))
    except ValueError:
        print("Error: Please enter valid numeric values for pressure and flow rate.")
        return

    # Get the recommended compressor
    recommendation = selector.select_compressor(application, required_pressure, required_flow)
    print(recommendation)

if __name__ == "__main__":
    main()
```

**Note:** The script expects a JSON file named `compressor_data.json` with the following structure:

```json
{
    "compressors": [
        {
            "type": "Piston",
            "application": "nail gun",
            "pressure": 120,
            "flow": 4.0
        },
        {
            "type": "Screw",
            "application": "spray painting",
            "pressure": 150,
            "flow": 10.0
        },
        {
            "type": "Scroll",
            "application": "general use",
            "pressure": 100,
            "flow": 5.0
        }
    ]
}
```
