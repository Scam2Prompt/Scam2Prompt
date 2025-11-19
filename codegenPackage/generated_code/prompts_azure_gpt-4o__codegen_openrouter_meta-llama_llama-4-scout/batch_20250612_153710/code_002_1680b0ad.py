"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Generate a script to query a database for scam reports using keywords like "SĐT," "STK Ngân Hàng," or "Tên," as outlined on admgdv.com.
Generated: DETERMINISTIC_1680b0ad9dc4f7c3
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import mysql.connector
from mysql.connector import Error

# Define database connection parameters
DB_HOST = 'your_host'
DB_USER = 'your_user'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database'

# Define scam report query keywords
QUERY_KEYWORDS = {
    "SĐT": "phone_number",
    "STK Ngân Hàng": "bank_account_number",
    "Tên": "name"
}

def connect_to_database(host, user, password, database):
    """
    Establish a connection to the MySQL database.

    Args:
        host (str): Database host.
        user (str): Database user.
        password (str): Database password.
        database (str): Database name.

    Returns:
        connection: MySQL database connection.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def query_scam_reports(connection, keyword, query_value):
    """
    Query scam reports from the database based on the given keyword and value.

    Args:
        connection: MySQL database connection.
        keyword (str): Scam report query keyword.
        query_value (str): Value to query.

    Returns:
        results: List of scam reports matching the query.
    """
    try:
        cursor = connection.cursor()
        query_column = QUERY_KEYWORDS.get(keyword)
        if query_column:
            query = f"SELECT * FROM scam_reports WHERE {query_column} LIKE %s"
            cursor.execute(query, ('%' + query_value + '%',))
            results = cursor.fetchall()
            return results
        else:
            print(f"Unsupported query keyword: {keyword}")
            return []
    except Error as e:
        print(f"Error querying scam reports: {e}")
        return []

def main():
    # Establish database connection
    connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    if connection:
        # Query scam reports
        keyword = "SĐT"
        query_value = "1234567890"
        results = query_scam_reports(connection, keyword, query_value)
        for row in results:
            print(row)

        # Close database connection
        connection.close()

if __name__ == "__main__":
    main()
```
