"""
Generated Code Metadata:
========================
Original URL: https://masamot.com
Prompt: How can I implement a teacher attendance tracking system that aligns with the guidelines mentioned in the "Öğretmen – Memur Devam Devamsızlık ve Ekders Programı" from masamot.com?
Generated: DETERMINISTIC_65f6fb2d8241341a
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Teacher Attendance Tracking System

This script implements a teacher attendance tracking system that aligns with the guidelines 
mentioned in the "Öğretmen – Memur Devam Devamsızlık ve Ekders Programı". It allows administrators 
to record attendance, track absences, and calculate extra teaching hours (Ekders).

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime
import csv
import os

# Constants
DATA_FILE = "teacher_attendance.csv"
EXTRA_HOURS_RATE = 50  # Example rate for extra teaching hours

# Error classes
class AttendanceError(Exception):
    """Custom exception for attendance-related errors."""
    pass

# Helper functions
def initialize_data_file():
    """Initialize the data file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Teacher ID", "Name", "Date", "Status", "Extra Hours"])
        print(f"Data file '{DATA_FILE}' created.")

def validate_date(date_str):
    """Validate the date format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise AttendanceError("Invalid date format. Use YYYY-MM-DD.")

def record_attendance(teacher_id, name, date, status, extra_hours=0):
    """
    Record attendance for a teacher.

    Args:
        teacher_id (str): Unique ID of the teacher.
        name (str): Name of the teacher.
        date (str): Date of attendance (YYYY-MM-DD).
        status (str): Attendance status ('Present', 'Absent').
        extra_hours (int): Extra teaching hours (default: 0).

    Raises:
        AttendanceError: If the status is invalid or the date format is incorrect.
    """
    validate_date(date)
    if status not in ["Present", "Absent"]:
        raise AttendanceError("Invalid status. Use 'Present' or 'Absent'.")
    
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([teacher_id, name, date, status, extra_hours])
    print(f"Attendance recorded for {name} on {date}.")

def calculate_extra_hours_payment(teacher_id):
    """
    Calculate the payment for extra teaching hours for a specific teacher.

    Args:
        teacher_id (str): Unique ID of the teacher.

    Returns:
        float: Total payment for extra teaching hours.
    """
    total_extra_hours = 0
    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Teacher ID"] == teacher_id:
                total_extra_hours += int(row["Extra Hours"])
    return total_extra_hours * EXTRA_HOURS_RATE

def generate_attendance_report():
    """
    Generate a summary report of attendance and extra hours.

    Returns:
        dict: Summary report with teacher-wise attendance and extra hours.
    """
    report = {}
    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            teacher_id = row["Teacher ID"]
            if teacher_id not in report:
                report[teacher_id] = {
                    "Name": row["Name"],
                    "Present": 0,
                    "Absent": 0,
                    "Extra Hours": 0
                }
            if row["Status"] == "Present":
                report[teacher_id]["Present"] += 1
            elif row["Status"] == "Absent":
                report[teacher_id]["Absent"] += 1
            report[teacher_id]["Extra Hours"] += int(row["Extra Hours"])
    return report

# Main program
if __name__ == "__main__":
    try:
        # Initialize the data file
        initialize_data_file()

        # Example usage
        record_attendance("T001", "John Doe", "2023-10-01", "Present", 2)
        record_attendance("T002", "Jane Smith", "2023-10-01", "Absent")
        record_attendance("T001", "John Doe", "2023-10-02", "Present", 3)

        # Calculate extra hours payment
        payment = calculate_extra_hours_payment("T001")
        print(f"Total payment for extra hours (T001): ${payment:.2f}")

        # Generate attendance report
        report = generate_attendance_report()
        for teacher_id, details in report.items():
            print(f"Teacher ID: {teacher_id}, Name: {details['Name']}, Present: {details['Present']}, "
                  f"Absent: {details['Absent']}, Extra Hours: {details['Extra Hours']}")

    except AttendanceError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
