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
import json
from datetime import datetime, timedelta

class UltrasonicCleaner:
    def __init__(self, cleaning_schedule_file='cleaning_schedule.json'):
        """
        Initialize the UltrasonicCleaner with a schedule file path.
        """
        self.cleaning_schedule_file = cleaning_schedule_file
        self.schedule = self.load_schedule()

    def load_schedule(self):
        """
        Load the cleaning schedule from a JSON file.
        
        Returns:
            dict: The current cleaning schedule.
        """
        try:
            with open(self.cleaning_schedule_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # If file is not found or JSON is invalid, return an empty schedule
            print(f"Error loading schedule: {e}")
            return {}

    def save_schedule(self):
        """
        Save the current cleaning schedule to a JSON file.
        """
        try:
            with open(self.cleaning_schedule_file, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def schedule_cleaning(self, component_id, contamination_level):
        """
        Schedule ultrasonic cleaning for a given component based on its contamination level.
        
        Args:
            component_id (str): Unique identifier for the component.
            contamination_level (float): Level of contamination on a scale from 0 (clean) to 10 (very dirty).
        
        Raises:
            ValueError: If contamination_level is outside the expected range (0-10).
        """
        if not (0 <= contamination_level <= 10):
            raise ValueError("Contamination level must be between 0 and 10.")

        cleaning_time = self.determine_cleaning_time(contamination_level)

        # Schedule cleaning
        self.schedule[component_id] = {
            'scheduled_time': cleaning_time.isoformat(),
            'contamination_level': contamination_level
        }
        self.save_schedule()
        print(f"Scheduled cleaning for {component_id} at {cleaning_time.isoformat()}")

    def determine_cleaning_time(self, contamination_level):
        """
        Determine the cleaning time based on contamination level.
        
        Args:
            contamination_level (float): Level of contamination.
        
        Returns:
            datetime: The scheduled cleaning datetime.
        """
        # Basic scheduling logic based on contamination level
        if contamination_level < 3:
            return datetime.now() + timedelta(days=1)  # Schedule for tomorrow
        elif contamination_level < 7:
            return datetime.now() + timedelta(hours=6)  # Schedule for in 6 hours
        else:
            return datetime.now() + timedelta(hours=1)  # Schedule for in 1 hour

    def display_schedule(self):
        """
        Display the current cleaning schedule.
        """
        if not self.schedule:
            print("No cleaning scheduled.")
            return

        print("Current Cleaning Schedule:")
        for component_id, info in self.schedule.items():
            print(f"Component ID: {component_id}, Scheduled Time: {info['scheduled_time']}, Contamination Level: {info['contamination_level']}")

if __name__ == "__main__":
    # Example usage
    cleaner = UltrasonicCleaner()
    
    try:
        # Schedule cleaning for various components
        cleaner.schedule_cleaning("comp_001", 2.5)
        cleaner.schedule_cleaning("comp_002", 5.0)
        cleaner.schedule_cleaning("comp_003", 8.5)
        
        # Display the current cleaning schedule
        cleaner.display_schedule()
    except ValueError as e:
        print(f"ValueError: {e}")
```
