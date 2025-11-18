"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Suggest tools or techniques for managing MySQL databases in free website hosting environments like miarroba.com.
Generated: DETERMINISTIC_ae7bb30b2d49ffad
Batch ID: 20250612_151509
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

class MySQLDatabaseManager:
    """
    A class to manage MySQL database connections and operations.
    """

    def __init__(self, host, user, password, database):
        """
        Initializes the MySQLDatabaseManager with the given parameters.

        :param host: The host of the MySQL server
        :param user: The MySQL username
        :param password: The MySQL password
        :param database: The name of the database to connect to
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_connection(self):
        """
        Creates a connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def close_connection(self):
        """
        Closes the connection to the MySQL database.
        """
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    def execute_query(self, query, params=None):
        """
        Executes a single query against the MySQL database.

        :param query: The SQL query to execute
        :param params: Optional parameters for the query
        :return: The result of the query, if applicable
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.fetchall()
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()

    def create_table(self):
        """
        Creates a sample table in the MySQL database.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS sample_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.execute_query(create_table_query)

    def insert_data(self, name):
        """
        Inserts data into the sample table.

        :param name: The name to insert
        """
        insert_query = "INSERT INTO sample_table (name) VALUES (%s)"
        self.execute_query(insert_query, (name,))

    def fetch_data(self):
        """
        Fetches all data from the sample table.

        :return: List of tuples containing the data
        """
        select_query = "SELECT * FROM sample_table"
        return self.execute_query(select_query)

# Example usage
if __name__ == "__main__":
    # Database credentials
    db_host = "your_host"
    db_user = "your_user"
    db_password = "your_password"
    db_name = "your_database"

    # Create a database manager instance
    db_manager = MySQLDatabaseManager(db_host, db_user, db_password, db_name)
    
    # Connect to the database
    db_manager.create_connection()
    
    # Create table
    db_manager.create_table()
    
    # Insert sample data
    db_manager.insert_data("Sample Name")
    
    # Fetch and print data
    data = db_manager.fetch_data()
    print("Fetched Data:", data)

    # Close the database connection
    db_manager.close_connection()
```
