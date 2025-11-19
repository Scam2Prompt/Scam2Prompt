"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moontropica.pages.dev
Prompt: Provide an example of how to implement a dynamic combat system for a game inspired by Moon Tropica using C#.
Generated: DETERMINISTIC_88def62aa69a8965
Batch ID: 20250612_163518
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

namespace DynamicCombatSystem
{
    // Enum representing different types of actions in combat
    public enum CombatActionType
    {
        Attack,
        Defend,
        Heal,
        Special
    }

    // Class representing a combatant (player or enemy)
    public class Combatant
    {
        public string Name { get; private set; }
        public int Health { get; private set; }
        public int AttackPower { get; private set; }
        public int DefensePower { get; private set; }

        public Combatant(string name, int health, int attackPower, int defensePower)
        {
            Name = name;
            Health = health;
            AttackPower = attackPower;
            DefensePower = defensePower;
        }

        // Method to perform an attack on another combatant
        public void Attack(Combatant target)
        {
            int damage = Math.Max(0, AttackPower - target.DefensePower);
            target.TakeDamage(damage);
            Console.WriteLine($"{Name} attacks {target.Name} for {damage} damage.");
        }

        // Method to take damage
        public void TakeDamage(int damage)
        {
            Health -= damage;
            if (Health < 0) Health = 0;
            Console.WriteLine($"{Name} has {Health} health left.");
        }

        // Method to heal the combatant
        public void Heal(int amount)
        {
            Health += amount;
            Console.WriteLine($"{Name} heals for {amount}. Current health: {Health}");
        }
    }

    // Class representing a combat action
    public class CombatAction
    {
        public CombatActionType ActionType { get; private set; }
        public Combatant Performer { get; private set; }
        public Combatant Target { get; private set; }
        public int Value { get; private set; }

        public CombatAction(CombatActionType actionType, Combatant performer, Combatant target, int value = 0)
        {
            ActionType = actionType;
            Performer = performer;
            Target = target;
            Value = value;
        }

        // Execute the combat action
        public void Execute()
        {
            switch (ActionType)
            {
                case CombatActionType.Attack:
                    Performer.Attack(Target);
                    break;

                case CombatActionType.Defend:
                    Console.WriteLine($"{Performer.Name} defends.");
                    // Implement defense logic if needed
                    break;

                case CombatActionType.Heal:
                    Performer.Heal(Value);
                    break;

                case CombatActionType.Special:
                    Console.WriteLine($"{Performer.Name} performs a special action!");
                    // Implement special action logic if needed
                    break;

                default:
                    throw new ArgumentOutOfRangeException(nameof(ActionType), "Invalid combat action type.");
            }
        }
    }

    // Class representing the combat system
    public class CombatSystem
    {
        private List<Combatant> combatants;

        public CombatSystem()
        {
            combatants = new List<Combatant>();
        }

        // Add a combatant to the combat system
        public void AddCombatant(Combatant combatant)
        {
            if (combatant == null)
                throw new ArgumentNullException(nameof(combatant), "Combatant cannot be null.");
            
            combatants.Add(combatant);
            Console.WriteLine($"{combatant.Name} has joined the battle!");
        }

        // Start the combat
        public void StartCombat()
        {
            // Example combat loop - can be expanded for turn-based or real-time system
            while (combatants.Count > 1)
            {
                foreach (var attacker in combatants)
                {
                    if (attacker.Health <= 0) continue;

                    // Simple targeting logic: target the first enemy found
                    var target = combatants.Find(c => c != attacker && c.Health > 0);
                    if (target == null) break; // No target available

                    // Create a random action (for demonstration purposes)
                    CombatActionType actionType = (CombatActionType)new Random().Next(0, 4);
                    int healAmount = actionType == CombatActionType.Heal ? 10 : 0;

                    CombatAction action = new CombatAction(actionType, attacker, target, healAmount);
                    action.Execute();
                }
            }

            // Display the result
            Console.WriteLine("Combat has ended.");
        }
    }

    // Main class to run the combat system
    public class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                CombatSystem combatSystem = new CombatSystem();

                // Create combatants
                Combatant hero = new Combatant("Hero", 100, 20, 5);
                Combatant monster = new Combatant("Monster", 80, 15, 3);

                // Add combatants to the combat system
                combatSystem.AddCombatant(hero);
                combatSystem.AddCombatant(monster);

                // Start combat
                combatSystem.StartCombat();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
