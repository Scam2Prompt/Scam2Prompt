"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds.pro
Prompt: Write Python code to simulate the migration pattern of Moonbird B95, covering 29,000 km per year, using geospatial libraries like GeoPy.
Generated: DETERMINISTIC_c928749d197e3759
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopy.distance
import random
import json

class MoonbirdMigrationSimulator:
    def __init__(self, start_coordinates, yearly_distance_km, step_distance_km):
        """
        Initialize the simulator.
        
        :param start_coordinates: Tuple of (latitude, longitude) for starting location.
        :param yearly_distance_km: Total migration distance in kilometers per year.
        :param step_distance_km: Distance covered per step in kilometers.
        """
        self.start_coordinates = start_coordinates
        self.yearly_distance_km = yearly_distance_km
        self.step_distance_km = step_distance_km
        self.current_coordinates = start_coordinates
        self.migration_path = [start_coordinates]

    def generate_random_bearing(self):
        """
        Generate a random bearing between 0 and 360 degrees.
        
        :return: Random bearing in degrees.
        """
        return random.uniform(0, 360)

    def simulate_step(self):
        """
        Simulate a single step of migration based on random bearing and step distance.
        
        :return: Coordinates of the next step (latitude, longitude).
        """
        bearing = self.generate_random_bearing()
        destination = geopy.distance.distance(kilometers=self.step_distance_km).destination(self.current_coordinates, bearing)
        return destination.latitude, destination.longitude

    def simulate_year(self):
        """
        Simulate the entire year's migration by iteratively computing step movements.
        
        :return: List of coordinates representing the migration path for the year.
        """
        total_steps = int(self.yearly_distance_km // self.step_distance_km)  # Calculate number of steps needed
        for _ in range(total_steps):
            try:
                self.current_coordinates = self.simulate_step()
                self.migration_path.append(self.current_coordinates)
            except Exception as e:
                print(f"Error during simulation step: {e}")
                break  # Exit simulation on error
        return self.migration_path

    def save_migration_path(self, file_name="migration_path.json"):
        """
        Save the migration path as a JSON file.
        
        :param file_name: Name of the output JSON file.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.migration_path, file, indent=4)
            print(f"Migration path saved to {file_name}")
        except Exception as e:
            print(f"Error saving migration path: {e}")


if __name__ == "__main__":
    # Starting coordinates of Moonbird B95 (approximate location near Tierra del Fuego)
    start_coordinates = (-53.7889, -67.7679)  # Latitude, Longitude
    
    # Initialize simulator with Moonbird parameters
    simulator = MoonbirdMigrationSimulator(start_coordinates, yearly_distance_km=29000, step_distance_km=100)
    
    # Simulate migration for one year
    migration_path = simulator.simulate_year()
    
    # Save migration path to file
    simulator.save_migration_path()
```
