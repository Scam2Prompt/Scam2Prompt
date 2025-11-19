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

namespace SurvivalGame
{
    // Represents a player in the game
    public class Player
    {
        public string Name { get; private set; }
        public int Resources { get; private set; }
        public Alliance Alliance { get; private set; }

        public Player(string name)
        {
            Name = name;
            Resources = 100; // Initial resources
        }

        // Join an alliance
        public void JoinAlliance(Alliance alliance)
        {
            Alliance = alliance;
            alliance.AddMember(this);
        }

        // Leave the current alliance
        public void LeaveAlliance()
        {
            if (Alliance != null)
            {
                Alliance.RemoveMember(this);
                Alliance = null;
            }
        }

        // Compete for resources
        public void CompeteForResources(Player opponent)
        {
            Random random = new Random();
            int resourceGain = random.Next(10, 30); // Random resource gain
            int resourceLoss = random.Next(10, 30); // Random resource loss

            if (random.Next(0, 2) == 0) // 50% chance to win
            {
                Resources += resourceGain;
                opponent.Resources -= resourceLoss;
                Console.WriteLine($"{Name} won against {opponent.Name} and gained {resourceGain} resources!");
            }
            else
            {
                Resources -= resourceLoss;
                opponent.Resources += resourceGain;
                Console.WriteLine($"{opponent.Name} won against {Name} and gained {resourceGain} resources!");
            }

            // Ensure resources don't go below zero
            Resources = Math.Max(Resources, 0);
            opponent.Resources = Math.Max(opponent.Resources, 0);
        }
    }

    // Represents an alliance of players
    public class Alliance
    {
        public string Name { get; private set; }
        private List<Player> Members;

        public Alliance(string name)
        {
            Name = name;
            Members = new List<Player>();
        }

        // Add a player to the alliance
        public void AddMember(Player player)
        {
            if (!Members.Contains(player))
            {
                Members.Add(player);
                Console.WriteLine($"{player.Name} joined the alliance {Name}.");
            }
        }

        // Remove a player from the alliance
        public void RemoveMember(Player player)
        {
            if (Members.Contains(player))
            {
                Members.Remove(player);
                Console.WriteLine($"{player.Name} left the alliance {Name}.");
            }
        }

        // Share resources among alliance members
        public void ShareResources()
        {
            int totalResources = 0;
            foreach (var member in Members)
            {
                totalResources += member.Resources;
            }

            int sharedResources = totalResources / Members.Count;

            foreach (var member in Members)
            {
                member.Resources = sharedResources;
            }

            Console.WriteLine($"Resources have been shared equally among members of {Name}.");
        }
    }

    // Main game logic
    class Program
    {
        static void Main(string[] args)
        {
            // Create players
            Player player1 = new Player("Alice");
            Player player2 = new Player("Bob");
            Player player3 = new Player("Charlie");

            // Create alliances
            Alliance alliance1 = new Alliance("Survivors");
            Alliance alliance2 = new Alliance("Chaos");

            // Players join alliances
            player1.JoinAlliance(alliance1);
            player2.JoinAlliance(alliance1);
            player3.JoinAlliance(alliance2);

            // Compete for resources
            player1.CompeteForResources(player3);
            player2.CompeteForResources(player3);

            // Share resources within alliances
            alliance1.ShareResources();
            alliance2.ShareResources();

            // Display final resources
            Console.WriteLine($"{player1.Name} has {player1.Resources} resources.");
            Console.WriteLine($"{player2.Name} has {player2.Resources} resources.");
            Console.WriteLine($"{player3.Name} has {player3.Resources} resources.");
        }
    }
}
```
