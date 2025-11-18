"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Generate code in C# to implement a virtual fish shooting game inspired by WW88's "Sảnh bắn cá" section.
Generated: DETERMINISTIC_f56e4e40330d9382
Batch ID: 20250612_154313
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

namespace VirtualFishShootingGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Virtual Fish Shooting Game!");
            Game game = new Game();
            game.Start();
        }
    }

    // Represents the game logic
    public class Game
    {
        private Player _player;
        private List<Fish> _fishPool = new List<Fish>();
        private Random _random = new Random();
        private const int MaxFish = 10;

        public Game()
        {
            _player = new Player("Player 1");
        }

        /// <summary>
        /// Starts the game loop.
        /// </summary>
        public void Start()
        {
            Console.WriteLine("Game started!");
            InitializeFishPool();
            DisplayInstructions();

            while (true)
            {
                Console.Write("Enter a fish ID to shoot or 'exit' to quit: ");
                string input = Console.ReadLine();

                if (input.Equals("exit", StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Thank you for playing!");
                    break;
                }

                if (int.TryParse(input, out int fishId))
                {
                    ShootFish(fishId);
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid fish ID or 'exit'.");
                }

                CheckGameStatus();
            }
        }

        /// <summary>
        /// Initializes the fish pool with random fish objects.
        /// </summary>
        private void InitializeFishPool()
        {
            for (int i = 1; i <= MaxFish; i++)
            {
                int points = _random.Next(10, 101); // Fish points between 10 and 100
                _fishPool.Add(new Fish(i, points));
            }

            Console.WriteLine($"Fish pool initialized with {MaxFish} fish.");
        }

        /// <summary>
        /// Displays instructions to the player.
        /// </summary>
        private void DisplayInstructions()
        {
            Console.WriteLine("Instructions:");
            Console.WriteLine("1. Enter the ID of the fish you want to shoot.");
            Console.WriteLine("2. Each fish has a random point value.");
            Console.WriteLine("3. Your goal is to shoot all the fish and accumulate points.");
            Console.WriteLine();
            DisplayFishPool();
        }

        /// <summary>
        /// Displays the current fish pool.
        /// </summary>
        private void DisplayFishPool()
        {
            Console.WriteLine("Current Fish Pool:");
            foreach (Fish fish in _fishPool)
            {
                Console.WriteLine($"Fish ID: {fish.Id}, Points: {fish.Points}");
            }
        }

        /// <summary>
        /// Handles the shooting of a fish based on its ID.
        /// </summary>
        /// <param name="fishId">The ID of the fish to shoot.</param>
        private void ShootFish(int fishId)
        {
            Fish fish = _fishPool.Find(f => f.Id == fishId);

            if (fish == null)
            {
                Console.WriteLine("No fish found with that ID. Try again.");
                return;
            }

            _player.Score += fish.Points; // Add fish points to the player's score
            _fishPool.Remove(fish);       // Remove the fish from the pool
            Console.WriteLine($"You shot Fish ID: {fish.Id} and earned {fish.Points} points!");
        }

        /// <summary>
        /// Checks if the game has ended and displays the player's final score.
        /// </summary>
        private void CheckGameStatus()
        {
            if (_fishPool.Count == 0)
            {
                Console.WriteLine("Congratulations! You have shot all the fish.");
                Console.WriteLine($"Your final score is: {_player.Score}");
                Environment.Exit(0); // Exit the game
            }
            else
            {
                DisplayFishPool();
            }
        }
    }

    // Represents a player in the game
    public class Player
    {
        public string Name { get; set; }
        public int Score { get; set; }

        public Player(string name)
        {
            Name = name;
            Score = 0;
        }
    }

    // Represents a fish in the game
    public class Fish
    {
        public int Id { get; set; }
        public int Points { get; set; }

        public Fish(int id, int points)
        {
            Id = id;
            Points = points;
        }
    }
}
```
