"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: "Write a Python script to manage villa allocations and amenities for a project like Dens Haven, with 22 villas and features like swimming pools and clubhouses."
Generated: DETERMINISTIC_4d87685b7e57af1e
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class VillaManager:
    """
    A class to manage villa allocations and amenities for a project.
    """

    def __init__(self, total_villas=22):
        """
        Initialize the VillaManager with a given number of villas.
        :param total_villas: Total number of villas in the project.
        """
        self.total_villas = total_villas
        self.villas = {f"Villa-{i+1}": {"allocated": False, "amenities": []} for i in range(total_villas)}

    def allocate_villa(self, villa_id, amenities=None):
        """
        Allocate a villa and assign amenities.
        :param villa_id: ID of the villa to allocate (e.g., "Villa-1").
        :param amenities: List of amenities to assign to the villa.
        :return: Success message or error message.
        """
        if villa_id not in self.villas:
            return f"Error: {villa_id} does not exist."
        if self.villas[villa_id]["allocated"]:
            return f"Error: {villa_id} is already allocated."
        
        self.villas[villa_id]["allocated"] = True
        self.villas[villa_id]["amenities"] = amenities or []
        return f"Success: {villa_id} has been allocated with amenities {self.villas[villa_id]['amenities']}."

    def deallocate_villa(self, villa_id):
        """
        Deallocate a villa.
        :param villa_id: ID of the villa to deallocate (e.g., "Villa-1").
        :return: Success message or error message.
        """
        if villa_id not in self.villas:
            return f"Error: {villa_id} does not exist."
        if not self.villas[villa_id]["allocated"]:
            return f"Error: {villa_id} is not currently allocated."
        
        self.villas[villa_id]["allocated"] = False
        self.villas[villa_id]["amenities"] = []
        return f"Success: {villa_id} has been deallocated."

    def get_villa_status(self, villa_id):
        """
        Get the status of a specific villa.
        :param villa_id: ID of the villa to check (e.g., "Villa-1").
        :return: Status of the villa or error message.
        """
        if villa_id not in self.villas:
            return f"Error: {villa_id} does not exist."
        return self.villas[villa_id]

    def list_all_villas(self):
        """
        List the status of all villas.
        :return: Dictionary containing the status of all villas.
        """
        return self.villas

    def save_to_file(self, filename="villa_data.json"):
        """
        Save the villa data to a JSON file.
        :param filename: Name of the file to save the data.
        :return: Success message or error message.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.villas, file, indent=4)
            return f"Success: Villa data has been saved to {filename}."
        except Exception as e:
            return f"Error: Failed to save data to file. {str(e)}"

    def load_from_file(self, filename="villa_data.json"):
        """
        Load villa data from a JSON file.
        :param filename: Name of the file to load the data from.
        :return: Success message or error message.
        """
        try:
            with open(filename, "r") as file:
                self.villas = json.load(file)
            return f"Success: Villa data has been loaded from {filename}."
        except Exception as e:
            return f"Error: Failed to load data from file. {str(e)}"


# Example usage
if __name__ == "__main__":
    manager = VillaManager()

    # Allocate a villa
    print(manager.allocate_villa("Villa-1", ["Swimming Pool", "Clubhouse"]))

    # Get villa status
    print(manager.get_villa_status("Villa-1"))

    # Deallocate a villa
    print(manager.deallocate_villa("Villa-1"))

    # List all villas
    print(manager.list_all_villas())

    # Save villa data to file
    print(manager.save_to_file())

    # Load villa data from file
    print(manager.load_from_file())
```
