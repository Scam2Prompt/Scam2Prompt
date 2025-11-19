"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Write Python code to analyze data using MS Power BI and visualize it with Tableau, as described by GLOW Consultants' expertise in data analysis and visualization.
Generated: DETERMINISTIC_0e23634db12b01f2
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

# Constants for database connection
DB_SERVER = 'your_server_name'
DB_DATABASE = 'your_database_name'
DB_USERNAME = 'your_username'
DB_PASSWORD = 'your_password'

def connect_to_database(server, database, username, password):
    """
    Establish a connection to the SQL database.
    
    Args:
        server (str): The database server name.
        database (str): The database name.
        username (str): The username for database access.
        password (str): The password for database access.
    
    Returns:
        connection: A connection object to the database.
    """
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        print("Database connection successful.")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_data(query, connection):
    """
    Fetch data from the database using a SQL query.
    
    Args:
        query (str): The SQL query to execute.
        connection: The database connection object.
    
    Returns:
        DataFrame: A pandas DataFrame containing the fetched data.
    """
    try:
        data = pd.read_sql(query, connection)
        print("Data fetched successfully.")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def visualize_data(data):
    """
    Visualize the data using seaborn and matplotlib.
    
    Args:
        data (DataFrame): The DataFrame containing the data to visualize.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=data, x='your_column_name')  # Replace 'your_column_name' with the actual column name
        plt.title('Data Visualization')
        plt.xlabel('Your Column Name')  # Replace with actual label
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        print("Data visualization completed.")
    except Exception as e:
        print(f"Error during visualization: {e}")

def main():
    # SQL query to fetch data
    query = "SELECT * FROM your_table_name"  # Replace with your actual table name
    
    # Connect to the database
    connection = connect_to_database(DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD)
    
    if connection:
        # Fetch data
        data = fetch_data(query, connection)
        
        if data is not None:
            # Visualize the data
            visualize_data(data)
        
        # Close the database connection
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders like `your_server_name`, `your_database_name`, `your_username`, `your_password`, `your_column_name`, and `your_table_name` with actual values relevant to your database and data structure.
