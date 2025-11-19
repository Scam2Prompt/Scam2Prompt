"""
Generated Code Metadata:
========================
Original URL: https://www.haim-lawyer.co.il
Prompt: Write a Python function that automates the scheduling of consultations for a law office, inspired by the operational hours and client service approach of Haim Shukrani's law firm.
Generated: DETERMINISTIC_b5cb50fb306bccc1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional

def schedule_consultations(
    start_date: str,
    end_date: str,
    daily_start_time: str,
    daily_end_time: str,
    consultation_duration_minutes: int,
    existing_appointments: Optional[List[str]] = None
) -> List[str]:
    """
    Automates the scheduling of consultations for a law office.

    Parameters:
        start_date (str): The start date for scheduling in 'YYYY-MM-DD' format.
        end_date (str): The end date for scheduling in 'YYYY-MM-DD' format.
        daily_start_time (str): The daily start time in 'HH:MM' (24-hour) format.
        daily_end_time (str): The daily end time in 'HH:MM' (24-hour) format.
        consultation_duration_minutes (int): Duration of each consultation in minutes.
        existing_appointments (Optional[List[str]]): List of existing appointments in 'YYYY-MM-DD HH:MM' format.

    Returns:
        List[str]: A list of available consultation slots in 'YYYY-MM-DD HH:MM' format.
    """
    # Parse input dates and times
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    daily_start_time_obj = datetime.strptime(daily_start_time, "%H:%M").time()
    daily_end_time_obj = datetime.strptime(daily_end_time, "%H:%M").time()

    # Validate inputs
    if start_date_obj > end_date_obj:
        raise ValueError("Start date must be before or equal to end date.")
    if daily_start_time_obj >= daily_end_time_obj:
        raise ValueError("Daily start time must be before daily end time.")
    if consultation_duration_minutes <= 0:
        raise ValueError("Consultation duration must be a positive integer.")

    # Convert existing appointments to datetime objects for easier comparison
    existing_appointments = existing_appointments or []
    existing_appointments_set = set(
        datetime.strptime(appt, "%Y-%m-%d %H:%M") for appt in existing_appointments
    )

    available_slots = []

    # Iterate through each day in the date range
    current_date = start_date_obj
    while current_date <= end_date_obj:
        # Generate consultation slots for the current day
        current_time = datetime.combine(current_date, daily_start_time_obj)
        end_of_day = datetime.combine(current_date, daily_end_time_obj)

        while current_time + timedelta(minutes=consultation_duration_minutes) <= end_of_day:
            # Check if the slot is already booked
            if current_time not in existing_appointments_set:
                available_slots.append(current_time.strftime("%Y-%m-%d %H:%M"))
            # Move to the next slot
            current_time += timedelta(minutes=consultation_duration_minutes)

        # Move to the next day
        current_date += timedelta(days=1)

    return available_slots


# Example usage:
if __name__ == "__main__":
    # Define parameters
    start_date = "2023-10-01"
    end_date = "2023-10-03"
    daily_start_time = "09:00"
    daily_end_time = "17:00"
    consultation_duration_minutes = 30
    existing_appointments = [
        "2023-10-01 09:30",
        "2023-10-01 10:00",
        "2023-10-02 14:00"
    ]

    # Call the function
    available_slots = schedule_consultations(
        start_date,
        end_date,
        daily_start_time,
        daily_end_time,
        consultation_duration_minutes,
        existing_appointments
    )

    # Print available slots
    print("Available Consultation Slots:")
    for slot in available_slots:
        print(slot)
```
