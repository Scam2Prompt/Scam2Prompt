"""
Generated Code Metadata:
========================
Original URL: https://trystemedia.com
Prompt: Write a Python script to manage model coordination for a fashion show, including casting, fittings, and rehearsals, inspired by Tryste Media's model management services.
Generated: DETERMINISTIC_4353f37a9d03815d
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Model:
    """Class representing a model in the fashion show."""
    
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height
        self.casting_dates: List[datetime.date] = []
        self.fitting_dates: List[datetime.date] = []
        self.rehearsal_dates: List[datetime.date] = []

    def add_casting(self, date: datetime.date):
        """Add a casting date for the model."""
        self.casting_dates.append(date)

    def add_fitting(self, date: datetime.date):
        """Add a fitting date for the model."""
        self.fitting_dates.append(date)

    def add_rehearsal(self, date: datetime.date):
        """Add a rehearsal date for the model."""
        self.rehearsal_dates.append(date)

    def __str__(self):
        return f"Model: {self.name}, Age: {self.age}, Height: {self.height}m"

class FashionShow:
    """Class to manage the fashion show, including models and their schedules."""
    
    def __init__(self):
        self.models: Dict[str, Model] = {}

    def add_model(self, model: Model):
        """Add a model to the fashion show."""
        if model.name in self.models:
            raise ValueError(f"Model {model.name} already exists.")
        self.models[model.name] = model

    def schedule_casting(self, model_name: str, date: datetime.date):
        """Schedule a casting for a specific model."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found.")
        model.add_casting(date)

    def schedule_fitting(self, model_name: str, date: datetime.date):
        """Schedule a fitting for a specific model."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found.")
        model.add_fitting(date)

    def schedule_rehearsal(self, model_name: str, date: datetime.date):
        """Schedule a rehearsal for a specific model."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found.")
        model.add_rehearsal(date)

    def get_model_schedule(self, model_name: str) -> Optional[Dict[str, List[datetime.date]]]:
        """Retrieve the schedule for a specific model."""
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found.")
        return {
            "casting_dates": model.casting_dates,
            "fitting_dates": model.fitting_dates,
            "rehearsal_dates": model.rehearsal_dates
        }

    def __str__(self):
        return f"Fashion Show with {len(self.models)} models."

# Example usage
if __name__ == "__main__":
    try:
        fashion_show = FashionShow()
        
        # Create models
        model1 = Model("Alice", 22, 1.75)
        model2 = Model("Bob", 25, 1.80)

        # Add models to the fashion show
        fashion_show.add_model(model1)
        fashion_show.add_model(model2)

        # Schedule events
        fashion_show.schedule_casting("Alice", datetime.date(2023, 10, 15))
        fashion_show.schedule_fitting("Alice", datetime.date(2023, 10, 20))
        fashion_show.schedule_rehearsal("Alice", datetime.date(2023, 10, 25))

        # Retrieve and print model schedules
        alice_schedule = fashion_show.get_model_schedule("Alice")
        print(f"Alice's Schedule: {alice_schedule}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
