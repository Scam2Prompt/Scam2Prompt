"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Write a Python script that integrates multiple AVL technologies to create an interactive experience, as highlighted in the Pro Integration Future Asia 2025 event.
Generated: DETERMINISTIC_01c1261f10b4fbc2
Batch ID: 20250612_163406
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.avl-future-asia.example.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import time
from typing import Dict, List, Optional, Union
import requests
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class AVLDevice:
    """Represents an AVL (Autonomous Vehicle & IoT) device."""
    device_id: str
    device_type: str
    status: str
    metadata: Dict[str, Union[str, int, float]]

class AVLIntegrationManager:
    """Manages integration of multiple AVL technologies for an interactive experience."""
    
    def __init__(self, api_endpoint: str, api_key: str):
        """
        Initialize the AVL integration manager.
        
        Args:
            api_endpoint: Base URL for the AVL API
            api_key: API key for authentication
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.devices: Dict[str, AVLDevice] = {}
        
    def fetch_devices(self) -> bool:
        """
        Fetch all registered AVL devices from the API.
        
        Returns:
            bool: True if successful, False otherwise
        """
        url = f"{self.api_endpoint}/devices"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            devices_data = response.json()
            
            self.devices.clear()
            for device_data in devices_data:
                device = AVLDevice(
                    device_id=device_data['id'],
                    device_type=device_data['type'],
                    status=device_data['status'],
                    metadata=device_data.get('metadata', {})
                )
                self.devices[device.device_id] = device
                
            logger.info(f"Successfully fetched {len(self.devices)} devices")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch devices: {str(e)}")
            return False
    
    def send_command(
        self,
        device_id: str,
        command: str,
        params: Optional[Dict[str, Union[str, int, float]]] = None
    ) -> bool:
        """
        Send a command to a specific AVL device.
        
        Args:
            device_id: ID of the target device
            command: Command to execute
            params: Optional parameters for the command
            
        Returns:
            bool: True if command was successful, False otherwise
        """
        if device_id not in self.devices:
            logger.error(f"Device {device_id} not found")
            return False
            
        url = f"{self.api_endpoint}/devices/{device_id}/command"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "command": command,
            "parameters": params or {}
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            logger.info(f"Command '{command}' sent to device {device_id}")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send command to device {device_id}: {str(e)}")
            return False
    
    def start_interactive_experience(self, scene_id: str) -> bool:
        """
        Start an interactive AVL experience with multiple synchronized devices.
        
        Args:
            scene_id: ID of the scene/experience to start
            
        Returns:
            bool: True if successful, False otherwise
        """
        url = f"{self.api_endpoint}/experiences/start"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "scene_id": scene_id,
            "timestamp": int(time.time())
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            
            # Update device statuses after experience starts
            self.fetch_devices()
            logger.info(f"Started interactive experience: {scene_id}")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to start experience {scene_id}: {str(e)}")
            return False
    
    def monitor_devices(self, interval: int = 5) -> None:
        """
        Continuously monitor device statuses.
        
        Args:
            interval: Monitoring interval in seconds
        """
        logger.info("Starting device monitoring...")
        try:
            while True:
                self.fetch_devices()
                for device_id, device in self.devices.items():
                    logger.debug(
                        f"Device {device_id} ({device.device_type}): {device.status}"
                    )
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Device monitoring stopped")

def main():
    # Configuration - these should ideally come from environment variables or config files
    config = {
        "api_endpoint": "https://api.avl-future-asia.example.com/v1",
        "api_key": "secure-api-key-here",
        "scene_id": "interactive-future-2025"
    }
    
    # Initialize the integration manager
    avl_manager = AVLIntegrationManager(
        api_endpoint=config["api_endpoint"],
        api_key=config["api_key"]
    )
    
    # Fetch and display devices
    if not avl_manager.fetch_devices():
        logger.error("Initial device fetch failed. Exiting.")
        return
    
    # Start the interactive experience
    if not avl_manager.start_interactive_experience(config["scene_id"]):
        logger.error("Failed to start interactive experience. Exiting.")
        return
    
    # Example: Send a command to the first device (if available)
    if avl_manager.devices:
        first_device_id = next(iter(avl_manager.devices))
        avl_manager.send_command(
            device_id=first_device_id,
            command="activate",
            params={"intensity": 75}
        )
    
    # Start monitoring devices (this will run until interrupted)
    avl_manager.monitor_devices()

if __name__ == "__main__":
    main()
```
