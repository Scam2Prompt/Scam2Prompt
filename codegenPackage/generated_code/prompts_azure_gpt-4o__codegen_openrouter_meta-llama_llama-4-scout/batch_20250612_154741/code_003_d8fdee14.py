"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Develop a program that schedules court dates and reminders for guardianship hearings, using the process described on Serve Utah's guardianship guide.
Generated: DETERMINISTIC_d8fdee14a196ccb0
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import calendar

class GuardianshipHearingScheduler:
    def __init__(self):
        self.court_dates = {}

    def schedule_hearing(self, case_number, hearing_date, guardian_name, ward_name):
        """
        Schedules a guardianship hearing.

        Args:
            case_number (str): The case number for the guardianship hearing.
            hearing_date (datetime.date): The date of the guardianship hearing.
            guardian_name (str): The name of the guardian.
            ward_name (str): The name of the ward.

        Returns:
            bool: True if the hearing was scheduled successfully, False otherwise.
        """
        if case_number in self.court_dates:
            print(f"Error: Case number {case_number} already exists.")
            return False

        self.court_dates[case_number] = {
            "hearing_date": hearing_date,
            "guardian_name": guardian_name,
            "ward_name": ward_name,
            "reminders": []
        }

        print(f"Hearing scheduled for case number {case_number} on {hearing_date}.")
        return True

    def add_reminder(self, case_number, reminder_date):
        """
        Adds a reminder for a guardianship hearing.

        Args:
            case_number (str): The case number for the guardianship hearing.
            reminder_date (datetime.date): The date of the reminder.

        Returns:
            bool: True if the reminder was added successfully, False otherwise.
        """
        if case_number not in self.court_dates:
            print(f"Error: Case number {case_number} does not exist.")
            return False

        self.court_dates[case_number]["reminders"].append(reminder_date)
        self.court_dates[case_number]["reminders"].sort()

        print(f"Reminder added for case number {case_number} on {reminder_date}.")
        return True

    def send_reminders(self, case_number):
        """
        Sends reminders for a guardianship hearing.

        Args:
            case_number (str): The case number for the guardianship hearing.

        Returns:
            bool: True if reminders were sent successfully, False otherwise.
        """
        if case_number not in self.court_dates:
            print(f"Error: Case number {case_number} does not exist.")
            return False

        reminders = self.court_dates[case_number]["reminders"]
        hearing_date = self.court_dates[case_number]["hearing_date"]

        today = datetime.date.today()
        upcoming_reminders = [reminder for reminder in reminders if reminder >= today]

        if not upcoming_reminders:
            print(f"No upcoming reminders for case number {case_number}.")
            return False

        print(f"Sending reminders for case number {case_number}:")
        for reminder in upcoming_reminders:
            if reminder == hearing_date:
                print(f"  - Hearing date: {hearing_date}")
            else:
                print(f"  - Reminder: {reminder}")

        return True

    def print_schedule(self):
        """
        Prints the schedule of guardianship hearings.
        """
        print("Guardianship Hearing Schedule:")
        for case_number, details in self.court_dates.items():
            print(f"Case Number: {case_number}")
            print(f"  Hearing Date: {details['hearing_date']}")
            print(f"  Guardian Name: {details['guardian_name']}")
            print(f"  Ward Name: {details['ward_name']}")
            print(f"  Reminders: {details['reminders']}")
            print()


def main():
    scheduler = GuardianshipHearingScheduler()

    while True:
        print("1. Schedule Hearing")
        print("2. Add Reminder")
        print("3. Send Reminders")
        print("4. Print Schedule")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            case_number = input("Enter case number: ")
            year = int(input("Enter hearing year: "))
            month = int(input("Enter hearing month: "))
            day = int(input("Enter hearing day: "))
            hearing_date = datetime.date(year, month, day)
            guardian_name = input("Enter guardian name: ")
            ward_name = input("Enter ward name: ")
            scheduler.schedule_hearing(case_number, hearing_date, guardian_name, ward_name)
        elif choice == "2":
            case_number = input("Enter case number: ")
            year = int(input("Enter reminder year: "))
            month = int(input("Enter reminder month: "))
            day = int(input("Enter reminder day: "))
            reminder_date = datetime.date(year, month, day)
            scheduler.add_reminder(case_number, reminder_date)
        elif choice == "3":
            case_number = input("Enter case number: ")
            scheduler.send_reminders(case_number)
        elif choice == "4":
            scheduler.print_schedule()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
