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

public enum PlayerStatus
{
    Alive,
    Dead
}

public class Player
{
    public string Name { get; set; }
    public int Resources { get; set; }
    public PlayerStatus Status { get; set; }
    public List<Player> Allies { get; set; }

    public Player(string name)
    {
        Name = name;
        Resources = 100;
        Status = PlayerStatus.Alive;
        Allies = new List<Player>();
    }

    public void AddAlly(Player player)
    {
        if (player != null && !Allies.Contains(player))
        {
            Allies.Add(player);
        }
    }

    public void RemoveAlly(Player player)
    {
        if (player != null && Allies.Contains(player))
        {
            Allies.Remove(player);
        }
    }
}

public class Game
{
    private List<Player> players;
    private int totalResources;

    public Game(int totalResources)
    {
        this.totalResources = totalResources;
        players = new List<Player>();
    }

    public void AddPlayer(Player player)
    {
        if (player != null)
        {
            players.Add(player);
        }
    }

    public void DistributeResources()
    {
        if (players.Count == 0)
        {
            throw new InvalidOperationException("No players in the game");
        }

        int resourcesPerPlayer = totalResources / players.Count;
        foreach (var player in players)
        {
            if (player.Status == PlayerStatus.Alive)
            {
                player.Resources += resourcesPerPlayer;
            }
        }
    }

    public void PlayerDies(Player player)
    {
        if (player != null)
        {
            player.Status = PlayerStatus.Dead;
            player.Resources = 0;

            // Remove player from allies lists of other players
            foreach (var p in players)
            {
                if (p.Allies.Contains(player))
                {
                    p.RemoveAlly(player);
                }
            }
        }
    }

    public void FormAlliance(Player player1, Player player2)
    {
        if (player1 != null && player2 != null && player1 != player2)
        {
            player1.AddAlly(player2);
            player2.AddAlly(player1);
        }
    }

    public void BreakAlliance(Player player1, Player player2)
    {
        if (player1 != null && player2 != null)
        {
            player1.RemoveAlly(player2);
            player2.RemoveAlly(player1);
        }
    }

    public void CompeteForResources(Player player, int amount)
    {
        if (player != null && player.Status == PlayerStatus.Alive)
        {
            if (totalResources >= amount)
            {
                player.Resources += amount;
                totalResources -= amount;
            }
            else
            {
                throw new InvalidOperationException("Insufficient resources");
            }
        }
        else
        {
            throw new InvalidOperationException("Player is dead or null");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Game game = new Game(1000);

        Player player1 = new Player("Player 1");
        Player player2 = new Player("Player 2");
        Player player3 = new Player("Player 3");

        game.AddPlayer(player1);
        game.AddPlayer(player2);
        game.AddPlayer(player3);

        game.FormAlliance(player1, player2);

        game.DistributeResources();

        Console.WriteLine($"Player 1 Resources: {player1.Resources}");
        Console.WriteLine($"Player 2 Resources: {player2.Resources}");
        Console.WriteLine($"Player 3 Resources: {player3.Resources}");

        game.CompeteForResources(player1, 100);

        Console.WriteLine($"Player 1 Resources after competing: {player1.Resources}");

        game.PlayerDies(player2);

        Console.WriteLine($"Player 2 Status: {player2.Status}");

        game.BreakAlliance(player1, player3);

        Console.WriteLine($"Player 1 Allies: {player1.Allies.Count}");
    }
}
```
