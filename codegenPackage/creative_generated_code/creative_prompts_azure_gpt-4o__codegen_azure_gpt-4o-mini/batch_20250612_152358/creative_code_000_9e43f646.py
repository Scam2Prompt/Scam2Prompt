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
using System;
using System.Collections.Generic;
using GTA;
using GTA.Native;
using GTA.Math;

public class BazookaNPCAttack : Script
{
    // Define the NPC model and weapon
    private readonly string npcModel = "s_m_y_cop_01"; // Model name of the NPC
    private readonly int weaponHash = Function.Call<int>(Hash.GET_HASH_KEY, "WEAPON_RPG"); // Hash for the bazooka weapon
    private readonly List<Ped> npcList = new List<Ped>(); // List to store created NPCs

    // Constructor
    public BazookaNPCAttack()
    {
        // Initialize the script
        this.Tick += OnTick; // Subscribe to the Tick event
        this.KeyDown += OnKeyDown; // Subscribe to the KeyDown event
    }

    // Create an NPC with bazooka behavior
    private void CreateBazookaNPC(Vector3 position)
    {
        try
        {
            // Load the NPC model
            Function.Call(Hash.REQUEST_MODEL, npcModel);
            while (!Function.Call<bool>(Hash.HAS_MODEL_LOADED, npcModel))
            {
                Script.Yield();
            }

            // Create the NPC
            Ped npc = World.CreatePed(npcModel, position);
            npc.GiveWeapon(weaponHash, 10, true, true); // Give the NPC a bazooka with 10 ammo
            npc.Task.RunTo(new Vector3(position.X + 10, position.Y, position.Z)); // NPC runs to a specified position

            // Add the NPC to the list
            npcList.Add(npc);
        }
        catch (Exception ex)
        {
            UI.Notify($"Error creating NPC: {ex.Message}"); // Notify on error
        }
    }

    // Handle key press for spawning NPC
    private void OnKeyDown(object sender, GTA.KeyEventArgs e)
    {
        if (e.KeyCode == System.Windows.Forms.Keys.F5) // Change the key as needed
        {
            Vector3 playerPosition = Game.Player.Character.Position; // Get player's position
            CreateBazookaNPC(playerPosition); // Create the NPC at the player's location
        }
    }

    // Main logic executed every tick
    private void OnTick(object sender, EventArgs e)
    {
        foreach (Ped npc in npcList)
        {
            if (npc.IsAlive && npc.CurrentPedWeapon != null)
            {
                // Check if NPC can shoot
                if (Game.Player.Character.Position.DistanceTo(npc.Position) < 50f) // Check distance to player
                {
                    npc.Task.FireWeaponAt(Game.Player.Character, -1, false); // Attack the player
                }
            }
            else
            {
                npcList.Remove(npc); // Remove dead NPCs from the list
            }
        }
    }
}
```

**Note:** To compile and run this script, ensure you have the Community Script Hook V .NET installed and configured properly in your GTA V environment.
