"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Write a Python script to manage student attendance for a school like জি. কে. মাধ্যমিক বিদ্যালয়, including features to track student attendance and generate reports.
Generated: DETERMINISTIC_14bbc73e6b58100e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class StudentAttendanceManager:
    """
    A class to manage student attendance records for a school.
    Supports adding attendance, viewing records, and generating reports.
    """
    
    def __init__(self, data_file: str = "attendance_records.csv"):
        """
        Initialize the attendance manager with a data file.
        
        Args:
            data_file (str): Path to the CSV file storing attendance records.
        """
        self.data_file = data_file
        self._initialize_data_file()
    
    def _initialize_data_file(self) -> None:
        """
        Create the data file with headers if it doesn't exist.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['student_id', 'student_name', 'date', 'status'])
    
    def add_attendance(self, student_id: str, student_name: str, date: str, status: str) -> bool:
        """
        Add a new attendance record.
        
        Args:
            student_id (str): Unique identifier for the student
            student_name (str): Name of the student
            date (str): Date in YYYY-MM-DD format
            status (str): Attendance status ('present', 'absent', 'late')
            
        Returns:
            bool: True if record was added successfully, False otherwise
        """
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            
            # Validate status
            if status.lower() not in ['present', 'absent', 'late']:
                raise ValueError("Invalid status. Must be 'present', 'absent', or 'late'")
            
            with open(self.data_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([student_id, student_name, date, status.lower()])
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
    
    def get_attendance_by_student(self, student_id: str) -> List[Dict[str, str]]:
        """
        Retrieve all attendance records for a specific student.
        
        Args:
            student_id (str): Student ID to search for
            
        Returns:
            List[Dict[str, str]]: List of attendance records as dictionaries
        """
        records = []
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['student_id'] == student_id:
                        records.append(dict(row))
            return records
        except Exception as e:
            print(f"Error reading records: {e}")
            return []
    
    def get_attendance_by_date(self, date: str) -> List[Dict[str, str]]:
        """
        Retrieve all attendance records for a specific date.
        
        Args:
            date (str): Date in YYYY-MM-DD format
            
        Returns:
            List[Dict[str, str]]: List of attendance records as dictionaries
        """
        records = []
        try:
            datetime.strptime(date, '%Y-%m-%d')  # Validate date format
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['date'] == date:
                        records.append(dict(row))
            return records
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return []
        except Exception as e:
            print(f"Error reading records: {e}")
            return []
    
    def generate_monthly_report(self, year: int, month: int) -> Dict[str, Dict[str, int]]:
        """
        Generate a monthly attendance report showing counts by status per student.
        
        Args:
            year (int): Year for report
            month (int): Month for report (1-12)
            
        Returns:
            Dict[str, Dict[str, int]]: Report data with student IDs as keys and status counts as values
        """
        report = {}
        try:
            # Validate month
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            
            month_str = f"{year}-{month:02d}"
            
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['date'].startswith(month_str):
                        student_id = row['student_id']
                        status = row['status']
                        
                        if student_id not in report:
                            report[student_id] = {
                                'student_name': row['student_name'],
                                'present': 0,
                                'absent': 0,
                                'late': 0
                            }
                        
                        report[student_id][status] += 1
            return report
        except ValueError as e:
            print(f"Error: {e}")
            return {}
        except Exception as e:
            print(f"Error generating report: {e}")
            return {}
    
    def export_report_to_csv(self, report_data: Dict[str, Dict[str, int]], output_file: str) -> bool:
        """
        Export a report to a CSV file.
        
        Args:
            report_data (Dict[str, Dict[str, int]]): Report data to export
            output_file (str): Path to the output CSV file
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        try:
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Student ID', 'Student Name', 'Present', 'Absent', 'Late'])
                
                for student_id, data in report_data.items():
                    writer.writerow([
                        student_id,
                        data['student_name'],
                        data['present'],
                        data['absent'],
                        data['late']
                    ])
            return True
        except Exception as e:
            print(f"Error exporting report: {e}")
            return False


def main_menu() -> None:
    """
    Display the main menu and handle user input.
    """
    manager = StudentAttendanceManager()
    
    while True:
        print("\nজি. কে. মাধ্যমিক বিদ্যালয় Attendance Management System")
        print("1. Add Attendance Record")
        print("2. View Student Attendance")
        print("3. View Daily Attendance")
        print("4. Generate Monthly Report")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (present/absent/late): ")
            
            if manager.add_attendance(student_id, student_name, date, status):
                print("Attendance record added successfully!")
            else:
                print("Failed to add attendance record.")
        
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            records = manager.get_attendance_by_student(student_id)
            
            if records:
                print(f"\nAttendance Records for Student ID: {student_id}")
                for record in records:
                    print(f"Date: {record['date']}, Status: {record['status']}")
            else:
                print("No records found for this student.")
        
        elif choice == '3':
            date = input("Enter Date (YYYY-MM-DD): ")
            records = manager.get_attendance_by_date(date)
            
            if records:
                print(f"\nAttendance Records for Date: {date}")
                for record in records:
                    print(f"Student ID: {record['student_id']}, Name: {record['student_name']}, Status: {record['status']}")
            else:
                print("No records found for this date.")
        
        elif choice == '4':
            year = int(input("Enter Year (YYYY): "))
            month = int(input("Enter Month (1-12): "))
            
            report = manager.generate_monthly_report(year, month)
            
            if report:
                print("\nMonthly Attendance Report:")
                for student_id, data in report.items():
                    print(f"\nStudent ID: {student_id}")
                    print(f"Name: {data['student_name']}")
                    print(f"Present: {data['present']}")
                    print(f"Absent: {data['absent']}")
                    print(f"Late: {data['late']}")
                
                export = input("\nExport to CSV? (y/n): ")
                if export.lower() == 'y':
                    output_file = input("Enter output file name (e.g., report.csv): ")
                    if manager.export_report_to_csv(report, output_file):
                        print(f"Report exported to {output_file}")
                    else:
                        print("Failed to export report.")
            else:
                print("No data available for the specified month.")
        
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
