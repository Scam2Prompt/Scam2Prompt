"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Develop a game mechanic in C# that allows players to form alliances and compete for scarce resources, based on the themes of survival and chaos from "The Cannibals" narrative.
Generated: DETERMINISTIC_fd5b8e5d84ecdeed
Batch ID: 20250612_160507
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

namespace CannibalsGame
{
    // Represents a player in the game
    public class Player
    {
        public string Name { get; private set; }
        public int Resources { get; private set; }
        public List<Player> Allies { get; private set; }

        public Player(string name)
        {
            Name = name;
            Resources = 100; // Starting resources
            Allies = new List<Player>();
        }

        // Method to form an alliance with another player
        public void FormAlliance(Player ally)
        {
            if (ally == null || ally == this)
            {
                throw new ArgumentException("Invalid ally.");
            }

            if (!Allies.Contains(ally))
            {
                Allies.Add(ally);
                ally.Allies.Add(this); // Mutual alliance
                Console.WriteLine($"{Name} formed an alliance with {ally.Name}.");
            }
            else
            {
                Console.WriteLine($"{Name} and {ally.Name} are already allies.");
            }
        }

        // Method to compete for resources against another player
        public void CompeteForResources(Player opponent)
        {
            if (opponent == null)
            {
                throw new ArgumentException("Opponent cannot be null.");
            }

            if (Allies.Contains(opponent))
            {
                Console.WriteLine($"{Name} cannot compete against an ally.");
                return;
            }

            Random rand = new Random();
            int outcome = rand.Next(0, 2); // Randomly determine the winner

            if (outcome == 0)
            {
                Console.WriteLine($"{Name} wins against {opponent.Name}!");
                Resources += 20; // Winner gains resources
                opponent.Resources -= 20; // Loser loses resources
            }
            else
            {
                Console.WriteLine($"{opponent.Name} wins against {Name}!");
                opponent.Resources += 20; // Winner gains resources
                Resources -= 20; // Loser loses resources
            }

            // Ensure resources do not go below zero
            Resources = Math.Max(Resources, 0);
            opponent.Resources = Math.Max(opponent.Resources, 0);
        }

        // Method to display player status
        public void DisplayStatus()
        {
            Console.WriteLine($"Player: {Name}, Resources: {Resources}, Allies: {Allies.Count}");
        }
    }

    // Main game class to manage players and game mechanics
    public class Game
    {
        private List<Player> players;

        public Game()
        {
            players = new List<Player>();
        }

        // Method to add a player to the game
        public void AddPlayer(string name)
        {
            if (string.IsNullOrWhiteSpace(name))
            {
                throw new ArgumentException("Player name cannot be empty.");
            }

            players.Add(new Player(name));
            Console.WriteLine($"Player {name} has joined the game.");
        }

        // Method to start the game
        public void StartGame()
        {
            Console.WriteLine("Game has started!");
            foreach (var player in players)
            {
                player.DisplayStatus();
            }
        }
    }

    // Entry point of the application
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Game game = new Game();
                game.AddPlayer("Alice");
                game.AddPlayer("Bob");
                game.AddPlayer("Charlie");

                game.StartGame();

                // Example of forming alliances and competing
                var alice = game.Players[0];
                var bob = game.Players[1];
                var charlie = game.Players[2];

                alice.FormAlliance(bob);
                alice.CompeteForResources(charlie);
                bob.CompeteForResources(charlie);

                // Display final status
                foreach (var player in game.Players)
                {
                    player.DisplayStatus();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
