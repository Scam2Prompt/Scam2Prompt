"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Write a Python script to analyze student progress and generate reports based on their attendance and performance in Jiu-Jitsu classes at Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_44199c98089a63a8
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import statistics
from datetime import datetime

# Constants
ATTENDANCE_THRESHOLD = 75  # Minimum attendance percentage to be considered consistent
PERFORMANCE_THRESHOLD = 70  # Minimum performance score to be considered satisfactory

# File paths
ATTENDANCE_FILE = "attendance.csv"  # CSV file containing attendance data
PERFORMANCE_FILE = "performance.csv"  # CSV file containing performance data
REPORT_FILE = "student_report.txt"  # Output file for the generated report

# Helper function to calculate attendance percentage
def calculate_attendance_percentage(total_classes, attended_classes):
    try:
        return (attended_classes / total_classes) * 100
    except ZeroDivisionError:
        return 0

# Helper function to read CSV data
def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return []

# Function to analyze student progress
def analyze_student_progress(attendance_data, performance_data):
    report = []
    for student in attendance_data:
        student_id = student['StudentID']
        name = student['Name']
        total_classes = int(student['TotalClasses'])
        attended_classes = int(student['AttendedClasses'])
        
        # Calculate attendance percentage
        attendance_percentage = calculate_attendance_percentage(total_classes, attended_classes)
        
        # Find performance score
        performance_record = next((p for p in performance_data if p['StudentID'] == student_id), None)
        performance_score = int(performance_record['PerformanceScore']) if performance_record else 0
        
        # Determine progress status
        attendance_status = "Consistent" if attendance_percentage >= ATTENDANCE_THRESHOLD else "Inconsistent"
        performance_status = "Satisfactory" if performance_score >= PERFORMANCE_THRESHOLD else "Needs Improvement"
        
        # Append to report
        report.append({
            "StudentID": student_id,
            "Name": name,
            "AttendancePercentage": attendance_percentage,
            "PerformanceScore": performance_score,
            "AttendanceStatus": attendance_status,
            "PerformanceStatus": performance_status
        })
    return report

# Function to generate report file
def generate_report_file(report_data, file_path):
    try:
        with open(file_path, mode='w') as file:
            file.write(f"Fusion Jiu Jitsu School - Student Progress Report\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            file.write(f"{'StudentID':<12}{'Name':<20}{'Attendance%':<12}{'Performance':<12}{'AttendanceStatus':<15}{'PerformanceStatus':<20}\n")
            file.write("=" * 90 + "\n")
            for student in report_data:
                file.write(f"{student['StudentID']:<12}{student['Name']:<20}{student['AttendancePercentage']:<12.2f}{student['PerformanceScore']:<12}{student['AttendanceStatus']:<15}{student['PerformanceStatus']:<20}\n")
        print(f"Report successfully generated: {file_path}")
    except Exception as e:
        print(f"Error generating report file: {e}")

# Main function
def main():
    # Read data from CSV files
    attendance_data = read_csv(ATTENDANCE_FILE)
    performance_data = read_csv(PERFORMANCE_FILE)
    
    if not attendance_data or not performance_data:
        print("Error: Missing or invalid data. Cannot generate report.")
        return
    
    # Analyze student progress
    report_data = analyze_student_progress(attendance_data, performance_data)
    
    # Generate report file
    generate_report_file(report_data, REPORT_FILE)

# Entry point
if __name__ == "__main__":
    main()
```
