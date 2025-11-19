"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raid.services
Prompt: Generate code to register new equipment in the Bioreact system, detailing the required parameters for the equipment type.
Generated: DETERMINISTIC_59377fbd475f6a79
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EquipmentRegistrationError(Exception):
    """Custom exception for equipment registration errors."""
    pass

class Equipment:
    """A class representing a piece of equipment in the Bioreact system."""
    
    def __init__(self, equipment_id, equipment_type, manufacturer, model, capacity_liters):
        """
        Initializes a new Equipment instance.

        :param equipment_id: Unique identifier for the equipment.
        :param equipment_type: Type of the equipment (e.g., fermenter, incubator).
        :param manufacturer: Manufacturer of the equipment.
        :param model: Model number of the equipment.
        :param capacity_liters: Capacity of the equipment in liters.
        """
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.manufacturer = manufacturer
        self.model = model
        self.capacity_liters = capacity_liters

    def validate(self):
        """Validates the equipment parameters."""
        if not isinstance(self.equipment_id, str) or not self.equipment_id:
            raise EquipmentRegistrationError("Equipment ID must be a non-empty string.")
        if not isinstance(self.equipment_type, str) or not self.equipment_type:
            raise EquipmentRegistrationError("Equipment type must be a non-empty string.")
        if not isinstance(self.manufacturer, str) or not self.manufacturer:
            raise EquipmentRegistrationError("Manufacturer must be a non-empty string.")
        if not isinstance(self.model, str) or not self.model:
            raise EquipmentRegistrationError("Model must be a non-empty string.")
        if not isinstance(self.capacity_liters, (int, float)) or self.capacity_liters <= 0:
            raise EquipmentRegistrationError("Capacity must be a positive number.")

class BioreactSystem:
    """A class representing the Bioreact system for equipment management."""
    
    def __init__(self):
        """Initializes an empty equipment registry."""
        self.equipment_registry = {}

    def register_equipment(self, equipment):
        """
        Registers new equipment in the Bioreact system.

        :param equipment: An instance of the Equipment class to be registered.
        :raises EquipmentRegistrationError: If validation of equipment fails.
        """
        try:
            # Validate the equipment parameters
            equipment.validate()

            # Check for duplicate equipment ID
            if equipment.equipment_id in self.equipment_registry:
                raise EquipmentRegistrationError(f"Equipment ID {equipment.equipment_id} is already registered.")

            # Register the equipment
            self.equipment_registry[equipment.equipment_id] = equipment
            print(f"Equipment {equipment.equipment_id} registered successfully.")

        except EquipmentRegistrationError as e:
            print(f"Error registering equipment: {e}")

# Example usage:
if __name__ == "__main__":
    bioreact_system = BioreactSystem()
    
    # Create a new equipment instance
    new_equipment = Equipment(
        equipment_id="EQ-001",
        equipment_type="Fermenter",
        manufacturer="Biotech Corp",
        model="BioFerment 3000",
        capacity_liters=150.0
    )
    
    # Register the equipment in the Bioreact system
    bioreact_system.register_equipment(new_equipment)
```
