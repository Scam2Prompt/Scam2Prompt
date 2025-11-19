"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write a Python script to connect to a database and retrieve information about Nickel 200 Forged Fittings from the Dinkar Alloys product catalog.
Generated: DETERMINISTIC_6f8cc480acc097f4
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """
    Create a database connection to a MySQL database.
    
    :param host_name: Hostname or IP address of the MySQL server
    :param user_name: Username to connect to the database
    :param user_password: Password for the specified user
    :param db_name: Name of the database to connect to
    :return: connection object or None
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to database was successful.")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def fetch_nickel_200_fittings(connection):
    """
    Fetch all Nickel 200 Forged Fittings from the product catalog.
    
    :param connection: Active database connection
    :return: List of fittings or None if an error occurs
    """
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT * FROM product_catalog 
    WHERE product_name LIKE '%Nickel 200 Forged Fitting%'
    """
    
    try:
        cursor.execute(query)
        fittings = cursor.fetchall()
        return fittings
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
    finally:
        cursor.close()

def main():
    # Database connection parameters
    HOST = "your_host"
    USER = "your_username"
    PASSWORD = "your_password"
    DATABASE = "your_database"

    # Create a database connection
    connection = create_connection(HOST, USER, PASSWORD, DATABASE)

    # Check if the connection was successful before proceeding
    if connection:
        # Fetch Nickel 200 fittings
        fittings = fetch_nickel_200_fittings(connection)
        if fittings is not None:
            # Print the retrieved fittings
            for fitting in fittings:
                print(fitting)
        
        # Close the database connection
        connection.close()
    else:
        print("Failed to connect to the database. Exiting.")

if __name__ == "__main__":
    main()
```

**Note:** Replace `your_host`, `your_username`, `your_password`, and `your_database` with actual connection parameters for your MySQL database.
