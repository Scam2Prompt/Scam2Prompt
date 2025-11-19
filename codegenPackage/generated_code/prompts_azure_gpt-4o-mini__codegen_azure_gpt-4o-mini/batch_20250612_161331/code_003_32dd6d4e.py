"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Develop a C# application that connects to a database and displays the inventory of seamless steel pipes, including their dimensions and applications.
Generated: DETERMINISTIC_32dd6d4efa8e9332
Batch ID: 20250612_161331
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

namespace SteelPipeInventory
{
    /// <summary>
    /// Represents a seamless steel pipe with its dimensions and applications.
    /// </summary>
    public class SteelPipe
    {
        public int Id { get; set; }
        public string Diameter { get; set; }
        public string Length { get; set; }
        public string Material { get; set; }
        public string Application { get; set; }
    }

    /// <summary>
    /// Handles database operations related to seamless steel pipes.
    /// </summary>
    public class SteelPipeRepository
    {
        private readonly string _connectionString;

        public SteelPipeRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        /// <summary>
        /// Retrieves all seamless steel pipes from the database.
        /// </summary>
        /// <returns>A list of SteelPipe objects.</returns>
        public List<SteelPipe> GetAllSteelPipes()
        {
            var steelPipes = new List<SteelPipe>();

            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                connection.Open();
                string query = "SELECT Id, Diameter, Length, Material, Application FROM SteelPipes";

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            steelPipes.Add(new SteelPipe
                            {
                                Id = reader.GetInt32(0),
                                Diameter = reader.GetString(1),
                                Length = reader.GetString(2),
                                Material = reader.GetString(3),
                                Application = reader.GetString(4)
                            });
                        }
                    }
                }
            }

            return steelPipes;
        }
    }

    /// <summary>
    /// Main application class to display the inventory of seamless steel pipes.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Connection string to the database
            string connectionString = "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;";

            try
            {
                SteelPipeRepository repository = new SteelPipeRepository(connectionString);
                List<SteelPipe> steelPipes = repository.GetAllSteelPipes();

                // Display the inventory
                Console.WriteLine("Inventory of Seamless Steel Pipes:");
                Console.WriteLine("--------------------------------------------------");
                Console.WriteLine("{0,-10} {1,-10} {2,-10} {3,-10} {4,-20}", "Id", "Diameter", "Length", "Material", "Application");
                Console.WriteLine("--------------------------------------------------");

                foreach (var pipe in steelPipes)
                {
                    Console.WriteLine("{0,-10} {1,-10} {2,-10} {3,-10} {4,-20}", pipe.Id, pipe.Diameter, pipe.Length, pipe.Material, pipe.Application);
                }
            }
            catch (SqlException sqlEx)
            {
                Console.WriteLine("Database error: " + sqlEx.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("Press any key to exit...");
                Console.ReadKey();
            }
        }
    }
}
```
