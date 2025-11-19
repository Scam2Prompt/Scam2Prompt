"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a code snippet that simulates a consultation scheduling system for a plastic surgeon's practice, incorporating features like procedure selection and patient details.
Generated: DETERMINISTIC_b9f206b2dd5e4880
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Class to represent a consultation scheduling system
class ConsultationScheduler:
    def __init__(self):
        # Available procedures at the practice
        self.procedures = {
            "Botox": 200,
            "Rhinoplasty": 5000,
            "Liposuction": 4000,
            "Facelift": 7000,
        }
        # Storage for scheduled consultations
        self.scheduled_consultations = []

    def display_procedures(self):
        """Display available procedures and their costs."""
        print("Available Procedures:")
        for procedure, cost in self.procedures.items():
            print(f"{procedure}: ${cost}")

    def schedule_consultation(self):
        """Interactive method to schedule a consultation."""
        try:
            # Get patient details
            print("\n--- Consultation Scheduling ---")
            patient_name = input("Enter patient's full name: ").strip()
            patient_contact = input("Enter patient's contact number: ").strip()

            # Display and select procedure
            self.display_procedures()
            selected_procedure = input("\nEnter the name of the desired procedure: ").strip()
            
            # Validate procedure selection
            if selected_procedure not in self.procedures:
                print("Invalid procedure selected. Please try again.")
                return

            # Get consultation date
            consultation_date_str = input("Enter the consultation date (YYYY-MM-DD): ").strip()
            consultation_date = datetime.datetime.strptime(consultation_date_str, "%Y-%m-%d")

            # Save scheduled consultation
            consultation = {
                "name": patient_name,
                "contact": patient_contact,
                "procedure": selected_procedure,
                "date": consultation_date,
                "cost": self.procedures[selected_procedure],
            }
            self.scheduled_consultations.append(consultation)
            print("\nConsultation scheduled successfully!")
            print(f"Patient: {patient_name}, Procedure: {selected_procedure}, Date: {consultation_date.strftime('%Y-%m-%d')}")

        except ValueError as e:
            print(f"Error: Invalid date format. {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_scheduled_consultations(self):
        """View all scheduled consultations."""
        print("\n--- Scheduled Consultations ---")
        if not self.scheduled_consultations:
            print("No consultations have been scheduled.")
            return
        for idx, consultation in enumerate(self.scheduled_consultations, start=1):
            print(f"{idx}. Patient: {consultation['name']}, Procedure: {consultation['procedure']}, Date: {consultation['date'].strftime('%Y-%m-%d')}, Cost: ${consultation['cost']}")

# Main function to interact with the scheduling system
def main():
    scheduler = ConsultationScheduler()
    while True:
        print("\n--- Plastic Surgeon Consultation Scheduler ---")
        print("1. View Procedures")
        print("2. Schedule Consultation")
        print("3. View Scheduled Consultations")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            scheduler.display_procedures()
        elif choice == "2":
            scheduler.schedule_consultation()
        elif choice == "3":
            scheduler.view_scheduled_consultations()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
