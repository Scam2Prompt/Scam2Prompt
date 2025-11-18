"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Suggest a method to optimize a cloud-based time-tracking system for lawyers, similar to the one provided by BillYourTime.com.
Generated: DETERMINISTIC_9b932da44eab9302
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of Python code that optimizes a cloud-based time-tracking system for lawyers. The optimization focuses on data storage, efficient querying, and proper error handling. It uses a database-backed design with caching for frequently accessed data.

```python
import sqlite3
from datetime import datetime
from functools import lru_cache

# Database setup: Create a SQLite database to store time-tracking data
class TimeTrackingDatabase:
    def __init__(self, db_name="time_tracking.db"):
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """Initialize the database and create required tables."""
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS time_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lawyer_id INTEGER NOT NULL,
                    client_id INTEGER NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT,
                    description TEXT
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def add_time_entry(self, lawyer_id, client_id, start_time, description):
        """Add a new time entry to the database."""
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO time_entries (lawyer_id, client_id, start_time, description)
                VALUES (?, ?, ?, ?)
            """, (lawyer_id, client_id, start_time, description))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def close_time_entry(self, entry_id, end_time):
        """Close an open time entry by adding an end time."""
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE time_entries
                SET end_time = ?
                WHERE id = ?
            """, (end_time, entry_id))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def fetch_time_entries(self, lawyer_id):
        """Fetch all time entries for a given lawyer."""
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM time_entries
                WHERE lawyer_id = ?
            """, (lawyer_id,))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()


# Caching layer for optimization
@lru_cache(maxsize=100)
def get_cached_time_entries(database, lawyer_id):
    """
    Fetch cached time entries for a given lawyer.
    Uses an LRU cache to optimize repeated calls for the same lawyer.
    """
    return database.fetch_time_entries(lawyer_id)


# Example usage of the system
if __name__ == "__main__":
    db = TimeTrackingDatabase()

    # Adding a new time entry
    db.add_time_entry(
        lawyer_id=101,
        client_id=202,
        start_time=datetime.now().isoformat(),
        description="Review contract for client"
    )

    # Closing an open time entry
    db.close_time_entry(entry_id=1, end_time=datetime.now().isoformat())

    # Fetching and caching time entries
    lawyer_entries = get_cached_time_entries(db, lawyer_id=101)
    print("Time entries for lawyer:", lawyer_entries)
```

Important Notes:
- **Database**: Uses SQLite for simplicity; in production, switch to a robust cloud-based database like PostgreSQL or MySQL.
- **Caching**: Uses Python's `functools.lru_cache` for efficient data access.
- **Error Handling**: Ensures that database errors are caught and logged.
- **Scalability**: Adjust caching and database settings as needed for larger data sets.
