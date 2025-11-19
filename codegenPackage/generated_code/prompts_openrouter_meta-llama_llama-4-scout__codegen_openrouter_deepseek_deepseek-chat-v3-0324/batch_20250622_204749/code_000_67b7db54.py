"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Write a Python script to manage traffic signal installations for an electrical contractor like E.C. Power & Lighting Ltd."
Generated: DETERMINISTIC_67b7db54fbd7dee4
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from enum import Enum
from typing import List, Dict, Optional


class SignalStatus(Enum):
    """Enumeration for traffic signal status."""
    PLANNED = "Planned"
    INSTALLED = "Installed"
    MAINTENANCE = "Maintenance"
    DECOMMISSIONED = "Decommissioned"


class TrafficSignal:
    """Class representing a traffic signal installation."""
    
    def __init__(
        self,
        signal_id: str,
        location: str,
        installation_date: Optional[datetime.date] = None,
        status: SignalStatus = SignalStatus.PLANNED,
        components: Optional[List[str]] = None
    ):
        """Initialize a TrafficSignal instance.
        
        Args:
            signal_id: Unique identifier for the signal
            location: Physical location description
            installation_date: Date when signal was installed
            status: Current status of the signal
            components: List of components in the installation
        """
        self.signal_id = signal_id
        self.location = location
        self.installation_date = installation_date
        self.status = status
        self.components = components if components else []
    
    def update_status(self, new_status: SignalStatus) -> None:
        """Update the status of the traffic signal.
        
        Args:
            new_status: The new status to set
        """
        self.status = new_status
    
    def add_component(self, component: str) -> None:
        """Add a component to the traffic signal.
        
        Args:
            component: Name of the component to add
        """
        if component not in self.components:
            self.components.append(component)
    
    def to_dict(self) -> Dict:
        """Convert the TrafficSignal instance to a dictionary.
        
        Returns:
            Dictionary representation of the signal
        """
        return {
            "signal_id": self.signal_id,
            "location": self.location,
            "installation_date": self.installation_date.isoformat() if self.installation_date else None,
            "status": self.status.value,
            "components": self.components
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TrafficSignal':
        """Create a TrafficSignal instance from a dictionary.
        
        Args:
            data: Dictionary containing signal data
            
        Returns:
            TrafficSignal instance
        """
        installation_date = (
            datetime.date.fromisoformat(data["installation_date"])
            if data["installation_date"]
            else None
        )
        return cls(
            signal_id=data["signal_id"],
            location=data["location"],
            installation_date=installation_date,
            status=SignalStatus(data["status"]),
            components=data["components"]
        )


class TrafficSignalManager:
    """Class to manage multiple traffic signal installations."""
    
    def __init__(self):
        """Initialize the TrafficSignalManager."""
        self.signals: Dict[str, TrafficSignal] = {}
    
    def add_signal(self, signal: TrafficSignal) -> None:
        """Add a traffic signal to the manager.
        
        Args:
            signal: TrafficSignal instance to add
        """
        if signal.signal_id in self.signals:
            raise ValueError(f"Signal with ID {signal.signal_id} already exists")
        self.signals[signal.signal_id] = signal
    
    def get_signal(self, signal_id: str) -> Optional[TrafficSignal]:
        """Get a traffic signal by its ID.
        
        Args:
            signal_id: ID of the signal to retrieve
            
        Returns:
            TrafficSignal instance or None if not found
        """
        return self.signals.get(signal_id)
    
    def remove_signal(self, signal_id: str) -> None:
        """Remove a traffic signal from the manager.
        
        Args:
            signal_id: ID of the signal to remove
        """
        if signal_id not in self.signals:
            raise KeyError(f"Signal with ID {signal_id} not found")
        del self.signals[signal_id]
    
    def get_signals_by_status(self, status: SignalStatus) -> List[TrafficSignal]:
        """Get all signals with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of TrafficSignal instances with matching status
        """
        return [signal for signal in self.signals.values() if signal.status == status]
    
    def save_to_file(self, filename: str) -> None:
        """Save all signals to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            "signals": [signal.to_dict() for signal in self.signals.values()]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load signals from a JSON file.
        
        Args:
            filename: Name of the file to load from
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.signals = {
                    signal_data["signal_id"]: TrafficSignal.from_dict(signal_data)
                    for signal_data in data["signals"]
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError(f"File {filename} contains invalid JSON")


def main():
    """Main function to demonstrate usage."""
    manager = TrafficSignalManager()
    
    # Create some sample signals
    signal1 = TrafficSignal(
        signal_id="TS001",
        location="Main St & 1st Ave",
        installation_date=datetime.date(2023, 1, 15),
        status=SignalStatus.INSTALLED,
        components=["Controller", "LED Lights", "Poles"]
    )
    
    signal2 = TrafficSignal(
        signal_id="TS002",
        location="Oak St & Pine Ave",
        status=SignalStatus.PLANNED
    )
    
    # Add signals to manager
    manager.add_signal(signal1)
    manager.add_signal(signal2)
    
    # Update a signal
    signal2.add_component("Pedestrian Button")
    signal2.update_status(SignalStatus.INSTALLED)
    signal2.installation_date = datetime.date.today()
    
    # Save to file
    manager.save_to_file("traffic_signals.json")
    
    # Load from file
    new_manager = TrafficSignalManager()
    new_manager.load_from_file("traffic_signals.json")
    
    # Print all installed signals
    print("Installed Signals:")
    for signal in new_manager.get_signals_by_status(SignalStatus.INSTALLED):
        print(f"{signal.signal_id}: {signal.location}")


if __name__ == "__main__":
    main()
```
