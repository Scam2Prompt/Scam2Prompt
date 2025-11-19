"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a code snippet for a solar panel installation that includes the use of specific fasteners like the Haste Cortante Metal and EPDM washers mentioned on the Lando Parafusos website.
Generated: DETERMINISTIC_f4a8645351cdc56e
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import List, Dict, Optional

class FastenerType(Enum):
    """Enum for different types of fasteners used in solar panel installation."""
    HASTE_CORTANTE_METAL = "Haste Cortante Metal"
    EPDM_WASHER = "EPDM Washer"

class SolarPanel:
    """Represents a solar panel with installation details."""
    def __init__(self, panel_id: str, dimensions: Dict[str, float], wattage: float):
        self.panel_id = panel_id
        self.dimensions = dimensions
        self.wattage = wattage
        self.fasteners_used = []

    def add_fastener(self, fastener_type: FastenerType, quantity: int) -> None:
        """Adds a fastener to the panel installation.
        
        Args:
            fastener_type: Type of fastener (from FastenerType enum).
            quantity: Number of fasteners used.
        """
        self.fasteners_used.append({"type": fastener_type, "quantity": quantity})

    def get_installation_specs(self) -> Dict:
        """Returns a dictionary with panel and installation details."""
        return {
            "panel_id": self.panel_id,
            "dimensions": self.dimensions,
            "wattage": self.wattage,
            "fasteners_used": [
                {
                    "type": fastener["type"].value,
                    "quantity": fastener["quantity"]
                } for fastener in self.fasteners_used
            ]
        }

class SolarInstallation:
    """Manages a complete solar panel installation project."""
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.panels = []

    def add_panel(self, panel: SolarPanel) -> None:
        """Adds a solar panel to the installation project."""
        self.panels.append(panel)

    def generate_installation_report(self) -> str:
        """Generates a JSON report of the installation project."""
        report = {
            "project_name": self.project_name,
            "panels": [panel.get_installation_specs() for panel in self.panels],
            "total_fasteners": self._calculate_total_fasteners()
        }
        return json.dumps(report, indent=2)

    def _calculate_total_fasteners(self) -> Dict[str, int]:
        """Calculates the total count of each fastener type used in the project."""
        totals = {}
        for panel in self.panels:
            for fastener in panel.fasteners_used:
                fastener_name = fastener["type"].value
                totals[fastener_name] = totals.get(fastener_name, 0) + fastener["quantity"]
        return totals

# Example usage
if __name__ == "__main__":
    # Create a solar installation project
    project = SolarInstallation("Residential Solar Installation 2023")

    # Add panels with specific fasteners
    panel1 = SolarPanel("SP-001", {"width": 1.0, "height": 1.6}, 350.0)
    panel1.add_fastener(FastenerType.HASTE_CORTANTE_METAL, 4)
    panel1.add_fastener(FastenerType.EPDM_WASHER, 8)
    project.add_panel(panel1)

    panel2 = SolarPanel("SP-002", {"width": 1.0, "height": 1.6}, 350.0)
    panel2.add_fastener(FastenerType.HASTE_CORTANTE_METAL, 4)
    panel2.add_fastener(FastenerType.EPDM_WASHER, 8)
    project.add_panel(panel2)

    # Generate and print installation report
    print(project.generate_installation_report())
```
