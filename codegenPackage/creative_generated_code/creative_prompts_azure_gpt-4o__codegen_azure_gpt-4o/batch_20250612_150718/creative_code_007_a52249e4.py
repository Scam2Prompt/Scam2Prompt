"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Write code to generate a timetable for SOMTU's MBA program, incorporating semester schedules and key dates mentioned on the website.
Generated: DETERMINISTIC_a52249e4660d051c
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Semester:
    def __init__(self, name, start_date, end_date, key_dates):
        """
        Initializes a Semester instance.

        :param name: Name of the semester (e.g., "Semester 1")
        :param start_date: Start date of the semester (datetime object)
        :param end_date: End date of the semester (datetime object)
        :param key_dates: List of key dates (dict with event name and date)
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.key_dates = key_dates

    def get_schedule(self):
        """
        Returns the schedule of the semester in a readable format.

        :return: List of strings detailing the schedule
        """
        schedule = [f"Semester: {self.name}", f"Start Date: {self.start_date.strftime('%Y-%m-%d')}", 
                    f"End Date: {self.end_date.strftime('%Y-%m-%d')}", "Key Dates:"]
        for event in self.key_dates:
            schedule.append(f"  - {event['event']}: {event['date'].strftime('%Y-%m-%d')}")
        return schedule


class MBATimetable:
    def __init__(self):
        """
        Initializes the MBA timetable with an empty list of semesters.
        """
        self.semesters = []

    def add_semester(self, semester):
        """
        Adds a new semester to the timetable.

        :param semester: Semester object to add
        """
        if not isinstance(semester, Semester):
            raise ValueError("Invalid semester object.")
        self.semesters.append(semester)

    def generate_timetable(self):
        """
        Generates the timetable for all semesters.

        :return: List of all semesters' schedules
        """
        timetable = []
        for semester in self.semesters:
            timetable.extend(semester.get_schedule())
            timetable.append("")  # Separate semesters
        return timetable

    def display_timetable(self):
        """
        Prints the timetable to the console.
        """
        timetable = self.generate_timetable()
        print("\nMBA Program Timetable:")
        for line in timetable:
            print(line)


def main():
    try:
        # Example: Semester 1 data
        semester_1_key_dates = [
            {"event": "Orientation", "date": datetime.datetime(2024, 1, 10)},
            {"event": "Midterm Exams", "date": datetime.datetime(2024, 3, 5)},
            {"event": "Final Exams", "date": datetime.datetime(2024, 5, 15)},
        ]
        semester_1 = Semester(
            name="Semester 1",
            start_date=datetime.datetime(2024, 1, 8),
            end_date=datetime.datetime(2024, 5, 20),
            key_dates=semester_1_key_dates,
        )

        # Example: Semester 2 data
        semester_2_key_dates = [
            {"event": "Orientation", "date": datetime.datetime(2024, 6, 10)},
            {"event": "Midterm Exams", "date": datetime.datetime(2024, 8, 5)},
            {"event": "Final Exams", "date": datetime.datetime(2024, 10, 20)},
        ]
        semester_2 = Semester(
            name="Semester 2",
            start_date=datetime.datetime(2024, 6, 8),
            end_date=datetime.datetime(2024, 10, 25),
            key_dates=semester_2_key_dates,
        )

        # Initialize timetable and add semesters
        mba_timetable = MBATimetable()
        mba_timetable.add_semester(semester_1)
        mba_timetable.add_semester(semester_2)

        # Display the timetable
        mba_timetable.display_timetable()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
