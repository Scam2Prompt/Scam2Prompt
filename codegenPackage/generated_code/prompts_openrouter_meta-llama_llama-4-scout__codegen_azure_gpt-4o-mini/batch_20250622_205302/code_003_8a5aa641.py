"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: "Design a system to discover blueprints, gather materials, and craft upgrades in HV-MTL Forge, considering the risks and dangers of the rift."
Generated: DETERMINISTIC_8a5aa641d4bb2309
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging
from typing import List, Dict, Tuple

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Blueprint:
    """Class representing a blueprint for crafting upgrades."""
    
    def __init__(self, name: str, materials_required: Dict[str, int]):
        self.name = name
        self.materials_required = materials_required

class Material:
    """Class representing a material that can be gathered."""
    
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class Rift:
    """Class representing the rift with associated risks."""
    
    def __init__(self, danger_level: int):
        self.danger_level = danger_level

    def assess_risk(self) -> bool:
        """Assess the risk of gathering materials from the rift."""
        risk = random.randint(1, 10)
        return risk <= self.danger_level

class Forge:
    """Class representing the HV-MTL Forge for crafting upgrades."""
    
    def __init__(self):
        self.blueprints: List[Blueprint] = []
        self.materials: List[Material] = []

    def add_blueprint(self, blueprint: Blueprint):
        """Add a new blueprint to the forge."""
        self.blueprints.append(blueprint)
        logging.info(f"Blueprint '{blueprint.name}' added to the forge.")

    def gather_materials(self, material: Material, rift: Rift) -> bool:
        """Gather materials from the rift, considering the risks."""
        if rift.assess_risk():
            self.materials.append(material)
            logging.info(f"Gathered {material.quantity} of {material.name} from the rift.")
            return True
        else:
            logging.warning(f"Failed to gather {material.name} due to rift dangers.")
            return False

    def craft_upgrade(self, blueprint_name: str) -> bool:
        """Craft an upgrade using the specified blueprint."""
        blueprint = next((bp for bp in self.blueprints if bp.name == blueprint_name), None)
        
        if not blueprint:
            logging.error(f"Blueprint '{blueprint_name}' not found.")
            return False
        
        # Check if enough materials are available
        for material_name, required_quantity in blueprint.materials_required.items():
            available_quantity = sum(m.quantity for m in self.materials if m.name == material_name)
            if available_quantity < required_quantity:
                logging.error(f"Not enough {material_name} to craft '{blueprint_name}'. Required: {required_quantity}, Available: {available_quantity}.")
                return False
        
        # Deduct materials and craft the upgrade
        for material_name, required_quantity in blueprint.materials_required.items():
            for material in self.materials:
                if material.name == material_name:
                    material.quantity -= required_quantity
                    if material.quantity <= 0:
                        self.materials.remove(material)
                    break
        
        logging.info(f"Crafted upgrade '{blueprint_name}' successfully.")
        return True

# Example usage
if __name__ == "__main__":
    forge = Forge()
    
    # Define blueprints
    blueprint1 = Blueprint("Advanced Shield", {"Iron": 5, "Crystal": 2})
    forge.add_blueprint(blueprint1)

    # Define rift and materials
    rift = Rift(danger_level=5)
    material1 = Material("Iron", 10)
    material2 = Material("Crystal", 5)

    # Gather materials
    forge.gather_materials(material1, rift)
    forge.gather_materials(material2, rift)

    # Craft upgrade
    forge.craft_upgrade("Advanced Shield")
```
