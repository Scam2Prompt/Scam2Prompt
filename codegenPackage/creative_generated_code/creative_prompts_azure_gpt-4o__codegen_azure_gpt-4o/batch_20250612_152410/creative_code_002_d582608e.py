"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argnt.xyz
Prompt: Generate Python code to query and display lottery results using a database schema similar to the one described in "查询信息 : 38 queries."
Generated: DETERMINISTIC_d582608eeda001b0
Batch ID: 20250612_152410
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

# Database configuration
DB_FILE = "lottery_results.db"

# Function to connect to the database
def connect_to_db(db_file):
    """
    Connects to the SQLite database.

    :param db_file: Path to the database file.
    :return: Connection object.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to query lottery results
def query_lottery_results(conn, draw_date=None):
    """
    Query lottery results from the database.

    :param conn: SQLite connection object.
    :param draw_date: Optional date to filter results (YYYY-MM-DD).
    :return: List of results or an empty list if none found.
    """
    try:
        cursor = conn.cursor()
        
        # SQL query to retrieve results
        if draw_date:
            sql_query = "SELECT draw_date, winning_numbers FROM lottery_results WHERE draw_date = ?"
            cursor.execute(sql_query, (draw_date,))
        else:
            sql_query = "SELECT draw_date, winning_numbers FROM lottery_results ORDER BY draw_date DESC"
            cursor.execute(sql_query)
        
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error querying lottery results: {e}")
        return []

# Function to display lottery results
def display_results(results):
    """
    Displays the lottery results.

    :param results: List of lottery results.
    """
    if not results:
        print("No lottery results found.")
        return
    
    print("Lottery Results:")
    print("-" * 30)
    for result in results:
        draw_date = result[0]
        winning_numbers = result[1]
        print(f"Date: {draw_date}, Winning Numbers: {winning_numbers}")

# Main function
def main():
    """
    Main function to query and display lottery results.
    """
    conn = connect_to_db(DB_FILE)
    if not conn:
        return

    try:
        # Example: Query lottery results for a specific date
        draw_date = input("Enter draw date (YYYY-MM-DD) or press Enter to see all results: ")
        if draw_date:
            # Validate date format
            try:
                datetime.strptime(draw_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
            
        results = query_lottery_results(conn, draw_date)
        display_results(results)
    finally:
        # Ensure database connection is closed
        conn.close()

# Run the script
if __name__ == "__main__":
    main()
```

### Notes:
1. This code assumes the existence of a database file `lottery_results.db` with a table `lottery_results` that has columns `draw_date` (TEXT) and `winning_numbers` (TEXT or similar format).
2. Please update the `DB_FILE` path to the actual location of your database file if different.
