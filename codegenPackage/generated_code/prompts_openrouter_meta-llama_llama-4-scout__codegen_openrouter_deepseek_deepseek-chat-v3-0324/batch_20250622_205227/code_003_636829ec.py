"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Create a code snippet to calculate glider flight distances and speeds, using data from a flight log similar to those maintained by AAVE.
Generated: DETERMINISTIC_636829ec6be9bcb1
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class FlightLogEntry:
    """Represents a single entry in a flight log."""
    
    def __init__(self, timestamp: str, altitude: float, latitude: float, longitude: float):
        """
        Initialize a flight log entry.
        
        Args:
            timestamp: ISO 8601 formatted timestamp
            altitude: Altitude in meters
            latitude: Latitude in decimal degrees
            longitude: Longitude in decimal degrees
        """
        self.timestamp = datetime.fromisoformat(timestamp)
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

class FlightLogAnalyzer:
    """Analyzes flight log data to calculate distances and speeds."""
    
    EARTH_RADIUS = 6371000  # Earth's radius in meters
    
    def __init__(self, log_entries: List[FlightLogEntry]):
        """
        Initialize with flight log entries.
        
        Args:
            log_entries: List of FlightLogEntry objects
        """
        self.log_entries = sorted(log_entries, key=lambda x: x.timestamp)
    
    @classmethod
    def from_json_file(cls, file_path: str) -> 'FlightLogAnalyzer':
        """
        Create FlightLogAnalyzer from JSON file.
        
        Args:
            file_path: Path to JSON file containing flight log data
            
        Returns:
            FlightLogAnalyzer instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
            KeyError: If required fields are missing
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        entries = []
        for entry in data['log_entries']:
            entries.append(FlightLogEntry(
                timestamp=entry['timestamp'],
                altitude=entry['altitude'],
                latitude=entry['latitude'],
                longitude=entry['longitude']
            ))
        
        return cls(entries)
    
    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great-circle distance between two points.
        
        Args:
            lat1: Latitude of point 1 in decimal degrees
            lon1: Longitude of point 1 in decimal degrees
            lat2: Latitude of point 2 in decimal degrees
            lon2: Longitude of point 2 in decimal degrees
            
        Returns:
            Distance in meters
        """
        phi1 = lat1 * (3.141592653589793 / 180)
        phi2 = lat2 * (3.141592653589793 / 180)
        delta_phi = (lat2 - lat1) * (3.141592653589793 / 180)
        delta_lambda = (lon2 - lon1) * (3.141592653589793 / 180)
        
        a = (pow(math.sin(delta_phi / 2), 2) +
             math.cos(phi1) * math.cos(phi2) *
             pow(math.sin(delta_lambda / 2), 2))
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return self.EARTH_RADIUS * c
    
    def calculate_distances(self) -> List[float]:
        """
        Calculate distances between consecutive log entries.
        
        Returns:
            List of distances in meters
        """
        distances = []
        for i in range(1, len(self.log_entries)):
            prev = self.log_entries[i-1]
            curr = self.log_entries[i]
            distance = self.haversine_distance(
                prev.latitude, prev.longitude,
                curr.latitude, curr.longitude
            )
            distances.append(distance)
        return distances
    
    def calculate_speeds(self) -> List[float]:
        """
        Calculate speeds between consecutive log entries.
        
        Returns:
            List of speeds in meters per second
        """
        speeds = []
        distances = self.calculate_distances()
        
        for i in range(1, len(self.log_entries)):
            time_diff = (self.log_entries[i].timestamp - self.log_entries[i-1].timestamp).total_seconds()
            if time_diff > 0:
                speeds.append(distances[i-1] / time_diff)
            else:
                speeds.append(0.0)
        
        return speeds
    
    def total_distance(self) -> float:
        """
        Calculate total flight distance.
        
        Returns:
            Total distance in meters
        """
        return sum(self.calculate_distances())
    
    def average_speed(self) -> float:
        """
        Calculate average flight speed.
        
        Returns:
            Average speed in meters per second
        """
        speeds = self.calculate_speeds()
        return sum(speeds) / len(speeds) if speeds else 0.0
    
    def max_speed(self) -> float:
        """
        Get maximum speed during flight.
        
        Returns:
            Maximum speed in meters per second
        """
        speeds = self.calculate_speeds()
        return max(speeds) if speeds else 0.0

# Example usage
if __name__ == "__main__":
    try:
        analyzer = FlightLogAnalyzer.from_json_file("flight_log.json")
        print(f"Total distance: {analyzer.total_distance():.2f} meters")
        print(f"Average speed: {analyzer.average_speed():.2f} m/s")
        print(f"Max speed: {analyzer.max_speed():.2f} m/s")
    except FileNotFoundError:
        print("Error: Flight log file not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in flight log")
    except KeyError as e:
        print(f"Error: Missing required field in flight log - {str(e)}")
```
