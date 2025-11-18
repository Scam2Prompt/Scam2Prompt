"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write Python code to simulate a scheduling system for medical exams like colonoscopy, endoscopy, and elastography, including options for selecting dates, times, and specialties such as gastroenterology and hepatology.
Generated: DETERMINISTIC_8cb1cd011b51504b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class MedicalSchedulingSystem:
    def __init__(self):
        # Initialize available specialties and procedures
        self.specialties = ["Gastroenterology", "Hepatology"]
        self.procedures = ["Colonoscopy", "Endoscopy", "Elastography"]
        self.schedule = []  # Stores scheduled appointments

    def display_specialties(self):
        """Display available specialties."""
        print("Available Specialties:")
        for index, specialty in enumerate(self.specialties, start=1):
            print(f"{index}. {specialty}")

    def display_procedures(self):
        """Display available procedures."""
        print("Available Procedures:")
        for index, procedure in enumerate(self.procedures, start=1):
            print(f"{index}. {procedure}")

    def schedule_appointment(self):
        """Schedule a medical exam."""
        try:
            # Select specialty
            self.display_specialties()
            specialty_choice = int(input("Select a specialty (Enter the number): "))
            if specialty_choice < 1 or specialty_choice > len(self.specialties):
                raise ValueError("Invalid specialty selection.")
            specialty = self.specialties[specialty_choice - 1]

            # Select procedure
            self.display_procedures()
            procedure_choice = int(input("Select a procedure (Enter the number): "))
            if procedure_choice < 1 or procedure_choice > len(self.procedures):
                raise ValueError("Invalid procedure selection.")
            procedure = self.procedures[procedure_choice - 1]

            # Select date
            date_input = input("Enter a date for the appointment (YYYY-MM-DD): ")
            appointment_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

            # Select time
            time_input = input("Enter a time for the appointment (HH:MM): ")
            appointment_time = datetime.datetime.strptime(time_input, "%H:%M").time()

            # Create appointment record
            appointment = {
                "Specialty": specialty,
                "Procedure": procedure,
                "Date": appointment_date,
                "Time": appointment_time
            }
            self.schedule.append(appointment)

            print("\nAppointment successfully scheduled!")
            print(f"Specialty: {specialty}")
            print(f"Procedure: {procedure}")
            print(f"Date: {appointment_date}")
            print(f"Time: {appointment_time}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_schedule(self):
        """View all scheduled appointments."""
        if not self.schedule:
            print("No appointments have been scheduled.")
        else:
            print("\nScheduled Appointments:")
            for index, appointment in enumerate(self.schedule, start=1):
                print(f"{index}. Specialty: {appointment['Specialty']}, Procedure: {appointment['Procedure']}, "
                      f"Date: {appointment['Date']}, Time: {appointment['Time']}")

def main():
    """Main function to run the scheduling system."""
    system = MedicalSchedulingSystem()
    while True:
        print("\nMedical Scheduling System")
        print("1. Schedule an Appointment")
        print("2. View Scheduled Appointments")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            system.schedule_appointment()
        elif choice == "2":
            system.view_schedule()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
