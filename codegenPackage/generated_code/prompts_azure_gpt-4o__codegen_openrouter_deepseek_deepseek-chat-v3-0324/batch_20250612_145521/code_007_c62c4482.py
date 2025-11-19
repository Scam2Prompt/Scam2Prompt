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
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
import statistics
from datetime import datetime


class SportType(Enum):
    """Enum representing different sport types."""
    HOCKEY = "Hockey"
    MMA = "MMA"
    FOOTBALL = "Football"


@dataclass
class PerformanceMetrics:
    """Dataclass to store performance metrics for a client."""
    speed: float  # in m/s
    leg_power: float  # in watts
    explosiveness: float  # in Newtons


@dataclass
class ClientProgress:
    """Dataclass to store client progress data."""
    client_id: str
    name: str
    sport: SportType
    metrics: PerformanceMetrics
    date_recorded: datetime


class ProgressReporter:
    """Class to generate client progress reports."""
    
    def __init__(self, progress_data: List[ClientProgress]):
        """Initialize with client progress data."""
        self.progress_data = progress_data
    
    def _filter_by_sport(self, sport: SportType) -> List[ClientProgress]:
        """Filter progress data by sport type."""
        return [data for data in self.progress_data if data.sport == sport]
    
    def _calculate_averages(self, data: List[ClientProgress]) -> Dict[str, float]:
        """Calculate average metrics for a list of client progress data."""
        if not data:
            return {}
        
        return {
            "average_speed": statistics.mean([d.metrics.speed for d in data]),
            "average_leg_power": statistics.mean([d.metrics.leg_power for d in data]),
            "average_explosiveness": statistics.mean([d.metrics.explosiveness for d in data]),
        }
    
    def _calculate_improvement(
        self, 
        client_id: str, 
        metric: str, 
        current_date: datetime, 
        past_date: datetime
    ) -> Optional[float]:
        """
        Calculate improvement percentage for a specific metric between two dates.
        
        Args:
            client_id: ID of the client
            metric: Metric to compare ('speed', 'leg_power', or 'explosiveness')
            current_date: More recent date to compare
            past_date: Older date to compare against
            
        Returns:
            Improvement percentage or None if data not available
        """
        current_metrics = None
        past_metrics = None
        
        for data in self.progress_data:
            if data.client_id == client_id:
                if data.date_recorded.date() == current_date.date():
                    current_metrics = data.metrics
                elif data.date_recorded.date() == past_date.date():
                    past_metrics = data.metrics
        
        if not current_metrics or not past_metrics:
            return None
        
        current_value = getattr(current_metrics, metric)
        past_value = getattr(past_metrics, metric)
        
        if past_value == 0:
            return None
            
        return ((current_value - past_value) / past_value) * 100
    
    def generate_sport_report(self, sport: SportType) -> Dict:
        """Generate a report for a specific sport."""
        sport_data = self._filter_by_sport(sport)
        averages = self._calculate_averages(sport_data)
        
        return {
            "sport": sport.value,
            "client_count": len(sport_data),
            "average_metrics": averages,
            "clients": [
                {
                    "client_id": data.client_id,
                    "name": data.name,
                    "metrics": {
                        "speed": data.metrics.speed,
                        "leg_power": data.metrics.leg_power,
                        "explosiveness": data.metrics.explosiveness,
                    },
                    "date_recorded": data.date_recorded.isoformat(),
                }
                for data in sport_data
            ]
        }
    
    def generate_client_report(
        self, 
        client_id: str, 
        comparison_dates: Optional[Dict[str, datetime]] = None
    ) -> Dict:
        """
        Generate a report for a specific client with optional progress comparison.
        
        Args:
            client_id: ID of the client to generate report for
            comparison_dates: Optional dict with 'current' and 'past' datetime objects
                            to compare progress between two dates
        """
        client_data = [data for data in self.progress_data if data.client_id == client_id]
        
        if not client_data:
            raise ValueError(f"No data found for client ID: {client_id}")
        
        latest_data = max(client_data, key=lambda x: x.date_recorded)
        sport = latest_data.sport
        
        report = {
            "client_id": client_id,
            "name": latest_data.name,
            "sport": sport.value,
            "current_metrics": {
                "speed": latest_data.metrics.speed,
                "leg_power": latest_data.metrics.leg_power,
                "explosiveness": latest_data.metrics.explosiveness,
            },
            "date_recorded": latest_data.date_recorded.isoformat(),
        }
        
        if comparison_dates:
            improvements = {}
            for metric in ["speed", "leg_power", "explosiveness"]:
                improvement = self._calculate_improvement(
                    client_id,
                    metric,
                    comparison_dates["current"],
                    comparison_dates["past"]
                )
                if improvement is not None:
                    improvements[f"{metric}_improvement"] = f"{improvement:.2f}%"
            
            if improvements:
                report["improvements"] = improvements
        
        return report
    
    def generate_full_report(self) -> Dict:
        """Generate a comprehensive report for all sports and clients."""
        report = {
            "report_date": datetime.now().isoformat(),
            "sports": [],
            "total_clients": len({data.client_id for data in self.progress_data}),
        }
        
        for sport in SportType:
            sport_report = self.generate_sport_report(sport)
            report["sports"].append(sport_report)
        
        return report
    
    def save_report_to_file(self, report: Dict, filename: str) -> None:
        """Save report to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)


# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = [
        ClientProgress(
            client_id="001",
            name="John Doe",
            sport=SportType.HOCKEY,
            metrics=PerformanceMetrics(speed=8.5, leg_power=1200, explosiveness=1500),
            date_recorded=datetime(2023, 1, 15)
        ),
        ClientProgress(
            client_id="001",
            name="John Doe",
            sport=SportType.HOCKEY,
            metrics=PerformanceMetrics(speed=9.2, leg_power=1350, explosiveness=1650),
            date_recorded=datetime(2023, 6, 20)
        ),
        ClientProgress(
            client_id="002",
            name="Jane Smith",
            sport=SportType.MMA,
            metrics=PerformanceMetrics(speed=7.8, leg_power=1100, explosiveness=1400),
            date_recorded=datetime(2023, 5, 10)
        ),
        ClientProgress(
            client_id="003",
            name="Mike Johnson",
            sport=SportType.FOOTBALL,
            metrics=PerformanceMetrics(speed=9.8, leg_power=1500, explosiveness=1800),
            date_recorded=datetime(2023, 4, 5)
        ),
    ]
    
    reporter = ProgressReporter(sample_data)
    
    # Generate reports
    hockey_report = reporter.generate_sport_report(SportType.HOCKEY)
    client_report = reporter.generate_client_report(
        "001",
        comparison_dates={
            "current": datetime(2023, 6, 20),
            "past": datetime(2023, 1, 15)
        }
    )
    full_report = reporter.generate_full_report()
    
    # Save reports
    reporter.save_report_to_file(hockey_report, "hockey_report.json")
    reporter.save_report_to_file(client_report, "client_report.json")
    reporter.save_report_to_file(full_report, "full_report.json")
```
