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
using Microsoft.Practices.EnterpriseLibrary.Data;
using Microsoft.Practices.EnterpriseLibrary.Data.Sql;

namespace DataAccessManager
{
    /// <summary>
    /// Data access manager class using Microsoft Enterprise Library.
    /// </summary>
    public class DataAccessManager
    {
        private readonly Database _database;

        /// <summary>
        /// Initializes a new instance of the <see cref="DataAccessManager"/> class.
        /// </summary>
        /// <param name="connectionString">Connection string to the database.</param>
        public DataAccessManager(string connectionString)
        {
            _database = new SqlDatabase(connectionString);
        }

        /// <summary>
        /// Executes a non-query SQL command.
        /// </summary>
        /// <param name="sqlCommand">SQL command to execute.</param>
        /// <returns>The number of rows affected.</returns>
        public int ExecuteNonQuery(string sqlCommand)
        {
            try
            {
                using (var command = _database.GetSqlStringCommand(sqlCommand))
                {
                    return _database.ExecuteNonQuery(command);
                }
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"An error occurred: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Executes a query SQL command and returns a <see cref="DataSet"/>.
        /// </summary>
        /// <param name="sqlCommand">SQL command to execute.</param>
        /// <returns>A <see cref="DataSet"/> containing the query results.</returns>
        public DataSet ExecuteQuery(string sqlCommand)
        {
            try
            {
                using (var command = _database.GetSqlStringCommand(sqlCommand))
                {
                    return _database.ExecuteDataSet(command);
                }
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"An error occurred: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Executes a scalar SQL command and returns the result.
        /// </summary>
        /// <param name="sqlCommand">SQL command to execute.</param>
        /// <returns>The result of the scalar query.</returns>
        public object ExecuteScalar(string sqlCommand)
        {
            try
            {
                using (var command = _database.GetSqlStringCommand(sqlCommand))
                {
                    return _database.ExecuteScalar(command);
                }
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"An error occurred: {ex.Message}");
                throw;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Replace with your connection string
            string connectionString = "Data Source=<your_server>;Initial Catalog=<your_database>;Integrated Security=True";

            var dataAccessManager = new DataAccessManager(connectionString);

            string sqlCommand = "SELECT * FROM <your_table>";

            try
            {
                DataSet dataSet = dataAccessManager.ExecuteQuery(sqlCommand);

                foreach (DataRow row in dataSet.Tables[0].Rows)
                {
                    foreach (DataColumn column in dataSet.Tables[0].Columns)
                    {
                        Console.Write(row[column] + " ");
                    }
                    Console.WriteLine();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
