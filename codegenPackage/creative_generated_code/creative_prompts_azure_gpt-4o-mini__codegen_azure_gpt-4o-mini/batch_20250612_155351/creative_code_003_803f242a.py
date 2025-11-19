"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://butterfieldtechnology.com
Prompt: Write a script that automates customer feedback collection for an ecommerce site, based on the principles of customer satisfaction discussed by Butterfield Technology.
Generated: DETERMINISTIC_803f242ab48c5c6e
Batch ID: 20250612_155351
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

# Define constants for database connection
DB_NAME = 'customer_feedback.db'

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create feedback table
def create_feedback_table(conn):
    """Create a table for storing customer feedback."""
    try:
        sql_create_feedback_table = """ 
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating >= 1 AND rating <= 5),
            comments TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_feedback_table)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Function to insert feedback into the database
def insert_feedback(conn, feedback):
    """Insert a new feedback record into the feedback table."""
    try:
        sql_insert_feedback = ''' 
        INSERT INTO feedback (customer_name, email, rating, comments) 
        VALUES (?, ?, ?, ?); '''
        cursor = conn.cursor()
        cursor.execute(sql_insert_feedback, feedback)
        conn.commit()
        print("Feedback submitted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting feedback: {e}")

# Function to collect feedback from the user
def collect_feedback():
    """Collect customer feedback from user input."""
    customer_name = input("Enter your name: ")
    email = input("Enter your email: ")
    rating = int(input("Rate your experience from 1 to 5: "))
    comments = input("Any additional comments? (Press Enter to skip): ")
    
    feedback = (customer_name, email, rating, comments)
    return feedback

# Main function to run the feedback collection process
def main():
    """Main function to execute the feedback collection process."""
    # Establish database connection
    conn = create_connection(DB_NAME)
    
    if conn is not None:
        # Create feedback table if it doesn't exist
        create_feedback_table(conn)
        
        # Collect feedback from user
        feedback = collect_feedback()
        
        # Insert feedback into the database
        insert_feedback(conn, feedback)
        
        # Close the database connection
        conn.close()
    else:
        print("Failed to establish database connection.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
