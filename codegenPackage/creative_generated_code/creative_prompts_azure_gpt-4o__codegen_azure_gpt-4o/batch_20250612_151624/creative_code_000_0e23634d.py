"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Write Python code to analyze data using MS Power BI and visualize it with Tableau, as described by GLOW Consultants' expertise in data analysis and visualization.
Generated: DETERMINISTIC_0e23634db12b01f2
Batch ID: 20250612_151624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-tableau-server.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import pyodbc
from tableau_api_lib import TableauServerConnection, TableauWorkbook, TableauProject

# Define MS Power BI connection function
def connect_to_power_bi():
    """
    Establishes a connection to MS Power BI data source using pyodbc.
    Ensure the correct connection string is provided.
    """
    try:
        # Example connection string (update as per your MS Power BI setup)
        connection_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=your_server_name;"
            "Database=your_database_name;"
            "Trusted_Connection=yes;"
        )
        connection = pyodbc.connect(connection_string)
        print("Successfully connected to Power BI.")
        return connection
    except Exception as e:
        print(f"Error connecting to Power BI: {e}")
        raise

# Fetch data from Power BI
def fetch_data_from_power_bi(connection, query):
    """
    Fetches data from the Power BI data source using SQL query.
    Args:
        connection: pyodbc connection object
        query: SQL query string to execute
    Returns:
        DataFrame containing the fetched data
    """
    try:
        # Execute query and fetch data into a Pandas DataFrame
        df = pd.read_sql_query(query, connection)
        print("Data successfully fetched from Power BI.")
        return df
    except Exception as e:
        print(f"Error fetching data from Power BI: {e}")
        raise

# Visualize data using Tableau
def visualize_data_with_tableau(dataframe, tableau_config):
    """
    Visualizes data using Tableau by creating a workbook and publishing it to a specified server.
    Args:
        dataframe: Pandas DataFrame containing data to visualize
        tableau_config: Dictionary containing Tableau server configuration details
    """
    try:
        # Establish connection to Tableau Server
        connection = TableauServerConnection(config_json=tableau_config)
        connection.sign_in()
        
        # Create a Tableau workbook from DataFrame
        workbook = TableauWorkbook(dataframe=dataframe, workbook_name="DataAnalysisWorkbook")
        
        # Publish workbook to the specified project
        tableau_project = TableauProject(connection, project_name="Data Analysis")
        tableau_project.upload_workbook(workbook)
        
        print("Data successfully visualized and published to Tableau.")
    except Exception as e:
        print(f"Error visualizing data with Tableau: {e}")
        raise
    finally:
        connection.sign_out()

# Main function to execute the workflow
def main():
    """
    Main function to connect to Power BI, fetch data, and visualize it using Tableau.
    """
    try:
        # Connect to Power BI
        power_bi_connection = connect_to_power_bi()
        
        # Define SQL query to fetch data
        sql_query = "SELECT * FROM your_table_name"
        
        # Fetch data
        data = fetch_data_from_power_bi(power_bi_connection, sql_query)
        
        # Define Tableau configuration (replace with actual values)
        tableau_config = {
            "server": "https://your-tableau-server.com",
            "username": "your_username",
            "password": "your_password",
            "site_name": "your_site_name",
            "site_id": "your_site_id"
        }
        
        # Visualize data using Tableau
        visualize_data_with_tableau(data, tableau_config)
    except Exception as e:
        print(f"An error occurred during the workflow: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
