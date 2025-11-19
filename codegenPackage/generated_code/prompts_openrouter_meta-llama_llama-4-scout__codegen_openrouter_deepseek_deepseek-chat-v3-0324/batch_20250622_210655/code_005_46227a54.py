"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "What are the best practices for implementing effective pest control measures in a residential area? Provide a code example in Python for tracking pest control activities."
Generated: DETERMINISTIC_46227a54cfd6a8e5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class PestControlTracker:
    """
    A class to track pest control activities in a residential area.
    """

    def __init__(self, db_name: str = "pest_control.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """
        Create necessary tables for tracking pest control activities.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                property_id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL,
                resident_name TEXT NOT NULL,
                contact_number TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pest_types (
                pest_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pest_name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS control_methods (
                method_id INTEGER PRIMARY KEY AUTOINCREMENT,
                method_name TEXT NOT NULL UNIQUE,
                description TEXT,
                safety_precautions TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pest_control_activities (
                activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                property_id INTEGER NOT NULL,
                pest_id INTEGER NOT NULL,
                method_id INTEGER NOT NULL,
                activity_date TEXT NOT NULL,
                technician_name TEXT NOT NULL,
                notes TEXT,
                follow_up_required INTEGER DEFAULT 0,
                follow_up_date TEXT,
                FOREIGN KEY (property_id) REFERENCES properties (property_id),
                FOREIGN KEY (pest_id) REFERENCES pest_types (pest_id),
                FOREIGN KEY (method_id) REFERENCES control_methods (method_id)
            )
        """)
        self.conn.commit()

    def add_property(self, address: str, resident_name: str, contact_number: str) -> int:
        """
        Add a new property to the database.
        """
        self.cursor.execute(
            "INSERT INTO properties (address, resident_name, contact_number) VALUES (?, ?, ?)",
            (address, resident_name, contact_number)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def add_pest_type(self, pest_name: str, description: Optional[str] = None) -> int:
        """
        Add a new pest type to the database.
        """
        self.cursor.execute(
            "INSERT INTO pest_types (pest_name, description) VALUES (?, ?)",
            (pest_name, description)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def add_control_method(self, method_name: str, description: Optional[str] = None, 
                          safety_precautions: Optional[str] = None) -> int:
        """
        Add a new control method to the database.
        """
        self.cursor.execute(
            "INSERT INTO control_methods (method_name, description, safety_precautions) VALUES (?, ?, ?)",
            (method_name, description, safety_precautions)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def log_activity(self, property_id: int, pest_id: int, method_id: int, 
                    activity_date: str, technician_name: str, notes: Optional[str] = None,
                    follow_up_required: bool = False, follow_up_date: Optional[str] = None) -> int:
        """
        Log a pest control activity.
        """
        self.cursor.execute(
            """INSERT INTO pest_control_activities 
            (property_id, pest_id, method_id, activity_date, technician_name, notes, 
            follow_up_required, follow_up_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (property_id, pest_id, method_id, activity_date, technician_name, notes,
             int(follow_up_required), follow_up_date)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_properties(self) -> List[Dict]:
        """
        Retrieve all properties from the database.
        """
        self.cursor.execute("SELECT * FROM properties")
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_pest_types(self) -> List[Dict]:
        """
        Retrieve all pest types from the database.
        """
        self.cursor.execute("SELECT * FROM pest_types")
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_control_methods(self) -> List[Dict]:
        """
        Retrieve all control methods from the database.
        """
        self.cursor.execute("SELECT * FROM control_methods")
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_activities(self) -> List[Dict]:
        """
        Retrieve all pest control activities from the database.
        """
        self.cursor.execute("""
            SELECT pca.*, pr.address, pr.resident_name, pt.pest_name, cm.method_name
            FROM pest_control_activities pca
            JOIN properties pr ON pca.property_id = pr.property_id
            JOIN pest_types pt ON pca.pest_id = pt.pest_id
            JOIN control_methods cm ON pca.method_id = cm.method_id
        """)
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_upcoming_follow_ups(self) -> List[Dict]:
        """
        Retrieve all upcoming follow-up activities.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("""
            SELECT pca.*, pr.address, pr.resident_name, pt.pest_name, cm.method_name
            FROM pest_control_activities pca
            JOIN properties pr ON pca.property_id = pr.property_id
            JOIN pest_types pt ON pca.pest_id = pt.pest_id
            JOIN control_methods cm ON pca.method_id = cm.method_id
            WHERE pca.follow_up_required = 1 AND pca.follow_up_date >= ?
            ORDER BY pca.follow_up_date ASC
        """, (today,))
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage
if __name__ == "__main__":
    with PestControlTracker() as tracker:
        # Add sample data
        property_id = tracker.add_property(
            "123 Main St", "John Doe", "555-1234"
        )
        pest_id = tracker.add_pest_type(
            "Cockroach", "German cockroach infestation"
        )
        method_id = tracker.add_control_method(
            "Baiting", "Gel bait application", "Keep away from children and pets"
        )
        
        # Log an activity
        activity_id = tracker.log_activity(
            property_id=property_id,
            pest_id=pest_id,
            method_id=method_id,
            activity_date="2023-11-15",
            technician_name="Jane Smith",
            notes="Applied bait in kitchen and bathroom",
            follow_up_required=True,
            follow_up_date="2023-12-01"
        )
        
        # Retrieve and print all activities
        activities = tracker.get_activities()
        for activity in activities:
            print(activity)
```
