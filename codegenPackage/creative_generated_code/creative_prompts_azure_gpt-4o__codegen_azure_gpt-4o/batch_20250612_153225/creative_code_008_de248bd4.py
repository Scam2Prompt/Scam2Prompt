"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Create a program to schedule health education activities and multi-diagnostic camps for rural areas, as described under MIMSR's outreach initiatives.
Generated: DETERMINISTIC_de248bd498679ed9
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
import sqlite3


class OutreachScheduler:
    def __init__(self, db_name="outreach.db"):
        """
        Initializes the OutreachScheduler with a connection to a SQLite database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None
        self._connect_to_db()
        self._setup_database()

    def _connect_to_db(self):
        """Connects to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _setup_database(self):
        """Sets up the database schema if it doesn't exist."""
        try:
            cursor = self.connection.cursor()
            # Create table for health activities scheduling
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS health_activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    activity_name TEXT NOT NULL,
                    activity_date DATE NOT NULL,
                    location TEXT NOT NULL,
                    description TEXT
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
            raise

    def schedule_activity(self, activity_name, activity_date, location, description=""):
        """
        Schedules a health education activity or multi-diagnostic camp.
        :param activity_name: Name of the activity.
        :param activity_date: Date of the activity in 'YYYY-MM-DD' format.
        :param location: Location of the activity.
        :param description: Optional description of the activity.
        :return: None
        """
        try:
            # Validate date format
            datetime.datetime.strptime(activity_date, "%Y-%m-%d")

            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO health_activities (activity_name, activity_date, location, description)
                VALUES (?, ?, ?, ?)
            """, (activity_name, activity_date, location, description))
            self.connection.commit()
            print(f"Activity '{activity_name}' scheduled successfully!")
        except ValueError:
            print("Error: Invalid date format. Use 'YYYY-MM-DD'.")
        except sqlite3.Error as e:
            print(f"Error scheduling activity: {e}")
            raise

    def view_upcoming_activities(self):
        """
        Retrieves and displays all upcoming health activities.
        :return: None
        """
        try:
            cursor = self.connection.cursor()
            today = datetime.datetime.today().strftime("%Y-%m-%d")
            cursor.execute("""
                SELECT activity_name, activity_date, location, description
                FROM health_activities
                WHERE activity_date >= ?
                ORDER BY activity_date ASC
            """, (today,))
            activities = cursor.fetchall()

            print("Upcoming Health Activities:")
            print("-" * 40)
            for activity in activities:
                print(f"Activity Name: {activity[0]}")
                print(f"Date: {activity[1]}")
                print(f"Location: {activity[2]}")
                print(f"Description: {activity[3]}\n")
            print("-" * 40)
        except sqlite3.Error as e:
            print(f"Error retrieving activities: {e}")
            raise

    def close_connection(self):
        """Closes the connection to the database."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    scheduler = OutreachScheduler()

    # Schedule some activities
    scheduler.schedule_activity(
        activity_name="Health Education Program",
        activity_date="2023-11-15",
        location="Village A",
        description="Teaching basic hygiene practices."
    )
    scheduler.schedule_activity(
        activity_name="Multi-Diagnostic Camp",
        activity_date="2023-11-20",
        location="Village B",
        description="General health check-up and diagnostic services."
    )

    # View upcoming activities
    scheduler.view_upcoming_activities()

    # Close the database connection
    scheduler.close_connection()
```
