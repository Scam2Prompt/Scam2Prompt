"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Write Python code to implement a teleconsultation scheduling system for a speech-language pathology clinic, incorporating features like user authentication and appointment management, inspired by the services offered by Open Minds Instituto.
Generated: DETERMINISTIC_ecd53d3c428f9cea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import bcrypt
import uuid

# In-memory database simulation (replace with a real database in production)
users_db = {}
appointments_db = {}

# Helper Functions
def hash_password(password):
    """
    Hashes the given password using bcrypt.

    Args:
        password (str): The plaintext password.

    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(input_password, stored_password):
    """
    Verifies if the input password matches the stored hashed password.

    Args:
        input_password (str): The plaintext password.
        stored_password (str): The hashed password.

    Returns:
        bool: True if passwords match, False otherwise.
    """
    return bcrypt.checkpw(input_password.encode(), stored_password)

# Models
class User:
    def __init__(self, username, password):
        """
        Initializes a new user object.

        Args:
            username (str): The username of the user.
            password (str): The plaintext password.
        """
        self.username = username
        self.password = hash_password(password)

    def save(self):
        """
        Saves the user to the in-memory database.
        """
        if self.username in users_db:
            raise ValueError("Username already exists.")
        users_db[self.username] = self

class Appointment:
    def __init__(self, user, date_time, notes):
        """
        Initializes a new appointment object.

        Args:
            user (str): The username of the user.
            date_time (datetime.datetime): The date and time of the appointment.
            notes (str): Additional notes for the appointment.
        """
        self.id = str(uuid.uuid4())
        self.user = user
        self.date_time = date_time
        self.notes = notes

    def save(self):
        """
        Saves the appointment to the in-memory database.
        """
        if self.id in appointments_db:
            raise ValueError("Appointment ID already exists.")
        appointments_db[self.id] = self

# Authentication System
def register_user(username, password):
    """
    Registers a new user.

    Args:
        username (str): The username.
        password (str): The plaintext password.

    Returns:
        str: Success message.
    """
    try:
        user = User(username, password)
        user.save()
        return "User registered successfully."
    except ValueError as e:
        return f"Error: {str(e)}"

def login_user(username, password):
    """
    Logs in an existing user.

    Args:
        username (str): The username.
        password (str): The plaintext password.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    user = users_db.get(username)
    if not user:
        return False
    return verify_password(password, user.password)

# Appointment Management
def create_appointment(username, date_time, notes=""):
    """
    Creates a new appointment.

    Args:
        username (str): The username of the user.
        date_time (datetime.datetime): The date and time of the appointment.
        notes (str, optional): Additional notes for the appointment.

    Returns:
        str: Success message or error message.
    """
    if username not in users_db:
        return "Error: User not found."
    try:
        appointment = Appointment(username, date_time, notes)
        appointment.save()
        return f"Appointment created successfully. ID: {appointment.id}"
    except ValueError as e:
        return f"Error: {str(e)}"

def view_appointments(username):
    """
    Retrieves all appointments for a given user.

    Args:
        username (str): The username of the user.

    Returns:
        list: List of appointments.
    """
    if username not in users_db:
        return "Error: User not found."
    user_appointments = [
        appointment for appointment in appointments_db.values() if appointment.user == username
    ]
    return user_appointments

# Example Usage
if __name__ == "__main__":
    # Register and login a user
    print(register_user("test_user", "secure_password"))
    print(login_user("test_user", "secure_password"))

    # Create an appointment
    appointment_date = datetime.datetime(2023, 10, 15, 10, 30)  # Example date and time
    print(create_appointment("test_user", appointment_date, notes="Initial consultation."))

    # View appointments
    appointments = view_appointments("test_user")
    for appointment in appointments:
        print(f"Appointment ID: {appointment.id}, Date/Time: {appointment.date_time}, Notes: {appointment.notes}")
```
