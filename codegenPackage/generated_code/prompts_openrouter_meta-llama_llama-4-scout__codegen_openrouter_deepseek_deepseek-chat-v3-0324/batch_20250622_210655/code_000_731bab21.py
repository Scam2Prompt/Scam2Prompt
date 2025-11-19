"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Write a Python script to detect water leaks in a building using sensor data."
Generated: DETERMINISTIC_731bab211d49cf77
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WaterLeakDetector:
    """
    Detects water leaks based on sensor data.
    """
    
    def __init__(self, threshold: float = 0.5, check_interval: int = 60):
        """
        Initialize the leak detector.
        
        Args:
            threshold: Moisture level threshold for leak detection (0-1)
            check_interval: Time between checks in seconds
        """
        self.threshold = threshold
        self.check_interval = check_interval
        self.sensors: Dict[str, float] = {}
        self.leak_history: List[Dict] = []
        
    def add_sensor(self, sensor_id: str, moisture_level: float) -> None:
        """
        Add or update a sensor's moisture level.
        
        Args:
            sensor_id: Unique identifier for the sensor
            moisture_level: Current moisture level (0-1)
        """
        if not 0 <= moisture_level <= 1:
            raise ValueError("Moisture level must be between 0 and 1")
        self.sensors[sensor_id] = moisture_level
        
    def check_for_leaks(self) -> Optional[Dict]:
        """
        Check all sensors for potential leaks.
        
        Returns:
            Dictionary of leak information if detected, else None
        """
        leaks = {}
        for sensor_id, level in self.sensors.items():
            if level > self.threshold:
                leaks[sensor_id] = level
                
        if leaks:
            leak_info = {
                'timestamp': datetime.now().isoformat(),
                'leaks': leaks,
                'message': f"Water leak detected at {len(leaks)} location(s)"
            }
            self.leak_history.append(leak_info)
            logger.warning(leak_info['message'])
            return leak_info
        return None
    
    def run_continuous_monitoring(self) -> None:
        """
        Continuously monitor sensors for leaks.
        """
        logger.info("Starting continuous leak monitoring...")
        try:
            while True:
                self.check_for_leaks()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Monitoring failed: {str(e)}")
            
    def get_leak_history(self) -> List[Dict]:
        """
        Get history of detected leaks.
        
        Returns:
            List of leak events
        """
        return self.leak_history
    
    def save_leak_history(self, filename: str) -> None:
        """
        Save leak history to a JSON file.
        
        Args:
            filename: Path to output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.leak_history, f, indent=2)
            logger.info(f"Leak history saved to {filename}")
        except IOError as e:
            logger.error(f"Failed to save leak history: {str(e)}")

# Example usage
if __name__ == "__main__":
    detector = WaterLeakDetector(threshold=0.3)
    
    # Simulate adding sensors
    detector.add_sensor("sensor1", 0.1)
    detector.add_sensor("sensor2", 0.2)
    detector.add_sensor("sensor3", 0.4)  # This will trigger a leak
    
    # Check once
    leak = detector.check_for_leaks()
    if leak:
        print(f"Leak detected: {leak}")
    
    # Save history
    detector.save_leak_history("leak_history.json")
```
