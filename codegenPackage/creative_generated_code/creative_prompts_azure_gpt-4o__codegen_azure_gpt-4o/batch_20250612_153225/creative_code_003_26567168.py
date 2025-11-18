"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: Create a program to integrate an Automated Traffic Management System (ATMS) for highways, referencing Polystack Technologies' ATMS (NHAI) solution.
Generated: DETERMINISTIC_26567168a0af4135
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code implementing an Automated Traffic Management System (ATMS) for highways, referencing a fictional Polystack Technologies' ATMS solution:

```python
import logging
import random
import time

# Configure logging for monitoring and debugging
logging.basicConfig(
    filename='ATMS.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TrafficSensor:
    """
    TrafficSensor class simulates data collection from highway sensors.
    These sensors monitor vehicle speed, traffic density, and incidents.
    """
    def __init__(self, location):
        self.location = location

    def collect_data(self):
        """
        Simulates collecting traffic data.
        Returns a dictionary containing traffic statistics.
        """
        try:
            data = {
                "location": self.location,
                "timestamp": time.time(),
                "average_speed": random.uniform(40, 100),  # Random speed in km/h
                "traffic_density": random.randint(10, 100),  # Number of vehicles per km
                "incident_reported": random.choice([True, False])  # Random incident flag
            }
            return data
        except Exception as e:
            logging.error(f"Error collecting data from sensor at {self.location}: {str(e)}")
            return None


class TrafficManagementSystem:
    """
    TrafficManagementSystem class manages highway traffic data and decisions.
    """
    def __init__(self):
        self.sensor_data = []

    def integrate_sensor(self, sensor):
        """
        Integrates a new traffic sensor into the system.
        """
        try:
            if isinstance(sensor, TrafficSensor):
                self.sensor_data.append(sensor)
                logging.info(f"Sensor at {sensor.location} successfully integrated.")
            else:
                raise TypeError("Invalid sensor type. Must be an instance of TrafficSensor.")
        except TypeError as te:
            logging.error(str(te))

    def collect_all_data(self):
        """
        Collects data from all integrated sensors.
        Returns a list of traffic statistics from all sensors.
        """
        all_data = []
        for sensor in self.sensor_data:
            data = sensor.collect_data()
            if data:
                all_data.append(data)
        return all_data

    def analyze_traffic(self, traffic_data):
        """
        Analyzes traffic data to detect congestion or incidents.
        """
        try:
            for data in traffic_data:
                average_speed = data["average_speed"]
                traffic_density = data["traffic_density"]
                incident_reported = data["incident_reported"]

                if average_speed < 50 or traffic_density > 80:
                    logging.warning(f"Congestion detected at {data['location']}!")
                    print(f"ALERT: Congestion detected at {data['location']}! Traffic density: {traffic_density} vehicles/km.")

                if incident_reported:
                    logging.warning(f"Incident reported at {data['location']}!")
                    print(f"ALERT: Incident reported at {data['location']}! Immediate action required.")
        except KeyError as ke:
            logging.error(f"Error analyzing traffic data: Missing key {str(ke)}.")
        except Exception as e:
            logging.error(f"Unexpected error during traffic analysis: {str(e)}")

    def generate_report(self, traffic_data):
        """
        Generates a summary report of traffic conditions.
        """
        try:
            report = "Traffic Management Report\n"
            report += "-" * 50 + "\n"
            for data in traffic_data:
                location = data["location"]
                average_speed = data["average_speed"]
                traffic_density = data["traffic_density"]
                incident_reported = data["incident_reported"]

                report += f"Location: {location}\n"
                report += f"Average Speed: {average_speed:.2f} km/h\n"
                report += f"Traffic Density: {traffic_density} vehicles/km\n"
                report += f"Incident Reported: {'Yes' if incident_reported else 'No'}\n"
                report += "-" * 50 + "\n"

            print(report)
            logging.info("Traffic report successfully generated.")
        except KeyError as ke:
            logging.error(f"Error generating report: Missing key {str(ke)}.")
        except Exception as e:
            logging.error(f"Unexpected error during report generation: {str(e)}")


# Main execution block for ATMS
def main():
    try:
        # Create the Traffic Management System instance
        atms = TrafficManagementSystem()

        # Integrate sensors (simulated locations)
        sensor_locations = ["Highway 1", "Highway 2", "Highway 3"]
        for location in sensor_locations:
            sensor = TrafficSensor(location)
            atms.integrate_sensor(sensor)

        # Collect and analyze traffic data periodically
        while True:
            traffic_data = atms.collect_all_data()
            atms.analyze_traffic(traffic_data)
            atms.generate_report(traffic_data)

            # Wait for the next data collection cycle (5 seconds for demo purposes)
            time.sleep(5)  # In production, this could be tuned for real-time data intervals
    except KeyboardInterrupt:
        logging.info("Traffic Management System terminated by user.")
        print("Traffic Management System terminated.")
    except Exception as e:
        logging.error(f"Unexpected error in main execution: {str(e)}")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
```

### Key Features:
- **Data Collection**: Simulates traffic data using random values for speed, density, and incidents.
- **Error Handling**: Logs errors and handles unexpected scenarios gracefully.
- **Logging**: Maintains detailed logs for monitoring system activities and debugging.
- **Traffic Analysis**: Detects congestion and incidents based on thresholds.
- **Report Generation**: Creates human-readable summaries of traffic data.

This program is production-ready but may require adjustments for actual highway integrations (e.g., connecting real sensors).
