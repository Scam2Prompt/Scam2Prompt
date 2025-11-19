"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Develop a training program for staff to learn how to use Infor SunSystems for financial management and accounting in Hong Kong.
Generated: DETERMINISTIC_1f9d48c30ec264dc
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

The request involves creating a training program, which is not directly related to code development. However, I can provide a Python-based solution to manage and schedule training sessions for staff learning Infor SunSystems. This program will allow administrators to create training sessions, assign staff, and track progress.

```python
import datetime
import json

class TrainingProgram:
    """
    A class to manage training sessions for staff learning Infor SunSystems.
    """

    def __init__(self):
        # Initialize the training program with empty sessions and staff data
        self.sessions = []
        self.staff = {}

    def add_staff(self, staff_id, name, email):
        """
        Add a new staff member to the program.

        :param staff_id: Unique identifier for the staff member
        :param name: Name of the staff member
        :param email: Email address of the staff member
        """
        if staff_id in self.staff:
            print(f"Error: Staff ID {staff_id} already exists.")
            return

        self.staff[staff_id] = {
            "name": name,
            "email": email,
            "sessions": []
        }
        print(f"Staff member {name} added successfully.")

    def create_session(self, session_id, topic, date, duration, trainer):
        """
        Create a new training session.

        :param session_id: Unique identifier for the session
        :param topic: Topic of the training session
        :param date: Date of the session (YYYY-MM-DD)
        :param duration: Duration of the session in hours
        :param trainer: Name of the trainer
        """
        try:
            session_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return

        if any(session["session_id"] == session_id for session in self.sessions):
            print(f"Error: Session ID {session_id} already exists.")
            return

        session = {
            "session_id": session_id,
            "topic": topic,
            "date": session_date,
            "duration": duration,
            "trainer": trainer,
            "attendees": []
        }
        self.sessions.append(session)
        print(f"Training session '{topic}' created successfully.")

    def assign_staff_to_session(self, staff_id, session_id):
        """
        Assign a staff member to a training session.

        :param staff_id: ID of the staff member
        :param session_id: ID of the training session
        """
        staff = self.staff.get(staff_id)
        if not staff:
            print(f"Error: Staff ID {staff_id} not found.")
            return

        session = next((s for s in self.sessions if s["session_id"] == session_id), None)
        if not session:
            print(f"Error: Session ID {session_id} not found.")
            return

        if staff_id in session["attendees"]:
            print(f"Error: Staff ID {staff_id} is already assigned to session {session_id}.")
            return

        session["attendees"].append(staff_id)
        staff["sessions"].append(session_id)
        print(f"Staff member {staff['name']} assigned to session '{session['topic']}'.")

    def list_sessions(self):
        """
        List all training sessions.
        """
        if not self.sessions:
            print("No training sessions available.")
            return

        print("Training Sessions:")
        for session in self.sessions:
            print(f"- ID: {session['session_id']}, Topic: {session['topic']}, Date: {session['date'].strftime('%Y-%m-%d')}, Trainer: {session['trainer']}")

    def list_staff(self):
        """
        List all staff members.
        """
        if not self.staff:
            print("No staff members available.")
            return

        print("Staff Members:")
        for staff_id, staff in self.staff.items():
            print(f"- ID: {staff_id}, Name: {staff['name']}, Email: {staff['email']}")

    def save_data(self, filename):
        """
        Save training program data to a JSON file.

        :param filename: Name of the file to save data
        """
        data = {
            "sessions": self.sessions,
            "staff": self.staff
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, default=str)  # Convert datetime to string
            print(f"Data saved to {filename}.")
        except IOError as e:
            print(f"Error: Unable to save data to {filename}. {e}")

    def load_data(self, filename):
        """
        Load training program data from a JSON file.

        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.sessions = data["sessions"]
                self.staff = data["staff"]
            print(f"Data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error: Unable to load data from {filename}. {e}")


# Example usage
if __name__ == "__main__":
    program = TrainingProgram()

    # Add staff members
    program.add_staff("S001", "Alice Wong", "alice.wong@example.com")
    program.add_staff("S002", "Bob Chan", "bob.chan@example.com")

    # Create training sessions
    program.create_session("T001", "Introduction to Infor SunSystems", "2023-11-01", 2, "John Lee")
    program.create_session("T002", "Advanced Financial Management", "2023-11-05", 3, "Jane Smith")

    # Assign staff to sessions
    program.assign_staff_to_session("S001", "T001")
    program.assign_staff_to_session("S002", "T002")

    # List sessions and staff
    program.list_sessions()
    program.list_staff()

    # Save and load data
    program.save_data("training_program.json")
    program.load_data("training_program.json")
```

This code provides a basic framework for managing training sessions and staff assignments. It includes error handling, data persistence, and follows Python best practices.
