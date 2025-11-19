"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Write a Python script to manage client sessions for a holistic therapy center like Reset Terapias e Movimento, including scheduling and personalized treatment plans."
Generated: DETERMINISTIC_862b0c6b6396704d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class TherapyCenter:
    def __init__(self):
        """
        Initializes the TherapyCenter with empty client and session data.
        """
        self.clients = {}  # Stores client information
        self.sessions = []  # Stores scheduled sessions

    def add_client(self, client_id, name, age, contact_info, treatment_plan):
        """
        Adds a new client to the system.

        Args:
            client_id (str): Unique identifier for the client.
            name (str): Name of the client.
            age (int): Age of the client.
            contact_info (str): Contact information for the client.
            treatment_plan (dict): Personalized treatment plan for the client.
        """
        if client_id in self.clients:
            raise ValueError("Client ID already exists.")
        
        self.clients[client_id] = {
            "name": name,
            "age": age,
            "contact_info": contact_info,
            "treatment_plan": treatment_plan
        }
        print(f"Client {name} added successfully.")

    def schedule_session(self, client_id, date, time, duration_minutes):
        """
        Schedules a session for a client.

        Args:
            client_id (str): Unique identifier for the client.
            date (str): Date of the session in YYYY-MM-DD format.
            time (str): Time of the session in HH:MM format.
            duration_minutes (int): Duration of the session in minutes.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist.")
        
        try:
            session_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format.")
        
        session_end = session_datetime + timedelta(minutes=duration_minutes)
        self.sessions.append({
            "client_id": client_id,
            "client_name": self.clients[client_id]["name"],
            "start_time": session_datetime,
            "end_time": session_end
        })
        print(f"Session scheduled for {self.clients[client_id]['name']} on {date} at {time}.")

    def view_sessions(self):
        """
        Displays all scheduled sessions.
        """
        if not self.sessions:
            print("No sessions scheduled.")
            return
        
        print("Scheduled Sessions:")
        for session in self.sessions:
            print(f"Client: {session['client_name']}, Start: {session['start_time']}, End: {session['end_time']}")

    def save_data(self, filename="therapy_center_data.json"):
        """
        Saves client and session data to a JSON file.

        Args:
            filename (str): Name of the file to save data to.
        """
        data = {
            "clients": self.clients,
            "sessions": [
                {
                    "client_id": session["client_id"],
                    "client_name": session["client_name"],
                    "start_time": session["start_time"].strftime("%Y-%m-%d %H:%M"),
                    "end_time": session["end_time"].strftime("%Y-%m-%d %H:%M")
                }
                for session in self.sessions
            ]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}.")

    def load_data(self, filename="therapy_center_data.json"):
        """
        Loads client and session data from a JSON file.

        Args:
            filename (str): Name of the file to load data from.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.clients = data["clients"]
                self.sessions = [
                    {
                        "client_id": session["client_id"],
                        "client_name": session["client_name"],
                        "start_time": datetime.strptime(session["start_time"], "%Y-%m-%d %H:%M"),
                        "end_time": datetime.strptime(session["end_time"], "%Y-%m-%d %H:%M")
                    }
                    for session in data["sessions"]
                ]
            print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty data.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with empty data.")

# Example usage
if __name__ == "__main__":
    center = TherapyCenter()

    # Add clients
    center.add_client(
        client_id="C001",
        name="Alice Smith",
        age=30,
        contact_info="alice@example.com",
        treatment_plan={"Yoga": "Twice a week", "Meditation": "Daily"}
    )
    center.add_client(
        client_id="C002",
        name="Bob Johnson",
        age=45,
        contact_info="bob@example.com",
        treatment_plan={"Massage": "Weekly", "Acupuncture": "Bi-weekly"}
    )

    # Schedule sessions
    center.schedule_session(client_id="C001", date="2023-10-15", time="10:00", duration_minutes=60)
    center.schedule_session(client_id="C002", date="2023-10-16", time="14:00", duration_minutes=90)

    # View sessions
    center.view_sessions()

    # Save and load data
    center.save_data()
    center.load_data()
```
