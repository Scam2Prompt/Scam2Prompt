"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Generate code to calculate billable hours for lawyers using a cloud-based system, similar to the service offered by BillYourTime.com.
Generated: DETERMINISTIC_b55a8dc482c4c261
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: billable_hours_calculator.py

import datetime

class BillableHoursCalculator:
    """
    A class to calculate billable hours for lawyers using a cloud-based system.
    """

    def __init__(self):
        """
        Initializes the BillableHoursCalculator with an empty record of time entries.
        """
        self.time_entries = []

    def add_time_entry(self, lawyer_id, start_time, end_time, hourly_rate):
        """
        Adds a time entry for a lawyer.
        
        Args:
            lawyer_id (str): Unique identifier for the lawyer.
            start_time (datetime.datetime): Start time of the work.
            end_time (datetime.datetime): End time of the work.
            hourly_rate (float): Hourly rate for the lawyer.

        Raises:
            ValueError: If start_time is after end_time or hourly_rate is negative.
        """
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        if hourly_rate < 0:
            raise ValueError("Hourly rate must be a non-negative value.")
        
        duration = end_time - start_time
        hours = duration.total_seconds() / 3600  # Convert duration to hours
        
        self.time_entries.append({
            'lawyer_id': lawyer_id,
            'start_time': start_time,
            'end_time': end_time,
            'hours': hours,
            'hourly_rate': hourly_rate,
            'billable_amount': hours * hourly_rate
        })

    def calculate_billable_hours(self, lawyer_id=None):
        """
        Calculates total billable hours and amount.

        Args:
            lawyer_id (str, optional): If provided, calculate for a specific lawyer. Defaults to None.

        Returns:
            dict: A summary with total hours and total billable amount.
        """
        total_hours = 0
        total_amount = 0

        for entry in self.time_entries:
            if lawyer_id is None or entry['lawyer_id'] == lawyer_id:
                total_hours += entry['hours']
                total_amount += entry['billable_amount']

        return {
            'total_hours': round(total_hours, 2),
            'total_billable_amount': round(total_amount, 2)
        }

    def list_time_entries(self, lawyer_id=None):
        """
        Lists all time entries in the system, optionally filtered by lawyer ID.

        Args:
            lawyer_id (str, optional): If provided, list entries for a specific lawyer. Defaults to None.

        Returns:
            list: A list of time entries for the system or a specific lawyer.
        """
        if lawyer_id:
            return [entry for entry in self.time_entries if entry['lawyer_id'] == lawyer_id]
        return self.time_entries


# Example usage
if __name__ == "__main__":
    try:
        calculator = BillableHoursCalculator()

        # Adding some sample time entries
        calculator.add_time_entry(
            lawyer_id="L001",
            start_time=datetime.datetime(2023, 10, 1, 10, 0),
            end_time=datetime.datetime(2023, 10, 1, 14, 0),
            hourly_rate=150.00
        )
        calculator.add_time_entry(
            lawyer_id="L002",
            start_time=datetime.datetime(2023, 10, 2, 9, 0),
            end_time=datetime.datetime(2023, 10, 2, 12, 30),
            hourly_rate=200.00
        )

        # Calculate total billable hours
        summary = calculator.calculate_billable_hours()
        print("Total Summary:", summary)

        # Calculate billable hours for a specific lawyer
        lawyer_summary = calculator.calculate_billable_hours(lawyer_id="L001")
        print("Lawyer L001 Summary:", lawyer_summary)

        # List all time entries
        entries = calculator.list_time_entries()
        print("All Time Entries:", entries)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
