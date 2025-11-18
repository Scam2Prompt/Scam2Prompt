"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Create a program to track and visualize public participation in environmental campaigns, inspired by the collaborative approach of "Čuvari Šare."
Generated: DETERMINISTIC_86af4a47514cf038
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program that tracks and visualizes public participation in environmental campaigns, inspired by "Čuvari Šare." It uses `matplotlib` for visualization and includes database interaction via SQLite for data storage:

```python
import sqlite3
import matplotlib.pyplot as plt

# Database setup
DATABASE_FILE = "campaign_participation.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Create table for tracking participation data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_name TEXT NOT NULL,
            participant_name TEXT NOT NULL,
            participation_date TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_participation(campaign_name, participant_name, participation_date):
    """
    Adds a participation record to the database.

    :param campaign_name: The name of the environmental campaign.
    :param participant_name: The name of the participant.
    :param participation_date: The date of participation (YYYY-MM-DD).
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO participation (campaign_name, participant_name, participation_date)
            VALUES (?, ?, ?)
        """, (campaign_name, participant_name, participation_date))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def get_participation_summary():
    """
    Retrieves a summary of participation grouped by campaign.

    :return: A dictionary with campaign names as keys and participation counts as values.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
            SELECT campaign_name, COUNT(*) 
            FROM participation 
            GROUP BY campaign_name
        """)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        results = []
    finally:
        connection.close()

    return {row[0]: row[1] for row in results}

def visualize_participation(summary):
    """
    Generates a bar chart to visualize participation data.

    :param summary: A dictionary with campaign names as keys and participation counts as values.
    """
    campaigns = list(summary.keys())
    counts = list(summary.values())

    plt.figure(figsize=(10, 6))
    plt.bar(campaigns, counts, color='green')
    plt.xlabel('Campaigns')
    plt.ylabel('Number of Participants')
    plt.title('Public Participation in Environmental Campaigns')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to demonstrate program functionality.
    """
    # Ensure the database is initialized
    initialize_database()

    # Sample data
    add_participation("Clean the Beach", "Alice", "2023-10-01")
    add_participation("Plant a Tree", "Bob", "2023-10-02")
    add_participation("Clean the Beach", "Charlie", "2023-10-01")
    add_participation("Save the Forest", "Dave", "2023-10-03")

    # Retrieve and visualize participation summary
    summary = get_participation_summary()
    visualize_participation(summary)

if __name__ == "__main__":
    main()
```

**Prerequisites:**
- Install `matplotlib` if not already installed: `pip install matplotlib`

**Usage:**
Run the program, and it will add sample data to the database, retrieve participation summaries, and visualize them in a bar chart. Replace the sample data and expand as needed for your use case.
