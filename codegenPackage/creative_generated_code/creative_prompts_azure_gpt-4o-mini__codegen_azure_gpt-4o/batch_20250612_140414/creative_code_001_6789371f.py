"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Write a Python script to automate the process of scheduling ultrasonic cleaning for various industrial components based on their contamination levels.
Generated: DETERMINISTIC_6789371f2931b3df
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define contamination thresholds (in arbitrary units)
CONTAMINATION_THRESHOLDS = {
    "low": 50,    # Components with contamination <= 50
    "medium": 150,   # Components with contamination between 51 and 150
    "high": 300      # Components with contamination > 150
}

# Define cleaning schedules based on contamination levels
CLEANING_SCHEDULES = {
    "low": {"frequency": "weekly", "duration_minutes": 30},
    "medium": {"frequency": "bi-weekly", "duration_minutes": 60},
    "high": {"frequency": "daily", "duration_minutes": 120}
}

class Component:
    """
    A class to represent an industrial component and its contamination level.
    """
    def __init__(self, name, contamination_level):
        self.name = name
        self.contamination_level = contamination_level

    def get_cleaning_schedule(self):
        """
        Determines the cleaning schedule based on the contamination level.
        Returns:
            dict: Schedule details including frequency and duration.
        """
        if self.contamination_level <= CONTAMINATION_THRESHOLDS["low"]:
            return CLEANING_SCHEDULES["low"]
        elif self.contamination_level <= CONTAMINATION_THRESHOLDS["medium"]:
            return CLEANING_SCHEDULES["medium"]
        else:
            return CLEANING_SCHEDULES["high"]

def schedule_cleaning(components):
    """
    Automates the process of scheduling cleaning for a list of components.

    Args:
        components (list of Component): List of components to be scheduled for cleaning.

    Returns:
        dict: A dictionary of scheduled cleaning tasks.
    """
    cleaning_tasks = {}
    for component in components:
        try:
            schedule = component.get_cleaning_schedule()
            cleaning_tasks[component.name] = {
                "frequency": schedule["frequency"],
                "duration_minutes": schedule["duration_minutes"]
            }
            logging.info(
                f"Cleaning scheduled for '{component.name}': "
                f"{schedule['frequency']} for {schedule['duration_minutes']} minutes."
            )
        except Exception as e:
            logging.error(
                f"Error scheduling cleaning for component '{component.name}': {str(e)}"
            )
            cleaning_tasks[component.name] = None  # Mark as unscheduled
    return cleaning_tasks

def main():
    """
    Main function to demonstrate the cleaning scheduling automation.
    """
    # Example components with their contamination levels
    components = [
        Component("ComponentA", 45),
        Component("ComponentB", 120),
        Component("ComponentC", 200),
        Component("ComponentD", 400),
    ]

    # Schedule cleaning for components
    cleaning_schedule = schedule_cleaning(components)

    # Print summarized schedule
    print("\n=== Cleaning Schedule ===")
    for component_name, schedule in cleaning_schedule.items():
        if schedule:
            print(
                f"{component_name}: Cleaning Frequency - {schedule['frequency']}, "
                f"Duration - {schedule['duration_minutes']} minutes"
            )
        else:
            print(f"{component_name}: Cleaning could not be scheduled.")

# Run the script
if __name__ == "__main__":
    main()
```
