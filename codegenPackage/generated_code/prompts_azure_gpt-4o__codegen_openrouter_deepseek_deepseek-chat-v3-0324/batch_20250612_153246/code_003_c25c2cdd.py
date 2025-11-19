"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Provide a code example for configuring IT cabling and audio-video integration in a smart home environment, based on eControl SA's services in câblages informatiques and audio/vidéo.
Generated: DETERMINISTIC_c25c2cdd32076848
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Smart Home IT Cabling and AV Integration Configuration
This script simulates the configuration of IT cabling and AV integration
for a smart home environment based on eControl SA's services.
"""

import json
from enum import Enum
from typing import Dict, List, Optional

class ConnectionType(Enum):
    """Types of connections available for cabling"""
    ETHERNET = "Ethernet"
    FIBER = "Fiber Optic"
    COAXIAL = "Coaxial"
    HDMI = "HDMI"
    AUDIO = "Audio"

class DeviceType(Enum):
    """Types of devices in the smart home"""
    ROUTER = "Router"
    SWITCH = "Switch"
    MEDIA_SERVER = "Media Server"
    TV = "Television"
    SPEAKER = "Speaker"
    CAMERA = "Security Camera"
    LIGHTING = "Smart Lighting"

class Room:
    """Represents a room in the smart home"""
    def __init__(self, name: str):
        self.name = name
        self.devices: List[Device] = []
        self.connections: List[Connection] = []

    def add_device(self, device: 'Device') -> None:
        """Add a device to the room"""
        self.devices.append(device)
    
    def add_connection(self, connection: 'Connection') -> None:
        """Add a connection to the room"""
        self.connections.append(connection)
    
    def to_dict(self) -> Dict:
        """Convert room configuration to dictionary"""
        return {
            "name": self.name,
            "devices": [device.to_dict() for device in self.devices],
            "connections": [conn.to_dict() for conn in self.connections]
        }

class Device:
    """Represents a smart home device"""
    def __init__(self, device_type: DeviceType, name: str, ip_address: Optional[str] = None):
        self.device_type = device_type
        self.name = name
        self.ip_address = ip_address
    
    def to_dict(self) -> Dict:
        """Convert device configuration to dictionary"""
        return {
            "type": self.device_type.value,
            "name": self.name,
            "ip_address": self.ip_address
        }

class Connection:
    """Represents a connection between devices"""
    def __init__(self, connection_type: ConnectionType, source: Device, destination: Device):
        self.connection_type = connection_type
        self.source = source
        self.destination = destination
    
    def to_dict(self) -> Dict:
        """Convert connection configuration to dictionary"""
        return {
            "type": self.connection_type.value,
            "source": self.source.name,
            "destination": self.destination.name
        }

class SmartHomeConfigurator:
    """Main class for configuring smart home IT and AV systems"""
    def __init__(self):
        self.rooms: Dict[str, Room] = {}
    
    def add_room(self, room_name: str) -> Room:
        """Add a new room to the configuration"""
        if room_name in self.rooms:
            raise ValueError(f"Room '{room_name}' already exists")
        self.rooms[room_name] = Room(room_name)
        return self.rooms[room_name]
    
    def get_room(self, room_name: str) -> Room:
        """Get an existing room"""
        if room_name not in self.rooms:
            raise ValueError(f"Room '{room_name}' not found")
        return self.rooms[room_name]
    
    def generate_configuration(self) -> Dict:
        """Generate the complete configuration"""
        return {
            "rooms": [room.to_dict() for room in self.rooms.values()]
        }
    
    def save_configuration(self, filename: str) -> None:
        """Save configuration to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_configuration(), f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save configuration: {str(e)}")

def configure_sample_smart_home() -> SmartHomeConfigurator:
    """Sample configuration of a smart home"""
    configurator = SmartHomeConfigurator()
    
    # Living Room Setup
    living_room = configurator.add_room("Living Room")
    router = Device(DeviceType.ROUTER, "Main Router", "192.168.1.1")
    media_server = Device(DeviceType.MEDIA_SERVER, "Media Server", "192.168.1.10")
    tv = Device(DeviceType.TV, "Smart TV", "192.168.1.20")
    speaker = Device(DeviceType.SPEAKER, "Sound System")
    
    living_room.add_device(router)
    living_room.add_device(media_server)
    living_room.add_device(tv)
    living_room.add_device(speaker)
    
    living_room.add_connection(Connection(ConnectionType.ETHERNET, router, media_server))
    living_room.add_connection(Connection(ConnectionType.HDMI, media_server, tv))
    living_room.add_connection(Connection(ConnectionType.AUDIO, media_server, speaker))
    
    # Bedroom Setup
    bedroom = configurator.add_room("Bedroom")
    tv_bedroom = Device(DeviceType.TV, "Bedroom TV", "192.168.1.21")
    bedroom.add_device(tv_bedroom)
    bedroom.add_connection(Connection(ConnectionType.HDMI, media_server, tv_bedroom))
    
    return configurator

if __name__ == "__main__":
    try:
        config = configure_sample_smart_home()
        config.save_configuration("smart_home_config.json")
        print("Smart home configuration saved successfully.")
    except Exception as e:
        print(f"Error configuring smart home: {str(e)}")
```
