"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindarch.cl
Prompt: Generate an ASP.NET code snippet to test database connectivity on a Windows hosting server, optimized for Chile-based hosting providers.
Generated: DETERMINISTIC_9b1e990485d007bd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Data.SqlClient;

public class DatabaseConnectivityTest
{
    public static void Main()
    {
        // Connection string example. Update with actual credentials and database details.
        // Ensure the connection string is optimized for your hosting provider's configuration.
        string connectionString = "Server=yourserver.hostname.cl;Database=yourdatabase;User Id=yourusername;Password=yourpassword;";

        TestDatabaseConnection(connectionString);
    }

    /// <summary>
    /// Tests the database connectivity using the provided connection string.
    /// </summary>
    /// <param name="connectionString">The connection string to the database.</param>
    public static void TestDatabaseConnection(string connectionString)
    {
        // Ensure proper error handling for production readiness.
        try
        {
            // Create a SqlConnection object.
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                Console.WriteLine("Attempting to connect to the database...");

                // Open the connection.
                connection.Open();

                // If successful, print a success message.
                Console.WriteLine("Database connection successful!");
            }
        }
        catch (SqlException sqlEx)
        {
            // Handle SQL exceptions (e.g., connection issues, authentication errors).
            Console.WriteLine($"SQL Error: {sqlEx.Message}");
        }
        catch (Exception ex)
        {
            // Handle general exceptions.
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
        finally
        {
            // Any cleanup code can go here if necessary.
            Console.WriteLine("Database connectivity test completed.");
        }
    }
}
```
