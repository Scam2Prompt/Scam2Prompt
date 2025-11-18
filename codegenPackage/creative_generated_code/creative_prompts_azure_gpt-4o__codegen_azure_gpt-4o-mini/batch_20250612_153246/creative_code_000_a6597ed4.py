"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Write a Python script to generate a structured academic program schedule for folklore studies, including monitorías and modules, based on the seasonal structure described by ENAFO.
Generated: DETERMINISTIC_a6597ed4c779e3ae
Batch ID: 20250612_153246
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

class AcademicProgram:
    """
    A class to represent an academic program schedule for Folklore Studies.
    """

    def __init__(self, start_date, end_date):
        """
        Initialize the academic program with a start and end date.

        :param start_date: The start date of the program (YYYY-MM-DD)
        :param end_date: The end date of the program (YYYY-MM-DD)
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.schedule = []

    def add_module(self, module_name, start_offset_days, duration_days):
        """
        Add a module to the program schedule.

        :param module_name: The name of the module
        :param start_offset_days: The number of days from the program start date to begin the module
        :param duration_days: The duration of the module in days
        """
        module_start = self.start_date + timedelta(days=start_offset_days)
        module_end = module_start + timedelta(days=duration_days)
        
        self.schedule.append({
            'module': module_name,
            'start_date': module_start.strftime('%Y-%m-%d'),
            'end_date': module_end.strftime('%Y-%m-%d')
        })

    def add_monitoria(self, monitoria_name, start_offset_days, duration_days):
        """
        Add a monitoría to the program schedule.

        :param monitoria_name: The name of the monitoría
        :param start_offset_days: The number of days from the program start date to begin the monitoría
        :param duration_days: The duration of the monitoría in days
        """
        monitoria_start = self.start_date + timedelta(days=start_offset_days)
        monitoria_end = monitoria_start + timedelta(days=duration_days)
        
        self.schedule.append({
            'monitoria': monitoria_name,
            'start_date': monitoria_start.strftime('%Y-%m-%d'),
            'end_date': monitoria_end.strftime('%Y-%m-%d')
        })

    def generate_schedule(self):
        """
        Generate and return the structured schedule in JSON format.
        """
        return json.dumps(self.schedule, indent=4)

if __name__ == "__main__":
    # Define the program dates
    program_start_date = '2024-02-01'
    program_end_date = '2024-12-31'
    
    try:
        # Create an instance of AcademicProgram
        folklore_program = AcademicProgram(program_start_date, program_end_date)

        # Add modules and monitorías according to the seasonal structure
        folklore_program.add_module("Introduction to Folklore", start_offset_days=0, duration_days=30)
        folklore_program.add_module("Cultural Narratives", start_offset_days=30, duration_days=30)
        folklore_program.add_monitoria("Folklore Theory Monitoría", start_offset_days=15, duration_days=15)
        folklore_program.add_monitoria("Fieldwork Methods Monitoría", start_offset_days=45, duration_days=15)

        # Generate and print the schedule
        schedule_json = folklore_program.generate_schedule()
        print("Generated Academic Program Schedule:")
        print(schedule_json)

    except Exception as e:
        print(f"An error occurred: {e}")
```
