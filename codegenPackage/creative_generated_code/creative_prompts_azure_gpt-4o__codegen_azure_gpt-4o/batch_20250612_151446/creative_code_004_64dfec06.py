"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Write a script to convert the "آیین نامه مرخصی" (leave regulations) into a searchable database, allowing users to query specific rules based on keywords or categories.
Generated: DETERMINISTIC_64dfec06d3e68641
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import os

def create_database(db_name="leave_regulations.db"):
    """Creates a database to store leave regulations."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS regulations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        rule TEXT NOT NULL
    );
    """)
    
    conn.commit()
    conn.close()

def insert_regulations(regulations, db_name="leave_regulations.db"):
    """Inserts regulations into the database."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Insert rules into the table
        cursor.executemany("""
        INSERT INTO regulations (category, rule) VALUES (?, ?);
        """, regulations)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting regulations: {e}")
    finally:
        conn.close()

def search_rules(keyword, db_name="leave_regulations.db"):
    """Searches for rules in the database based on a keyword."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Query rules based on keyword
        cursor.execute("""
        SELECT id, category, rule FROM regulations
        WHERE rule LIKE ? OR category LIKE ?;
        """, (f"%{keyword}%", f"%{keyword}%"))
        
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error searching for rules: {e}")
        return []
    finally:
        conn.close()

def main():
    """Main function to initialize the database and provide search functionality."""
    # Define the database name
    db_name = "leave_regulations.db"
    
    # If database does not exist, create it and populate it with sample data
    if not os.path.exists(db_name):
        create_database(db_name)
        sample_regulations = [
            ("Paid Leave", "Employees are entitled to 20 days of paid leave annually."),
            ("Sick Leave", "Employees can take up to 10 days of sick leave per year."),
            ("Unpaid Leave", "Unpaid leave may be granted upon manager approval."),
            ("Parental Leave", "New parents are entitled to 30 days of parental leave."),
        ]
        insert_regulations(sample_regulations, db_name)
        print("Database created and populated with sample data.")
    else:
        print("Database already exists.")
    
    # Query loop for the user
    print("\nLeave Regulations Search Tool")
    while True:
        keyword = input("Enter a keyword or category to search (or 'exit' to quit): ").strip()
        if keyword.lower() == 'exit':
            print("Exiting search tool. Goodbye!")
            break
        
        results = search_rules(keyword, db_name)
        if results:
            print("\nSearch Results:")
            for row in results:
                print(f"ID: {row[0]}, Category: {row[1]}, Rule: {row[2]}")
        else:
            print("No matching rules found.")

if __name__ == "__main__":
    main()
```
