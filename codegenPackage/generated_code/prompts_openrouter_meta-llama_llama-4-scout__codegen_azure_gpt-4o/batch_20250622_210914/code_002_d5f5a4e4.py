"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write a code snippet to create a simple database for managing donations and volunteer information for an organization like Kibera Hamlets.
Generated: DETERMINISTIC_d5f5a4e4aadb6634
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Establish a connection to the SQLite database (or create it if it doesn't exist)
db_name = "organization.db"
connection = sqlite3.connect(db_name)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table for managing donations
cursor.execute("""
CREATE TABLE IF NOT EXISTS Donations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each donation
    donor_name TEXT NOT NULL,              -- Name of the donor
    amount REAL NOT NULL,                  -- Donation amount
    donation_date TEXT NOT NULL            -- Date of the donation (ISO format: YYYY-MM-DD)
);
""")

# Create a table for managing volunteer information
cursor.execute("""
CREATE TABLE IF NOT EXISTS Volunteers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each volunteer
    name TEXT NOT NULL,                    -- Name of the volunteer
    contact_info TEXT NOT NULL,            -- Contact information (e.g., phone or email)
    availability TEXT NOT NULL             -- Availability details (e.g., days or hours)
);
""")

# Commit the changes to the database
connection.commit()

# Close the connection to the database
connection.close()

# Note: To interact with the database (e.g., insert, update, query data), 
# you can reopen the connection and use similar patterns.
```
