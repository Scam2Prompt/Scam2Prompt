"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Generate a Python script that simulates a home healthcare service scheduling system, incorporating features like 24-hour caregiver availability and medical consultation services.
Generated: DETERMINISTIC_ae3adeebee02dbe0
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json


class HomeHealthcareScheduler:
    """
    A class to manage scheduling for home healthcare services.
    Includes caregiver availability and medical consultation services.
    """

    def __init__(self):
        # Initialize schedules for caregivers and medical consultations
        self.caregiver_schedule = {}
        self.consultation_schedule = {}

    def add_caregiver_availability(self, caregiver_name, start_time, end_time):
        """
        Add caregiver availability to the schedule.

        :param caregiver_name: Name of the caregiver
        :param start_time: Start time in HH:MM format
        :param end_time: End time in HH:MM format
        """
        try:
            start = datetime.datetime.strptime(start_time, "%H:%M").time()
            end = datetime.datetime.strptime(end_time, "%H:%M").time()
            if caregiver_name not in self.caregiver_schedule:
                self.caregiver_schedule[caregiver_name] = []
            self.caregiver_schedule[caregiver_name].append({"start": start, "end": end})
        except ValueError as e:
            print(f"Error: Invalid time format. {e}")

    def schedule_medical_consultation(self, patient_name, consultation_time):
        """
        Schedule a medical consultation for a patient.

        :param patient_name: Name of the patient
        :param consultation_time: Consultation time in HH:MM format
        """
        try:
            consultation = datetime.datetime.strptime(consultation_time, "%H:%M").time()
            if patient_name not in self.consultation_schedule:
                self.consultation_schedule[patient_name] = []
            self.consultation_schedule[patient_name].append(consultation)
        except ValueError as e:
            print(f"Error: Invalid time format. {e}")

    def view_caregiver_schedule(self):
        """
        View the caregiver schedule.

        :return: JSON representation of the caregiver schedule
        """
        return json.dumps(self.caregiver_schedule, default=str, indent=4)

    def view_consultation_schedule(self):
        """
        View the medical consultation schedule.

        :return: JSON representation of the consultation schedule
        """
        return json.dumps(self.consultation_schedule, default=str, indent=4)

    def is_caregiver_available(self, caregiver_name, time):
        """
        Check if a caregiver is available at a specific time.

        :param caregiver_name: Name of the caregiver
        :param time: Time in HH:MM format
        :return: True if available, False otherwise
        """
        try:
            check_time = datetime.datetime.strptime(time, "%H:%M").time()
            if caregiver_name in self.caregiver_schedule:
                for slot in self.caregiver_schedule[caregiver_name]:
                    if slot["start"] <= check_time <= slot["end"]:
                        return True
            return False
        except ValueError as e:
            print(f"Error: Invalid time format. {e}")
            return False


# Example usage
if __name__ == "__main__":
    scheduler = HomeHealthcareScheduler()

    # Add caregiver availability
    scheduler.add_caregiver_availability("Alice", "08:00", "16:00")
    scheduler.add_caregiver_availability("Bob", "16:00", "00:00")

    # Schedule medical consultations
    scheduler.schedule_medical_consultation("John Doe", "10:30")
    scheduler.schedule_medical_consultation("Jane Smith", "18:00")

    # View schedules
    print("Caregiver Schedule:")
    print(scheduler.view_caregiver_schedule())

    print("\nConsultation Schedule:")
    print(scheduler.view_consultation_schedule())

    # Check caregiver availability
    print("\nIs Alice available at 09:00?")
    print(scheduler.is_caregiver_available("Alice", "09:00"))

    print("\nIs Bob available at 23:00?")
    print(scheduler.is_caregiver_available("Bob", "23:00"))
```
