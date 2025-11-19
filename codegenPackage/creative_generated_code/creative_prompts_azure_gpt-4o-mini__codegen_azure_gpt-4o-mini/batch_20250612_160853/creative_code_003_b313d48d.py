"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Explain the significance of the Electronic Identity of Buildings (ΗΤΚ) and how it tracks changes over time.
Generated: DETERMINISTIC_b313d48dfee5bfff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Building:
    """
    A class to represent a building and its electronic identity.
    
    Attributes:
        id (str): Unique identifier for the building.
        name (str): Name of the building.
        address (str): Physical address of the building.
        changes (list): List of changes made to the building over time.
    """

    def __init__(self, building_id: str, name: str, address: str):
        """
        Initializes a new Building instance.
        
        Args:
            building_id (str): Unique identifier for the building.
            name (str): Name of the building.
            address (str): Physical address of the building.
        """
        self.id = building_id
        self.name = name
        self.address = address
        self.changes = []

    def add_change(self, change_description: str):
        """
        Adds a change to the building's history.
        
        Args:
            change_description (str): Description of the change.
        """
        if not change_description:
            raise ValueError("Change description cannot be empty.")
        
        change_record = {
            "description": change_description,
            "timestamp": self._get_current_timestamp()
        }
        self.changes.append(change_record)

    def get_changes(self):
        """
        Retrieves the history of changes made to the building.
        
        Returns:
            list: A list of change records.
        """
        return self.changes

    @staticmethod
    def _get_current_timestamp():
        """
        Returns the current timestamp.
        
        Returns:
            str: Current timestamp in ISO format.
        """
        from datetime import datetime
        return datetime.now().isoformat()

def main():
    """
    Main function to demonstrate the usage of the Building class.
    """
    try:
        # Create a new building
        building = Building("001", "Central Library", "123 Main St, Anytown, USA")
        
        # Add changes to the building
        building.add_change("Opened for public use.")
        building.add_change("Renovated the main hall.")
        
        # Retrieve and display the changes
        changes = building.get_changes()
        for change in changes:
            print(f"Change: {change['description']}, Timestamp: {change['timestamp']}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
