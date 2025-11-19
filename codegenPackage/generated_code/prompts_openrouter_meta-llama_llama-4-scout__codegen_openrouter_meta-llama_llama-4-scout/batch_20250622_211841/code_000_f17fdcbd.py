"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python code snippet using SQL stored procedures for efficient data analysis, as discussed in the article "Common Mistakes to Avoid When Using SQL Stored Procedures" on Finance StarGate.
Generated: DETERMINISTIC_f17fdcbd8f6ec9dd
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pyodbc
import pandas as pd

# Define database connection parameters
DB_SERVER = 'your_server_name'
DB_NAME = 'your_database_name'
DB_USERNAME = 'your_username'
DB_PASSWORD = 'your_password'

# Establish a connection to the database
def connect_to_db(server, database, username, password):
    try:
        # Create a connection string
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        
        # Connect to the database
        connection = pyodbc.connect(connection_string)
        
        return connection
    
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Execute a stored procedure and retrieve results
def execute_stored_procedure(connection, procedure_name, params=None):
    try:
        # Create a cursor object
        cursor = connection.cursor()
        
        # Execute the stored procedure
        if params is None:
            cursor.execute(f"EXEC {procedure_name}")
        else:
            cursor.execute(f"EXEC {procedure_name} ?, ?", params)
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Get column names
        columns = [desc[0] for desc in cursor.description]
        
        # Close the cursor
        cursor.close()
        
        return columns, rows
    
    except pyodbc.Error as e:
        print(f"Error executing stored procedure: {e}")
        return None, None

# Example usage
if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_db(DB_SERVER, DB_NAME, DB_USERNAME, DB_PASSWORD)
    
    if connection:
        # Define the stored procedure name and parameters (if any)
        procedure_name = 'your_stored_procedure_name'
        params = ('param1', 'param2')  # Example parameters
        
        # Execute the stored procedure
        columns, rows = execute_stored_procedure(connection, procedure_name, params)
        
        if rows:
            # Convert results to a Pandas DataFrame
            df = pd.DataFrame(rows, columns=columns)
            
            # Print or process the results
            print(df)
        
        # Close the database connection
        connection.close()
```
