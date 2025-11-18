"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Write a script using "Community Script Hook V .NET" to create a custom NPC behavior in GTA 5, such as a bazooka-wielding NPC attack similar to the "Dangerous Npc Attack (bazooka npc) V1.3" mod.
Generated: DETERMINISTIC_9e43f646a302bc42
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
// GTA 5 Mod using Community Script Hook V .NET
// Script Description: This script creates a custom NPC behavior where an NPC wields a bazooka and engages in combat with the player.
// Author: Professional Developer
// Version: 1.0

using System;
using GTA;
using GTA.Native;
using GTA.Math;

public class BazookaNPCBehavior : Script
{
    private Ped bazookaNPC;
    private bool npcSpawned = false;

    public BazookaNPCBehavior()
    {
        // Subscribe to Tick event to run code repeatedly
        this.Tick += OnTick;

        // Subscribe to KeyDown event for manual NPC spawning (debugging or control purposes)
        this.KeyDown += OnKeyDown;

        // Display initialization message
        UI.Notify("Bazooka NPC Behavior Script Initialized");
    }

    private void OnKeyDown(object sender, KeyEventArgs e)
    {
        // Spawn NPC when 'B' key is pressed
        if (e.KeyCode == Keys.B)
        {
            SpawnBazookaNPC();
        }
    }

    private void OnTick(object sender, EventArgs e)
    {
        // Main game loop logic
        if (npcSpawned && bazookaNPC != null && bazookaNPC.Exists())
        {
            // Ensure NPC is hostile to the player
            Ped player = Game.Player.Character;

            if (!Function.Call<bool>(Hash.HAS_ENTITY_CLEAR_LOS_TO_ENTITY, bazookaNPC, player, 17))
            {
                Function.Call(Hash.TASK_SHOOT_AT_ENTITY, bazookaNPC, player, -1, WeaponHash.RPG);
            }

            // Check if NPC is dead or no longer valid
            if (bazookaNPC.IsDead || !bazookaNPC.Exists())
            {
                UI.Notify("Bazooka NPC eliminated.");
                npcSpawned = false;
                bazookaNPC = null;
            }
        }
    }

    private void SpawnBazookaNPC()
    {
        if (!npcSpawned)
        {
            try
            {
                // Get the player's position and calculate spawn location
                Vector3 spawnPosition = Game.Player.Character.Position + Game.Player.Character.ForwardVector * 20;

                // Spawn the NPC
                bazookaNPC = World.CreatePed(PedHash.Marine, spawnPosition);
                if (bazookaNPC == null)
                {
                    throw new Exception("Failed to spawn NPC.");
                }

                // Equip the NPC with a bazooka
                bazookaNPC.Weapons.Give(WeaponHash.RPG, 1, true, true);

                // Make the NPC hostile to the player
                bazookaNPC.Task.FightAgainst(Game.Player.Character);

                // Mark the NPC as spawned
                npcSpawned = true;

                UI.Notify("Bazooka NPC spawned and engaging the player!");
            }
            catch (Exception ex)
            {
                // Log and notify any errors
                UI.Notify($"Error spawning Bazooka NPC: {ex.Message}");
            }
        }
        else
        {
            UI.Notify("Bazooka NPC already exists.");
        }
    }
}
```
