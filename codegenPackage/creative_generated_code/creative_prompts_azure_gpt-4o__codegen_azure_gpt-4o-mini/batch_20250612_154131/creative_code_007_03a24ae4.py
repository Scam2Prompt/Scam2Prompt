"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Provide a step-by-step guide to implement a database management system for small businesses, referencing the technical experience described on uuip-hualdlugeen.
Generated: DETERMINISTIC_03a24ae49272c35d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    """
    A class to manage a SQLite database for small businesses.
    
    Attributes:
        database (str): Path to the SQLite database file.
    """

    def __init__(self, db_file):
        """
        Initializes the DatabaseManager with a database file.
        
        Parameters:
            db_file (str): Path to the SQLite database file.
        """
        self.database = db_file

    def create_connection(self):
        """
        Create a database connection to a SQLite database.
        
        Returns:
            conn: SQLite connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.database)
            print("Connection established to database.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def execute_query(self, query):
        """
        Execute a single SQL query.
        
        Parameters:
            query (str): SQL query to execute.
        """
        conn = self.create_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            if conn:
                conn.close()

    def execute_read_query(self, query):
        """
        Execute a read SQL query and return the results.
        
        Parameters:
            query (str): SQL query to execute.
        
        Returns:
            list: List of results from the query execution.
        """
        conn = self.create_connection()
        results = []
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            print("Read query executed successfully.")
        except Error as e:
            print(f"Error reading query: {e}")
        finally:
            if conn:
                conn.close()
        return results

def main():
    # Path to the database file
    database_path = "small_business.db"
    
    # Create DatabaseManager instance
    db_manager = DatabaseManager(database_path)

    # SQL statements
    create_employees_table = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    );
    """

    insert_employee = """
    INSERT INTO employees (name, position, salary) 
    VALUES ('John Doe', 'Software Engineer', 70000);
    """

    select_all_employees = "SELECT * FROM employees;"

    # Create tables
    db_manager.execute_query(create_employees_table)
    
    # Insert an employee
    db_manager.execute_query(insert_employee)

    # Read all employees
    employees = db_manager.execute_read_query(select_all_employees)
    
    # Print the results
    for employee in employees:
        print(employee)

if __name__ == "__main__":
    main()
```
