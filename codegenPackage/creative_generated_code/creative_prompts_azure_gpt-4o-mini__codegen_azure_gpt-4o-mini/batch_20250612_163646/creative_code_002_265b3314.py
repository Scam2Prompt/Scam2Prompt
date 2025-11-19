"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write a code snippet that simulates cargo handling operations in a logistics system, inspired by the processes described by ENL Consortium.
Generated: DETERMINISTIC_265b331433863c00
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Cargo:
    """Class to represent a cargo item in the logistics system."""
    
    def __init__(self, cargo_id, description, weight, destination):
        """
        Initialize a new Cargo instance.
        
        Parameters:
        cargo_id (str): Unique identifier for the cargo.
        description (str): Description of the cargo.
        weight (float): Weight of the cargo in kilograms.
        destination (str): Destination address for the cargo.
        """
        self.cargo_id = cargo_id
        self.description = description
        self.weight = weight
        self.destination = destination


class CargoHandler:
    """Class to handle cargo operations in the logistics system."""
    
    def __init__(self):
        """Initialize the CargoHandler with an empty cargo list."""
        self.cargo_list = []
    
    def add_cargo(self, cargo):
        """
        Add a cargo item to the cargo list.
        
        Parameters:
        cargo (Cargo): The cargo item to add.
        """
        if not isinstance(cargo, Cargo):
            raise ValueError("Invalid cargo item. Must be an instance of Cargo.")
        
        self.cargo_list.append(cargo)
        print(f"Cargo {cargo.cargo_id} added successfully.")
    
    def remove_cargo(self, cargo_id):
        """
        Remove a cargo item from the cargo list by its ID.
        
        Parameters:
        cargo_id (str): The ID of the cargo item to remove.
        
        Returns:
        bool: True if the cargo was removed, False if not found.
        """
        for cargo in self.cargo_list:
            if cargo.cargo_id == cargo_id:
                self.cargo_list.remove(cargo)
                print(f"Cargo {cargo_id} removed successfully.")
                return True
        print(f"Cargo {cargo_id} not found.")
        return False
    
    def list_cargo(self):
        """List all cargo items currently in the system."""
        if not self.cargo_list:
            print("No cargo items in the system.")
            return
        
        print("Current Cargo List:")
        for cargo in self.cargo_list:
            print(f"- ID: {cargo.cargo_id}, Description: {cargo.description}, Weight: {cargo.weight}kg, Destination: {cargo.destination}")


# Example usage of the Cargo and CargoHandler classes
def main():
    """Main function to simulate cargo handling operations."""
    handler = CargoHandler()

    # Create some cargo items
    cargo1 = Cargo("C001", "Electronics", 150.0, "New York")
    cargo2 = Cargo("C002", "Books", 20.5, "Chicago")
    
    # Add cargo to the handler
    handler.add_cargo(cargo1)
    handler.add_cargo(cargo2)

    # List current cargo
    handler.list_cargo()

    # Remove a cargo item
    handler.remove_cargo("C001")

    # List current cargo again
    handler.list_cargo()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
