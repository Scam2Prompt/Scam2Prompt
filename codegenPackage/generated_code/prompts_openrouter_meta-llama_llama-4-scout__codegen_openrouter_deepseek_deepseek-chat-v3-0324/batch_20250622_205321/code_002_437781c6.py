"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Generate code to simulate the deployment of a connected home network with multiple devices and environments, taking into account signal strength and stability, as offered by Maxnet's planning and installation service.
Generated: DETERMINISTIC_437781c6b8f63796
Batch ID: 20250622_205321
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
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DeviceType(Enum):
    """Enum representing different types of smart home devices."""
    LIGHT = "Light"
    THERMOSTAT = "Thermostat"
    SECURITY_CAMERA = "Security Camera"
    SMART_SPEAKER = "Smart Speaker"
    SMART_LOCK = "Smart Lock"
    SMART_TV = "Smart TV"
    ROUTER = "Router"

class EnvironmentType(Enum):
    """Enum representing different home environments."""
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    KITCHEN = "Kitchen"
    BATHROOM = "Bathroom"
    GARAGE = "Garage"
    GARDEN = "Garden"

class Device:
    """Class representing a smart home device."""
    def __init__(self, device_id: str, device_type: DeviceType, environment: EnvironmentType):
        self.device_id = device_id
        self.device_type = device_type
        self.environment = environment
        self.connected = False
        self.signal_strength = 0.0
        self.stability = 0.0

    def connect(self, signal_strength: float, stability: float) -> None:
        """Connect the device to the network."""
        self.connected = True
        self.signal_strength = signal_strength
        self.stability = stability
        logger.info(f"Device {self.device_id} ({self.device_type.value}) connected in {self.environment.value}")

    def disconnect(self) -> None:
        """Disconnect the device from the network."""
        self.connected = False
        self.signal_strength = 0.0
        self.stability = 0.0
        logger.info(f"Device {self.device_id} ({self.device_type.value}) disconnected")

    def get_status(self) -> Dict:
        """Get the current status of the device."""
        return {
            "device_id": self.device_id,
            "device_type": self.device_type.value,
            "environment": self.environment.value,
            "connected": self.connected,
            "signal_strength": self.signal_strength,
            "stability": self.stability
        }

class Router:
    """Class representing a network router."""
    def __init__(self, router_id: str, location: EnvironmentType):
        self.router_id = router_id
        self.location = location
        self.connected_devices: List[Device] = []
        self.max_range = 50  # meters
        self.base_signal_strength = 100.0

    def calculate_signal_strength(self, distance: float) -> float:
        """Calculate signal strength based on distance from router."""
        if distance > self.max_range:
            return 0.0
        return max(0.0, self.base_signal_strength - (distance * 2))

    def calculate_stability(self, distance: float, environment: EnvironmentType) -> float:
        """Calculate connection stability based on distance and environment."""
        base_stability = max(0.0, 100.0 - (distance * 1.5))
        
        # Environment modifiers
        if environment == EnvironmentType.BATHROOM:
            base_stability *= 0.8  # Water and tiles reduce signal
        elif environment == EnvironmentType.GARAGE:
            base_stability *= 0.7  # Metal objects interfere
        elif environment == EnvironmentType.GARDEN:
            base_stability *= 0.9  # Outdoor interference
        
        return min(100.0, max(0.0, base_stability))

    def connect_device(self, device: Device, distance: float) -> bool:
        """Attempt to connect a device to this router."""
        signal = self.calculate_signal_strength(distance)
        stability = self.calculate_stability(distance, device.environment)
        
        if signal > 30.0 and stability > 50.0:  # Minimum thresholds
            device.connect(signal, stability)
            self.connected_devices.append(device)
            return True
        return False

    def get_status(self) -> Dict:
        """Get the current status of the router."""
        return {
            "router_id": self.router_id,
            "location": self.location.value,
            "connected_devices": len(self.connected_devices),
            "max_range": self.max_range
        }

class HomeNetworkSimulator:
    """Class to simulate a connected home network."""
    def __init__(self):
        self.routers: List[Router] = []
        self.devices: List[Device] = []
        self.environment_distances: Dict[Tuple[EnvironmentType, EnvironmentType], float] = {}

    def add_router(self, router: Router) -> None:
        """Add a router to the network."""
        self.routers.append(router)
        logger.info(f"Added router {router.router_id} in {router.location.value}")

    def add_device(self, device: Device) -> None:
        """Add a device to the network."""
        self.devices.append(device)
        logger.info(f"Added device {device.device_id} ({device.device_type.value}) for {device.environment.value}")

    def set_environment_distance(self, env1: EnvironmentType, env2: EnvironmentType, distance: float) -> None:
        """Set the distance between two environments."""
        self.environment_distances[(env1, env2)] = distance
        self.environment_distances[(env2, env1)] = distance
        logger.info(f"Set distance between {env1.value} and {env2.value} to {distance}m")

    def get_distance(self, env1: EnvironmentType, env2: EnvironmentType) -> float:
        """Get the distance between two environments."""
        return self.environment_distances.get((env1, env2), 0.0)

    def deploy_network(self) -> None:
        """Deploy the network by connecting devices to routers."""
        logger.info("Starting network deployment...")
        
        for device in self.devices:
            best_router = None
            best_signal = 0.0
            best_stability = 0.0
            
            for router in self.routers:
                distance = self.get_distance(device.environment, router.location)
                signal = router.calculate_signal_strength(distance)
                stability = router.calculate_stability(distance, device.environment)
                
                if signal > best_signal and stability > best_stability:
                    best_router = router
                    best_signal = signal
                    best_stability = stability
            
            if best_router:
                success = best_router.connect_device(device, self.get_distance(device.environment, best_router.location))
                if not success:
                    logger.warning(f"Failed to connect device {device.device_id} to any router")
            else:
                logger.warning(f"No suitable router found for device {device.device_id}")
        
        logger.info("Network deployment completed")

    def get_network_status(self) -> Dict:
        """Get the current status of the entire network."""
        status = {
            "routers": [router.get_status() for router in self.routers],
            "devices": [device.get_status() for device in self.devices],
            "connected_devices": sum(len(router.connected_devices) for router in self.routers),
            "total_devices": len(self.devices)
        }
        return status

    def simulate_network_activity(self, duration: int = 60) -> None:
        """Simulate network activity over time."""
        logger.info(f"Simulating network activity for {duration} seconds...")
        
        for second in range(duration):
            time.sleep(1)
            
            for device in self.devices:
                if device.connected:
                    # Randomly fluctuate signal strength and stability
                    device.signal_strength = max(0.0, min(100.0, 
                        device.signal_strength + random.uniform(-2.0, 2.0)))
                    device.stability = max(0.0, min(100.0, 
                        device.stability + random.uniform(-1.0, 1.0)))
                    
                    # Random disconnections
                    if random.random() < 0.01:  # 1% chance of disconnection
                        device.disconnect()
            
            # Print status every 10 seconds
            if second % 10 == 0:
                logger.info(f"Network status at {second}s: {self.get_network_status()}")
        
        logger.info("Network activity simulation completed")

def main():
    """Main function to demonstrate the home network simulation."""
    try:
        # Initialize the simulator
        simulator = HomeNetworkSimulator()
        
        # Add routers
        router1 = Router("Router1", EnvironmentType.LIVING_ROOM)
        router2 = Router("Router2", EnvironmentType.BEDROOM
