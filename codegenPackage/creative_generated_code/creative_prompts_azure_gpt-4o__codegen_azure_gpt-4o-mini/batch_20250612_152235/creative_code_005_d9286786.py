"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raid.services
Prompt: Create a function to register new equipment types on RAID Services, including fields for manufacturer, model, and version.
Generated: DETERMINISTIC_d928678649689bd6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class EquipmentRegistrationError(Exception):
    """Custom exception for equipment registration errors."""
    pass

class EquipmentRegistry:
    """Class to handle registration of equipment types for RAID Services."""
    
    def __init__(self):
        # In-memory storage for equipment types
        self.equipment_types = []

    def register_equipment(self, manufacturer: str, model: str, version: str) -> Dict[str, Any]:
        """
        Registers a new equipment type with the provided manufacturer, model, and version.
        
        :param manufacturer: Name of the manufacturer
        :param model: Model of the equipment
        :param version: Version of the equipment
        :return: A dictionary containing the registered equipment details
        :raises EquipmentRegistrationError: If registration fails due to validation errors
        """
        if not manufacturer or not model or not version:
            raise EquipmentRegistrationError("All fields (manufacturer, model, version) must be provided.")

        equipment_entry = {
            "manufacturer": manufacturer,
            "model": model,
            "version": version
        }

        self.equipment_types.append(equipment_entry)

        # Return the registered equipment entry
        return equipment_entry

    def get_registered_equipment(self) -> str:
        """
        Retrieves a JSON string of all registered equipment types.
        
        :return: JSON string of registered equipment types
        """
        return json.dumps(self.equipment_types, indent=4)

# Example usage
if __name__ == "__main__":
    registry = EquipmentRegistry()
    
    try:
        # Register new equipment types
        print(registry.register_equipment("Manufacturer A", "Model X", "1.0"))
        print(registry.register_equipment("Manufacturer B", "Model Y", "2.0"))
        
        # Retrieve and print all registered equipment
        print("Registered Equipment:")
        print(registry.get_registered_equipment())
        
    except EquipmentRegistrationError as e:
        print(f"Registration error: {e}")
```
