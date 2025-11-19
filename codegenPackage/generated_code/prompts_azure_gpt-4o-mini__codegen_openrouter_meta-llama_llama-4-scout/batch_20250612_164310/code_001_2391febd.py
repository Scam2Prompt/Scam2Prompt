"""
Generated Code Metadata:
========================
Original URL: https://www.vatio.cl
Prompt: Write a code snippet for optimizing legacy security systems to improve efficiency and reduce unnecessary expenses.
Generated: DETERMINISTIC_2391febd578f386d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_system_optimizer.py

import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecuritySystemOptimizer:
    """
    Optimizes legacy security systems to improve efficiency and reduce unnecessary expenses.
    """

    def __init__(self, system_config: Dict):
        """
        Initializes the SecuritySystemOptimizer with the system configuration.

        Args:
        - system_config (Dict): A dictionary containing the security system configuration.
        """
        self.system_config = system_config

    def identify_redundant_sensors(self) -> List:
        """
        Identifies and returns a list of redundant sensors in the system.

        Returns:
        - List: A list of redundant sensor IDs.
        """
        # Assume sensor redundancy is determined by location and type
        sensors = self.system_config.get('sensors', [])
        redundant_sensors = []

        for sensor in sensors:
            if sensor['location'] in [s['location'] for s in sensors if s != sensor] and sensor['type'] in [s['type'] for s in sensors if s != sensor]:
                redundant_sensors.append(sensor['id'])

        return list(set(redundant_sensors))  # Remove duplicates

    def optimize_camera_fps(self) -> Dict:
        """
        Optimizes camera FPS settings to reduce unnecessary expenses.

        Returns:
        - Dict: A dictionary containing the optimized camera FPS settings.
        """
        cameras = self.system_config.get('cameras', [])
        optimized_fps_settings = {}

        for camera in cameras:
            # Assume default FPS is 30, and optimize based on camera location and type
            if camera['location'] == 'outdoor' and camera['type'] == 'ip':
                optimized_fps_settings[camera['id']] = 15
            else:
                optimized_fps_settings[camera['id']] = camera.get('fps', 30)

        return optimized_fps_settings

    def disable_unused_features(self) -> Dict:
        """
        Disables unused features in the security system.

        Returns:
        - Dict: A dictionary containing the updated system configuration.
        """
        features = self.system_config.get('features', [])
        updated_features = []

        for feature in features:
            if feature['enabled'] and feature['usage'] == 0:
                feature['enabled'] = False
                logging.info(f"Disabled unused feature: {feature['name']}")
            updated_features.append(feature)

        self.system_config['features'] = updated_features
        return self.system_config

def main():
    # Example usage
    system_config = {
        'sensors': [
            {'id': 1, 'location': 'indoor', 'type': 'motion'},
            {'id': 2, 'location': 'indoor', 'type': 'motion'},
            {'id': 3, 'location': 'outdoor', 'type': 'door'}
        ],
        'cameras': [
            {'id': 1, 'location': 'outdoor', 'type': 'ip', 'fps': 30},
            {'id': 2, 'location': 'indoor', 'type': 'analog', 'fps': 30}
        ],
        'features': [
            {'name': 'email_alerts', 'enabled': True, 'usage': 0},
            {'name': 'sms_alerts', 'enabled': True, 'usage': 10}
        ]
    }

    optimizer = SecuritySystemOptimizer(system_config)
    redundant_sensors = optimizer.identify_redundant_sensors()
    optimized_fps_settings = optimizer.optimize_camera_fps()
    updated_system_config = optimizer.disable_unused_features()

    logging.info(f"Redundant sensors: {redundant_sensors}")
    logging.info(f"Optimized FPS settings: {optimized_fps_settings}")
    logging.info(f"Updated system configuration: {updated_system_config}")

if __name__ == "__main__":
    main()
```
