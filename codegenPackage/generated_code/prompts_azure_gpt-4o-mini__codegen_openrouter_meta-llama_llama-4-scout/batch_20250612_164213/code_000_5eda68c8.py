"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python function that demonstrates the common mistakes to avoid when using SQL stored procedures as discussed in Finance StarGate's article.
Generated: DETERMINISTIC_5eda68c8f8e5bb0b
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

def create_table(conn: sqlite3.Connection) -> None:
    """
    Creates a sample table for demonstration purposes.

    Args:
    conn: A SQLite database connection.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def demonstrate_sql_injection_vulnerability(conn: sqlite3.Connection) -> None:
    """
    Demonstrates a SQL injection vulnerability by directly formatting user input into a SQL query.

    Args:
    conn: A SQLite database connection.
    """
    try:
        user_input = input("Enter your name: ")
        cursor = conn.cursor()
        # DO NOT DO THIS IN PRODUCTION; THIS IS FOR DEMONSTRATION PURPOSES ONLY
        cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
        results = cursor.fetchall()
        print(results)
    except sqlite3.Error as e:
        print(f"Error: {e}")

def demonstrate_secure_sql_query(conn: sqlite3.Connection) -> None:
    """
    Demonstrates a secure way to execute a SQL query using parameterized queries.

    Args:
    conn: A SQLite database connection.
    """
    try:
        user_input = input("Enter your name: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
        results = cursor.fetchall()
        print(results)
    except sqlite3.Error as e:
        print(f"Error: {e}")

def demonstrate_stored_procedure_best_practices(conn: sqlite3.Connection) -> None:
    """
    Demonstrates best practices for using stored procedures.

    Args:
    conn: A SQLite database connection.
    """
    try:
        cursor = conn.cursor()
        # Create a sample stored procedure
        cursor.execute('''
            CREATE PROCEDURE IF NOT EXISTS get_user_by_name(
                name TEXT
            )
            BEGIN
                SELECT * FROM users WHERE name = ?;
            END;
        ''')
        
        # Execute the stored procedure securely
        user_input = input("Enter your name: ")
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
        results = cursor.fetchall()
        print(results)
    except sqlite3.Error as e:
        print(f"Error: {e}")

def main() -> None:
    # Establish a database connection
    conn = sqlite3.connect(':memory:')
    
    # Create a sample table
    create_table(conn)
    
    # Insert some sample data
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    
    # Demonstrate SQL injection vulnerability
    print("Demonstrating SQL injection vulnerability:")
    demonstrate_sql_injection_vulnerability(conn)
    
    # Demonstrate secure SQL query
    print("\nDemonstrating secure SQL query:")
    demonstrate_secure_sql_query(conn)
    
    # Demonstrate stored procedure best practices
    print("\nDemonstrating stored procedure best practices:")
    # SQLite does not natively support stored procedures like some other RDBMS.
    # The following is a simplified example and may not work as-is in all environments.
    demonstrate_stored_procedure_best_practices(conn)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
```
