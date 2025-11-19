"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: Write a script using "Community Script Hook V .NET" to create a custom NPC behavior in GTA 5, such as a bazooka-wielding NPC attack similar to the "Dangerous Npc Attack (bazooka npc) V1.3" mod.
Generated: DETERMINISTIC_9e43f646a302bc42
Batch ID: 20250612_152358
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
using System.Drawing;
using System.Threading;
using System.Windows.Forms;
using GTA;
using GTA.Math;
using GTA.Native;

public class BazookaNpc : Script
{
    private readonly List<Ped> _attackers = new List<Ped>();
    private bool _isActive = false;
    private readonly Random _random = new Random();
    private readonly Model _bazookaModel = WeaponHash.RPG;
    private readonly Model _pedModel = new Model(PedHash.ArmBoss01GMM);

    public BazookaNpc()
    {
        Tick += OnTick;
        KeyDown += OnKeyDown;
        Interval = 100;

        // Load models at startup
        _pedModel.Request(1000);
        _bazookaModel.Request(1000);
    }

    private void OnKeyDown(object sender, KeyEventArgs e)
    {
        if (e.KeyCode == Keys.F6)
        {
            _isActive = !_isActive;
            UI.Notify(_isActive ? "Bazooka NPCs Activated" : "Bazooka NPCs Deactivated");

            if (!_isActive)
            {
                CleanUpAttackers();
            }
        }
    }

    private void OnTick(object sender, EventArgs e)
    {
        if (!_isActive) return;
        if (!Game.Player.Character.IsAlive) return;

        try
        {
            // Spawn new attackers if needed
            if (_attackers.Count < 5)
            {
                SpawnAttacker();
            }

            // Manage existing attackers
            for (int i = _attackers.Count - 1; i >= 0; i--)
            {
                var attacker = _attackers[i];

                if (!attacker.Exists() || !attacker.IsAlive)
                {
                    _attackers.RemoveAt(i);
                    continue;
                }

                ControlAttacker(attacker);
            }
        }
        catch (Exception ex)
        {
            UI.Notify($"Error: {ex.Message}");
        }
    }

    private void SpawnAttacker()
    {
        try
        {
            Vector3 spawnPosition = GetSpawnPosition();
            Ped attacker = World.CreatePed(_pedModel, spawnPosition);

            if (attacker.Exists())
            {
                attacker.Weapons.Give(_bazookaModel, 100, true, true);
                attacker.Task.FightAgainst(Game.Player.Character);
                attacker.CanRagdoll = false;
                attacker.MaxHealth = 500;
                attacker.Health = 500;
                attacker.Armor = 100;
                attacker.Accuracy = 80;
                attacker.RelationshipGroup = RelationshipGroup.HatesPlayer;

                _attackers.Add(attacker);
            }
        }
        catch (Exception ex)
        {
            UI.Notify($"Spawn Error: {ex.Message}");
        }
    }

    private Vector3 GetSpawnPosition()
    {
        Vector3 playerPos = Game.Player.Character.Position;
        float angle = (float)(_random.NextDouble() * Math.PI * 2);
        float distance = 20f + (float)_random.NextDouble() * 10f;

        return playerPos + new Vector3(
            (float)Math.Cos(angle) * distance,
            (float)Math.Sin(angle) * distance,
            0f
        );
    }

    private void ControlAttacker(Ped attacker)
    {
        if (!attacker.IsInCombat)
        {
            attacker.Task.FightAgainst(Game.Player.Character);
        }

        // Keep distance from player
        float distanceToPlayer = attacker.Position.DistanceTo(Game.Player.Character.Position);
        if (distanceToPlayer < 15f)
        {
            Vector3 fleeDirection = (attacker.Position - Game.Player.Character.Position).Normalized;
            attacker.Task.RunTo(attacker.Position + fleeDirection * 10f);
        }
    }

    private void CleanUpAttackers()
    {
        foreach (var attacker in _attackers)
        {
            if (attacker.Exists())
            {
                attacker.Delete();
            }
        }
        _attackers.Clear();
    }

    protected override void Dispose(bool disposing)
    {
        if (disposing)
        {
            CleanUpAttackers();
            _pedModel.MarkAsNoLongerNeeded();
            _bazookaModel.MarkAsNoLongerNeeded();
        }
        base.Dispose(disposing);
    }
}
```
