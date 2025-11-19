"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Develop a C# application that retrieves and displays the history of polygraph tests conducted for organizational integrity assessments.
Generated: DETERMINISTIC_02487c3b45019105
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace PolygraphTestHistoryApp
{
    /// <summary>
    /// Represents the data model for a polygraph test record.
    /// </summary>
    public class PolygraphTest
    {
        public int TestId { get; set; }
        public string EmployeeName { get; set; }
        public DateTime TestDate { get; set; }
        public string Result { get; set; }
    }

    /// <summary>
    /// Handles data access related to polygraph tests.
    /// </summary>
    public class PolygraphTestRepository
    {
        private readonly string _connectionString;

        public PolygraphTestRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        /// <summary>
        /// Retrieves the list of polygraph test history from the database.
        /// </summary>
        /// <returns>List of polygraph tests</returns>
        public List<PolygraphTest> GetPolygraphTests()
        {
            var polygraphTests = new List<PolygraphTest>();

            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();

                    string query = "SELECT TestId, EmployeeName, TestDate, Result FROM PolygraphTests";

                    using (var command = new SqlCommand(query, connection))
                    using (var reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            polygraphTests.Add(new PolygraphTest
                            {
                                TestId = reader.GetInt32(0),
                                EmployeeName = reader.GetString(1),
                                TestDate = reader.GetDateTime(2),
                                Result = reader.GetString(3)
                            });
                        }
                    }
                }
            }
            catch (SqlException ex)
            {
                // Log error message for debugging (not shown in this example for simplicity)
                Console.WriteLine($"Database error: {ex.Message}");
            }
            catch (Exception ex)
            {
                // Log generic error
                Console.WriteLine($"Unexpected error: {ex.Message}");
            }

            return polygraphTests;
        }
    }

    /// <summary>
    /// Main application class to display polygraph test history.
    /// </summary>
    public class Program
    {
        public static void Main(string[] args)
        {
            // Replace with your actual database connection string
            string connectionString = "YourDatabaseConnectionStringHere";

            var repository = new PolygraphTestRepository(connectionString);

            Console.WriteLine("Polygraph Test History:");
            Console.WriteLine(new string('-', 40));

            try
            {
                var tests = repository.GetPolygraphTests();

                if (tests.Count == 0)
                {
                    Console.WriteLine("No polygraph tests found.");
                }
                else
                {
                    foreach (var test in tests)
                    {
                        Console.WriteLine($"Test ID: {test.TestId}");
                        Console.WriteLine($"Employee Name: {test.EmployeeName}");
                        Console.WriteLine($"Test Date: {test.TestDate.ToShortDateString()}");
                        Console.WriteLine($"Result: {test.Result}");
                        Console.WriteLine(new string('-', 40));
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred while retrieving data: {ex.Message}");
            }

            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
    }
}
```
