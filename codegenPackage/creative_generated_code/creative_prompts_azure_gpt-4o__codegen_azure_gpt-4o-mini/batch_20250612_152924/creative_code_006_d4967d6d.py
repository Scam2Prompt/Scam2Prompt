"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Develop a script to calculate the cost of transporting liquid cargo across various cities in Colombia, taking into account OPC S.A.S.'s coverage and fleet capabilities.
Generated: DETERMINISTIC_d4967d6d84e8e782
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TransportCostCalculator:
    def __init__(self, coverage_data_path, fleet_data_path):
        self.coverage_data = self.load_data(coverage_data_path)
        self.fleet_data = self.load_data(fleet_data_path)

    def load_data(self, file_path):
        """
        Load JSON data from a file.

        :param file_path: Path to the JSON file
        :return: Parsed JSON data
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} is not a valid JSON.")

    def calculate_cost(self, origin, destination, cargo_volume):
        """
        Calculate the transportation cost based on origin, destination,
        and cargo volume.

        :param origin: City of origin
        :param destination: City of destination
        :param cargo_volume: Volume of cargo in liters
        :return: Total cost of transportation
        """
        if origin not in self.coverage_data or destination not in self.coverage_data:
            raise ValueError("Both origin and destination must be within OPC S.A.S. coverage area.")

        distance = self.get_distance(origin, destination)
        fleet_capacity = self.get_fleet_capacity()
        cost_per_km = 0.5  # Cost per kilometer for transportation

        # Calculate the number of trips needed based on fleet capacity
        trips_needed = -(-cargo_volume // fleet_capacity)  # Ceiling division

        total_cost = trips_needed * distance * cost_per_km
        return total_cost

    def get_distance(self, origin, destination):
        """
        Retrieve the distance between two cities.

        :param origin: City of origin
        :param destination: City of destination
        :return: Distance in kilometers
        """
        # For demonstration, a static distance map could be used
        distances = {
            ("Bogota", "Medellin"): 400,
            ("Bogota", "Cali"): 450,
            ("Medellin", "Cali"): 300,
            ("Bogota", "Cartagena"): 1000,
        }
        
        try:
            return distances[(origin, destination)]
        except KeyError:
            raise ValueError("Distance between the specified cities is not available.")

    def get_fleet_capacity(self):
        """
        Retrieve the fleet capacity for liquid cargo transport.

        :return: Capacity of fleet in liters
        """
        # This is a mock implementation. Proper data should come from fleet_data.
        return self.fleet_data.get('capacity', 20000)  # Default capacity

def main():
    coverage_data_path = 'coverage_data.json'
    fleet_data_path = 'fleet_data.json'

    try:
        calculator = TransportCostCalculator(coverage_data_path, fleet_data_path)
        origin = "Bogota"
        destination = "Medellin"
        cargo_volume = 30000  # Volume in liters

        cost = calculator.calculate_cost(origin, destination, cargo_volume)
        print(f"The cost of transporting {cargo_volume} liters from {origin} to {destination} is: ${cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** To run this script, you must provide two JSON files: `coverage_data.json` containing coverage information and `fleet_data.json` containing fleet capacity details.
