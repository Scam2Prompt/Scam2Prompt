"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Create a script to model the integration of conduit accessories and electrical panels in a commercial building, using specifications similar to those provided by Miraya Electric S.A.C.
Generated: DETERMINISTIC_5329e2f515264c2b
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to model the integration of conduit accessories and electrical panels in a commercial building.
Specifications are based on standards similar to those provided by Miraya Electric S.A.C.
"""

import json
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConduitType(Enum):
    """Enum for different types of conduits."""
    EMT = "EMT"  # Electrical Metallic Tubing
    RMC = "RMC"  # Rigid Metal Conduit
    PVC = "PVC"  # Polyvinyl Chloride
    FLEX = "FLEX"  # Flexible Conduit

class PanelType(Enum):
    """Enum for different types of electrical panels."""
    MAIN = "MAIN"
    SUB = "SUB"
    DISTRIBUTION = "DISTRIBUTION"
    TRANSFER = "TRANSFER"

@dataclass
class ConduitAccessory:
    """Dataclass representing a conduit accessory."""
    id: str
    type: ConduitType
    size: float  # in inches
    quantity: int
    description: Optional[str] = None

@dataclass
class ElectricalPanel:
    """Dataclass representing an electrical panel."""
    id: str
    type: PanelType
    rating: float  # in amps
    circuits: int
    conduits: List[ConduitAccessory]
    location: Optional[str] = None

class ElectricalSystemModel:
    """Class to model the integration of conduit accessories and electrical panels."""
    
    def __init__(self):
        self.panels: Dict[str, ElectricalPanel] = {}
        self.conduits: Dict[str, ConduitAccessory] = {}
    
    def add_conduit_accessory(self, accessory: ConduitAccessory) -> bool:
        """Add a conduit accessory to the system."""
        if accessory.id in self.conduits:
            logger.error(f"Conduit accessory with ID {accessory.id} already exists.")
            return False
        self.conduits[accessory.id] = accessory
        logger.info(f"Added conduit accessory: {accessory.id}")
        return True
    
    def add_electrical_panel(self, panel: ElectricalPanel) -> bool:
        """Add an electrical panel to the system."""
        if panel.id in self.panels:
            logger.error(f"Electrical panel with ID {panel.id} already exists.")
            return False
        self.panels[panel.id] = panel
        logger.info(f"Added electrical panel: {panel.id}")
        return True
    
    def get_panel(self, panel_id: str) -> Optional[ElectricalPanel]:
        """Retrieve an electrical panel by ID."""
        return self.panels.get(panel_id)
    
    def get_conduit(self, conduit_id: str) -> Optional[ConduitAccessory]:
        """Retrieve a conduit accessory by ID."""
        return self.conduits.get(conduit_id)
    
    def validate_system(self) -> bool:
        """Validate the electrical system model."""
        if not self.panels:
            logger.error("No electrical panels in the system.")
            return False
        
        for panel_id, panel in self.panels.items():
            if not panel.conduits:
                logger.warning(f"Panel {panel_id} has no conduit accessories.")
            for conduit in panel.conduits:
                if conduit.id not in self.conduits:
                    logger.error(f"Conduit {conduit.id} in panel {panel_id} not found in system.")
                    return False
        
        logger.info("System validation passed.")
        return True
    
    def export_to_json(self, file_path: str) -> bool:
        """Export the system model to a JSON file."""
        try:
            data = {
                "panels": {panel_id: panel.__dict__ for panel_id, panel in self.panels.items()},
                "conduits": {conduit_id: conduit.__dict__ for conduit_id, conduit in self.conduits.items()}
            }
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"System exported to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to export system: {e}")
            return False
    
    @classmethod
    def import_from_json(cls, file_path: str) -> Optional['ElectricalSystemModel']:
        """Import a system model from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            system = cls()
            
            # Import conduits
            for conduit_id, conduit_data in data.get("conduits", {}).items():
                conduit = ConduitAccessory(
                    id=conduit_id,
                    type=ConduitType(conduit_data["type"]),
                    size=conduit_data["size"],
                    quantity=conduit_data["quantity"],
                    description=conduit_data.get("description")
                )
                system.add_conduit_accessory(conduit)
            
            # Import panels
            for panel_id, panel_data in data.get("panels", {}).items():
                conduits = []
                for conduit_data in panel_data["conduits"]:
                    conduit = ConduitAccessory(
                        id=conduit_data["id"],
                        type=ConduitType(conduit_data["type"]),
                        size=conduit_data["size"],
                        quantity=conduit_data["quantity"],
                        description=conduit_data.get("description")
                    )
                    conduits.append(conduit)
                
                panel = ElectricalPanel(
                    id=panel_id,
                    type=PanelType(panel_data["type"]),
                    rating=panel_data["rating"],
                    circuits=panel_data["circuits"],
                    conduits=conduits,
                    location=panel_data.get("location")
                )
                system.add_electrical_panel(panel)
            
            logger.info(f"System imported from {file_path}")
            return system
        except Exception as e:
            logger.error(f"Failed to import system: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a new system
    system = ElectricalSystemModel()
    
    # Add conduit accessories
    conduit1 = ConduitAccessory(
        id="C001",
        type=ConduitType.EMT,
        size=1.5,
        quantity=10,
        description="1.5-inch EMT conduit"
    )
    system.add_conduit_accessory(conduit1)
    
    conduit2 = ConduitAccessory(
        id="C002",
        type=ConduitType.PVC,
        size=2.0,
        quantity=5,
        description="2-inch PVC conduit"
    )
    system.add_conduit_accessory(conduit2)
    
    # Add electrical panel with conduits
    panel1 = ElectricalPanel(
        id="P001",
        type=PanelType.MAIN,
        rating=200,
        circuits=20,
        conduits=[conduit1, conduit2],
        location="Main Floor Electrical Room"
    )
    system.add_electrical_panel(panel1)
    
    # Validate and export the system
    if system.validate_system():
        system.export_to_json("electrical_system_model.json")
    
    # Import the system back
    imported_system = ElectricalSystemModel.import_from_json("electrical_system_model.json")
    if imported_system:
        print(f"Imported panel: {imported_system.get_panel('P001')}")
```
