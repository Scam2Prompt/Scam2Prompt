"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labour.events
Prompt: "Construct a SQL query to extract Labour Events data for constituencies in 'Westminster' and 'Liverpool Riverside' from a database."
Generated: DETERMINISTIC_4fd637a9e98a53aa
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def fetch_labour_events(constituencies):
    """
    Fetch Labour Events data for specified constituencies from the database.
    
    Parameters:
    constituencies (list): A list of constituency names to filter the data.

    Returns:
    list: A list of tuples containing the Labour Events data for the selected constituencies.
    """
    
    # Establish a connection to the database
    try:
        conn = sqlite3.connect('labour_events.db')  # Update with the actual database path
        cursor = conn.cursor()
        
        # Create a parameterized SQL query to prevent SQL injection
        query = """
        SELECT * FROM labour_events
        WHERE constituency IN (?, ?);
        """
        
        # Execute the query with the provided constituency names
        cursor.execute(query, constituencies)
        
        # Fetch all results
        results = cursor.fetchall()
        return results
        
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred: {db_err}")
        return []
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    constituencies_to_fetch = ['Westminster', 'Liverpool Riverside']
    labour_events_data = fetch_labour_events(constituencies_to_fetch)
    
    # Display the fetched data
    for event in labour_events_data:
        print(event)
```
