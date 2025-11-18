"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rararaibar.com
Prompt: Write code to create a database schema for storing news articles from the "Rara Raibar" website, including fields for title, date, category, and content.
Generated: DETERMINISTIC_5880541cc2c16550
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_database_schema():
    """
    Creates a database schema for storing news articles from the 'Rara Raibar' website.
    The schema includes fields for title, date, category, and content.
    """
    try:
        # Connect to the database (creates the database file if it doesn't exist)
        conn = sqlite3.connect("rara_raibar.db")
        cursor = conn.cursor()

        # Create the articles table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique ID for each article
            title TEXT NOT NULL,                 -- Title of the article
            date TEXT NOT NULL,                  -- Publication date in ISO format (YYYY-MM-DD)
            category TEXT NOT NULL,              -- Category of the article (e.g., Politics, Sports)
            content TEXT NOT NULL                -- Full content of the article
        );
        """)

        # Commit the changes and close the connection
        conn.commit()
        print("Database schema created successfully!")

    except sqlite3.Error as e:
        # Handle database errors gracefully
        print(f"An error occurred while creating the database schema: {e}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

# Run the function to create the schema
if __name__ == "__main__":
    create_database_schema()
```
