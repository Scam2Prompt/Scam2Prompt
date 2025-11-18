"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Write a script to automate client consultation scheduling for construction services like interior design, metal roofing, or home expansion, as offered by ExpertStroy.
Generated: DETERMINISTIC_77cdb77fe14e2ffa
Batch ID: 20250612_150653
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

# A simple scheduling script for client consultations

class ConsultationScheduler:
    def __init__(self):
        # Load existing appointments or create an empty schedule
        self.schedule_file = "consultation_schedule.json"
        try:
            with open(self.schedule_file, "r") as file:
                self.schedule = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.schedule = {}

    def display_available_services(self):
        """
        Display the list of services offered by ExpertStroy.
        """
        services = [
            "Interior Design",
            "Metal Roofing",
            "Home Expansion"
        ]
        print("Available Services:")
        for idx, service in enumerate(services, 1):
            print(f"{idx}. {service}")

    def schedule_consultation(self, client_name, service, date, time):
        """
        Schedule a consultation with the client.
        :param client_name: Name of the client
        :param service: Service selected by the client
        :param date: Date of the consultation (format: YYYY-MM-DD)
        :param time: Time of the consultation (format: HH:MM)
        """
        try:
            # Validate the date and time format
            consultation_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

            # Check if the requested date and time are available
            if date not in self.schedule:
                self.schedule[date] = {}

            if time in self.schedule[date]:
                print(f"Error: The time slot {time} on {date} is already booked.")
                return False

            # Save the consultation appointment
            self.schedule[date][time] = {
                "client_name": client_name,
                "service": service
            }
            self.save_schedule()
            print(f"Consultation scheduled successfully for {client_name} on {date} at {time} for {service}.")
            return True

        except ValueError as e:
            print(f"Invalid date or time format: {e}")
            return False

    def save_schedule(self):
        """
        Save the schedule to a JSON file to persist appointments.
        """
        try:
            with open(self.schedule_file, "w") as file:
                json.dump(self.schedule, file, indent=4)
        except Exception as e:
            print(f"Error saving schedule: {e}")

    def view_schedule(self):
        """
        Display the entire schedule of consultations.
        """
        print("Consultation Schedule:")
        if not self.schedule:
            print("No consultations scheduled yet.")
            return

        for date, time_slots in self.schedule.items():
            print(f"Date: {date}")
            for time, details in time_slots.items():
                print(f"  Time: {time}, Client: {details['client_name']}, Service: {details['service']}")

def main():
    scheduler = ConsultationScheduler()

    while True:
        print("\n--- Consultation Scheduler ---")
        print("1. View Available Services")
        print("2. Schedule a Consultation")
        print("3. View Schedule")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            scheduler.display_available_services()
        elif choice == 2:
            client_name = input("Enter client name: ")
            scheduler.display_available_services()
            service_choice = int(input("Select a service (1-3): "))
            services = ["Interior Design", "Metal Roofing", "Home Expansion"]
            if service_choice < 1 or service_choice > len(services):
                print("Invalid service choice.")
                continue
            service = services[service_choice - 1]
            date = input("Enter consultation date (YYYY-MM-DD): ")
            time = input("Enter consultation time (HH:MM): ")
            scheduler.schedule_consultation(client_name, service, date, time)
        elif choice == 3:
            scheduler.view_schedule()
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
```
