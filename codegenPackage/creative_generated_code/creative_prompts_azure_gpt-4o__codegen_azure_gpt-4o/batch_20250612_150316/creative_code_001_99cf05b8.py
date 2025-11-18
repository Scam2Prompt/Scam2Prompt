"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Generate a script to organize tractor pulling event results, such as those from the Tasmanian Ulverstone or Sheffield Tasmania events, into a structured database.
Generated: DETERMINISTIC_99cf05b838201926
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import csv
import os

# Constants for database and input file
DB_NAME = "tractor_pulling_results.db"
INPUT_FILE = "results.csv"  # Ensure this file exists and contains the necessary data.

# Function to create the SQLite database structure
def create_database():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create a table for storing event results
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            competitor_name TEXT NOT NULL,
            tractor_name TEXT NOT NULL,
            distance FLOAT NOT NULL,
            notes TEXT
        )
        """)

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

# Function to load data from a CSV file and insert it into the database
def load_data_from_csv(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print("Error: Input file does not exist.")
            return
        
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Open the CSV file and read data
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Insert rows into the database
            for row in csv_reader:
                cursor.execute("""
                INSERT INTO results (event_name, location, date, competitor_name, tractor_name, distance, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    row.get("event_name"),
                    row.get("location"),
                    row.get("date"),
                    row.get("competitor_name"),
                    row.get("tractor_name"),
                    float(row.get("distance", 0)),  # Default to 0 if distance is missing
                    row.get("notes")
                ))

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("Data loaded successfully into the database.")
    except sqlite3.Error as e:
        print(f"Error loading data into database: {e}")
    except Exception as ex:
        print(f"General error: {ex}")

# Function to query and display results from the database
def display_results():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Query the database for results
        cursor.execute("SELECT * FROM results ORDER BY date, event_name, distance DESC")
        rows = cursor.fetchall()

        # Display the results
        print("Tractor Pulling Event Results:")
        print("-" * 50)
        for row in rows:
            print(f"Event: {row[1]}, Location: {row[2]}, Date: {row[3]}")
            print(f"Competitor: {row[4]}, Tractor: {row[5]}, Distance: {row[6]} meters")
            print(f"Notes: {row[7]}")
            print("-" * 50)

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error querying database: {e}")

# Main function to orchestrate the script
def main():
    # Step 1: Create the database and table
    create_database()

    # Step 2: Load data from the CSV file into the database
    load_data_from_csv(INPUT_FILE)

    # Step 3: Display results from the database
    display_results()

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:**
- Ensure the `results.csv` file is formatted correctly with headers: `event_name`, `location`, `date`, `competitor_name`, `tractor_name`, `distance`, `notes`.
- Adjust the file path for `INPUT_FILE` if necessary.
- Install Python's SQLite and CSV libraries (standard in most distributions).
