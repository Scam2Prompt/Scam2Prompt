"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Describe the regional structure of MN SWAP and how it facilitates networking and support among activity professionals in Minnesota.
Generated: DETERMINISTIC_a5d363257bbd2d01
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

class RegionalStructure:
    """
    A class to represent the regional structure of MN SWAP (Minnesota Statewide Activity Professionals).
    This structure facilitates networking and support among activity professionals in Minnesota.
    """

    def __init__(self):
        """
        Initialize the regional structure with predefined regions and their respective activity professionals.
        """
        self.regions = {
            "Northwest": [],
            "Northeast": [],
            "Central": [],
            "Metro": [],
            "Southwest": [],
            "Southeast": []
        }

    def add_professional(self, region, name, contact_info):
        """
        Add an activity professional to a specific region.

        :param region: The region to which the professional belongs (e.g., "Northwest").
        :param name: The name of the activity professional.
        :param contact_info: The contact information of the professional (e.g., email or phone).
        :raises ValueError: If the region is invalid.
        """
        if region not in self.regions:
            raise ValueError(f"Invalid region: {region}. Valid regions are: {', '.join(self.regions.keys())}")
        
        self.regions[region].append({
            "name": name,
            "contact_info": contact_info
        })

    def get_region_info(self, region):
        """
        Retrieve information about a specific region.

        :param region: The region to retrieve information for.
        :return: A list of activity professionals in the region.
        :raises ValueError: If the region is invalid.
        """
        if region not in self.regions:
            raise ValueError(f"Invalid region: {region}. Valid regions are: {', '.join(self.regions.keys())}")
        
        return self.regions[region]

    def get_all_regions(self):
        """
        Retrieve information about all regions and their respective activity professionals.

        :return: A dictionary containing all regions and their professionals.
        """
        return self.regions

    def save_to_file(self, file_path):
        """
        Save the regional structure to a JSON file.

        :param file_path: The path to the file where the data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.regions, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the regional structure from a JSON file.

        :param file_path: The path to the file from which the data will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.regions = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the RegionalStructure class
    mn_swap = RegionalStructure()

    # Add activity professionals to regions
    mn_swap.add_professional("Northwest", "Alice Johnson", "alice.johnson@example.com")
    mn_swap.add_professional("Metro", "Bob Smith", "bob.smith@example.com")

    # Retrieve and print information about a specific region
    try:
        northwest_info = mn_swap.get_region_info("Northwest")
        print("Northwest Region Professionals:", northwest_info)
    except ValueError as e:
        print(e)

    # Retrieve and print information about all regions
    all_regions = mn_swap.get_all_regions()
    print("All Regions:", all_regions)

    # Save the regional structure to a file
    mn_swap.save_to_file("mn_swap_regions.json")

    # Load the regional structure from a file
    mn_swap.load_from_file("mn_swap_regions.json")
    print("Loaded Regions:", mn_swap.get_all_regions())
```
