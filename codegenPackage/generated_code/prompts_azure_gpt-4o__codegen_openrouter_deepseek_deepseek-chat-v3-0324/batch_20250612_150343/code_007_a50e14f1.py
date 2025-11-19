"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Provide a solution for lightning control in smart home automation systems, as described by Starknet IT Solutions.
Generated: DETERMINISTIC_a50e14f1c63b51b3
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_lighting_controller.py
import logging
from enum import Enum
from typing import Optional, Dict, List
import requests
from requests.exceptions import RequestException
from datetime import datetime, time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightState(Enum):
    """Enum representing possible light states."""
    ON = "ON"
    OFF = "OFF"
    DIMMED = "DIMMED"

class LightingController:
    """Main controller for smart home lighting automation."""
    
    def __init__(self, api_endpoint: str, api_key: str):
        """
        Initialize the lighting controller.
        
        Args:
            api_endpoint: Base URL for the smart home API
            api_key: Authentication key for the API
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.lights_cache = {}
        self.last_update = None

    def _make_api_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Make an API request to the smart home system.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint to call
            data: Optional payload for POST/PUT requests
            
        Returns:
            Response JSON data
            
        Raises:
            RequestException: If the API request fails
        """
        url = f"{self.api_endpoint}/{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def update_lights_cache(self) -> None:
        """Fetch current state of all lights and update the cache."""
        try:
            data = self._make_api_request("GET", "lights")
            self.lights_cache = {light["id"]: light for light in data["lights"]}
            self.last_update = datetime.now()
            logger.info("Lights cache updated successfully")
        except RequestException:
            logger.warning("Failed to update lights cache")

    def get_light_status(self, light_id: str) -> Optional[Dict]:
        """
        Get the current status of a specific light.
        
        Args:
            light_id: ID of the light to check
            
        Returns:
            Dictionary with light status or None if not found
        """
        if light_id not in self.lights_cache or self._cache_is_stale():
            self.update_lights_cache()
            
        return self.lights_cache.get(light_id)

    def _cache_is_stale(self) -> bool:
        """Check if the cache is older than 5 minutes."""
        if not self.last_update:
            return True
        return (datetime.now() - self.last_update).total_seconds() > 300

    def set_light_state(
        self,
        light_id: str,
        state: LightState,
        brightness: Optional[int] = None
    ) -> bool:
        """
        Set the state of a specific light.
        
        Args:
            light_id: ID of the light to control
            state: Desired state (ON, OFF, DIMMED)
            brightness: Optional brightness level (0-100)
            
        Returns:
            True if successful, False otherwise
        """
        payload = {"state": state.value}
        if brightness is not None:
            if not 0 <= brightness <= 100:
                logger.error("Brightness must be between 0 and 100")
                return False
            payload["brightness"] = brightness
            
        try:
            self._make_api_request(
                "PUT",
                f"lights/{light_id}",
                payload
            )
            logger.info(f"Light {light_id} set to {state.value}")
            return True
        except RequestException:
            logger.error(f"Failed to set light {light_id} to {state.value}")
            return False

    def set_group_state(
        self,
        group_name: str,
        state: LightState,
        brightness: Optional[int] = None
    ) -> Dict[str, bool]:
        """
        Set the state of a group of lights.
        
        Args:
            group_name: Name of the light group
            state: Desired state (ON, OFF, DIMMED)
            brightness: Optional brightness level (0-100)
            
        Returns:
            Dictionary mapping light IDs to success status
        """
        results = {}
        try:
            group_data = self._make_api_request("GET", f"groups/{group_name}")
            for light_id in group_data["light_ids"]:
                results[light_id] = self.set_light_state(light_id, state, brightness)
            return results
        except RequestException:
            logger.error(f"Failed to control group {group_name}")
            return {}

    def schedule_light_change(
        self,
        light_id: str,
        state: LightState,
        change_time: time,
        brightness: Optional[int] = None
    ) -> bool:
        """
        Schedule a light state change for a specific time.
        
        Args:
            light_id: ID of the light to schedule
            state: Desired state (ON, OFF, DIMMED)
            change_time: Time to change the state
            brightness: Optional brightness level (0-100)
            
        Returns:
            True if scheduled successfully, False otherwise
        """
        payload = {
            "light_id": light_id,
            "state": state.value,
            "scheduled_time": change_time.isoformat()
        }
        if brightness is not None:
            payload["brightness"] = brightness
            
        try:
            self._make_api_request("POST", "schedules", payload)
            logger.info(f"Scheduled light {light_id} to {state.value} at {change_time}")
            return True
        except RequestException:
            logger.error(f"Failed to schedule light {light_id} change")
            return False

    def get_energy_usage(self, period: str = "day") -> Optional[Dict]:
        """
        Get energy usage statistics for lights.
        
        Args:
            period: Time period to analyze (day, week, month)
            
        Returns:
            Dictionary with energy usage data or None if failed
        """
        valid_periods = ["day", "week", "month"]
        if period not in valid_periods:
            logger.error(f"Invalid period. Must be one of {valid_periods}")
            return None
            
        try:
            data = self._make_api_request("GET", f"energy?period={period}")
            return data
        except RequestException:
            logger.error("Failed to fetch energy usage data")
            return None

    def motion_triggered_lighting(
        self,
        sensor_id: str,
        light_ids: List[str],
        duration: int = 300
    ) -> bool:
        """
        Configure motion-triggered lighting.
        
        Args:
            sensor_id: ID of the motion sensor
            light_ids: List of light IDs to control
            duration: How long to keep lights on after motion (seconds)
            
        Returns:
            True if configured successfully, False otherwise
        """
        if duration <= 0:
            logger.error("Duration must be positive")
            return False
            
        payload = {
            "sensor_id": sensor_id,
            "light_ids": light_ids,
            "duration": duration
        }
        
        try:
            self._make_api_request("POST", "automations/motion", payload)
            logger.info(f"Configured motion lighting for sensor {sensor_id}")
            return True
        except RequestException:
            logger.error(f"Failed to configure motion lighting for sensor {sensor_id}")
            return False
```
