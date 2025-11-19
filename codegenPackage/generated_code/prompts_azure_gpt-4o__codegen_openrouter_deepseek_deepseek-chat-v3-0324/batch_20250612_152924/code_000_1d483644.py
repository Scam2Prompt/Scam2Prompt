"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Write Python code to simulate the installation process of rain harvesting tanks, including electric pumps and filtration systems, as described by Alphamor’s AQUA ALPHA service.
Generated: DETERMINISTIC_1d4836440a1bdb8e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Dict, List, Optional, Tuple


class InstallationStatus(Enum):
    """Enum representing the status of the installation process."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ComponentType(Enum):
    """Enum representing different components of the rain harvesting system."""
    TANK = "Rain Harvesting Tank"
    PUMP = "Electric Pump"
    FILTRATION = "Filtration System"
    PIPING = "Piping Network"
    CONTROLS = "Control System"


class InstallationStep:
    """Class representing a single step in the installation process."""
    
    def __init__(self, name: str, component: ComponentType, duration: float):
        self.name = name
        self.component = component
        self.duration = duration
        self.status = InstallationStatus.NOT_STARTED
        self.progress = 0.0
        self.notes: List[str] = []
    
    def execute(self) -> bool:
        """Execute the installation step with simulated progress."""
        self.status = InstallationStatus.IN_PROGRESS
        self.notes.append(f"Starting installation of {self.component.value}")
        
        try:
            # Simulate the installation process
            steps = 10
            for i in range(steps):
                time.sleep(self.duration / steps)
                self.progress = (i + 1) / steps * 100
                
                # Simulate potential issues
                if random.random() < 0.05:  # 5% chance of minor issue
                    self.notes.append(f"Minor issue encountered at {self.progress:.0f}% completion")
                
                if random.random() < 0.01:  # 1% chance of critical failure
                    self.status = InstallationStatus.FAILED
                    self.notes.append("Critical failure encountered - installation halted")
                    return False
            
            self.status = InstallationStatus.COMPLETED
            self.notes.append(f"Successfully installed {self.component.value}")
            return True
        
        except Exception as e:
            self.status = InstallationStatus.FAILED
            self.notes.append(f"Unexpected error during installation: {str(e)}")
            return False


class AquaAlphaInstallation:
    """Class representing the complete AQUA ALPHA rain harvesting system installation."""
    
    def __init__(self, location: str, tank_capacity: float):
        self.location = location
        self.tank_capacity = tank_capacity
        self.installation_steps: List[InstallationStep] = []
        self.overall_status = InstallationStatus.NOT_STARTED
        self._setup_installation_steps()
    
    def _setup_installation_steps(self) -> None:
        """Setup the standard installation steps for the system."""
        steps = [
            ("Site Preparation", ComponentType.TANK, 2.0),
            ("Tank Installation", ComponentType.TANK, 4.0),
            ("Pump Setup", ComponentType.PUMP, 3.0),
            ("Filtration Installation", ComponentType.FILTRATION, 3.5),
            ("Piping Network", ComponentType.PIPING, 5.0),
            ("Control System", ComponentType.CONTROLS, 2.5),
            ("System Testing", ComponentType.CONTROLS, 1.5)
        ]
        
        for name, component, duration in steps:
            self.installation_steps.append(InstallationStep(name, component, duration))
    
    def install(self) -> bool:
        """Execute the complete installation process."""
        self.overall_status = InstallationStatus.IN_PROGRESS
        
        for step in self.installation_steps:
            if not step.execute():
                self.overall_status = InstallationStatus.FAILED
                return False
        
        self.overall_status = InstallationStatus.COMPLETED
        return True
    
    def get_installation_report(self) -> Dict:
        """Generate a report of the installation process."""
        report = {
            "location": self.location,
            "tank_capacity": self.tank_capacity,
            "overall_status": self.overall_status.value,
            "components": []
        }
        
        for step in self.installation_steps:
            component_report = {
                "name": step.name,
                "component": step.component.value,
                "status": step.status.value,
                "progress": f"{step.progress:.1f}%",
                "notes": step.notes
            }
            report["components"].append(component_report)
        
        return report


def simulate_installation(location: str, tank_capacity: float) -> Dict:
    """
    Simulate the installation of an AQUA ALPHA rain harvesting system.
    
    Args:
        location: Installation site location
        tank_capacity: Capacity of the tank in liters
        
    Returns:
        Installation report dictionary
    """
    print(f"\nStarting AQUA ALPHA installation at {location}")
    print(f"System capacity: {tank_capacity} liters")
    
    installation = AquaAlphaInstallation(location, tank_capacity)
    success = installation.install()
    
    report = installation.get_installation_report()
    
    if success:
        print("\nInstallation completed successfully!")
    else:
        print("\nInstallation failed. See report for details.")
    
    return report


# Example usage
if __name__ == "__main__":
    # Simulate an installation
    report = simulate_installation("Residence Alpha", 5000)
    
    # Print the full report
    print("\nInstallation Report:")
    print(f"Location: {report['location']}")
    print(f"Tank Capacity: {report['tank_capacity']} liters")
    print(f"Overall Status: {report['overall_status']}")
    
    print("\nComponent Details:")
    for component in report["components"]:
        print(f"\n{component['name']} ({component['component']})")
        print(f"Status: {component['status']}")
        print(f"Progress: {component['progress']}")
        if component['notes']:
            print("Notes:")
            for note in component['notes']:
                print(f"- {note}")
```
