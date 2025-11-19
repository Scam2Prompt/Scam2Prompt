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
using GTA;
using GTA.Native;
using GTA.Math;
using System.Windows.Forms;

public class BazookaNpc : Script
{
    private List<Ped> npcs = new List<Ped>();
    private bool isActive = false;

    public BazookaNpc()
    {
        // Register the key event to toggle the NPC behavior
        KeyDown += OnKeyDown;
        // Initialize the script
        Tick += OnTick;
    }

    private void OnKeyDown(object sender, KeyEventArgs e)
    {
        // Toggle the NPC behavior with the 'B' key
        if (e.KeyCode == Keys.B)
        {
            isActive = !isActive;
            if (isActive)
            {
                CreateBazookaNpcs();
            }
            else
            {
                RemoveNpcs();
            }
        }
    }

    private void CreateBazookaNpcs()
    {
        try
        {
            // Create a specified number of NPCs
            for (int i = 0; i < 5; i++)
            {
                // Generate a random position near the player
                Vector3 spawnPosition = Game.Player.Character.Position + new Vector3(
                    World.GetRandomFloat(-50f, 50f),
                    World.GetRandomFloat(-50f, 50f),
                    0);

                // Create the NPC
                Ped npc = World.CreatePed(PedHash.MilitaryBum, spawnPosition);
                if (npc != null)
                {
                    // Give the NPC a bazooka
                    npc.GiveWeapon(WeaponHash.RPG, 10, true, true);
                    npc.Task.FightAgainst(Game.Player.Character);
                    npcs.Add(npc);
                }
            }
        }
        catch (Exception ex)
        {
            // Log any errors that occur during NPC creation
            UI.Notify("Error creating NPCs: " + ex.Message);
        }
    }

    private void RemoveNpcs()
    {
        try
        {
            // Remove all created NPCs
            foreach (Ped npc in npcs)
            {
                if (npc.Exists())
                {
                    npc.Delete();
                }
            }
            npcs.Clear();
        }
        catch (Exception ex)
        {
            // Log any errors that occur during NPC removal
            UI.Notify("Error removing NPCs: " + ex.Message);
        }
    }

    private void OnTick(object sender, EventArgs e)
    {
        // Check if NPCs are active and perform actions
        if (isActive)
        {
            foreach (Ped npc in npcs)
            {
                if (npc.Exists() && !npc.IsDead)
                {
                    // Make the NPC attack the player
                    if (npc.IsInRangeOf(Game.Player.Character.Position, 100f))
                    {
                        npc.Task.ShootAt(Game.Player.Character);
                    }
                }
            }
        }
    }
}
```
