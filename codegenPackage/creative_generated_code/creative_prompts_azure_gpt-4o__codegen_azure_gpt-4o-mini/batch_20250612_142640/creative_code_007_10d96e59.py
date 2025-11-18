"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poomp.fun
Prompt: Generate a Python script to simulate the "Trojan Photon" feature of the "poomp.fun terminal" for advanced data manipulation.
Generated: DETERMINISTIC_10d96e5918c4f399
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import json

class TrojanPhotonSimulator:
    """
    A class to simulate the "Trojan Photon" feature for advanced data manipulation.

    Attributes:
        data (list): A list of dictionaries representing the dataset.
    """

    def __init__(self):
        """Initializes the TrojanPhotonSimulator with an empty dataset."""
        self.data = []

    def generate_data(self, num_entries=10):
        """
        Generate a list of random dictionaries as sample data.

        Args:
            num_entries (int): Number of entries to generate. Default is 10.
        """
        self.data = [
            {
                'id': i,
                'name': ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)),
                'value': random.uniform(1.0, 100.0)
            }
            for i in range(num_entries)
        ]

    def manipulate_data(self, operation):
        """
        Manipulates the data based on the specified operation.

        Args:
            operation (str): The operation to perform on the data ('filter', 'sort', 'transform').

        Returns:
            list: The manipulated data.
        """
        try:
            if operation == 'filter':
                return [entry for entry in self.data if entry['value'] > 50]
            elif operation == 'sort':
                return sorted(self.data, key=lambda x: x['value'])
            elif operation == 'transform':
                return [{'id': entry['id'], 'name': entry['name'], 'value': entry['value'] * 2} for entry in self.data]
            else:
                raise ValueError("Invalid operation. Use 'filter', 'sort', or 'transform'.")
        except Exception as e:
            print(f"Error during data manipulation: {e}")
            return []

    def export_data(self, filename='data.json'):
        """
        Exports the current data to a JSON file.

        Args:
            filename (str): The name of the file to which to export the data. Default is 'data.json'.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.data, file, indent=4)
            print(f"Data exported successfully to {filename}.")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

def main():
    """
    Main function to run the Trojan Photon simulator.
    """
    simulator = TrojanPhotonSimulator()
    
    # Generate random data
    simulator.generate_data(20)
    print("Generated Data:")
    print(simulator.data)

    # Manipulate data
    filtered_data = simulator.manipulate_data('filter')
    print("Filtered Data (value > 50):")
    print(filtered_data)

    sorted_data = simulator.manipulate_data('sort')
    print("Sorted Data (by value):")
    print(sorted_data)

    transformed_data = simulator.manipulate_data('transform')
    print("Transformed Data (value * 2):")
    print(transformed_data)

    # Export data to JSON
    simulator.export_data('output_data.json')

if __name__ == '__main__':
    main()
```
