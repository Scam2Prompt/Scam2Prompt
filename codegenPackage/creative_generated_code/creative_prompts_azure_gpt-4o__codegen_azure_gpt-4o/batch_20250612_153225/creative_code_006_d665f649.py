"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Develop code to create a DBT therapy progress tracker that monitors skill development in areas like emotional regulation, impulse control, and interpersonal effectiveness, as described on the Mente Sana Psicología website.
Generated: DETERMINISTIC_d665f649496a9d09
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Define constants for skill areas
SKILL_AREAS = ["Emotional Regulation", "Impulse Control", "Interpersonal Effectiveness"]

# Database setup function
def setup_database():
    """
    Initializes the SQLite database and creates necessary table(s) if they don't exist.
    """
    connection = sqlite3.connect("dbt_progress_tracker.db")
    cursor = connection.cursor()

    # Create the progress table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_area TEXT NOT NULL,
            date TEXT NOT NULL,
            skill_rating INTEGER NOT NULL CHECK(skill_rating BETWEEN 1 AND 10),
            notes TEXT
        )
        """
    )
    connection.commit()
    connection.close()

# Function to log progress
def log_progress(skill_area, skill_rating, notes=""):
    """
    Logs progress in a specific skill area.

    Args:
        skill_area (str): The skill area being evaluated (e.g., emotional regulation, impulse control).
        skill_rating (int): A skill rating between 1 and 10.
        notes (str): Optional notes about the progress.
    """
    if skill_area not in SKILL_AREAS:
        raise ValueError(f"Invalid skill area. Must be one of: {', '.join(SKILL_AREAS)}")
    if not isinstance(skill_rating, int) or not (1 <= skill_rating <= 10):
        raise ValueError("Skill rating must be an integer between 1 and 10.")

    connection = sqlite3.connect("dbt_progress_tracker.db")
    cursor = connection.cursor()

    # Insert progress data
    cursor.execute(
        """
        INSERT INTO progress (skill_area, date, skill_rating, notes)
        VALUES (?, ?, ?, ?)
        """,
        (skill_area, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), skill_rating, notes),
    )
    connection.commit()
    connection.close()

# Function to fetch progress data
def fetch_progress(skill_area=None):
    """
    Fetches progress data from the database.

    Args:
        skill_area (str): Optional filter to fetch progress data for a specific skill area.
    
    Returns:
        list: A list of progress records.
    """
    connection = sqlite3.connect("dbt_progress_tracker.db")
    cursor = connection.cursor()

    # Query the data based on the skill area filter
    if skill_area:
        if skill_area not in SKILL_AREAS:
            raise ValueError(f"Invalid skill area. Must be one of: {', '.join(SKILL_AREAS)}")
        cursor.execute(
            """
            SELECT * FROM progress WHERE skill_area = ?
            """,
            (skill_area,),
        )
    else:
        cursor.execute("SELECT * FROM progress")

    rows = cursor.fetchall()
    connection.close()

    # Return fetched data
    return rows

# Main section to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    setup_database()

    # Example: Log progress
    try:
        log_progress("Emotional Regulation", 8, "Practiced mindfulness techniques today.")
        log_progress("Impulse Control", 6, "Struggled with overeating but noticed triggers.")
        log_progress("Interpersonal Effectiveness", 9, "Successfully expressed needs in a conversation.")
    except ValueError as e:
        print(f"Error: {e}")

    # Example: Fetch progress data
    try:
        print("All Progress Records:")
        records = fetch_progress()
        for record in records:
            print(record)

        print("\nFiltered Progress Records (Emotional Regulation):")
        filtered_records = fetch_progress("Emotional Regulation")
        for record in filtered_records:
            print(record)
    except ValueError as e:
        print(f"Error: {e}")
```
