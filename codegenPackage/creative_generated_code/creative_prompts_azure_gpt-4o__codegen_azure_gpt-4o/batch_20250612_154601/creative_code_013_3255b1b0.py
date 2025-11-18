"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Write code to generate a leaderboard of top investors based on their investment amounts, similar to the "Top Investors" section on Finance Impact Pro.
Generated: DETERMINISTIC_3255b1b0e0592292
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database setup: Initialize a SQLite database to store investor data
DATABASE_NAME = "investors.db"

def initialize_database():
    """
    Initialize the SQLite database and create the investors table.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        # Create the investors table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS investors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            investment_amount REAL NOT NULL
        )
        """)
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()

def add_investor(name, investment_amount):
    """
    Add a new investor to the database.
    
    Args:
        name (str): Name of the investor.
        investment_amount (float): Amount invested by the investor.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO investors (name, investment_amount)
        VALUES (?, ?)
        """, (name, investment_amount))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()

def get_leaderboard(limit=10):
    """
    Retrieve the top investors based on investment amounts.
    
    Args:
        limit (int): Number of top investors to retrieve. Default is 10.
    
    Returns:
        list: List of top investors (name and investment amount) sorted by investment amount.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        SELECT name, investment_amount
        FROM investors
        ORDER BY investment_amount DESC
        LIMIT ?
        """, (limit,))

        leaderboard = cursor.fetchall()
        return leaderboard
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if connection:
            connection.close()

def print_leaderboard(leaderboard):
    """
    Print the leaderboard in a formatted manner.
    
    Args:
        leaderboard (list): List of top investors.
    """
    print("Leaderboard: Top Investors")
    print("---------------------------")
    for rank, (name, investment_amount) in enumerate(leaderboard, start=1):
        print(f"{rank}. {name} - ${investment_amount:.2f}")

# Main function: Demonstrates the functionality
def main():
    """
    Main function to demonstrate the leaderboard functionality.
    """
    initialize_database()
    
    # Sample data: Adding investors to the database
    sample_investors = [
        ("Alice", 5000),
        ("Bob", 12000),
        ("Charlie", 8000),
        ("Diana", 15000),
        ("Eve", 7600)
    ]

    for name, investment_amount in sample_investors:
        add_investor(name, investment_amount)

    # Generate and print the leaderboard
    leaderboard = get_leaderboard()
    print_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
```
