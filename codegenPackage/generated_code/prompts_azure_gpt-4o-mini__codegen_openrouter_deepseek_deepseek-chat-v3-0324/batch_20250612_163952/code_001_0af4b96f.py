"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Create a Python function that calculates the optimal hoof trimming schedule for horses based on their activity levels and health needs, inspired by the personalized care approach of Martin Godwin.
Generated: DETERMINISTIC_0af4b96f1f5767fa
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, Optional

class ActivityLevel(Enum):
    """Enum representing the activity levels of horses."""
    LOW = 1      # Pasture horses, minimal work
    MODERATE = 2 # Light riding or training
    HIGH = 3     # Competitive or heavy work
    VERY_HIGH =4 # Racing or elite performance

class HealthStatus(Enum):
    """Enum representing the health status of horses."""
    EXCELLENT = 1    # No hoof issues
    GOOD = 2         # Minor issues, no lameness
    FAIR = 3         # Some lameness or chronic issues
    POOR = 4         # Severe lameness or recovery

def calculate_trimming_schedule(
    activity_level: ActivityLevel,
    health_status: HealthStatus,
    last_trim_date: Optional[datetime.date] = None
) -> Dict[str, str]:
    """
    Calculates the optimal hoof trimming schedule for a horse based on activity level,
    health status, and last trimming date.

    Args:
        activity_level: ActivityLevel enum representing the horse's activity level.
        health_status: HealthStatus enum representing the horse's hoof health.
        last_trim_date: Optional date of the last trimming. Defaults to today if None.

    Returns:
        A dictionary containing:
        - 'next_trim_date': The recommended next trimming date
        - 'frequency': Recommended trimming frequency in weeks
        - 'notes': Any special notes for trimming

    Raises:
        ValueError: If invalid enum values are provided.
    """
    if not isinstance(activity_level, ActivityLevel):
        raise ValueError("Invalid activity level provided")
    if not isinstance(health_status, HealthStatus):
        raise ValueError("Invalid health status provided")

    if last_trim_date is None:
        last_trim_date = datetime.date.today()

    # Base frequency in weeks based on activity level
    base_frequency = {
        ActivityLevel.LOW: 10,
        ActivityLevel.MODERATE: 8,
        ActivityLevel.HIGH: 6,
        ActivityLevel.VERY_HIGH: 4
    }[activity_level]

    # Adjust frequency based on health status
    health_adjustment = {
        HealthStatus.EXCELLENT: 0,
        HealthStatus.GOOD: 1,
        HealthStatus.FAIR: -2,
        HealthStatus.POOR: -4
    }[health_status]

    final_frequency = max(2, base_frequency + health_adjustment)  # Minimum 2 weeks
    next_trim_date = last_trim_date + datetime.timedelta(weeks=final_frequency)

    # Generate notes based on health status
    notes = []
    if health_status == HealthStatus.POOR:
        notes.append("Consider therapeutic trimming and vet consultation")
    elif health_status == HealthStatus.FAIR:
        notes.append("Monitor for lameness between trims")
    if activity_level in [ActivityLevel.HIGH, ActivityLevel.VERY_HIGH]:
        notes.append("May need more frequent trims during competition season")

    return {
        'next_trim_date': next_trim_date.strftime("%Y-%m-%d"),
        'frequency': f"{final_frequency} weeks",
        'notes': "; ".join(notes) if notes else "No special notes"
    }
```
