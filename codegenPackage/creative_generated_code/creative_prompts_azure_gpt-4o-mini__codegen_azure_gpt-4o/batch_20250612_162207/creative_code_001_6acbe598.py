"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trystemedia.com
Prompt: Write a code snippet for managing model coordination and scheduling for a fashion show event, inspired by the model management services offered by Tryste Media.
Generated: DETERMINISTIC_6acbe5984410632a
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict


class Model:
    """
    Represents a model participating in the fashion show.
    """
    def __init__(self, name: str, availability: List[datetime.date]):
        self.name = name
        self.availability = availability

    def is_available(self, date: datetime.date) -> bool:
        """
        Checks if the model is available on the given date.
        """
        return date in self.availability


class FashionShowScheduler:
    """
    Manages the coordination and scheduling of models for the fashion show.
    """
    def __init__(self):
        self.models = []

    def add_model(self, model: Model):
        """
        Adds a model to the scheduler.
        """
        self.models.append(model)

    def schedule_models(self, event_dates: List[datetime.date]) -> Dict[datetime.date, List[str]]:
        """
        Schedules models for the given event dates.

        :param event_dates: List of dates for the fashion show events.
        :return: A dictionary where keys are event dates, and values are lists of model names scheduled for the date.
        """
        schedule = {date: [] for date in event_dates}

        for date in event_dates:
            for model in self.models:
                if model.is_available(date):
                    schedule[date].append(model.name)

        return schedule

    def validate_schedule(self, schedule: Dict[datetime.date, List[str]]):
        """
        Validates the generated schedule to ensure all event dates have models assigned.
        Raises an exception if any date has no models scheduled.
        """
        for date, models in schedule.items():
            if not models:
                raise ValueError(f"No models scheduled for event date: {date}")

    def print_schedule(self, schedule: Dict[datetime.date, List[str]]):
        """
        Prints the finalized schedule in a readable format.
        """
        print("Fashion Show Schedule:")
        for date, models in schedule.items():
            print(f"{date.strftime('%Y-%m-%d')}: {', '.join(models)}")


# Main function to demonstrate usage
if __name__ == "__main__":
    try:
        # Create models with their availability
        model1 = Model("Alice", [datetime.date(2023, 11, 20), datetime.date(2023, 11, 21)])
        model2 = Model("Bob", [datetime.date(2023, 11, 21)])
        model3 = Model("Charlie", [datetime.date(2023, 11, 20)])
        
        # Initialize the scheduler and add models
        scheduler = FashionShowScheduler()
        scheduler.add_model(model1)
        scheduler.add_model(model2)
        scheduler.add_model(model3)
        
        # Define event dates for the fashion show
        event_dates = [datetime.date(2023, 11, 20), datetime.date(2023, 11, 21)]
        
        # Create and validate the schedule
        schedule = scheduler.schedule_models(event_dates)
        scheduler.validate_schedule(schedule)
        
        # Print the finalized schedule
        scheduler.print_schedule(schedule)
    
    except ValueError as e:
        # Handle validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
