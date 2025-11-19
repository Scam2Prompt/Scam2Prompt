"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Develop a C# program for managing data access with Microsoft Enterprise Library, based on the content from edukacija.net.
Generated: DETERMINISTIC_4f0caa0ad79302ef
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Data;
using System.Data.Common;
using Microsoft.Practices.EnterpriseLibrary.Data;

namespace DataAccessExample
{
    /// <summary>
    /// This class provides methods to manage data access using Microsoft Enterprise Library.
    /// </summary>
    public class DataAccessManager
    {
        private readonly Database _database;

        /// <summary>
        /// Initializes a new instance of the <see cref="DataAccessManager"/> class.
        /// </summary>
        /// <param name="connectionString">The connection string to the database.</param>
        public DataAccessManager(string connectionString)
        {
            // Create a database instance using the provided connection string
            _database = DatabaseFactory.CreateDatabase(connectionString);
        }

        /// <summary>
        /// Retrieves a data table from the database based on the provided query.
        /// </summary>
        /// <param name="query">The SQL query to execute.</param>
        /// <returns>A DataTable containing the results of the query.</returns>
        /// <exception cref="DbException">Thrown when a database error occurs.</exception>
        public DataTable GetDataTable(string query)
        {
            try
            {
                // Create a command to execute the query
                using (DbCommand command = _database.GetSqlStringCommand(query))
                {
                    // Execute the command and fill a DataTable with the results
                    DataSet dataSet = _database.ExecuteDataSet(command);
                    return dataSet.Tables[0];
                }
            }
            catch (DbException ex)
            {
                // Log the exception (logging mechanism not implemented here)
                Console.WriteLine($"Database error: {ex.Message}");
                throw; // Rethrow the exception for further handling
            }
            catch (Exception ex)
            {
                // Log the exception (logging mechanism not implemented here)
                Console.WriteLine($"An error occurred: {ex.Message}");
                throw; // Rethrow the exception for further handling
            }
        }

        /// <summary>
        /// Executes a non-query command (INSERT, UPDATE, DELETE) against the database.
        /// </summary>
        /// <param name="commandText">The SQL command to execute.</param>
        /// <returns>The number of rows affected.</returns>
        /// <exception cref="DbException">Thrown when a database error occurs.</exception>
        public int ExecuteNonQuery(string commandText)
        {
            try
            {
                // Create a command to execute the non-query
                using (DbCommand command = _database.GetSqlStringCommand(commandText))
                {
                    // Execute the command and return the number of affected rows
                    return _database.ExecuteNonQuery(command);
                }
            }
            catch (DbException ex)
            {
                // Log the exception (logging mechanism not implemented here)
                Console.WriteLine($"Database error: {ex.Message}");
                throw; // Rethrow the exception for further handling
            }
            catch (Exception ex)
            {
                // Log the exception (logging mechanism not implemented here)
                Console.WriteLine($"An error occurred: {ex.Message}");
                throw; // Rethrow the exception for further handling
            }
        }
    }

    /// <summary>
    /// The main program to demonstrate the usage of DataAccessManager.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Define the connection string (update with your actual connection string)
            string connectionString = "YourConnectionStringHere";

            // Create an instance of DataAccessManager
            DataAccessManager dataAccessManager = new DataAccessManager(connectionString);

            // Example: Retrieve data from the database
            try
            {
                DataTable resultTable = dataAccessManager.GetDataTable("SELECT * FROM YourTableName");
                foreach (DataRow row in resultTable.Rows)
                {
                    Console.WriteLine(string.Join(", ", row.ItemArray));
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error retrieving data: {ex.Message}");
            }

            // Example: Execute a non-query command
            try
            {
                int rowsAffected = dataAccessManager.ExecuteNonQuery("INSERT INTO YourTableName (Column1, Column2) VALUES ('Value1', 'Value2')");
                Console.WriteLine($"{rowsAffected} rows inserted.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error executing non-query: {ex.Message}");
            }
        }
    }
}
```
