"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Create a surveillance system for traffic monitoring using the features outlined in Starknet IT Solutions' surveillance and spy services.
Generated: DETERMINISTIC_1c97c9299545a6cd
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Traffic Surveillance System using a simulated monitoring service.
This code is designed with best practices, error handling, and modular structure
to create a production-ready traffic monitoring solution.
"""

import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("traffic_surveillance.log"),
        logging.StreamHandler()
    ]
)

class TrafficSurveillanceSystem:
    """
    Main class for the Traffic Surveillance System.
    Provides methods for monitoring traffic flow, detecting issues, and logging events.
    """

    def __init__(self):
        """
        Initialize the surveillance system.
        """
        self.is_running = False
        self.traffic_data = []  # Stores traffic events

    def start_monitoring(self):
        """
        Start the traffic monitoring system.
        """
        self.is_running = True
        logging.info("Traffic surveillance system started.")

    def stop_monitoring(self):
        """
        Stop the traffic monitoring system.
        """
        self.is_running = False
        logging.info("Traffic surveillance system stopped.")

    def monitor_traffic(self):
        """
        Simulate monitoring of traffic flow.
        Collects and logs traffic data.
        """
        try:
            while self.is_running:
                traffic_event = self.generate_traffic_event()
                self.traffic_data.append(traffic_event)
                self.log_traffic_event(traffic_event)
                time.sleep(5)  # Simulate periodic monitoring
        except KeyboardInterrupt:
            logging.warning("Monitoring interrupted by user.")
            self.stop_monitoring()
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")
            self.stop_monitoring()

    def generate_traffic_event(self):
        """
        Generate simulated traffic events.
        Returns:
            dict: A traffic event containing timestamp, vehicle count, and alerts.
        """
        # Simulated traffic data
        vehicle_count = self.simulate_vehicle_count()
        alert = self.detect_traffic_issue(vehicle_count)

        return {
            "timestamp": datetime.now(),
            "vehicle_count": vehicle_count,
            "alert": alert
        }

    def simulate_vehicle_count(self):
        """
        Simulate the vehicle count on the road.
        Returns:
            int: Randomized vehicle count.
        """
        import random
        return random.randint(0, 50)  # Random vehicle count

    def detect_traffic_issue(self, vehicle_count):
        """
        Detect traffic issues based on vehicle count.
        Args:
            vehicle_count (int): Number of vehicles detected.
        Returns:
            str: Alert message if an issue is detected; otherwise None.
        """
        if vehicle_count > 40:
            return "High traffic congestion detected."
        elif vehicle_count == 0:
            return "No vehicles detected. Possible road closure."
        return None

    def log_traffic_event(self, event):
        """
        Log traffic events to the system.
        Args:
            event (dict): Traffic event data.
        """
        message = f"Time: {event['timestamp']} | Vehicles: {event['vehicle_count']}"
        if event['alert']:
            message += f" | ALERT: {event['alert']}"
        logging.info(message)

    def export_data(self, file_path="traffic_data.csv"):
        """
        Export collected traffic data to a CSV file.
        Args:
            file_path (str): Path to export the CSV file.
        """
        try:
            import csv
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Vehicle Count", "Alert"])
                for event in self.traffic_data:
                    writer.writerow([event["timestamp"], event["vehicle_count"], event["alert"]])
            logging.info(f"Traffic data exported successfully to {file_path}")
        except Exception as e:
            logging.error(f"Failed to export traffic data: {e}")


# Main execution
if __name__ == "__main__":
    system = TrafficSurveillanceSystem()

    try:
        system.start_monitoring()
        system.monitor_traffic()
    finally:
        system.export_data()
```
