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

// Namespace for the application
namespace PolygraphTestHistory
{
    // Main program entry point
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Retrieve and display polygraph test history
                List<PolygraphTest> tests = RetrievePolygraphTestHistory();
                DisplayPolygraphTestHistory(tests);
            }
            catch (Exception ex)
            {
                // Log and display error message
                Console.WriteLine("An error occurred: " + ex.Message);
            }
        }

        /// <summary>
        /// Retrieves the history of polygraph tests from the database.
        /// </summary>
        /// <returns>A list of PolygraphTest objects.</returns>
        /// <exception cref="SqlException">Thrown when there's an issue with the database query.</exception>
        private static List<PolygraphTest> RetrievePolygraphTestHistory()
        {
            // Connection string for the database
            string connectionString = "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;";
            List<PolygraphTest> tests = new List<PolygraphTest>();

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                // SQL query to retrieve polygraph test history
                string query = "SELECT TestId, EmployeeId, TestDate, Result FROM PolygraphTests ORDER BY TestDate DESC";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        // Read data from the database
                        while (reader.Read())
                        {
                            PolygraphTest test = new PolygraphTest
                            {
                                TestId = reader.GetInt32(0),
                                EmployeeId = reader.GetString(1),
                                TestDate = reader.GetDateTime(2),
                                Result = reader.GetString(3)
                            };
                            tests.Add(test);
                        }
                    }
                }
            }

            return tests;
        }

        /// <summary>
        /// Displays the history of polygraph tests in the console.
        /// </summary>
        /// <param name="tests">A list of PolygraphTest objects.</param>
        private static void DisplayPolygraphTestHistory(List<PolygraphTest> tests)
        {
            Console.WriteLine("Polygraph Test History:");
            Console.WriteLine("-----------------------------------");
            Console.WriteLine("{0,-10} {1,-15} {2,-20} {3,-10}", "Test ID", "Employee ID", "Test Date", "Result");
            Console.WriteLine("-----------------------------------");

            // Display each test record
            foreach (var test in tests)
            {
                Console.WriteLine("{0,-10} {1,-15} {2,-20} {3,-10}", test.TestId, test.EmployeeId, test.TestDate.ToString("yyyy-MM-dd"), test.Result);
            }
        }
    }

    /// <summary>
    /// Represents a polygraph test record.
    /// </summary>
    public class PolygraphTest
    {
        public int TestId { get; set; }
        public string EmployeeId { get; set; }
        public DateTime TestDate { get; set; }
        public string Result { get; set; }
    }
}
```

Ensure to replace `your_server`, `your_database`, `your_user`, and `your_password` with actual database connection details for the application to run correctly.
