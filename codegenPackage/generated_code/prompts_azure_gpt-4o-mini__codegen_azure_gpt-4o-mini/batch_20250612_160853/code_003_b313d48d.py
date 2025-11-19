"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Explain the significance of the Electronic Identity of Buildings (ΗΤΚ) and how it tracks changes over time.
Generated: DETERMINISTIC_b313d48dfee5bfff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ElectronicIdentityOfBuildings:
    """
    A class to represent the Electronic Identity of Buildings (ΗΤΚ).
    
    Attributes:
        building_id (str): Unique identifier for the building.
        creation_date (str): Date when the electronic identity was created.
        modifications (list): List of modifications made to the building's identity.
    """

    def __init__(self, building_id, creation_date):
        """
        Initializes the Electronic Identity of Buildings with a unique ID and creation date.
        
        Args:
            building_id (str): Unique identifier for the building.
            creation_date (str): Date when the electronic identity was created.
        """
        self.building_id = building_id
        self.creation_date = creation_date
        self.modifications = []

    def add_modification(self, modification):
        """
        Adds a modification to the building's electronic identity.
        
        Args:
            modification (str): Description of the modification.
        
        Raises:
            ValueError: If the modification description is empty.
        """
        if not modification:
            raise ValueError("Modification description cannot be empty.")
        
        self.modifications.append(modification)

    def get_modifications(self):
        """
        Returns the list of modifications made to the building's electronic identity.
        
        Returns:
            list: A list of modification descriptions.
        """
        return self.modifications

    def __str__(self):
        """
        Returns a string representation of the Electronic Identity of the Building.
        
        Returns:
            str: A string containing the building ID, creation date, and modifications.
        """
        return (f"Building ID: {self.building_id}\n"
                f"Creation Date: {self.creation_date}\n"
                f"Modifications: {', '.join(self.modifications) if self.modifications else 'None'}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of ElectronicIdentityOfBuildings
        building = ElectronicIdentityOfBuildings("B12345", "2023-01-01")
        
        # Add modifications
        building.add_modification("Initial construction completed.")
        building.add_modification("Renovation of the lobby.")
        
        # Print the building's electronic identity
        print(building)
        
        # Retrieve and print modifications
        modifications = building.get_modifications()
        print("Modifications:", modifications)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
