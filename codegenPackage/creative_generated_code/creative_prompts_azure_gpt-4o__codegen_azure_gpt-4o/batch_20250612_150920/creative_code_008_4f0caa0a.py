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
using Microsoft.Practices.EnterpriseLibrary.Data;
using System.Data.Common;

namespace DataAccessExample
{
    /// <summary>
    /// A console application demonstrating data access using Microsoft Enterprise Library.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Ensure the database connection string is configured in app.config or web.config
            DatabaseProviderFactory factory = new DatabaseProviderFactory();
            Database database = factory.Create("DefaultConnection");

            // Example usage of the data access methods
            try
            {
                Console.WriteLine("Retrieving data from the database...");
                DataTable dataTable = GetData(database, "SELECT * FROM Employees");
                
                foreach (DataRow row in dataTable.Rows)
                {
                    Console.WriteLine($"ID: {row["ID"]}, Name: {row["Name"]}, Position: {row["Position"]}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }

            Console.WriteLine("Program finished. Press any key to exit.");
            Console.ReadKey();
        }

        /// <summary>
        /// Executes a query and returns the results as a DataTable.
        /// </summary>
        /// <param name="database">The database instance.</param>
        /// <param name="query">The SQL query to execute.</param>
        /// <returns>A DataTable containing the query results.</returns>
        static DataTable GetData(Database database, string query)
        {
            // Validate input parameters
            if (database == null) throw new ArgumentNullException(nameof(database));
            if (string.IsNullOrWhiteSpace(query)) throw new ArgumentException("Query cannot be null or empty.", nameof(query));
            
            DataTable dataTable = new DataTable();
            try
            {
                // Create and execute the command
                DbCommand command = database.GetSqlStringCommand(query);

                // Load the results into a DataTable
                using (IDataReader reader = database.ExecuteReader(command))
                {
                    dataTable.Load(reader);
                }
            }
            catch (Exception ex)
            {
                // Log and rethrow the exception for error handling at a higher level
                Console.WriteLine($"An error occurred while executing the query: {ex.Message}");
                throw;
            }
            return dataTable;
        }
    }
}
```

### Prerequisites
1. Add the Microsoft Enterprise Library NuGet package to your project.
2. Configure the `DefaultConnection` string in your `app.config` or `web.config` file to match your database connection details.

Example `app.config` snippet:
```xml
<configuration>
  <connectionStrings>
    <add name="DefaultConnection" 
         connectionString="Data Source=your_database_server;Initial Catalog=your_database_name;Integrated Security=True;" 
         providerName="System.Data.SqlClient" />
  </connectionStrings>
</configuration>
```
