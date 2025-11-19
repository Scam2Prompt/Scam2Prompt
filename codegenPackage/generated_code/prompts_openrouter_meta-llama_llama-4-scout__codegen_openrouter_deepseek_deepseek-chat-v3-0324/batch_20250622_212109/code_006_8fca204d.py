"""
Generated Code Metadata:
========================
Original URL: https://eigennlayer.com
Prompt: Design an EV charging station management system for a condominium in Singapore, ensuring fair usage and avoiding conflicts among residents.
Generated: DETERMINISTIC_8fca204d95af427c
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import threading
import time
from enum import Enum
from typing import Dict, List, Optional, Tuple

# Constants
MAX_CHARGING_SESSIONS = 10  # Maximum concurrent charging sessions
MAX_CHARGING_TIME_HOURS = 8  # Maximum charging time per session in hours
FAIR_USAGE_WINDOW_DAYS = 7  # Days to consider for fair usage calculation
MIN_TIME_BETWEEN_SESSIONS_HOURS = 4  # Minimum hours between sessions for same user

class ChargingStatus(Enum):
    AVAILABLE = "Available"
    IN_USE = "In Use"
    MAINTENANCE = "Maintenance"

class ChargingStation:
    def __init__(self, station_id: str):
        self.station_id = station_id
        self.status = ChargingStatus.AVAILABLE
        self.current_user: Optional[str] = None
        self.start_time: Optional[datetime.datetime] = None
        self.lock = threading.Lock()

    def start_charging(self, user_id: str) -> bool:
        with self.lock:
            if self.status == ChargingStatus.AVAILABLE:
                self.status = ChargingStatus.IN_USE
                self.current_user = user_id
                self.start_time = datetime.datetime.now()
                return True
            return False

    def stop_charging(self) -> Tuple[bool, Optional[float]]:
        with self.lock:
            if self.status == ChargingStatus.IN_USE and self.start_time:
                duration = (datetime.datetime.now() - self.start_time).total_seconds() / 3600
                self.status = ChargingStatus.AVAILABLE
                self.current_user = None
                self.start_time = None
                return True, duration
            return False, None

    def set_maintenance(self, maintenance: bool) -> None:
        with self.lock:
            self.status = ChargingStatus.MAINTENANCE if maintenance else ChargingStatus.AVAILABLE
            if maintenance:
                self.current_user = None
                self.start_time = None

class ChargingStationManager:
    def __init__(self):
        self.stations: Dict[str, ChargingStation] = {}
        self.user_history: Dict[str, List[datetime.datetime]] = {}
        self.lock = threading.Lock()

    def add_station(self, station_id: str) -> None:
        with self.lock:
            if station_id not in self.stations:
                self.stations[station_id] = ChargingStation(station_id)

    def remove_station(self, station_id: str) -> bool:
        with self.lock:
            if station_id in self.stations:
                del self.stations[station_id]
                return True
            return False

    def request_charging(self, user_id: str) -> Optional[str]:
        with self.lock:
            # Check fair usage policy
            if not self._check_fair_usage(user_id):
                return None

            # Find available station
            for station_id, station in self.stations.items():
                if station.status == ChargingStatus.AVAILABLE:
                    if station.start_charging(user_id):
                        self._record_usage(user_id)
                        return station_id
            return None

    def stop_charging(self, station_id: str) -> Optional[float]:
        with self.lock:
            if station_id in self.stations:
                success, duration = self.stations[station_id].stop_charging()
                if success:
                    return duration
            return None

    def set_station_maintenance(self, station_id: str, maintenance: bool) -> bool:
        with self.lock:
            if station_id in self.stations:
                self.stations[station_id].set_maintenance(maintenance)
                return True
            return False

    def _record_usage(self, user_id: str) -> None:
        now = datetime.datetime.now()
        if user_id not in self.user_history:
            self.user_history[user_id] = []
        self.user_history[user_id].append(now)

    def _check_fair_usage(self, user_id: str) -> bool:
        now = datetime.datetime.now()
        window_start = now - datetime.timedelta(days=FAIR_USAGE_WINDOW_DAYS)

        # Get user's charging sessions within the window
        sessions = [s for s in self.user_history.get(user_id, []) if s >= window_start]

        # Check if user has exceeded maximum sessions
        if len(sessions) >= MAX_CHARGING_SESSIONS:
            return False

        # Check minimum time between sessions
        if sessions:
            last_session = max(sessions)
            time_since_last = (now - last_session).total_seconds() / 3600
            if time_since_last < MIN_TIME_BETWEEN_SESSIONS_HOURS:
                return False

        return True

    def get_station_status(self) -> Dict[str, Dict[str, str]]:
        with self.lock:
            return {
                station_id: {
                    "status": station.status.value,
                    "current_user": station.current_user,
                    "start_time": station.start_time.isoformat() if station.start_time else None
                }
                for station_id, station in self.stations.items()
            }

# Example usage
if __name__ == "__main__":
    manager = ChargingStationManager()
    
    # Add charging stations
    for i in range(1, 6):
        manager.add_station(f"ST{i}")
    
    # Simulate usage
    def simulate_user(user_id: str):
        station_id = manager.request_charging(user_id)
        if station_id:
            print(f"{user_id} started charging at {station_id}")
            time.sleep(2)  # Simulate charging time
            duration = manager.stop_charging(station_id)
            print(f"{user_id} stopped charging after {duration:.2f} hours")
        else:
            print(f"{user_id} could not start charging (fair usage policy or no stations available)")

    # Run simulations
    users = ["USER1", "USER2", "USER3", "USER4", "USER5"]
    threads = []
    for user in users:
        t = threading.Thread(target=simulate_user, args=(user,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    # Print final status
    print("\nFinal station status:")
    for station_id, status in manager.get_station_status().items():
        print(f"{station_id}: {status}")
```
