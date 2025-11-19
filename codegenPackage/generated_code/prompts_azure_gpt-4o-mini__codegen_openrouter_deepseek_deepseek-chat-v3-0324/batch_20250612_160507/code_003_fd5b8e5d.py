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
using System.Linq;

namespace SurvivalAllianceGame
{
    /// <summary>
    /// Represents a player in the game
    /// </summary>
    public class Player
    {
        public string Name { get; private set; }
        public int Health { get; private set; }
        public int ResourceCount { get; private set; }
        public Alliance CurrentAlliance { get; set; }

        public Player(string name, int initialHealth)
        {
            Name = name ?? throw new ArgumentNullException(nameof(name));
            Health = initialHealth > 0 ? initialHealth : throw new ArgumentException("Health must be positive");
            ResourceCount = 0;
            CurrentAlliance = null;
        }

        public void AddResources(int amount)
        {
            if (amount < 0) throw new ArgumentException("Cannot add negative resources");
            ResourceCount += amount;
        }

        public void TakeDamage(int damage)
        {
            if (damage < 0) throw new ArgumentException("Damage must be positive");
            Health = Math.Max(0, Health - damage);
        }

        public bool IsAlive => Health > 0;
    }

    /// <summary>
    /// Represents an alliance between players
    /// </summary>
    public class Alliance
    {
        public string Name { get; private set; }
        public List<Player> Members { get; private set; }
        public int SharedResources { get; private set; }

        public Alliance(string name)
        {
            Name = name ?? throw new ArgumentNullException(nameof(name));
            Members = new List<Player>();
            SharedResources = 0;
        }

        public void AddMember(Player player)
        {
            if (player == null) throw new ArgumentNullException(nameof(player));
            if (Members.Contains(player)) throw new InvalidOperationException("Player already in alliance");
            
            Members.Add(player);
            player.CurrentAlliance = this;
        }

        public void RemoveMember(Player player)
        {
            if (player == null) throw new ArgumentNullException(nameof(player));
            if (!Members.Contains(player)) throw new InvalidOperationException("Player not in alliance");
            
            Members.Remove(player);
            player.CurrentAlliance = null;
        }

        public void ContributeResources(Player player, int amount)
        {
            if (player == null) throw new ArgumentNullException(nameof(player));
            if (!Members.Contains(player)) throw new InvalidOperationException("Player not in alliance");
            if (amount < 0) throw new ArgumentException("Cannot contribute negative resources");
            if (player.ResourceCount < amount) throw new InvalidOperationException("Player doesn't have enough resources");

            player.ResourceCount -= amount;
            SharedResources += amount;
        }

        public void DistributeResources(int amountPerMember)
        {
            if (amountPerMember < 0) throw new ArgumentException("Cannot distribute negative resources");
            if (SharedResources < amountPerMember * Members.Count) 
                throw new InvalidOperationException("Not enough shared resources");

            foreach (var member in Members)
            {
                member.AddResources(amountPerMember);
            }
            SharedResources -= amountPerMember * Members.Count;
        }
    }

    /// <summary>
    /// Manages the game state including resources and alliances
    /// </summary>
    public class GameManager
    {
        private List<Player> players;
        private List<Alliance> alliances;
        private int totalResources;
        private Random random;

        public GameManager(int initialResources)
        {
            if (initialResources < 0) throw new ArgumentException("Initial resources must be non-negative");
            
            players = new List<Player>();
            alliances = new List<Alliance>();
            totalResources = initialResources;
            random = new Random();
        }

        public void AddPlayer(Player player)
        {
            if (player == null) throw new ArgumentNullException(nameof(player));
            if (players.Contains(player)) throw new InvalidOperationException("Player already exists");
            
            players.Add(player);
        }

        public Alliance CreateAlliance(string name, params Player[] foundingMembers)
        {
            if (string.IsNullOrWhiteSpace(name)) throw new ArgumentException("Alliance name cannot be empty");
            if (foundingMembers == null || foundingMembers.Length == 0) 
                throw new ArgumentException("Alliance must have at least one founding member");

            var alliance = new Alliance(name);
            alliances.Add(alliance);

            foreach (var member in foundingMembers)
            {
                if (member.CurrentAlliance != null)
                    throw new InvalidOperationException($"Player {member.Name} is already in an alliance");
                
                alliance.AddMember(member);
            }

            return alliance;
        }

        public void SpawnResources(int amount)
        {
            if (amount < 0) throw new ArgumentException("Cannot spawn negative resources");
            totalResources += amount;
        }

        public void DistributeResources()
        {
            if (totalResources <= 0) return;

            int resourcesPerPlayer = totalResources / players.Count;
            int remaining = totalResources % players.Count;

            foreach (var player in players.Where(p => p.IsAlive))
            {
                player.AddResources(resourcesPerPlayer);
            }

            // Distribute remaining resources randomly
            for (int i = 0; i < remaining; i++)
            {
                var alivePlayers = players.Where(p => p.IsAlive).ToList();
                if (alivePlayers.Count == 0) break;
                
                var luckyPlayer = alivePlayers[random.Next(alivePlayers.Count)];
                luckyPlayer.AddResources(1);
            }

            totalResources = 0;
        }

        public void SimulateConflict(Alliance alliance1, Alliance alliance2)
        {
            if (alliance1 == null || alliance2 == null) throw new ArgumentNullException("Alliances cannot be null");
            if (alliance1 == alliance2) throw new ArgumentException("Alliance cannot conflict with itself");

            // Calculate alliance strengths based on member count and resources
            int strength1 = alliance1.Members.Count + alliance1.SharedResources;
            int strength2 = alliance2.Members.Count + alliance2.SharedResources;

            // Determine winner and loser
            Alliance winner, loser;
            if (strength1 > strength2)
            {
                winner = alliance1;
                loser = alliance2;
            }
            else if (strength2 > strength1)
            {
                winner = alliance2;
                loser = alliance1;
            }
            else // Equal strength - random outcome
            {
                winner = random.Next(2) == 0 ? alliance1 : alliance2;
                loser = winner == alliance1 ? alliance2 : alliance1;
            }

            // Apply consequences
            foreach (var member in loser.Members.ToList())
            {
                member.TakeDamage(random.Next(1, 4));
                if (!member.IsAlive)
                {
                    loser.RemoveMember(member);
                }
            }

            // Winner takes some resources from loser
            int stolenResources = Math.Min(loser.SharedResources, random.Next(1, loser.SharedResources + 1));
            loser.SharedResources -= stolenResources;
            winner.SharedResources += stolenResources;
        }

        public void SimulateRandomEvent()
        {
            if (players.Count == 0) return;

            int eventType = random.Next(3);
            switch (eventType)
            {
                case 0: // Resource windfall
                    int windfall = random.Next(5, 15);
                    SpawnResources(windfall);
                    break;
                
                case 1: // Natural disaster
                    foreach (var player in players.Where(p => p.IsAlive))
                    {
                        player.TakeDamage(random.Next(1, 3));
                    }
                    break;
                
                case 2: // Alliance betrayal
                    if (alliances.Count >= 2)
                    {
                        var betrayer = alliances[random.Next(alliances.Count)];
                        var victim = alliances.Where(a => a != betrayer).OrderBy(a => random.Next()).FirstOrDefault();
                        
                        if (victim != null)
                        {
                            // Random member defects
                            if (betrayer.Members.Count > 0 && victim.Members.Count > 0)
                            {
                                var traitor = victim.Members[random.Next(victim.Members.Count)];
                                victim.RemoveMember(traitor);
                                betrayer.AddMember(traitor);
                            }
                        }
                    }
                    break;
            }
        }
    }
}
```
