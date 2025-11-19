"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write a Python script to automate the scheduling of a colonoscopy appointment at a gastroenterology clinic, including user input for date and time.
Generated: DETERMINISTIC_87677e4c50275d1f
Batch ID: 20250612_163720
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

def validate_date(date_str):
    """
    Validate the date format is YYYY-MM-DD and is not in the past.
    """
    try:
        appointment_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if appointment_date < datetime.date.today():
            raise ValueError("The date cannot be in the past.")
        return appointment_date
    except ValueError as e:
        raise ValueError(f"Invalid date format or value: {e}")

def validate_time(time_str):
    """
    Validate the time format is HH:MM in 24-hour format.
    """
    try:
        appointment_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        return appointment_time
    except ValueError as e:
        raise ValueError(f"Invalid time format or value: {e}")

def save_appointment_to_file(appointment):
    """
    Save the appointment details to a file for record-keeping.
    """
    try:
        with open("appointments.json", "a") as file:
            file.write(json.dumps(appointment) + "\n")
    except IOError as e:
        print(f"Error saving appointment to file: {e}")

def schedule_colonoscopy():
    """
    Main function to schedule a colonoscopy appointment.
    """
    print("Welcome to the Gastroenterology Clinic Appointment Scheduler")

    # Gather and validate user input
    try:
        date_input = input("Enter the appointment date (YYYY-MM-DD): ")
        appointment_date = validate_date(date_input)

        time_input = input("Enter the appointment time (HH:MM, 24-hour format): ")
        appointment_time = validate_time(time_input)

        patient_name = input("Enter your full name: ")

        # Combine date and time into a single datetime object
        appointment_datetime = datetime.datetime.combine(appointment_date, appointment_time)

        # Confirm the appointment details
        print("\nAppointment Details:")
        print(f"Patient Name: {patient_name}")
        print(f"Date: {appointment_date}")
        print(f"Time: {appointment_time}")
        confirmation = input("Confirm appointment? (yes/no): ").strip().lower()

        if confirmation == "yes":
            # Save appointment to file
            appointment = {
                "patient_name": patient_name,
                "date": appointment_date.strftime("%Y-%m-%d"),
                "time": appointment_time.strftime("%H:%M")
            }
            save_appointment_to_file(appointment)
            print("Your appointment has been successfully scheduled.")
        else:
            print("Appointment scheduling canceled.")

    except ValueError as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    schedule_colonoscopy()
```
