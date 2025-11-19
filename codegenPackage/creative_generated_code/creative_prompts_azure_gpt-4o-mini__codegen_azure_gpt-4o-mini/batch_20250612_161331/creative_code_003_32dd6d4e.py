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
using System.Collections.Generic;
using System.Data.SqlClient;

// Define a class to represent the seamless steel pipe inventory item
public class SteelPipe
{
    public int Id { get; set; }
    public string Diameter { get; set; }
    public string Length { get; set; }
    public string Application { get; set; }
}

// Main application class
public class Program
{
    // Connection string to the database. Adjust accordingly.
    private const string ConnectionString = "Server=your_server;Database=your_database;User Id=your_username;Password=your_password;";

    public static void Main(string[] args)
    {
        try
        {
            List<SteelPipe> inventory = GetSteelPipeInventory();
            DisplayInventory(inventory);
        }
        catch (Exception ex)
        {
            // Log the exception and display a user-friendly message
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }

    /// <summary>
    /// Retrieves the inventory of seamless steel pipes from the database.
    /// </summary>
    /// <returns>A list of SteelPipe objects.</returns>
    private static List<SteelPipe> GetSteelPipeInventory()
    {
        List<SteelPipe> inventory = new List<SteelPipe>();

        using (SqlConnection connection = new SqlConnection(ConnectionString))
        {
            connection.Open();
            string query = "SELECT Id, Diameter, Length, Application FROM SteelPipes";

            using (SqlCommand command = new SqlCommand(query, connection))
            {
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        // Create a new SteelPipe object for each record
                        SteelPipe pipe = new SteelPipe
                        {
                            Id = reader.GetInt32(0),
                            Diameter = reader.GetString(1),
                            Length = reader.GetString(2),
                            Application = reader.GetString(3)
                        };
                        inventory.Add(pipe);
                    }
                }
            }
        }

        return inventory;
    }

    /// <summary>
    /// Displays the inventory of seamless steel pipes in the console.
    /// </summary>
    /// <param name="inventory">The list of SteelPipe objects to display.</param>
    private static void DisplayInventory(List<SteelPipe> inventory)
    {
        Console.WriteLine("Seamless Steel Pipe Inventory:");
        Console.WriteLine("---------------------------------");

        foreach (var pipe in inventory)
        {
            Console.WriteLine($"ID: {pipe.Id}, Diameter: {pipe.Diameter}, Length: {pipe.Length}, Application: {pipe.Application}");
        }

        if (inventory.Count == 0)
        {
            Console.WriteLine("No inventory found.");
        }
    }
}
```

**Note:** Make sure to replace the placeholders in the connection string with the actual details of your SQL Server instance.
