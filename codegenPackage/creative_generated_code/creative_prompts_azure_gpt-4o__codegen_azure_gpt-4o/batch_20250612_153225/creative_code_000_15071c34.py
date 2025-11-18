"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Write Python code to simulate a neighborhood design based on the "pocket neighborhoods" concept described in Kallimos Communities, where small dwellings are clustered around shared green spaces.
Generated: DETERMINISTIC_15071c34e3545a3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PocketNeighborhood:
    """
    A class to simulate a pocket neighborhood design.
    Pocket neighborhoods consist of small dwellings clustered around shared green spaces.
    """

    def __init__(self, name, num_dwellings, green_space_size):
        """
        Initialize a pocket neighborhood.

        :param name: Name of the neighborhood.
        :param num_dwellings: Number of small dwellings in the neighborhood.
        :param green_space_size: Size of the shared green space in square meters.
        """
        self.name = name
        self.num_dwellings = num_dwellings
        self.green_space_size = green_space_size
        self.dwellings = self._create_dwellings()
        self.shared_green_space = self._create_green_space()

    def _create_dwellings(self):
        """
        Generate dwellings with random attributes.
        
        :return: List of dwellings.
        """
        dwellings = []
        for i in range(1, self.num_dwellings + 1):
            dwelling = {
                "id": i,
                "size": random.randint(50, 120),  # Dwelling size in square meters
                "occupants": random.randint(1, 5),  # Number of occupants
                "has_private_garden": random.choice([True, False])
            }
            dwellings.append(dwelling)
        return dwellings

    def _create_green_space(self):
        """
        Create the shared green space with random attributes.
        
        :return: Information about the shared green space.
        """
        green_space = {
            "size": self.green_space_size,  # Green space size in square meters
            "features": random.sample(
                ["community garden", "playground", "seating area", "walking paths", "pond"],
                k=random.randint(2, 5)  # Randomly select 2-5 features
            )
        }
        return green_space

    def display_neighborhood(self):
        """
        Print the details of the neighborhood including dwellings and green space.
        """
        print(f"Neighborhood Name: {self.name}")
        print(f"Number of Dwellings: {self.num_dwellings}")
        print(f"Shared Green Space Size: {self.green_space_size} sq meters")
        print(f"Green Space Features: {', '.join(self.shared_green_space['features'])}")
        print("\nDwellings:")
        for dwelling in self.dwellings:
            print(
                f"  Dwelling ID: {dwelling['id']}, "
                f"Size: {dwelling['size']} sq meters, "
                f"Occupants: {dwelling['occupants']}, "
                f"Private Garden: {'Yes' if dwelling['has_private_garden'] else 'No'}"
            )

    def save_to_file(self, filename):
        """
        Save the neighborhood details to a file in text format.

        :param filename: Name of the file to save the neighborhood details.
        """
        try:
            with open(filename, 'w') as file:
                file.write(f"Neighborhood Name: {self.name}\n")
                file.write(f"Number of Dwellings: {self.num_dwellings}\n")
                file.write(f"Shared Green Space Size: {self.green_space_size} sq meters\n")
                file.write(f"Green Space Features: {', '.join(self.shared_green_space['features'])}\n")
                file.write("\nDwellings:\n")
                for dwelling in self.dwellings:
                    file.write(
                        f"  Dwelling ID: {dwelling['id']}, "
                        f"Size: {dwelling['size']} sq meters, "
                        f"Occupants: {dwelling['occupants']}, "
                        f"Private Garden: {'Yes' if dwelling['has_private_garden'] else 'No'}\n"
                    )
            print(f"Neighborhood details successfully saved to {filename}")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

# Main function
if __name__ == "__main__":
    # Create a pocket neighborhood
    neighborhood = PocketNeighborhood(name="Kallimos Pocket", num_dwellings=10, green_space_size=500)

    # Display the neighborhood details
    neighborhood.display_neighborhood()

    # Save details to a file
    neighborhood.save_to_file("neighborhood_details.txt")
```
