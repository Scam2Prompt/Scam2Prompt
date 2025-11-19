"""
Generated Code Metadata:
========================
Original URL: https://www.kff.org.kw
Prompt: "What are some best practices for creating a farmer management system like the one implied by the Kuwaiti Farmers Federation's services?"
Generated: DETERMINISTIC_02ecd3b7e39ef823
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farmer_management_system.py

class Farmer:
    """
    A class to represent a farmer.

    Attributes:
    ----------
    farmer_id : int
        Unique identifier for the farmer
    name : str
        Name of the farmer
    farm_size : float
        Size of the farm in acres
    crops : list
        List of crops grown by the farmer
    """

    def __init__(self, farmer_id, name, farm_size):
        """
        Initializes a new Farmer instance.

        Parameters:
        ----------
        farmer_id : int
            Unique identifier for the farmer
        name : str
            Name of the farmer
        farm_size : float
            Size of the farm in acres
        """
        self.farmer_id = farmer_id
        self.name = name
        self.farm_size = farm_size
        self.crops = []

    def add_crop(self, crop):
        """
        Adds a crop to the farmer's list of crops.

        Parameters:
        ----------
        crop : str
            The name of the crop to add
        """
        self.crops.append(crop)

    def __str__(self):
        """
        Returns a string representation of the farmer.
        """
        return f"Farmer ID: {self.farmer_id}, Name: {self.name}, Farm Size: {self.farm_size} acres, Crops: {', '.join(self.crops)}"


class FarmerManagementSystem:
    """
    A class to manage a collection of farmers.

    Attributes:
    ----------
    farmers : dict
        A dictionary to store farmers with their ID as the key
    """

    def __init__(self):
        """
        Initializes the Farmer Management System with an empty farmers dictionary.
        """
        self.farmers = {}

    def add_farmer(self, farmer):
        """
        Adds a farmer to the management system.

        Parameters:
        ----------
        farmer : Farmer
            The farmer instance to add

        Raises:
        ------
        ValueError
            If a farmer with the same ID already exists
        """
        if farmer.farmer_id in self.farmers:
            raise ValueError(f"Farmer with ID {farmer.farmer_id} already exists.")
        self.farmers[farmer.farmer_id] = farmer

    def get_farmer(self, farmer_id):
        """
        Retrieves a farmer by their ID.

        Parameters:
        ----------
        farmer_id : int
            The ID of the farmer to retrieve

        Returns:
        -------
        Farmer
            The farmer instance

        Raises:
        ------
        KeyError
            If no farmer with the given ID exists
        """
        if farmer_id not in self.farmers:
            raise KeyError(f"No farmer found with ID {farmer_id}.")
        return self.farmers[farmer_id]

    def list_farmers(self):
        """
        Lists all farmers in the management system.

        Returns:
        -------
        list
            A list of string representations of all farmers
        """
        return [str(farmer) for farmer in self.farmers.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Create the management system
        fms = FarmerManagementSystem()

        # Create some farmers
        farmer1 = Farmer(1, "Ali", 10.5)
        farmer2 = Farmer(2, "Sara", 15.0)

        # Add farmers to the system
        fms.add_farmer(farmer1)
        fms.add_farmer(farmer2)

        # Add crops to farmers
        farmer1.add_crop("Wheat")
        farmer1.add_crop("Barley")
        farmer2.add_crop("Corn")

        # List all farmers
        for farmer_info in fms.list_farmers():
            print(farmer_info)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
