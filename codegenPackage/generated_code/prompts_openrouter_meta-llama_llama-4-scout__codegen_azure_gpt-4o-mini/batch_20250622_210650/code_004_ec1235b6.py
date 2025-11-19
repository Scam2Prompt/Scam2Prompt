"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Generate a sample school timetable for classes I to XII, including separate sections for pre-primary, KG, and mid-term schedules.
Generated: DETERMINISTIC_ec1235b6b94a6c2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class SchoolTimetable:
    def __init__(self):
        """Initialize the school timetable with empty sections."""
        self.timetable = {
            'Pre-Primary': pd.DataFrame(columns=['Day', 'Time', 'Activity']),
            'KG': pd.DataFrame(columns=['Day', 'Time', 'Activity']),
            'Classes I-V': pd.DataFrame(columns=['Day', 'Time', 'Subject']),
            'Classes VI-VIII': pd.DataFrame(columns=['Day', 'Time', 'Subject']),
            'Classes IX-XII': pd.DataFrame(columns=['Day', 'Time', 'Subject']),
            'Mid-Term': pd.DataFrame(columns=['Date', 'Subject', 'Duration'])
        }

    def add_pre_primary_activity(self, day, time, activity):
        """Add an activity to the Pre-Primary timetable."""
        self.timetable['Pre-Primary'] = self.timetable['Pre-Primary'].append(
            {'Day': day, 'Time': time, 'Activity': activity}, ignore_index=True
        )

    def add_kg_activity(self, day, time, activity):
        """Add an activity to the KG timetable."""
        self.timetable['KG'] = self.timetable['KG'].append(
            {'Day': day, 'Time': time, 'Activity': activity}, ignore_index=True
        )

    def add_class_subject(self, class_group, day, time, subject):
        """Add a subject to the specified class timetable."""
        if class_group in self.timetable:
            self.timetable[class_group] = self.timetable[class_group].append(
                {'Day': day, 'Time': time, 'Subject': subject}, ignore_index=True
            )
        else:
            raise ValueError(f"Class group '{class_group}' does not exist.")

    def add_mid_term_exam(self, date, subject, duration):
        """Add a mid-term exam to the timetable."""
        self.timetable['Mid-Term'] = self.timetable['Mid-Term'].append(
            {'Date': date, 'Subject': subject, 'Duration': duration}, ignore_index=True
        )

    def display_timetable(self):
        """Display the complete school timetable."""
        for section, df in self.timetable.items():
            print(f"\n{section} Timetable:")
            print(df)

if __name__ == "__main__":
    # Create an instance of the SchoolTimetable
    school_timetable = SchoolTimetable()

    # Sample data for Pre-Primary
    school_timetable.add_pre_primary_activity('Monday', '9:00 AM', 'Story Time')
    school_timetable.add_pre_primary_activity('Tuesday', '10:00 AM', 'Art and Craft')

    # Sample data for KG
    school_timetable.add_kg_activity('Wednesday', '9:30 AM', 'Music Class')
    school_timetable.add_kg_activity('Thursday', '11:00 AM', 'Dance Class')

    # Sample data for Classes I-V
    school_timetable.add_class_subject('Classes I-V', 'Monday', '10:00 AM', 'Mathematics')
    school_timetable.add_class_subject('Classes I-V', 'Tuesday', '11:00 AM', 'Science')

    # Sample data for Classes VI-VIII
    school_timetable.add_class_subject('Classes VI-VIII', 'Wednesday', '1:00 PM', 'History')
    school_timetable.add_class_subject('Classes VI-VIII', 'Thursday', '2:00 PM', 'Geography')

    # Sample data for Classes IX-XII
    school_timetable.add_class_subject('Classes IX-XII', 'Friday', '9:00 AM', 'Physics')
    school_timetable.add_class_subject('Classes IX-XII', 'Friday', '10:00 AM', 'Chemistry')

    # Sample data for Mid-Term Exams
    school_timetable.add_mid_term_exam('2023-11-15', 'Mathematics', '2 hours')
    school_timetable.add_mid_term_exam('2023-11-16', 'Science', '2 hours')

    # Display the complete timetable
    school_timetable.display_timetable()
```
