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
using Microsoft.AspNetCore.Mvc;

namespace DatabaseConnectivityTest.Controllers
{
    /// <summary>
    /// Controller to handle database connectivity tests.
    /// </summary>
    [Route("api/[controller]")]
    [ApiController]
    public class DatabaseTestController : ControllerBase
    {
        private readonly string _connectionString;

        /// <summary>
        /// Constructor to initialize the connection string.
        /// Note: Replace with your actual connection string.
        /// </summary>
        public DatabaseTestController()
        {
            // Connection string to the SQL Server database
            _connectionString = "Server=your_server;Database=your_database;User Id=your_username;Password=your_password;";
        }

        /// <summary>
        /// Tests the connectivity to the database.
        /// </summary>
        /// <returns>Returns a message indicating the result of the connection test.</returns>
        [HttpGet("test-connection")]
        public IActionResult TestConnection()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    // Open the connection
                    connection.Open();
                    // If we reach this point, the connection is successful
                    return Ok("Database connection successful.");
                }
            }
            catch (SqlException sqlEx)
            {
                // Log the SQL exception (consider using a logging framework)
                return StatusCode(500, $"Database connection failed: {sqlEx.Message}");
            }
            catch (Exception ex)
            {
                // Log the general exception (consider using a logging framework)
                return StatusCode(500, $"An error occurred: {ex.Message}");
            }
        }
    }
}
```
