"""
Generated Code Metadata:
========================
Original URL: https://blindarch.cl
Prompt: Generate an ASP.NET code snippet to test database connectivity on a Windows hosting server, optimized for Chile-based hosting providers.
Generated: DETERMINISTIC_9b1e990485d007bd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Data.SqlClient;
using System.Data;

namespace DatabaseConnectivityTest
{
    class Program
    {
        static void Main(string[] args)
        {
            // Database connection settings
            string serverName = "your_server_name"; // e.g., "localhost" or "your_server_ip"
            string databaseName = "your_database_name";
            string username = "your_database_username";
            string password = "your_database_password";

            // Connection string
            string connectionString = $"Data Source={serverName};Initial Catalog={databaseName};User ID={username};Password={password};";

            try
            {
                // Test database connectivity
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    Console.WriteLine("Database connection established successfully.");

                    // Execute a simple query to test connectivity
                    string query = "SELECT @@VERSION";
                    using (SqlCommand command = new SqlCommand(query, connection))
                    {
                        object result = command.ExecuteScalar();
                        Console.WriteLine($"Database server version: {result}");
                    }
                }
            }
            catch (SqlException ex)
            {
                Console.WriteLine($"Error connecting to database: {ex.Message}");
                // Handle specific error codes for Chile-based hosting providers
                if (ex.Number == 18456) // Login failed
                {
                    Console.WriteLine("Verify your database credentials.");
                }
                else if (ex.Number == 10060) // Timeout expired
                {
                    Console.WriteLine("Check your server name and firewall settings.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
            finally
            {
                Console.ReadLine(); // Pause before exiting
            }
        }
    }
}
```

**app.config (if using .NET Framework) or appsettings.json (if using .NET Core)**
```xml
<!-- .NET Framework (app.config) -->
<configuration>
  <connectionStrings>
    <add name="DatabaseConnection" connectionString="Data Source=your_server_name;Initial Catalog=your_database_name;User ID=your_database_username;Password=your_database_password;" providerName="System.Data.SqlClient" />
  </connectionStrings>
</configuration>
```

```json
// .NET Core (appsettings.json)
{
  "ConnectionStrings": {
    "DatabaseConnection": "Data Source=your_server_name;Initial Catalog=your_database_name;User ID=your_database_username;Password=your_database_password;"
  }
}
```

**Note**: Make sure to replace placeholders (`your_server_name`, `your_database_name`, `your_database_username`, `your_database_password`) with actual values for your database. 

Also, ensure that the `System.Data.SqlClient` NuGet package is installed in your project:

```
Install-Package System.Data.SqlClient
```
