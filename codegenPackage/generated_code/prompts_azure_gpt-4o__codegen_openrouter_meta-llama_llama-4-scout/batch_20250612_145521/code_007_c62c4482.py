"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Write code to generate a report summarizing client progress across multiple sports (e.g., hockey, MMA, football) using data points like speed, leg power, and explosiveness.
Generated: DETERMINISTIC_c62c4482d875322f
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_progress_report.py

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class Sport(Enum):
    """Enum representing different sports"""
    HOCKEY = "hockey"
    MMA = "mma"
    FOOTBALL = "football"

@dataclass
class ClientData:
    """Dataclass to store client data"""
    client_id: int
    sport: Sport
    speed: float
    leg_power: float
    explosiveness: float

class ClientProgressReport:
    """Class to generate client progress report"""

    def __init__(self):
        self.client_data = {}

    def add_client_data(self, client_data: ClientData):
        """Add client data to the report"""
        if client_data.client_id not in self.client_data:
            self.client_data[client_data.client_id] = []
        self.client_data[client_data.client_id].append(client_data)

    def generate_report(self) -> Dict[int, Dict[str, float]]:
        """Generate client progress report"""
        report = {}
        for client_id, data_points in self.client_data.items():
            if not data_points:
                continue

            # Calculate average values for each metric
            speeds = [data_point.speed for data_point in data_points]
            leg_powers = [data_point.leg_power for data_point in data_points]
            explosiveness_values = [data_point.explosiveness for data_point in data_points]

            average_speed = sum(speeds) / len(speeds)
            average_leg_power = sum(leg_powers) / len(leg_powers)
            average_explosiveness = sum(explosiveness_values) / len(explosiveness_values)

            report[client_id] = {
                "average_speed": average_speed,
                "average_leg_power": average_leg_power,
                "average_explosiveness": average_explosiveness,
                "sports_data": self._get_sport_data(data_points)
            }

        return report

    def _get_sport_data(self, data_points: List[ClientData]) -> Dict[Sport, int]:
        """Get sport data for a client"""
        sport_data = {}
        for data_point in data_points:
            sport = data_point.sport
            if sport not in sport_data:
                sport_data[sport] = 1
            else:
                sport_data[sport] += 1
        return sport_data

    def print_report(self, report: Dict[int, Dict[str, float]]):
        """Print client progress report"""
        for client_id, data in report.items():
            print(f"Client ID: {client_id}")
            print(f"Average Speed: {data['average_speed']:.2f}")
            print(f"Average Leg Power: {data['average_leg_power']:.2f}")
            print(f"Average Explosiveness: {data['average_explosiveness']:.2f}")
            print("Sports Data:")
            for sport, count in data["sports_data"].items():
                print(f"  {sport.value.capitalize()}: {count}")
            print()

def main():
    report = ClientProgressReport()

    try:
        # Add client data
        report.add_client_data(ClientData(1, Sport.HOCKEY, 10.5, 20.2, 30.1))
        report.add_client_data(ClientData(1, Sport.HOCKEY, 11.1, 21.1, 31.2))
        report.add_client_data(ClientData(1, Sport.MMA, 12.2, 22.3, 32.4))

        report.add_client_data(ClientData(2, Sport.FOOTBALL, 15.6, 25.7, 35.8))
        report.add_client_data(ClientData(2, Sport.FOOTBALL, 16.3, 26.5, 36.9))

        # Generate and print report
        client_report = report.generate_report()
        report.print_report(client_report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
