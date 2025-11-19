"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a script to convert the "آیین نامه مرخصی" (leave regulations) into a searchable database, allowing users to query specific rules based on keywords or categories.
Generated: DETERMINISTIC_64dfec06d3e68641
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import csv
import os

# Define the database file name
DB_FILE = 'leave_regulations.db'

def create_database():
    """Create a SQLite database and a table for leave regulations."""
    try:
        # Connect to the SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create a table for leave regulations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS regulations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                rule TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def import_data_from_csv(csv_file):
    """Import leave regulations from a CSV file into the database."""
    if not os.path.exists(csv_file):
        print(f"Error: The file {csv_file} does not exist.")
        return

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute('''
                    INSERT INTO regulations (category, rule) VALUES (?, ?)
                ''', (row['category'], row['rule']))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error importing data: {e}")
    finally:
        if conn:
            conn.close()

def search_regulations(keyword):
    """Search for regulations containing the specified keyword."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM regulations WHERE rule LIKE ?
        ''', ('%' + keyword + '%',))
        
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def main():
    """Main function to create the database, import data, and allow user queries."""
    create_database()
    
    # Import data from CSV (update the path to your CSV file)
    import_data_from_csv('leave_regulations.csv')
    
    # Example of searching for regulations
    keyword = input("Enter a keyword to search for regulations: ")
    results = search_regulations(keyword)
    
    if results:
        print("Search Results:")
        for row in results:
            print(f"ID: {row[0]}, Category: {row[1]}, Rule: {row[2]}")
    else:
        print("No regulations found for the given keyword.")

if __name__ == '__main__':
    main()
```

**Note:** Ensure that you have a CSV file named `leave_regulations.csv` with columns `category` and `rule` for the import function to work correctly. Adjust the file path as necessary.
