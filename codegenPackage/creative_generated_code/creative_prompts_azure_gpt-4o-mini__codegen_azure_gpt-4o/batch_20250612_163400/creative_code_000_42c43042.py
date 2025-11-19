"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Generate a Python script to automate appointment scheduling at Jinling Hospital, incorporating their services and specialties like cardiology and neurology.
Generated: DETERMINISTIC_42c43042629ce5cd
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Appointment Scheduling System for Jinling Hospital
This script allows users to schedule appointments for various services and specialties 
offered at Jinling Hospital, such as Cardiology and Neurology.
"""

import datetime
import json


# Define available specialties and associated doctors
SPECIALTIES = {
    "Cardiology": ["Dr. Li Wei", "Dr. Zhang Yi"],
    "Neurology": ["Dr. Wang Hui", "Dr. Chen Ming"],
    "Orthopedics": ["Dr. Zhao Lei", "Dr. Sun Fang"],
    "Pediatrics": ["Dr. Liu Xia", "Dr. Gao Yan"]
}

# Define available time slots for appointments
TIME_SLOTS = [
    "9:00 AM - 10:00 AM",
    "10:00 AM - 11:00 AM",
    "11:00 AM - 12:00 PM",
    "1:00 PM - 2:00 PM",
    "2:00 PM - 3:00 PM",
    "3:00 PM - 4:00 PM"
]

# File to store scheduled appointments persistently
APPOINTMENT_FILE = "appointments.json"


def load_appointments():
    """
    Load existing appointments from the file.
    Returns:
        dict: A dictionary of scheduled appointments.
    """
    try:
        with open(APPOINTMENT_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty dictionary if the file doesn't exist or is corrupted
        return {}


def save_appointments(appointments):
    """
    Save appointments to the file.
    Args:
        appointments (dict): A dictionary of appointments to save.
    """
    try:
        with open(APPOINTMENT_FILE, 'w') as file:
            json.dump(appointments, file, indent=4)
    except Exception as e:
        print(f"Error saving appointments: {e}")


def display_specialties():
    """
    Display available specialties and associated doctors.
    """
    print("Available Specialties at Jinling Hospital:")
    for specialty, doctors in SPECIALTIES.items():
        print(f"- {specialty}: {', '.join(doctors)}")


def display_time_slots():
    """
    Display available time slots for appointments.
    """
    print("Available Time Slots:")
    for index, slot in enumerate(TIME_SLOTS, start=1):
        print(f"{index}. {slot}")


def schedule_appointment():
    """
    Schedule a new appointment.
    """
    appointments = load_appointments()

    # Prompt user for specialty
    display_specialties()
    specialty = input("Enter the specialty for the appointment: ").strip()
    if specialty not in SPECIALTIES:
        print("Invalid specialty. Please try again.")
        return

    # Prompt user for doctor
    doctors = SPECIALTIES[specialty]
    print(f"Available Doctors for {specialty}: {', '.join(doctors)}")
    doctor = input("Enter the doctor's name: ").strip()
    if doctor not in doctors:
        print("Invalid doctor. Please try again.")
        return

    # Prompt user for date
    try:
        date_str = input("Enter the appointment date (YYYY-MM-DD): ").strip()
        appointment_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if appointment_date < datetime.date.today():
            print("The appointment date cannot be in the past. Please try again.")
            return
    except ValueError:
        print("Invalid date format. Please try again.")
        return

    # Prompt user for time slot
    display_time_slots()
    try:
        time_slot_index = int(input("Select a time slot (1-6): ").strip())
        if time_slot_index < 1 or time_slot_index > len(TIME_SLOTS):
            print("Invalid time slot. Please try again.")
            return
        time_slot = TIME_SLOTS[time_slot_index - 1]
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return

    # Check for conflicts
    appointment_key = f"{appointment_date} {time_slot} {doctor}"
    if appointment_key in appointments:
        print("This time slot is already booked. Please choose another.")
        return

    # Save the appointment
    patient_name = input("Enter your full name: ").strip()
    appointments[appointment_key] = {
        "Patient Name": patient_name,
        "Specialty": specialty,
        "Doctor": doctor,
        "Date": str(appointment_date),
        "Time Slot": time_slot
    }
    save_appointments(appointments)
    print("Appointment successfully scheduled!")


def view_appointments():
    """
    View all scheduled appointments.
    """
    appointments = load_appointments()
    if not appointments:
        print("No appointments have been scheduled yet.")
        return

    print("Scheduled Appointments:")
    for key, details in appointments.items():
        print(f"Date & Time: {details['Date']} {details['Time Slot']}")
        print(f"Patient: {details['Patient Name']}")
        print(f"Specialty: {details['Specialty']}")
        print(f"Doctor: {details['Doctor']}")
        print("-" * 40)


def main():
    """
    Main function to run the scheduling system.
    """
    while True:
        print("\nJinling Hospital Appointment Scheduling System")
        print("1. Schedule an Appointment")
        print("2. View Scheduled Appointments")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                schedule_appointment()
            elif choice == 2:
                view_appointments()
            elif choice == 3:
                print("Thank you for using the scheduling system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
```
