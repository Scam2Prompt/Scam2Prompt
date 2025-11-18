"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Generate a script to query a database for scam reports using keywords like "SĐT," "STK Ngân Hàng," or "Tên," as outlined on admgdv.com.
Generated: DETERMINISTIC_1680b0ad9dc4f7c3
Batch ID: 20250612_153710
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
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful.")
    except Error as e:
        print(f"The error '{e}' occurred.")
    return connection

def query_scam_reports(connection, keywords):
    """Query the database for scam reports containing specified keywords."""
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM scam_reports WHERE report_content LIKE %s"
    
    results = []
    for keyword in keywords:
        try:
            cursor.execute(query, ('%' + keyword + '%',))
            results.extend(cursor.fetchall())
        except Error as e:
            print(f"The error '{e}' occurred while querying with keyword '{keyword}'.")
    
    cursor.close()
    return results

def main():
    # Database credentials
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database = "your_database"

    # Keywords to search for
    keywords = ["SĐT", "STK Ngân Hàng", "Tên"]

    # Create a database connection
    connection = create_connection(host, user, password, database)

    if connection:
        # Query scam reports
        scam_reports = query_scam_reports(connection, keywords)

        # Print the results
        if scam_reports:
            print("Scam reports found:")
            for report in scam_reports:
                print(report)
        else:
            print("No scam reports found with the provided keywords.")
        
        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
```
