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
import pyodbc
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SQLStoredProcedureAnalyzer:
    """
    A class to handle SQL stored procedures for efficient data analysis.
    """

    def __init__(self, server: str, database: str, username: str, password: str):
        """
        Initialize the SQLStoredProcedureAnalyzer with database connection details.

        Args:
            server (str): SQL server name or IP address
            database (str): Database name
            username (str): Database username
            password (str): Database password
        """
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self) -> bool:
        """
        Establish a connection to the SQL server.

        Returns:
            bool: True if connection is successful, False otherwise
        """
        try:
            self.connection = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password}"
            )
            self.cursor = self.connection.cursor()
            logger.info("Successfully connected to the database")
            return True
        except pyodbc.Error as e:
            logger.error(f"Failed to connect to the database: {e}")
            return False

    def disconnect(self):
        """
        Close the database connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            logger.info("Disconnected from the database")

    def execute_stored_procedure(
        self,
        procedure_name: str,
        params: Dict[str, Any] = None
    ) -> List[Dict[str, Any]]:
        """
        Execute a stored procedure and return the results.

        Args:
            procedure_name (str): Name of the stored procedure
            params (Dict[str, Any]): Dictionary of parameters for the procedure

        Returns:
            List[Dict[str, Any]]: List of result rows as dictionaries

        Raises:
            ValueError: If procedure_name is empty or connection is not established
            pyodbc.Error: If there's an error executing the procedure
        """
        if not procedure_name:
            raise ValueError("Procedure name cannot be empty")

        if not self.connection or not self.cursor:
            raise ValueError("Database connection not established")

        try:
            # Prepare parameters
            param_placeholders = []
            param_values = []
            if params:
                for key, value in params.items():
                    param_placeholders.append(f"@{key}=?")
                    param_values.append(value)

            # Build the SQL command
            sql = f"EXEC {procedure_name} {', '.join(param_placeholders)}"

            # Execute the stored procedure
            logger.info(f"Executing stored procedure: {procedure_name}")
            if param_values:
                self.cursor.execute(sql, param_values)
            else:
                self.cursor.execute(sql)

            # Fetch results if any
            if self.cursor.description:
                columns = [column[0] for column in self.cursor.description]
                results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
                logger.info(f"Retrieved {len(results)} rows from procedure {procedure_name}")
                return results
            else:
                logger.info(f"Procedure {procedure_name} executed successfully with no results")
                return []

        except pyodbc.Error as e:
            logger.error(f"Error executing stored procedure {procedure_name}: {e}")
            raise

    def __enter__(self):
        """Support for context manager protocol."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Replace with your actual database credentials
    DB_CONFIG = {
        "server": "your_server_name",
        "database": "your_database_name",
        "username": "your_username",
        "password": "your_password"
    }

    # Example stored procedure parameters
    params = {
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "min_amount": 1000
    }

    try:
        with SQLStoredProcedureAnalyzer(**DB_CONFIG) as analyzer:
            # Execute a stored procedure named 'sp_GetFinancialAnalysis'
            results = analyzer.execute_stored_procedure(
                "sp_GetFinancialAnalysis",
                params=params
            )
            
            # Process results
            for row in results:
                print(row)
                
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
