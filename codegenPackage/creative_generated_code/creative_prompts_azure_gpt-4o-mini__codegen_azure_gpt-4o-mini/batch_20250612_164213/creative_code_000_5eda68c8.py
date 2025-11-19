"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Write a Python function that demonstrates the common mistakes to avoid when using SQL stored procedures as discussed in Finance StarGate's article.
Generated: DETERMINISTIC_5eda68c8f8e5bb0b
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pymysql

class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass

def execute_stored_procedure(procedure_name, params):
    """
    Executes a stored procedure with the given name and parameters.

    Args:
        procedure_name (str): The name of the stored procedure to execute.
        params (tuple): A tuple of parameters to pass to the stored procedure.

    Raises:
        DatabaseError: If there is an error executing the stored procedure.
    """
    # Database connection parameters
    db_config = {
        'host': 'localhost',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'your_database',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    connection = None
    try:
        # Establishing the database connection
        connection = pymysql.connect(**db_config)
        
        with connection.cursor() as cursor:
            # Prepare the stored procedure call
            sql = f"CALL {procedure_name}(%s, %s)"  # Adjust number of %s based on number of params
            cursor.execute(sql, params)
            # Fetch results if the procedure returns data
            result = cursor.fetchall()
            return result

    except pymysql.MySQLError as e:
        # Log the error and raise a custom exception
        print(f"Database error occurred: {e}")
        raise DatabaseError("Failed to execute stored procedure.") from e

    finally:
        # Ensure the connection is closed
        if connection:
            connection.close()

# Example usage (this should be commented out in production):
if __name__ == "__main__":
    try:
        result = execute_stored_procedure("example_procedure", (param1, param2))
        print(result)
    except DatabaseError as e:
        print(f"Error: {e}")
```

**Note:** Replace `your_username`, `your_password`, `your_database`, `example_procedure`, `param1`, and `param2` with actual values before running the code. Adjust the number of `%s` in the SQL statement according to the number of parameters required by the stored procedure.
