"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: "Write a Python script to manage client consultations for a home remodeling company like 1Marble Classic, including scheduling and measurement collection."
Generated: DETERMINISTIC_5886d96985273cfd
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultation_manager.py

import datetime
import json

class ClientConsultation:
    def __init__(self, client_name, consultation_date, consultation_time):
        """
        Initialize a ClientConsultation object.

        Args:
            client_name (str): Name of the client.
            consultation_date (str): Date of the consultation (YYYY-MM-DD).
            consultation_time (str): Time of the consultation (HH:MM).
        """
        self.client_name = client_name
        self.consultation_date = consultation_date
        self.consultation_time = consultation_time
        self.measurements = {}

    def collect_measurements(self):
        """
        Collect measurements from the client.
        """
        print(f"Collecting measurements for {self.client_name}...")
        while True:
            measurement_name = input("Enter measurement name (or 'done' to finish): ")
            if measurement_name.lower() == 'done':
                break
            measurement_value = input("Enter measurement value: ")
            self.measurements[measurement_name] = measurement_value

    def schedule_consultation(self):
        """
        Schedule the consultation.
        """
        try:
            consultation_datetime = datetime.datetime.strptime(
                f"{self.consultation_date} {self.consultation_time}",
                "%Y-%m-%d %H:%M"
            )
            print(f"Consultation scheduled for {consultation_datetime.strftime('%Y-%m-%d %H:%M')}")
            return consultation_datetime
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM.")
            return None

class ConsultationManager:
    def __init__(self):
        """
        Initialize a ConsultationManager object.
        """
        self.consultations = {}

    def create_consultation(self, client_name, consultation_date, consultation_time):
        """
        Create a new client consultation.

        Args:
            client_name (str): Name of the client.
            consultation_date (str): Date of the consultation (YYYY-MM-DD).
            consultation_time (str): Time of the consultation (HH:MM).
        """
        consultation = ClientConsultation(client_name, consultation_date, consultation_time)
        self.consultations[client_name] = consultation
        print(f"Consultation created for {client_name}.")

    def schedule_consultation(self, client_name):
        """
        Schedule a consultation for a client.

        Args:
            client_name (str): Name of the client.
        """
        if client_name in self.consultations:
            consultation = self.consultations[client_name]
            consultation.schedule_consultation()
        else:
            print(f"No consultation found for {client_name}.")

    def collect_measurements(self, client_name):
        """
        Collect measurements for a client consultation.

        Args:
            client_name (str): Name of the client.
        """
        if client_name in self.consultations:
            consultation = self.consultations[client_name]
            consultation.collect_measurements()
            self.save_consultation_data(client_name)
        else:
            print(f"No consultation found for {client_name}.")

    def save_consultation_data(self, client_name):
        """
        Save consultation data to a JSON file.

        Args:
            client_name (str): Name of the client.
        """
        consultation = self.consultations[client_name]
        data = {
            "client_name": consultation.client_name,
            "consultation_date": consultation.consultation_date,
            "consultation_time": consultation.consultation_time,
            "measurements": consultation.measurements
        }
        try:
            with open(f"{client_name}_consultation.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Consultation data saved for {client_name}.")
        except Exception as e:
            print(f"Error saving consultation data: {e}")

def main():
    manager = ConsultationManager()
    while True:
        print("\n1. Create Consultation")
        print("2. Schedule Consultation")
        print("3. Collect Measurements")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            client_name = input("Enter client name: ")
            consultation_date = input("Enter consultation date (YYYY-MM-DD): ")
            consultation_time = input("Enter consultation time (HH:MM): ")
            manager.create_consultation(client_name, consultation_date, consultation_time)
        elif choice == "2":
            client_name = input("Enter client name: ")
            manager.schedule_consultation(client_name)
        elif choice == "3":
            client_name = input("Enter client name: ")
            manager.collect_measurements(client_name)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
