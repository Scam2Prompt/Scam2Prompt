"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: Write Python code to implement an edge computing solution using concepts mentioned in Polystack Technologies' STAQ-R1, STAQ-R2, or STAQ-R3 products. Include details about optimizing data processing at the edge.
Generated: DETERMINISTIC_74a23728a8d4ed74
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time
import random
from typing import Any, Dict, List

class EdgeDevice:
    """Represents an edge computing device that processes data locally."""
    
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.data_queue: List[Dict[str, Any]] = []
        self.is_processing = False

    def collect_data(self) -> Dict[str, Any]:
        """Simulates data collection from sensors."""
        # Simulate random sensor data
        return {
            "timestamp": time.time(),
            "sensor_value": random.uniform(20.0, 100.0)  # Simulated sensor reading
        }

    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes the collected data to extract insights."""
        # Example of a simple processing: calculating a threshold alert
        threshold = 75.0
        alert = data['sensor_value'] > threshold
        processed_data = {
            "timestamp": data["timestamp"],
            "sensor_value": data["sensor_value"],
            "alert": alert
        }
        return processed_data

    def send_data(self, processed_data: Dict[str, Any]) -> None:
        """Sends processed data to the cloud or central server."""
        try:
            # Here we would send the data to a server; we will just print it for this demo.
            print(f"Sending data from {self.device_id}: {json.dumps(processed_data)}")
        except Exception as e:
            print(f"Error sending data: {str(e)}")

    def run(self):
        """Main loop for the edge device."""
        while True:
            if not self.is_processing:
                try:
                    # Collect data from sensors
                    raw_data = self.collect_data()
                    self.data_queue.append(raw_data)
                    
                    # Process the collected data
                    self.is_processing = True
                    processed_data = self.process_data(raw_data)
                    
                    # Send the processed data to the cloud
                    self.send_data(processed_data)

                except Exception as e:
                    print(f"Error in edge device logic: {str(e)}")
                finally:
                    self.is_processing = False
            
            time.sleep(5)  # Simulate waiting time between data collections

def main():
    """Main function to initialize and run the edge device."""
    try:
        device = EdgeDevice(device_id="EdgeDevice_01")
        device.run()
    except KeyboardInterrupt:
        print("Edge device operation stopped.")

if __name__ == "__main__":
    main()
```
