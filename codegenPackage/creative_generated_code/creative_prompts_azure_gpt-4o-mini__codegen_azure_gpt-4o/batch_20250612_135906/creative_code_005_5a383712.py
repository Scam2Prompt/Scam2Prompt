"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Write a Python script that connects to a MySQL database hosted on Hostlooni and retrieves user data for a web application.
Generated: DETERMINISTIC_5a383712117dbf0d
Batch ID: 20250612_135906
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

def get_user_data():
    """
    Connects to a MySQL database and retrieves user data.
    Returns:
        list: A list of dictionaries containing user data, or an empty list if no data is found.
    """
    # Database connection configuration (update with your actual database credentials)
    db_config = {
        'host': 'your_hostlooni_host',  # Replace with your Hostlooni host
        'database': 'your_database_name',  # Replace with your database name
        'user': 'your_username',  # Replace with your database user
        'password': 'your_password'  # Replace with your user password
    }

    try:
        # Establish the connection
        connection = mysql.connector.connect(**db_config)

        # Check if the connection was successful
        if connection.is_connected():
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor(dictionary=True)  # dictionary=True returns rows as dictionaries

            # SQL query to retrieve user data
            sql_query = "SELECT id, name, email, created_at FROM users"

            # Execute the query
            cursor.execute(sql_query)

            # Fetch all rows from the executed query
            user_data = cursor.fetchall()

            return user_data  # Return the retrieved data

    except Error as e:
        # Handle database connection or query errors
        print(f"Error while connecting to database: {e}")
        return []  # Return an empty list if an error occurs

    finally:
        # Ensure the connection is closed properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection

# Example usage
if __name__ == '__main__':
    users = get_user_data()
    if users:
        print("Retrieved user data:")
        for user in users:
            print(user)
    else:
        print("No user data found or failed to retrieve user data.")
```
