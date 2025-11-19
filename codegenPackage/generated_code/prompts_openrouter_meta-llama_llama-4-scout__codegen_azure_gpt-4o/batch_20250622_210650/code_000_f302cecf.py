"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Write a Python script to create a simple text-based appointment booking system for a counseling service, including features for sending messages and storing client information.
Generated: DETERMINISTIC_f302cecfc87fdb46
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

# File to store client information and appointments
DATA_FILE = "appointments.json"

# Load data from file or initialize empty data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"clients": {}, "appointments": []}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new client
def add_client(data):
    print("\n--- Add New Client ---")
    name = input("Enter client name: ").strip()
    email = input("Enter client email: ").strip()
    phone = input("Enter client phone number: ").strip()

    if not name or not email or not phone:
        print("Error: All fields are required.")
        return

    client_id = len(data["clients"]) + 1
    data["clients"][client_id] = {"name": name, "email": email, "phone": phone}
    print(f"Client '{name}' added successfully!")

# Book an appointment
def book_appointment(data):
    print("\n--- Book Appointment ---")
    client_id = input("Enter client ID: ").strip()
    if client_id not in data["clients"]:
        print("Error: Client ID not found.")
        return

    date_str = input("Enter appointment date (YYYY-MM-DD): ").strip()
    time_str = input("Enter appointment time (HH:MM): ").strip()

    try:
        appointment_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        appointment_time = datetime.datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Error: Invalid date or time format.")
        return

    appointment = {
        "client_id": client_id,
        "date": date_str,
        "time": time_str,
    }
    data["appointments"].append(appointment)
    print(f"Appointment booked successfully for {data['clients'][client_id]['name']} on {date_str} at {time_str}.")

# Send a message to a client
def send_message(data):
    print("\n--- Send Message ---")
    client_id = input("Enter client ID: ").strip()
    if client_id not in data["clients"]:
        print("Error: Client ID not found.")
        return

    message = input("Enter your message: ").strip()
    if not message:
        print("Error: Message cannot be empty.")
        return

    client = data["clients"][client_id]
    print(f"Message sent to {client['name']} ({client['email']}): {message}")

# View all clients
def view_clients(data):
    print("\n--- View All Clients ---")
    if not data["clients"]:
        print("No clients found.")
        return

    for client_id, client_info in data["clients"].items():
        print(f"ID: {client_id}, Name: {client_info['name']}, Email: {client_info['email']}, Phone: {client_info['phone']}")

# View all appointments
def view_appointments(data):
    print("\n--- View All Appointments ---")
    if not data["appointments"]:
        print("No appointments found.")
        return

    for appointment in data["appointments"]:
        client = data["clients"][appointment["client_id"]]
        print(f"Client: {client['name']}, Date: {appointment['date']}, Time: {appointment['time']}")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- Counseling Service Appointment System ---")
        print("1. Add New Client")
        print("2. Book Appointment")
        print("3. Send Message to Client")
        print("4. View All Clients")
        print("5. View All Appointments")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_client(data)
        elif choice == "2":
            book_appointment(data)
        elif choice == "3":
            send_message(data)
        elif choice == "4":
            view_clients(data)
        elif choice == "5":
            view_appointments(data)
        elif choice == "6":
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
