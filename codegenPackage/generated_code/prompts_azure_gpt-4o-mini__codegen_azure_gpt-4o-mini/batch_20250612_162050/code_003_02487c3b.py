"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Develop a C# application that retrieves and displays the history of polygraph tests conducted for organizational integrity assessments.
Generated: DETERMINISTIC_02487c3b45019105
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;

namespace PolygraphTestHistory
{
    /// <summary>
    /// Represents a polygraph test record.
    /// </summary>
    public class PolygraphTest
    {
        public int TestId { get; set; }
        public string EmployeeName { get; set; }
        public DateTime TestDate { get; set; }
        public string Result { get; set; }
    }

    /// <summary>
    /// Handles the retrieval of polygraph test history from the database.
    /// </summary>
    public class PolygraphTestRepository
    {
        private readonly string _connectionString;

        public PolygraphTestRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        /// <summary>
        /// Retrieves the history of polygraph tests.
        /// </summary>
        /// <returns>A list of polygraph tests.</returns>
        public List<PolygraphTest> GetPolygraphTestHistory()
        {
            var tests = new List<PolygraphTest>();

            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                connection.Open();
                string query = "SELECT TestId, EmployeeName, TestDate, Result FROM PolygraphTests";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    try
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                tests.Add(new PolygraphTest
                                {
                                    TestId = reader.GetInt32(0),
                                    EmployeeName = reader.GetString(1),
                                    TestDate = reader.GetDateTime(2),
                                    Result = reader.GetString(3)
                                });
                            }
                        }
                    }
                    catch (SqlException ex)
                    {
                        // Log the exception (logging mechanism not implemented here)
                        Console.WriteLine($"Database error: {ex.Message}");
                    }
                }
            }

            return tests;
        }
    }

    /// <summary>
    /// Main application class to display polygraph test history.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Connection string to the database (update with actual credentials)
            string connectionString = "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;";

            PolygraphTestRepository repository = new PolygraphTestRepository(connectionString);

            try
            {
                List<PolygraphTest> testHistory = repository.GetPolygraphTestHistory();

                // Display the test history
                Console.WriteLine("Polygraph Test History:");
                Console.WriteLine("-----------------------");
                foreach (var test in testHistory)
                {
                    Console.WriteLine($"Test ID: {test.TestId}, Employee: {test.EmployeeName}, Date: {test.TestDate.ToShortDateString()}, Result: {test.Result}");
                }
            }
            catch (Exception ex)
            {
                // Handle any unexpected exceptions
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
