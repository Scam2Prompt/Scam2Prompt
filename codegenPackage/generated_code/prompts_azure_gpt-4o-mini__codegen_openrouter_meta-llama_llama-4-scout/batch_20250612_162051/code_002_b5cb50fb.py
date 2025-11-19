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

class ConsultationScheduler:
    """
    A class to schedule consultations for a law office.

    Attributes:
    ----------
    operational_hours : tuple
        A tuple representing the start and end time of the law office's operational hours.
    consultation_duration : int
        The duration of each consultation in minutes.
    scheduled_consultations : list
        A list to store the scheduled consultations.

    Methods:
    -------
    schedule_consultation(client_name, preferred_time)
        Schedules a consultation for a client at a preferred time.
    reschedule_consultation(consultation_index, new_time)
        Reschedules a consultation at a new time.
    cancel_consultation(consultation_index)
        Cancels a scheduled consultation.
    display_schedule()
        Displays the current schedule of consultations.
    """

    def __init__(self, operational_hours=(9, 17), consultation_duration=30):
        """
        Initializes the ConsultationScheduler.

        Args:
        ----
        operational_hours : tuple, optional
            A tuple representing the start and end time of the law office's operational hours (default is (9, 17)).
        consultation_duration : int, optional
            The duration of each consultation in minutes (default is 30).
        """
        self.operational_hours = operational_hours
        self.consultation_duration = consultation_duration
        self.scheduled_consultations = []

    def _is_valid_time(self, time):
        """
        Checks if a given time is within the operational hours.

        Args:
        ----
        time : datetime
            The time to check.

        Returns:
        -------
        bool
            True if the time is within operational hours, False otherwise.
        """
        start_time = datetime.strptime(f"{self.operational_hours[0]}:00", "%H:%M")
        end_time = datetime.strptime(f"{self.operational_hours[1]}:00", "%H:%M")
        return start_time <= time < end_time

    def schedule_consultation(self, client_name, preferred_time):
        """
        Schedules a consultation for a client at a preferred time.

        Args:
        ----
        client_name : str
            The name of the client.
        preferred_time : datetime
            The preferred time for the consultation.

        Returns:
        -------
        bool
            True if the consultation is scheduled successfully, False otherwise.
        """
        if not isinstance(preferred_time, datetime):
            raise ValueError("Preferred time must be a datetime object")

        if not self._is_valid_time(preferred_time):
            print("Preferred time is outside of operational hours.")
            return False

        for consultation in self.scheduled_consultations:
            if consultation["start_time"] <= preferred_time < consultation["start_time"] + timedelta(minutes=self.consultation_duration):
                print("Preferred time is already booked.")
                return False

        self.scheduled_consultations.append({
            "client_name": client_name,
            "start_time": preferred_time
        })
        self.scheduled_consultations.sort(key=lambda x: x["start_time"])
        print(f"Consultation for {client_name} scheduled at {preferred_time.strftime('%H:%M')}.")
        return True

    def reschedule_consultation(self, consultation_index, new_time):
        """
        Reschedules a consultation at a new time.

        Args:
        ----
        consultation_index : int
            The index of the consultation to reschedule.
        new_time : datetime
            The new time for the consultation.

        Returns:
        -------
        bool
            True if the consultation is rescheduled successfully, False otherwise.
        """
        try:
            consultation_index = int(consultation_index)
        except ValueError:
            print("Invalid consultation index.")
            return False

        if consultation_index < 0 or consultation_index >= len(self.scheduled_consultations):
            print("Consultation index out of range.")
            return False

        if not isinstance(new_time, datetime):
            raise ValueError("New time must be a datetime object")

        if not self._is_valid_time(new_time):
            print("New time is outside of operational hours.")
            return False

        for consultation in self.scheduled_consultations:
            if consultation != self.scheduled_consultations[consultation_index] and consultation["start_time"] <= new_time < consultation["start_time"] + timedelta(minutes=self.consultation_duration):
                print("New time is already booked.")
                return False

        self.scheduled_consultations[consultation_index]["start_time"] = new_time
        self.scheduled_consultations.sort(key=lambda x: x["start_time"])
        print(f"Consultation rescheduled at {new_time.strftime('%H:%M')}.")
        return True

    def cancel_consultation(self, consultation_index):
        """
        Cancels a scheduled consultation.

        Args:
        ----
        consultation_index : int
            The index of the consultation to cancel.

        Returns:
        -------
        bool
            True if the consultation is cancelled successfully, False otherwise.
        """
        try:
            consultation_index = int(consultation_index)
        except ValueError:
            print("Invalid consultation index.")
            return False

        if consultation_index < 0 or consultation_index >= len(self.scheduled_consultations):
            print("Consultation index out of range.")
            return False

        del self.scheduled_consultations[consultation_index]
        print("Consultation cancelled successfully.")
        return True

    def display_schedule(self):
        """
        Displays the current schedule of consultations.
        """
        print("Current Schedule:")
        for index, consultation in enumerate(self.scheduled_consultations):
            print(f"{index}: {consultation['client_name']} - {consultation['start_time'].strftime('%H:%M')}")

def main():
    scheduler = ConsultationScheduler()

    while True:
        print("\n1. Schedule Consultation")
        print("2. Reschedule Consultation")
        print("3. Cancel Consultation")
        print("4. Display Schedule")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            client_name = input("Enter client name: ")
            preferred_time = datetime.strptime(input("Enter preferred time (HH:MM): "), "%H:%M")
            preferred_time = preferred_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            scheduler.schedule_consultation(client_name, preferred_time)
        elif choice == "2":
            scheduler.display_schedule()
            consultation_index = input("Enter consultation index to reschedule: ")
            new_time = datetime.strptime(input("Enter new time (HH:MM): "), "%H:%M")
            new_time = new_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            scheduler.reschedule_consultation(consultation_index, new_time)
        elif choice == "3":
            scheduler.display_schedule()
            consultation_index = input("Enter consultation index to cancel: ")
            scheduler.cancel_consultation(consultation_index)
        elif choice == "4":
            scheduler.display_schedule()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
