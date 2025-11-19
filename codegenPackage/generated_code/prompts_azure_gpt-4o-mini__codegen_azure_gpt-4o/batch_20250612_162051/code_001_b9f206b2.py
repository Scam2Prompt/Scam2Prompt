"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a code snippet that simulates a consultation scheduling system for a plastic surgeon's practice, incorporating features like procedure selection and patient details.
Generated: DETERMINISTIC_b9f206b2dd5e4880
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ConsultationScheduler:
    def __init__(self):
        # List of available procedures
        self.procedures = {
            "1": "Rhinoplasty",
            "2": "Breast Augmentation",
            "3": "Liposuction",
            "4": "Facelift",
            "5": "Tummy Tuck"
        }
        # List to store scheduled consultations
        self.scheduled_consultations = []

    def display_procedures(self):
        """Display the list of available procedures."""
        print("Available Procedures:")
        for key, procedure in self.procedures.items():
            print(f"{key}. {procedure}")

    def schedule_consultation(self):
        """Schedule a new consultation."""
        try:
            # Collect patient details
            print("\n--- Schedule a Consultation ---")
            patient_name = input("Enter patient's full name: ").strip()
            if not patient_name:
                raise ValueError("Patient name cannot be empty.")

            patient_contact = input("Enter patient's contact number: ").strip()
            if not patient_contact:
                raise ValueError("Contact number cannot be empty.")

            # Display and select procedure
            self.display_procedures()
            procedure_choice = input("Select a procedure by number: ").strip()
            if procedure_choice not in self.procedures:
                raise ValueError("Invalid procedure selection.")

            # Collect and validate consultation date
            consultation_date = input("Enter consultation date (YYYY-MM-DD): ").strip()
            consultation_date = datetime.datetime.strptime(consultation_date, "%Y-%m-%d").date()
            if consultation_date < datetime.date.today():
                raise ValueError("Consultation date cannot be in the past.")

            # Save the consultation details
            consultation = {
                "patient_name": patient_name,
                "patient_contact": patient_contact,
                "procedure": self.procedures[procedure_choice],
                "consultation_date": consultation_date
            }
            self.scheduled_consultations.append(consultation)
            print("\nConsultation successfully scheduled!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_scheduled_consultations(self):
        """View all scheduled consultations."""
        print("\n--- Scheduled Consultations ---")
        if not self.scheduled_consultations:
            print("No consultations scheduled.")
        else:
            for idx, consultation in enumerate(self.scheduled_consultations, start=1):
                print(f"{idx}. {consultation['patient_name']} - {consultation['procedure']} on {consultation['consultation_date']}")

def main():
    """Main function to run the consultation scheduling system."""
    scheduler = ConsultationScheduler()
    while True:
        print("\n--- Plastic Surgeon Consultation Scheduler ---")
        print("1. Schedule a Consultation")
        print("2. View Scheduled Consultations")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            scheduler.schedule_consultation()
        elif choice == "2":
            scheduler.view_scheduled_consultations()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
