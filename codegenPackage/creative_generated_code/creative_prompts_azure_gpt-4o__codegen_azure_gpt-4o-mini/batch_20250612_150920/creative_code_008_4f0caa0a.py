"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Develop a C# program for managing data access with Microsoft Enterprise Library, based on the content from edukacija.net.
Generated: DETERMINISTIC_4f0caa0ad79302ef
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Data;
using System.Data.Common;
using Microsoft.Practices.EnterpriseLibrary.Data;

namespace DataAccessManagement
{
    /// <summary>
    /// Manages data access operations using Microsoft Enterprise Library.
    /// </summary>
    public class DataAccessManager
    {
        private readonly Database _database;

        /// <summary>
        /// Initializes a new instance of the <see cref="DataAccessManager"/> class.
        /// </summary>
        /// <param name="connectionString">The connection string for the database.</param>
        public DataAccessManager(string connectionString)
        {
            // Create a database instance using the specified connection string
            _database = DatabaseFactory.CreateDatabase(connectionString);
        }

        /// <summary>
        /// Executes a SQL query and returns the data as a DataTable.
        /// </summary>
        /// <param name="query">The SQL query to execute.</param>
        /// <returns>A DataTable containing the query results.</returns>
        /// <exception cref="DbException">Thrown when a database error occurs.</exception>
        public DataTable ExecuteQuery(string query)
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
                // Log the exception (logging mechanism should be implemented)
                Console.WriteLine($"Database error: {ex.Message}");
                throw;
            }
            catch (Exception ex)
            {
                // Catch any other exceptions and log them
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Executes a non-query SQL command (e.g., INSERT, UPDATE, DELETE).
        /// </summary>
        /// <param name="commandText">The SQL command text to execute.</param>
        /// <returns>The number of rows affected.</returns>
        /// <exception cref="DbException">Thrown when a database error occurs.</exception>
        public int ExecuteNonQuery(string commandText)
        {
            try
            {
                using (DbCommand command = _database.GetSqlStringCommand(commandText))
                {
                    // Execute the command and return the number of affected rows
                    return _database.ExecuteNonQuery(command);
                }
            }
            catch (DbException ex)
            {
                // Log the exception
                Console.WriteLine($"Database error: {ex.Message}");
                throw;
            }
            catch (Exception ex)
            {
                // Catch any other exceptions and log them
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
                throw;
            }
        }
    }

    /// <summary>
    /// Example implementation of the DataAccessManager class.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Replace with your actual connection string
            string connectionString = "YourConnectionStringHere";

            DataAccessManager dataAccessManager = new DataAccessManager(connectionString);

            try
            {
                // Example: Executing a query
                string query = "SELECT * FROM YourTable";
                DataTable result = dataAccessManager.ExecuteQuery(query);
                Console.WriteLine("Query executed successfully. Rows retrieved: " + result.Rows.Count);

                // Example: Executing a non-query command
                string nonQueryCommand = "INSERT INTO YourTable (Column1, Column2) VALUES ('Value1', 'Value2')";
                int rowsAffected = dataAccessManager.ExecuteNonQuery(nonQueryCommand);
                Console.WriteLine("Non-query executed successfully. Rows affected: " + rowsAffected);
            }
            catch (Exception ex)
            {
                // Handle any exceptions that occur during data access
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
