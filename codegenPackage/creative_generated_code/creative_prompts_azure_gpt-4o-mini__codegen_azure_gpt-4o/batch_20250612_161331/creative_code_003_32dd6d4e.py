"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Develop a C# application that connects to a database and displays the inventory of seamless steel pipes, including their dimensions and applications.
Generated: DETERMINISTIC_32dd6d4efa8e9332
Batch ID: 20250612_161331
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

namespace SteelPipeInventoryApp
{
    class Program
    {
        // Connection string to the database (update with your credentials and server details)
        private const string ConnectionString = "Server=YOUR_SERVER_NAME;Database=YOUR_DATABASE_NAME;User Id=YOUR_USERNAME;Password=YOUR_PASSWORD;";

        static void Main(string[] args)
        {
            try
            {
                // Display application information
                Console.WriteLine("Seamless Steel Pipe Inventory");
                Console.WriteLine("=============================");
                Console.WriteLine();

                // Fetch and display inventory
                DisplayInventory();
            }
            catch (Exception ex)
            {
                // Handle any unexpected errors
                Console.WriteLine("An error occurred: " + ex.Message);
            }
        }

        /// <summary>
        /// Fetches and displays the inventory of seamless steel pipes from the database.
        /// </summary>
        private static void DisplayInventory()
        {
            // SQL query to fetch inventory data
            string query = "SELECT PipeID, Dimensions, Application FROM SteelPipeInventory";

            // Establish database connection
            using (SqlConnection connection = new SqlConnection(ConnectionString))
            {
                try
                {
                    connection.Open();
                    Console.WriteLine("Connected to the database successfully.");
                    Console.WriteLine();

                    // Execute query
                    using (SqlCommand command = new SqlCommand(query, connection))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            // Check if any data exists
                            if (!reader.HasRows)
                            {
                                Console.WriteLine("No inventory data found.");
                                return;
                            }

                            // Display inventory data
                            Console.WriteLine("Inventory:");
                            Console.WriteLine("----------");
                            while (reader.Read())
                            {
                                int pipeId = reader.GetInt32(0); // Column index 0: PipeID
                                string dimensions = reader.GetString(1); // Column index 1: Dimensions
                                string application = reader.GetString(2); // Column index 2: Application

                                Console.WriteLine($"Pipe ID: {pipeId}, Dimensions: {dimensions}, Application: {application}");
                            }
                        }
                    }
                }
                catch (SqlException sqlEx)
                {
                    // Handle database-related errors
                    Console.WriteLine("Database error: " + sqlEx.Message);
                }
                finally
                {
                    // Close connection
                    connection.Close();
                    Console.WriteLine();
                    Console.WriteLine("Database connection closed.");
                }
            }
        }
    }
}
```

**Notes for Deployment:**
- Replace `YOUR_SERVER_NAME`, `YOUR_DATABASE_NAME`, `YOUR_USERNAME`, and `YOUR_PASSWORD` in the connection string with appropriate values.
- Ensure the database table `SteelPipeInventory` exists with columns `PipeID`, `Dimensions`, and `Application`.
- Validate permissions for the database user specified in the connection string.
