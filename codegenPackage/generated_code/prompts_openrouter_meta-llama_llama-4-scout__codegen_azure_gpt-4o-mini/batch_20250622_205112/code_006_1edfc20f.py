"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a function in C# to simulate the Forge system, where players can upgrade their weapons using $BIGTIME and other materials.
Generated: DETERMINISTIC_1edfc20f158fcc69
Batch ID: 20250622_205112
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

namespace ForgeSystem
{
    /// <summary>
    /// Represents a weapon with a name and level.
    /// </summary>
    public class Weapon
    {
        public string Name { get; private set; }
        public int Level { get; private set; }

        public Weapon(string name, int level)
        {
            Name = name;
            Level = level;
        }

        /// <summary>
        /// Upgrades the weapon to the next level.
        /// </summary>
        public void Upgrade()
        {
            Level++;
        }
    }

    /// <summary>
    /// Represents the Forge system where players can upgrade their weapons.
    /// </summary>
    public class Forge
    {
        private const int UpgradeCost = 100; // Cost in $BIGTIME to upgrade a weapon
        private Dictionary<string, int> materialsRequired;

        public Forge()
        {
            // Initialize required materials for upgrades
            materialsRequired = new Dictionary<string, int>
            {
                { "Iron", 5 },
                { "Wood", 3 },
                { "Leather", 2 }
            };
        }

        /// <summary>
        /// Upgrades the specified weapon if the player has enough $BIGTIME and materials.
        /// </summary>
        /// <param name="weapon">The weapon to upgrade.</param>
        /// <param name="bigTime">The amount of $BIGTIME the player has.</param>
        /// <param name="playerMaterials">The materials the player has.</param>
        /// <returns>True if the upgrade was successful, otherwise false.</returns>
        public bool UpgradeWeapon(Weapon weapon, int bigTime, Dictionary<string, int> playerMaterials)
        {
            try
            {
                // Check if the player has enough $BIGTIME
                if (bigTime < UpgradeCost)
                {
                    Console.WriteLine("Not enough $BIGTIME to upgrade the weapon.");
                    return false;
                }

                // Check if the player has enough materials
                foreach (var material in materialsRequired)
                {
                    if (!playerMaterials.ContainsKey(material.Key) || playerMaterials[material.Key] < material.Value)
                    {
                        Console.WriteLine($"Not enough {material.Key} to upgrade the weapon.");
                        return false;
                    }
                }

                // Deduct the cost and materials
                bigTime -= UpgradeCost;
                foreach (var material in materialsRequired)
                {
                    playerMaterials[material.Key] -= material.Value;
                }

                // Upgrade the weapon
                weapon.Upgrade();
                Console.WriteLine($"Weapon {weapon.Name} upgraded to level {weapon.Level}.");
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred during the upgrade: {ex.Message}");
                return false;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Example usage of the Forge system
            Weapon sword = new Weapon("Sword", 1);
            int playerBigTime = 150; // Player's $BIGTIME
            Dictionary<string, int> playerMaterials = new Dictionary<string, int>
            {
                { "Iron", 10 },
                { "Wood", 5 },
                { "Leather", 3 }
            };

            Forge forge = new Forge();
            bool upgradeSuccess = forge.UpgradeWeapon(sword, playerBigTime, playerMaterials);

            if (upgradeSuccess)
            {
                Console.WriteLine($"Upgrade successful! New weapon level: {sword.Level}");
            }
            else
            {
                Console.WriteLine("Upgrade failed.");
            }
        }
    }
}
```
