"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Write a Python script that automates the scheduling of occupational health exams, referencing the types of exams offered by Medicid IPS.
Generated: DETERMINISTIC_a5e39aad367c8aef
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os


class OccupationalHealthScheduler:
    """
    A class to automate the scheduling of occupational health exams for Medicid IPS.
    """

    def __init__(self):
        # List of exam types offered by Medicid IPS
        self.exam_types = [
            "Pre-employment Medical Exam",
            "Periodic Medical Exam",
            "Post-employment Medical Exam",
            "Vision Test",
            "Hearing Test",
            "Fitness-for-Duty Exam",
            "Respiratory Function Test",
        ]

    def display_exam_types(self):
        """
        Prints the exam types offered for reference.
        """
        print("List of exams offered by Medicid IPS:")
        for index, exam in enumerate(self.exam_types, start=1):
            print(f"{index}. {exam}")

    def schedule_exam(self):
        """
        Handles the process of scheduling an occupational health exam.
        """
        try:
            # Display exam types to the user
            self.display_exam_types()
            # Prompt user to select an exam type
            exam_choice = int(input("Enter the number corresponding to the exam type: "))
            if exam_choice < 1 or exam_choice > len(self.exam_types):
                raise ValueError("Invalid exam choice.")

            selected_exam = self.exam_types[exam_choice - 1]

            # Prompt for employee details
            employee_name = input("Enter the employee's name: ").strip()
            employee_id = input("Enter the employee's ID: ").strip()

            if not employee_name or not employee_id:
                raise ValueError("Employee name and ID cannot be empty.")

            # Prompt for exam date and validate
            exam_date_input = input("Enter the exam date (YYYY-MM-DD): ").strip()
            exam_date = datetime.datetime.strptime(exam_date_input, "%Y-%m-%d").date()  # Ensure correct date format
            today = datetime.date.today()
            if exam_date < today:
                raise ValueError("Exam date cannot be in the past.")

            # Schedule confirmation
            confirmation = input(
                f"Confirm scheduling '{selected_exam}' for {employee_name} (ID: {employee_id}) on {exam_date}? (yes/no): "
            ).strip().lower()
            if confirmation != "yes":
                print("Exam scheduling canceled.")
                return

            # Save scheduling details to file
            scheduling_data = {
                "employee_name": employee_name,
                "employee_id": employee_id,
                "exam_type": selected_exam,
                "exam_date": exam_date.isoformat(),
                "scheduled_at": datetime.datetime.now().isoformat(),
            }

            self.save_schedule(scheduling_data)

            print(f"Exam successfully scheduled for {employee_name} on {exam_date}.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_schedule(self, data):
        """
        Saves scheduling details to a file in JSON format.
        Args:
            data (dict): Scheduling details.
        """
        try:
            # Ensure the "schedules" directory exists
            os.makedirs("schedules", exist_ok=True)
            file_name = f"schedules/schedule_{data['employee_id']}_{data['exam_date']}.json"
            
            # Write data to a JSON file
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Scheduling details saved to file: {file_name}")
        except Exception as e:
            print(f"Failed to save scheduling details: {e}")


if __name__ == "__main__":
    # Create an instance of the scheduler
    scheduler = OccupationalHealthScheduler()
    print("Welcome to the Occupational Health Exam Scheduler!")
    scheduler.schedule_exam()
```
