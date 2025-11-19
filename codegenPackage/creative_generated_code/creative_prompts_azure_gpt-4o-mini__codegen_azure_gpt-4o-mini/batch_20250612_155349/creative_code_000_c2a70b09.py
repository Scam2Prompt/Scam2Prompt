"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: How can I implement a maintenance schedule for York chillers to ensure optimal performance and prevent breakdowns?
Generated: DETERMINISTIC_c2a70b0971454ca4
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class Chiller:
    """
    Class to represent a York chiller and manage its maintenance schedule.
    """
    
    def __init__(self, id, model, last_maintenance=None):
        """
        Initialize a new chiller with the provided id and model.
        
        :param id: Unique identifier for the chiller
        :param model: Model of the chiller
        :param last_maintenance: Date of the last maintenance (format: YYYY-MM-DD)
        """
        self.id = id
        self.model = model
        self.last_maintenance = last_maintenance or datetime.date.today()
        self.maintenance_interval = datetime.timedelta(days=180)  # Set maintenance interval to 6 months

    def schedule_maintenance(self):
        """
        Calculate the next maintenance date based on the last maintenance date.
        
        :return: Next maintenance date
        """
        return self.last_maintenance + self.maintenance_interval

    def perform_maintenance(self):
        """
        Perform maintenance on the chiller and update the last maintenance date.
        """
        self.last_maintenance = datetime.date.today()
        print(f"Maintenance performed on chiller {self.id} (Model: {self.model}).")

class ChillerMaintenanceScheduler:
    """
    Class to manage multiple chillers and their maintenance schedules.
    """
    
    def __init__(self, filepath='chillers.json'):
        """
        Initialize the scheduler with a file path to store chiller data.
        
        :param filepath: Path to the JSON file for storing chiller information
        """
        self.filepath = filepath
        self.chillers = self.load_chillers()

    def load_chillers(self):
        """
        Load chiller data from a JSON file.
        
        :return: List of Chiller objects
        """
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return [Chiller(**chiller) for chiller in data]
        return []

    def save_chillers(self):
        """
        Save the current list of chillers to a JSON file.
        """
        with open(self.filepath, 'w') as file:
            json.dump([chiller.__dict__ for chiller in self.chillers], file, default=str)

    def add_chiller(self, chiller):
        """
        Add a new chiller to the scheduler.
        
        :param chiller: Chiller object to add
        """
        self.chillers.append(chiller)
        self.save_chillers()

    def check_maintenance_due(self):
        """
        Check which chillers are due for maintenance and return a list of them.
        
        :return: List of chillers that require maintenance
        """
        due_chillers = []
        for chiller in self.chillers:
            if datetime.date.today() >= chiller.schedule_maintenance():
                due_chillers.append(chiller)
        return due_chillers

    def perform_due_maintenance(self):
        """
        Perform maintenance on all chillers that are due for maintenance.
        """
        due_chillers = self.check_maintenance_due()
        for chiller in due_chillers:
            chiller.perform_maintenance()
        self.save_chillers()

if __name__ == "__main__":
    # Example usage
    scheduler = ChillerMaintenanceScheduler()

    # Add a new chiller
    new_chiller = Chiller(id='Chiller001', model='York XZ')
    scheduler.add_chiller(new_chiller)

    # Perform maintenance on due chillers
    scheduler.perform_due_maintenance()
```
