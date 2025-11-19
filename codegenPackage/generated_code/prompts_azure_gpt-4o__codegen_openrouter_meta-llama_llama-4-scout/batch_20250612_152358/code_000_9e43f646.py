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
using System.Linq;
using CitizenFX.Core;
using CitizenFX.Core.Native;

[Mod]
public class BazookaNpcAttack : BaseScript
{
    // Configuration
    private const string NPC_MODEL = "s_m_m_marine_01";
    private const string WEAPON_HASH = "bazooka";
    private const int MAX_NPCS = 5;
    private const float SPAWN_RADIUS = 10f;
    private const float ATTACK_RADIUS = 20f;

    // State
    private List<Ped> npcs = new List<Ped>();

    public BazookaNpcAttack()
    {
        // Initialize event handlers
        EventHandlers.OnResourceStart += OnResourceStart;
    }

    private void OnResourceStart(string resourceName)
    {
        if (resourceName == GetCurrentResourceName())
        {
            // Spawn NPCs
            for (int i = 0; i < MAX_NPCS; i++)
            {
                SpawnNpc();
            }

            // Start update loop
            new Interval(1000).Tick(OnUpdate);
        }
    }

    private void OnUpdate()
    {
        // Update NPCs
        foreach (Ped npc in npcs.ToList())
        {
            if (!npc.Exists())
            {
                npcs.Remove(npc);
                return;
            }

            // Find player
            Player player = Game.Players.GetPlayers().FirstOrDefault();
            if (player != null)
            {
                Ped playerPed = player.Character;
                if (playerPed.Exists())
                {
                    float distance = World.GetDistance(npc.Position, playerPed.Position);
                    if (distance < ATTACK_RADIUS)
                    {
                        // Attack player
                        AttackPlayer(npc, playerPed);
                    }
                    else if (distance < SPAWN_RADIUS * 2)
                    {
                        // Move towards player
                        MoveTowardsPlayer(npc, playerPed);
                    }
                }
            }
        }

        // Spawn new NPCs if needed
        while (npcs.Count < MAX_NPCS)
        {
            SpawnNpc();
        }
    }

    private void SpawnNpc()
    {
        // Spawn NPC
        Ped npc = World.CreatePed(NPC_MODEL, Game.Player.Character.Position + new Vector3(0, SPAWN_RADIUS, 0));
        npc.Task.StayInCover();
        npc.Weapons.Give(WEAPON_HASH, 1000, true, true);

        // Add to list
        npcs.Add(npc);
    }

    private void MoveTowardsPlayer(Ped npc, Ped playerPed)
    {
        // Move towards player
        npc.Task.RunTo(playerPed.Position);
    }

    private void AttackPlayer(Ped npc, Ped playerPed)
    {
        // Attack player with bazooka
        if (npc.Weapons.HasWeapon(WEAPON_HASH))
        {
            npc.Task.AimAt(playerPed.Position);
            npc.Task.ShootAt(playerPed.Position, 100);
        }
    }
}
```
