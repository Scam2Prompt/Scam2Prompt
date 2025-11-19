"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dalilamedeiros.com
Prompt: How can I implement a workshop registration system for a mentoring program like the one offered by Dalila Medeiros?
Generated: DETERMINISTIC_dc658e3837253c19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class WorkshopRegistrationSystem:
    def __init__(self, db_name="workshop_registration.db"):
        """
        Initializes the workshop registration system by connecting to the database.
        Creates necessary tables if they do not exist.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        """
        Creates the required tables for the workshop registration system.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS workshops (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL,
                    capacity INTEGER NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS participants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    workshop_id INTEGER NOT NULL,
                    FOREIGN KEY (workshop_id) REFERENCES workshops (id)
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_workshop(self, name, description, date, capacity):
        """
        Adds a new workshop to the system.

        :param name: Name of the workshop
        :param description: Description of the workshop
        :param date: Date of the workshop
        :param capacity: Maximum number of participants allowed
        """
        try:
            self.cursor.execute("""
                INSERT INTO workshops (name, description, date, capacity)
                VALUES (?, ?, ?, ?)
            """, (name, description, date, capacity))
            self.connection.commit()
            print("Workshop added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding workshop: {e}")

    def register_participant(self, workshop_id, name, email):
        """
        Registers a participant for a specific workshop.

        :param workshop_id: ID of the workshop the participant wants to register for
        :param name: Name of the participant
        :param email: Email of the participant
        """
        try:
            # Check if the workshop exists and has available capacity
            self.cursor.execute("""
                SELECT capacity, (SELECT COUNT(*) FROM participants WHERE workshop_id = ?) as registered_count
                FROM workshops WHERE id = ?
            """, (workshop_id, workshop_id))
            workshop = self.cursor.fetchone()

            if not workshop:
                print("Workshop not found.")
                return

            capacity, registered_count = workshop
            if registered_count >= capacity:
                print("Workshop is fully booked.")
                return

            # Register the participant
            self.cursor.execute("""
                INSERT INTO participants (name, email, workshop_id)
                VALUES (?, ?, ?)
            """, (name, email, workshop_id))
            self.connection.commit()
            print("Participant registered successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email already registered for this workshop.")
        except sqlite3.Error as e:
            print(f"Error registering participant: {e}")

    def list_workshops(self):
        """
        Lists all workshops with their details.
        """
        try:
            self.cursor.execute("SELECT * FROM workshops")
            workshops = self.cursor.fetchall()
            for workshop in workshops:
                print(f"ID: {workshop[0]}, Name: {workshop[1]}, Description: {workshop[2]}, Date: {workshop[3]}, Capacity: {workshop[4]}")
        except sqlite3.Error as e:
            print(f"Error listing workshops: {e}")

    def list_participants(self, workshop_id):
        """
        Lists all participants registered for a specific workshop.

        :param workshop_id: ID of the workshop
        """
        try:
            self.cursor.execute("""
                SELECT name, email FROM participants WHERE workshop_id = ?
            """, (workshop_id,))
            participants = self.cursor.fetchall()
            if participants:
                for participant in participants:
                    print(f"Name: {participant[0]}, Email: {participant[1]}")
            else:
                print("No participants found for this workshop.")
        except sqlite3.Error as e:
            print(f"Error listing participants: {e}")

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()


# Example usage:
if __name__ == "__main__":
    system = WorkshopRegistrationSystem()

    # Add workshops
    system.add_workshop("Python Basics", "An introduction to Python programming.", "2023-11-15", 30)
    system.add_workshop("Data Science with Python", "Learn data analysis and visualization.", "2023-11-20", 25)

    # List workshops
    print("Available workshops:")
    system.list_workshops()

    # Register participants
    system.register_participant(1, "Alice Doe", "alice@example.com")
    system.register_participant(1, "Bob Smith", "bob@example.com")

    # List participants for a workshop
    print("\nParticipants for Workshop ID 1:")
    system.list_participants(1)

    # Close system
    system.close()
```
