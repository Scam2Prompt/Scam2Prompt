"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.specialmetal.ir
Prompt: Write a program to classify superalloys based on their application in industries like oil and gas, aerospace, and power plants using a database of alloys such as DUPLEX ALLOY 2205 and ALLOY 17-4PH.
Generated: DETERMINISTIC_8573fbab4fe71c23
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Define the database schema and populate it with sample data
def initialize_database():
    """
    Initializes the database, creates tables, and inserts sample data.
    """
    conn = sqlite3.connect('superalloys.db')
    cursor = conn.cursor()

    # Create table for superalloys
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS superalloys (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        industry TEXT NOT NULL
    )
    """)

    # Insert sample data
    superalloy_data = [
        ("DUPLEX ALLOY 2205", "Oil and Gas"),
        ("ALLOY 17-4PH", "Aerospace"),
        ("INCONEL 718", "Aerospace"),
        ("HASTELLOY C-22", "Power Plants"),
        ("MONEL 400", "Oil and Gas"),
    ]

    # Insert data into the table
    cursor.executemany("INSERT INTO superalloys (name, industry) VALUES (?, ?)", superalloy_data)
    conn.commit()
    conn.close()

# Function to classify superalloys based on industry
def classify_superalloys(industry):
    """
    Classifies superalloys based on the given industry.

    Args:
        industry (str): The industry to filter superalloys by.

    Returns:
        list: A list of superalloys used in the given industry.
    """
    try:
        conn = sqlite3.connect('superalloys.db')
        cursor = conn.cursor()

        # Query to fetch superalloys for the given industry
        cursor.execute("SELECT name FROM superalloys WHERE industry = ?", (industry,))
        results = cursor.fetchall()

        conn.close()

        # Return the results as a list of alloy names
        return [row[0] for row in results]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Main program
if __name__ == "__main__":
    # Initialize the database (only for first-time setup)
    initialize_database()

    # Prompt the user to input an industry
    print("Available industries: Oil and Gas, Aerospace, Power Plants")
    industry = input("Enter an industry to classify superalloys: ")

    # Fetch and display the classification results
    alloys = classify_superalloys(industry)
    if alloys:
        print(f"Superalloys used in {industry}:")
        for alloy in alloys:
            print(f"- {alloy}")
    else:
        print(f"No superalloys found for industry: {industry}")
```
