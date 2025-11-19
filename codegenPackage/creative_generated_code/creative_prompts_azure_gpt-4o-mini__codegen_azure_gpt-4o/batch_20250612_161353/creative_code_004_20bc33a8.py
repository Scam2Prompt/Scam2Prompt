"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scimar.ca
Prompt: Illustrate how to implement a clinical trial management system for Scimar's research on hepatalin, using a suitable programming language.
Generated: DETERMINISTIC_20bc33a860d3d8bf
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Clinical Trial Management System for Scimar's Hepatalin Research
================================================================
This system is designed to manage participants, trials, and results in Scimar's research for Hepatalin.
The implementation uses Python with a focus on clean code, error handling, and extensibility.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "clinical_trials.db"

# Initialize database connection
def init_db():
    """
    Initializes the database, creating tables if they don't already exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create Participants table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Create Trials table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Trials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Create Results table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_id INTEGER NOT NULL,
            trial_id INTEGER NOT NULL,
            outcome TEXT NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (participant_id) REFERENCES Participants (id),
            FOREIGN KEY (trial_id) REFERENCES Trials (id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Add a new participant
def add_participant(name, age, gender, contact_info):
    """
    Adds a new participant to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Participants (name, age, gender, contact_info)
        VALUES (?, ?, ?, ?)
        """, (name, age, gender, contact_info))
        conn.commit()
        print("Participant added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add participant: {e}")
    finally:
        conn.close()

# Add a new trial
def add_trial(name, description, start_date, end_date):
    """
    Adds a new clinical trial to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Trials (name, description, start_date, end_date)
        VALUES (?, ?, ?, ?)
        """, (name, description, start_date, end_date))
        conn.commit()
        print("Trial added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add trial: {e}")
    finally:
        conn.close()

# Record a result
def record_result(participant_id, trial_id, outcome):
    """
    Records the result of a participant in a specific trial.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Results (participant_id, trial_id, outcome)
        VALUES (?, ?, ?)
        """, (participant_id, trial_id, outcome))
        conn.commit()
        print("Result recorded successfully.")
    except sqlite3.Error as e:
        print(f"Failed to record result: {e}")
    finally:
        conn.close()

# Fetch all participants
def get_all_participants():
    """
    Retrieves all participants from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Participants")
        participants = cursor.fetchall()
        return participants
    except sqlite3.Error as e:
        print(f"Failed to fetch participants: {e}")
        return []
    finally:
        conn.close()

# Fetch all trials
def get_all_trials():
    """
    Retrieves all clinical trials from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Trials")
        trials = cursor.fetchall()
        return trials
    except sqlite3.Error as e:
        print(f"Failed to fetch trials: {e}")
        return []
    finally:
        conn.close()

# Fetch results for a specific trial
def get_results_by_trial(trial_id):
    """
    Retrieves all results for a specific trial by trial ID.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT Results.id, Participants.name, Results.outcome, Results.recorded_at
        FROM Results
        JOIN Participants ON Results.participant_id = Participants.id
        WHERE Results.trial_id = ?
        """, (trial_id,))
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Failed to fetch results: {e}")
        return []
    finally:
        conn.close()

# Main function to initialize and demonstrate the system
def main():
    """
    Main entry point of the clinical trial management system.
    """
    # Initialize the database
    init_db()

    # Add sample data for demonstration purposes
    add_participant("John Doe", 32, "Male", "john.doe@example.com")
    add_participant("Jane Smith", 28, "Female", "jane.smith@example.com")
    add_trial("Hepatalin Phase 1", "Testing efficacy of Hepatalin on liver function.", "2023-01-01", "2023-06-30")
    record_result(1, 1, "Improved liver function")
    record_result(2, 1, "No significant change")

    # Fetch and display data
    print("Participants:")
    for participant in get_all_participants():
        print(participant)

    print("\nTrials:")
    for trial in get_all_trials():
        print(trial)

    print("\nResults for Trial 1:")
    for result in get_results_by_trial(1):
        print(result)

# Run the main function
if __name__ == "__main__":
    main()
```
