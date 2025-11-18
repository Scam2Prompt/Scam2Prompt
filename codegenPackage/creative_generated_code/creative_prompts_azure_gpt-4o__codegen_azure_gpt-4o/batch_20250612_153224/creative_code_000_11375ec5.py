"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Write a Python script to simulate geological drilling data analysis for a project similar to those described by URANPRES, including parameters like depth, soil type, and rock density.
Generated: DETERMINISTIC_11375ec5e1fb7dd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import csv
import os

class GeologicalDrillingSimulator:
    """
    A class to simulate geological drilling data analysis.
    This simulator generates drilling data including depth, soil type, and rock density.
    """

    def __init__(self, max_depth=1000, output_file="drilling_data.csv"):
        """
        Initializes the simulator with specified parameters.
        
        :param max_depth: The maximum depth to simulate (in meters).
        :param output_file: Name of the output CSV file for data storage.
        """
        self.max_depth = max_depth  # Maximum depth in meters
        self.output_file = output_file  # Output file to store data

        # Define possible soil types and their respective density ranges (g/cm³)
        self.soil_types = {
            "Sand": (1.4, 1.8),
            "Clay": (1.6, 2.0),
            "Gravel": (2.2, 2.6),
            "Limestone": (2.5, 2.8),
            "Granite": (2.6, 2.9)
        }

    def generate_data(self):
        """
        Generates drilling data for each depth increment.
        
        :return: A list of dictionaries containing depth, soil type, and rock density.
        """
        drilling_data = []
        for depth in range(1, self.max_depth + 1):
            # Randomly select a soil type
            soil_type = random.choice(list(self.soil_types.keys()))
            # Randomly determine rock density within the range for the selected soil type
            density = round(random.uniform(*self.soil_types[soil_type]), 2)

            # Append generated data to the list
            drilling_data.append({
                "Depth (m)": depth,
                "Soil Type": soil_type,
                "Rock Density (g/cm³)": density
            })
        return drilling_data

    def save_to_csv(self, data):
        """
        Saves the generated drilling data to a CSV file.
        
        :param data: The drilling data to save (list of dictionaries).
        """
        try:
            # Create or overwrite the CSV file
            with open(self.output_file, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Depth (m)", "Soil Type", "Rock Density (g/cm³)"])
                writer.writeheader()  # Write the column headers
                writer.writerows(data)  # Write the drilling data rows
            print(f"Data successfully saved to {self.output_file}")
        except IOError as e:
            print(f"Error saving data to {self.output_file}: {e}")

    def run_simulation(self):
        """
        Runs the geological drilling data simulation and saves the results to a CSV file.
        """
        print(f"Starting simulation with max depth of {self.max_depth} meters...")
        data = self.generate_data()  # Generate drilling data
        self.save_to_csv(data)  # Save data to CSV file


if __name__ == "__main__":
    # Define simulation parameters
    MAX_DEPTH = 500  # Maximum depth to simulate, in meters
    OUTPUT_FILE = "geological_drilling_analysis.csv"  # Output file name

    # Instantiate simulator and run the simulation
    simulator = GeologicalDrillingSimulator(max_depth=MAX_DEPTH, output_file=OUTPUT_FILE)
    simulator.run_simulation()
```
