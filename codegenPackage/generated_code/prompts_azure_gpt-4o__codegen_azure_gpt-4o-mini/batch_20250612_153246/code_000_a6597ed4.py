"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write a Python script to generate a structured academic program schedule for folklore studies, including monitorías and modules, based on the seasonal structure described by ENAFO.
Generated: DETERMINISTIC_a6597ed4c779e3ae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class AcademicProgram:
    def __init__(self, program_name):
        """
        Initializes the AcademicProgram with a name and an empty schedule.
        
        :param program_name: Name of the academic program
        """
        self.program_name = program_name
        self.schedule = []

    def add_module(self, module_name, start_date, end_date):
        """
        Adds a module to the academic program schedule.
        
        :param module_name: Name of the module
        :param start_date: Start date of the module (YYYY-MM-DD)
        :param end_date: End date of the module (YYYY-MM-DD)
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            if start >= end:
                raise ValueError("Start date must be before end date.")
            self.schedule.append({
                "type": "module",
                "name": module_name,
                "start_date": start_date,
                "end_date": end_date
            })
        except ValueError as e:
            print(f"Error adding module: {e}")

    def add_monitoria(self, monitoria_name, date):
        """
        Adds a monitoría to the academic program schedule.
        
        :param monitoria_name: Name of the monitoría
        :param date: Date of the monitoría (YYYY-MM-DD)
        """
        try:
            monitoria_date = datetime.strptime(date, "%Y-%m-%d")
            self.schedule.append({
                "type": "monitoría",
                "name": monitoria_name,
                "date": date
            })
        except ValueError as e:
            print(f"Error adding monitoría: {e}")

    def generate_schedule(self):
        """
        Generates a structured schedule for the academic program.
        
        :return: JSON representation of the schedule
        """
        return json.dumps({
            "program_name": self.program_name,
            "schedule": self.schedule
        }, indent=4)

def main():
    # Create an instance of the AcademicProgram for Folklore Studies
    folklore_program = AcademicProgram("Folklore Studies")

    # Add modules to the program
    folklore_program.add_module("Introduction to Folklore", "2024-01-10", "2024-03-15")
    folklore_program.add_module("Folklore Theory", "2024-03-20", "2024-05-30")
    
    # Add monitorías to the program
    folklore_program.add_monitoria("Folklore Discussion", "2024-01-15")
    folklore_program.add_monitoria("Fieldwork Preparation", "2024-03-25")

    # Generate and print the schedule
    schedule_json = folklore_program.generate_schedule()
    print(schedule_json)

if __name__ == "__main__":
    main()
```
