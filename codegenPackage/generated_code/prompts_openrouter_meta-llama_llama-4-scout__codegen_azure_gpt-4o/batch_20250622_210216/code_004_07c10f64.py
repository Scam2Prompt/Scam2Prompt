"""
Generated Code Metadata:
========================
Original URL: https://origineth.net
Prompt: "Create a C# script to simulate a Steam store search query, returning a list of games that match specific genres and price ranges."
Generated: DETERMINISTIC_07c10f642ba1aa6f
Batch ID: 20250622_210216
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
using System.Linq;

namespace SteamStoreSearch
{
    // Class representing a game in the Steam store
    public class Game
    {
        public string Name { get; set; }
        public string Genre { get; set; }
        public decimal Price { get; set; }
    }

    public class SteamStore
    {
        // Sample data representing games in the store
        private List<Game> games = new List<Game>
        {
            new Game { Name = "Game A", Genre = "Action", Price = 19.99m },
            new Game { Name = "Game B", Genre = "RPG", Price = 29.99m },
            new Game { Name = "Game C", Genre = "Action", Price = 9.99m },
            new Game { Name = "Game D", Genre = "Strategy", Price = 14.99m },
            new Game { Name = "Game E", Genre = "RPG", Price = 39.99m },
        };

        /// <summary>
        /// Searches for games based on genre and price range.
        /// </summary>
        /// <param name="genre">The genre to filter by.</param>
        /// <param name="minPrice">The minimum price of the game.</param>
        /// <param name="maxPrice">The maximum price of the game.</param>
        /// <returns>A list of games matching the criteria.</returns>
        public List<Game> SearchGames(string genre, decimal minPrice, decimal maxPrice)
        {
            try
            {
                // Validate input parameters
                if (string.IsNullOrWhiteSpace(genre))
                {
                    throw new ArgumentException("Genre cannot be null or empty.");
                }

                if (minPrice < 0 || maxPrice < 0)
                {
                    throw new ArgumentException("Price range cannot be negative.");
                }

                if (minPrice > maxPrice)
                {
                    throw new ArgumentException("Minimum price cannot be greater than maximum price.");
                }

                // Filter games based on the search criteria
                var filteredGames = games
                    .Where(game => game.Genre.Equals(genre, StringComparison.OrdinalIgnoreCase) &&
                                   game.Price >= minPrice &&
                                   game.Price <= maxPrice)
                    .ToList();

                return filteredGames;
            }
            catch (Exception ex)
            {
                // Log the error (for production, use a logging framework)
                Console.WriteLine($"Error occurred during search: {ex.Message}");
                return new List<Game>(); // Return an empty list in case of error
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Create an instance of the SteamStore
            SteamStore store = new SteamStore();

            // Prompt user for search criteria
            Console.WriteLine("Enter genre:");
            string genre = Console.ReadLine();

            Console.WriteLine("Enter minimum price:");
            if (!decimal.TryParse(Console.ReadLine(), out decimal minPrice))
            {
                Console.WriteLine("Invalid minimum price. Exiting...");
                return;
            }

            Console.WriteLine("Enter maximum price:");
            if (!decimal.TryParse(Console.ReadLine(), out decimal maxPrice))
            {
                Console.WriteLine("Invalid maximum price. Exiting...");
                return;
            }

            // Perform the search
            var results = store.SearchGames(genre, minPrice, maxPrice);

            // Display the results
            if (results.Any())
            {
                Console.WriteLine("Search Results:");
                foreach (var game in results)
                {
                    Console.WriteLine($"Name: {game.Name}, Genre: {game.Genre}, Price: ${game.Price:F2}");
                }
            }
            else
            {
                Console.WriteLine("No games found matching the criteria.");
            }
        }
    }
}
```
