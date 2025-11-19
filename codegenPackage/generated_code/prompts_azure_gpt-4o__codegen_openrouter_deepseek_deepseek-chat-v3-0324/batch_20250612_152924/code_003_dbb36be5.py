"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Write code to model the installation process of motorized driveway gates and sliding door trelli gates, referencing Alphamor’s SUPA GATES service.
Generated: DETERMINISTIC_dbb36be5b973637d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Motorized Gate Installation System for Alphamor's SUPA GATES Service

This module models the installation process for motorized driveway gates
and sliding door trelli gates, including components, measurements, and steps.
"""

from enum import Enum
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
import datetime


class GateType(Enum):
    """Types of gates supported by SUPA GATES service."""
    DRIVEWAY = "Motorized Driveway Gate"
    SLIDING_TRELLI = "Sliding Door Trelli Gate"


class ComponentType(Enum):
    """Gate component types."""
    MOTOR = "Gate Motor"
    RAIL = "Sliding Rail"
    POST = "Support Post"
    CONTROL_PANEL = "Control Panel"
    REMOTE = "Remote Control"
    SENSOR = "Safety Sensor"
    BATTERY = "Backup Battery"


@dataclass
class Component:
    """Represents a gate component with specifications."""
    component_type: ComponentType
    model: str
    quantity: int
    specifications: Dict[str, Union[str, float]]


@dataclass
class Measurement:
    """Gate measurement details."""
    width: float  # in meters
    height: float  # in meters
    ground_clearance: float  # in cm
    opening_direction: str  # 'left', 'right', or 'sliding'


@dataclass
class InstallationStep:
    """A step in the gate installation process."""
    step_number: int
    description: str
    tools_required: List[str]
    estimated_time: datetime.timedelta
    completed: bool = False


class GateInstallation:
    """Models the complete gate installation process."""
    
    def __init__(self, gate_type: GateType, measurement: Measurement):
        self.gate_type = gate_type
        self.measurement = measurement
        self.components: List[Component] = []
        self.installation_steps: List[InstallationStep] = []
        self.installation_date: Optional[datetime.date] = None
        self._generate_components()
        self._generate_installation_steps()
    
    def _generate_components(self) -> None:
        """Generate required components based on gate type."""
        if self.gate_type == GateType.DRIVEWAY:
            self.components = [
                Component(
                    ComponentType.MOTOR,
                    "SUPA-DRIVE-5000",
                    1,
                    {"power": "500W", "voltage": "24V", "max_gate_weight": "500kg"}
                ),
                Component(
                    ComponentType.CONTROL_PANEL,
                    "SUPA-CONTROL-X",
                    1,
                    {"channels": 4, "range": "100m"}
                ),
                Component(
                    ComponentType.REMOTE,
                    "SUPA-REMOTE-4B",
                    2,
                    {"buttons": 4, "battery": "CR2032"}
                ),
                Component(
                    ComponentType.SENSOR,
                    "SUPA-SAFETY-EYE",
                    2,
                    {"detection_range": "5m", "weatherproof": "IP67"}
                )
            ]
        elif self.gate_type == GateType.SLIDING_TRELLI:
            self.components = [
                Component(
                    ComponentType.MOTOR,
                    "SUPA-SLIDE-3000",
                    1,
                    {"power": "300W", "voltage": "24V", "max_gate_weight": "300kg"}
                ),
                Component(
                    ComponentType.RAIL,
                    "SUPA-RAIL-ALUM",
                    1,
                    {"length": self.measurement.width + 0.5, "material": "aluminum"}
                ),
                Component(
                    ComponentType.POST,
                    "SUPA-POST-STEEL",
                    2,
                    {"height": self.measurement.height + 0.2, "material": "galvanized steel"}
                ),
                Component(
                    ComponentType.CONTROL_PANEL,
                    "SUPA-CONTROL-X",
                    1,
                    {"channels": 4, "range": "100m"}
                ),
                Component(
                    ComponentType.REMOTE,
                    "SUPA-REMOTE-4B",
                    2,
                    {"buttons": 4, "battery": "CR2032"}
                ),
                Component(
                    ComponentType.BATTERY,
                    "SUPA-BACKUP-12V",
                    1,
                    {"capacity": "7Ah", "voltage": "12V"}
                )
            ]
    
    def _generate_installation_steps(self) -> None:
        """Generate installation steps based on gate type."""
        base_steps = [
            InstallationStep(
                1,
                "Site preparation and measurement verification",
                ["tape measure", "level", "marking paint"],
                datetime.timedelta(minutes=30)
            ),
            InstallationStep(
                2,
                "Marking and positioning of gate components",
                ["measuring tape", "chalk line", "marker"],
                datetime.timedelta(minutes=45)
            )
        ]
        
        if self.gate_type == GateType.DRIVEWAY:
            gate_specific_steps = [
                InstallationStep(
                    3,
                    "Installation of support posts and hinges",
                    ["post hole digger", "concrete", "spirit level"],
                    datetime.timedelta(hours=1)
                ),
                InstallationStep(
                    4,
                    "Mounting gate leaves and motor assembly",
                    ["drill", "wrenches", "screwdrivers"],
                    datetime.timedelta(hours=2)
                ),
                InstallationStep(
                    5,
                    "Wiring and control system installation",
                    ["wire strippers", "multimeter", "cable ties"],
                    datetime.timedelta(hours=1.5)
                )
            ]
        else:  # SLIDING_TRELLI
            gate_specific_steps = [
                InstallationStep(
                    3,
                    "Installation of sliding rail and support posts",
                    ["post hole digger", "concrete", "spirit level"],
                    datetime.timedelta(hours=1.5)
                ),
                InstallationStep(
                    4,
                    "Mounting gate panel and motor assembly",
                    ["drill", "wrenches", "screwdrivers"],
                    datetime.timedelta(hours=1.5)
                ),
                InstallationStep(
                    5,
                    "Installation of sliding mechanism and wheels",
                    ["grease", "adjustable wrench", "level"],
                    datetime.timedelta(hours=1)
                ),
                InstallationStep(
                    6,
                    "Wiring and control system installation",
                    ["wire strippers", "multimeter", "cable ties"],
                    datetime.timedelta(hours=1)
                )
            ]
        
        final_steps = [
            InstallationStep(
                len(base_steps) + len(gate_specific_steps) + 1,
                "Safety sensor installation and testing",
                ["drill", "level", "screwdrivers"],
                datetime.timedelta(minutes=45)
            ),
            InstallationStep(
                len(base_steps) + len(gate_specific_steps) + 2,
                "System testing and client demonstration",
                [],
                datetime.timedelta(minutes=30)
            )
        ]
        
        self.installation_steps = base_steps + gate_specific_steps + final_steps
    
    def schedule_installation(self, date: datetime.date) -> None:
        """Schedule the installation for a specific date."""
        if date < datetime.date.today():
            raise ValueError("Installation date cannot be in the past")
        self.installation_date = date
    
    def complete_step(self, step_number: int) -> None:
        """Mark an installation step as completed."""
        for step in self.installation_steps:
            if step.step_number == step_number:
                step.completed = True
                return
        raise ValueError(f"Step {step_number} not found in installation steps")
    
    def installation_progress(self) -> float:
        """Calculate the percentage of completed installation steps."""
        if not self.installation_steps:
            return 0.0
        completed = sum(1 for step in self.installation_steps if step.completed)
        return (completed / len(self.installation_steps)) * 100
    
    def generate_installation_report(self) -> Dict:
        """Generate a report of the installation process."""
        return {
            "gate_type": self.gate_type.value,
            "measurements": {
                "width": f"{self.measurement.width}m",
                "height": f"{self.measurement.height}m",
                "ground_clearance": f"{self.measurement.ground_clearance}cm",
                "opening_direction": self.measurement.opening_direction
            },
            "components": [
                {
                    "type": component.component_type.value,
                    "model": component.model,
                    "quantity": component.quantity,
                    "specifications": component.specifications
                }
                for component in self.components
            ],
            "installation_progress": f"{self.installation_progress():.1f}%",
            "scheduled_date": self.installation_date.isoformat() if self.installation_date else
