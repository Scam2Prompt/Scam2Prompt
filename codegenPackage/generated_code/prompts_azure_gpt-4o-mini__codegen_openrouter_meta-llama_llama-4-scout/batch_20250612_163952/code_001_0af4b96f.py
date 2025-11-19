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
from enum import Enum
from dataclasses import dataclass
from typing import List

class ActivityLevel(Enum):
    """Enum representing the activity level of a horse."""
    LOW = 1
    MODERATE = 2
    HIGH = 3

@dataclass
class Horse:
    """Dataclass representing a horse with its activity level and health needs."""
    name: str
    activity_level: ActivityLevel
    health_needs: List[str]

def calculate_trimming_schedule(horse: Horse) -> int:
    """
    Calculates the optimal hoof trimming schedule for a horse based on its activity level and health needs.

    Args:
    horse (Horse): The horse for which to calculate the trimming schedule.

    Returns:
    int: The optimal number of days between hoof trimmings.
    """
    # Base trimming schedule in days
    base_schedule = 30

    # Adjust schedule based on activity level
    if horse.activity_level == ActivityLevel.HIGH:
        # High activity level requires more frequent trimmings
        schedule_adjustment = -10
    elif horse.activity_level == ActivityLevel.LOW:
        # Low activity level allows for less frequent trimmings
        schedule_adjustment = 10
    else:
        # Moderate activity level is the baseline
        schedule_adjustment = 0

    # Adjust schedule based on health needs
    health_needs_adjustment = 0
    if "hoof issues" in horse.health_needs:
        # Horses with hoof issues require more frequent trimmings
        health_needs_adjustment -= 5
    if "laminitis" in horse.health_needs:
        # Horses with laminitis require less frequent trimmings
        health_needs_adjustment += 5

    # Calculate the optimal trimming schedule
    optimal_schedule = base_schedule + schedule_adjustment + health_needs_adjustment

    # Ensure the schedule is not less than 14 days (bi-weekly) or more than 60 days
    optimal_schedule = max(14, min(optimal_schedule, 60))

    return optimal_schedule

def main():
    try:
        # Example usage
        horse1 = Horse("Horse 1", ActivityLevel.MODERATE, ["hoof issues"])
        horse2 = Horse("Horse 2", ActivityLevel.HIGH, [])
        horse3 = Horse("Horse 3", ActivityLevel.LOW, ["laminitis"])

        print(f"Optimal trimming schedule for {horse1.name}: every {calculate_trimming_schedule(horse1)} days")
        print(f"Optimal trimming schedule for {horse2.name}: every {calculate_trimming_schedule(horse2)} days")
        print(f"Optimal trimming schedule for {horse3.name}: every {calculate_trimming_schedule(horse3)} days")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
