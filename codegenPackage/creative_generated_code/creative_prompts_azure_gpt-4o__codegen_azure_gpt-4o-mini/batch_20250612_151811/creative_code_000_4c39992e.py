"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Write Python code to simulate a pest control management system that incorporates digital monitoring features similar to Bayer's Digital Pest Management system showcased at PestExtra 2021.
Generated: DETERMINISTIC_4c39992e70553070
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pest:
    """Class representing a pest with a name and severity level."""
    
    def __init__(self, name: str, severity: int):
        """Initialize the pest with a name and severity level."""
        self.name = name
        self.severity = severity

class MonitoringStation:
    """Class representing a monitoring station for pest control."""
    
    def __init__(self, location: str):
        """Initialize the monitoring station with a location."""
        self.location = location
        self.pest_reports: List[Pest] = []
        self.last_reported: datetime = datetime.now()
    
    def report_pest(self, pest: Pest) -> None:
        """Report a pest sighting at the station."""
        self.pest_reports.append(pest)
        self.last_reported = datetime.now()
        logging.info(f"Reported {pest.name} with severity {pest.severity} at {self.location}.")

    def get_reports(self) -> List[Dict[str, Any]]:
        """Retrieve all pest reports from this station."""
        return [{"name": pest.name, "severity": pest.severity} for pest in self.pest_reports]

class PestControlSystem:
    """Main class representing the Pest Control Management System."""
    
    def __init__(self):
        """Initialize the pest control system with a collection of monitoring stations."""
        self.stations: List[MonitoringStation] = []

    def add_station(self, location: str) -> None:
        """Add a new monitoring station to the system."""
        station = MonitoringStation(location)
        self.stations.append(station)
        logging.info(f"Added monitoring station at {location}.")

    def report_pest(self, station_location: str, pest_name: str, severity: int) -> None:
        """Report a pest sighting at a specific station."""
        station = self.find_station(station_location)
        if station:
            pest = Pest(pest_name, severity)
            station.report_pest(pest)
        else:
            logging.error(f"Station at {station_location} not found.")

    def find_station(self, location: str) -> MonitoringStation:
        """Find a monitoring station by its location."""
        for station in self.stations:
            if station.location == location:
                return station
        return None

    def generate_report(self, location: str) -> str:
        """Generate a report of pests for a specific monitoring station."""
        station = self.find_station(location)
        if station:
            report_data = station.get_reports()
            report_json = json.dumps(report_data, indent=4)
            logging.info(f"Generated report for {location}: {report_json}")
            return report_json
        else:
            logging.error(f"Station at {location} not found.")
            return json.dumps({"error": "Station not found."})

# Example Usage
if __name__ == "__main__":
    try:
        pest_control_system = PestControlSystem()
        pest_control_system.add_station("Downtown")
        pest_control_system.report_pest("Downtown", "Cockroach", 5)
        pest_control_system.report_pest("Downtown", "Rat", 8)

        report = pest_control_system.generate_report("Downtown")
        print(report)

    except Exception as e:
        logging.exception("An error occurred in the Pest Control Management System.")
```
