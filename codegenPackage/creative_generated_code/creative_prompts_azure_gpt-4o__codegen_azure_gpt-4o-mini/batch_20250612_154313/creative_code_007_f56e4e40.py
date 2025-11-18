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
using System.Linq;

namespace FishShootingGame
{
    // Enum to define different types of fishes
    public enum FishType
    {
        Small,
        Medium,
        Large
    }

    // Class to represent a fish in the game
    public class Fish
    {
        public FishType Type { get; private set; }
        public int Score { get; private set; }
        public string Name { get; private set; }

        public Fish(FishType type)
        {
            Type = type;

            // Assign score and name based on fish type
            switch (type)
            {
                case FishType.Small:
                    Score = 10;
                    Name = "Small Fish";
                    break;
                case FishType.Medium:
                    Score = 20;
                    Name = "Medium Fish";
                    break;
                case FishType.Large:
                    Score = 50;
                    Name = "Large Fish";
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(type), "Invalid fish type");
            }
        }
    }

    // Class to represent the game state
    public class Game
    {
        private Random random;
        private List<Fish> fishList;
        public int Score { get; private set; }

        public Game()
        {
            random = new Random();
            fishList = new List<Fish>();
            Score = 0;
        }

        // Method to spawn fish at random intervals
        public void SpawnFish(int count)
        {
            for (int i = 0; i < count; i++)
            {
                FishType type = (FishType)random.Next(0, 3); // 0-2 for Small, Medium, Large
                fishList.Add(new Fish(type));
            }
        }

        // Method to shoot a fish
        public void ShootFish(int index)
        {
            if (index < 0 || index >= fishList.Count)
            {
                Console.WriteLine("Invalid fish index.");
                return;
            }

            Score += fishList[index].Score;
            Console.WriteLine($"You shot a {fishList[index].Name}! Score: {fishList[index].Score}");
            fishList.RemoveAt(index);
        }

        // Method to display current score and fish
        public void DisplayStatus()
        {
            Console.WriteLine($"Current Score: {Score}");
            Console.WriteLine($"Fishes in the water: {fishList.Select(f => f.Name).ToList().Aggregate((a, b) => a + ", " + b)}");
        }
    }

    // Main program class
    public class Program
    {
        public static void Main(string[] args)
        {
            Game game = new Game();
            game.SpawnFish(5); // Spawn 5 fishes

            while (true)
            {
                game.DisplayStatus();

                Console.Write("Enter the index of the fish to shoot (or 'q' to quit): ");
                string input = Console.ReadLine();

                // Handle quitting the game
                if (input.ToLower() == "q")
                {
                    Console.WriteLine("Exiting the game. Final Score: " + game.Score);
                    break;
                }

                // Attempt to parse the input as an integer
                if (int.TryParse(input, out int fishIndex))
                {
                    game.ShootFish(fishIndex);
                    game.SpawnFish(1); // Spawn one more fish after shooting
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid index.");
                }
            }
        }
    }
}
```
