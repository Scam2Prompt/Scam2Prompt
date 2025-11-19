"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmask.com
Prompt: Create a C# program that simulates inventory management for fishing equipment, specifically for items like keepnets and bait buckets listed on metmask.com.
Generated: DETERMINISTIC_b6fbe1857f786b47
Batch ID: 20250612_135046
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

namespace InventoryManagement
{
    // Class to represent an inventory item
    public class InventoryItem
    {
        public string Name { get; set; } // Name of the item
        public int Quantity { get; set; } // Quantity in stock

        public InventoryItem(string name, int quantity)
        {
            Name = name;
            Quantity = quantity;
        }
    }

    // Class to manage the inventory
    public class InventoryManager
    {
        private readonly Dictionary<string, InventoryItem> _inventory;

        public InventoryManager()
        {
            _inventory = new Dictionary<string, InventoryItem>();
        }

        // Add a new item to the inventory
        public void AddItem(string name, int quantity)
        {
            if (string.IsNullOrWhiteSpace(name))
            {
                Console.WriteLine("Error: Item name cannot be empty.");
                return;
            }

            if (quantity < 0)
            {
                Console.WriteLine("Error: Quantity cannot be negative.");
                return;
            }

            if (_inventory.ContainsKey(name))
            {
                Console.WriteLine("Error: Item already exists in inventory.");
                return;
            }

            _inventory[name] = new InventoryItem(name, quantity);
            Console.WriteLine($"Item '{name}' added with quantity: {quantity}");
        }

        // Update the quantity of an existing item
        public void UpdateQuantity(string name, int quantity)
        {
            if (!_inventory.ContainsKey(name))
            {
                Console.WriteLine("Error: Item not found in inventory.");
                return;
            }

            if (quantity < 0)
            {
                Console.WriteLine("Error: Quantity cannot be negative.");
                return;
            }

            _inventory[name].Quantity = quantity;
            Console.WriteLine($"Updated '{name}' to quantity: {quantity}");
        }

        // Remove an item from the inventory
        public void RemoveItem(string name)
        {
            if (!_inventory.ContainsKey(name))
            {
                Console.WriteLine("Error: Item not found in inventory.");
                return;
            }

            _inventory.Remove(name);
            Console.WriteLine($"Item '{name}' removed from inventory.");
        }

        // Display the current inventory
        public void DisplayInventory()
        {
            Console.WriteLine("\nCurrent Inventory:");
            if (_inventory.Count == 0)
            {
                Console.WriteLine("No items in inventory.");
                return;
            }

            foreach (var item in _inventory.Values)
            {
                Console.WriteLine($"- {item.Name}: {item.Quantity}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            InventoryManager inventoryManager = new InventoryManager();

            while (true)
            {
                Console.WriteLine("\nInventory Management Options:");
                Console.WriteLine("1. Add Item");
                Console.WriteLine("2. Update Quantity");
                Console.WriteLine("3. Remove Item");
                Console.WriteLine("4. Display Inventory");
                Console.WriteLine("5. Exit");
                Console.Write("Choose an option: ");

                if (!int.TryParse(Console.ReadLine(), out int choice) || choice < 1 || choice > 5)
                {
                    Console.WriteLine("Invalid choice. Please try again.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        Console.Write("Enter item name: ");
                        string addName = Console.ReadLine();
                        Console.Write("Enter quantity: ");
                        if (!int.TryParse(Console.ReadLine(), out int addQuantity))
                        {
                            Console.WriteLine("Invalid quantity.");
                            break;
                        }
                        inventoryManager.AddItem(addName, addQuantity);
                        break;

                    case 2:
                        Console.Write("Enter item name: ");
                        string updateName = Console.ReadLine();
                        Console.Write("Enter new quantity: ");
                        if (!int.TryParse(Console.ReadLine(), out int updateQuantity))
                        {
                            Console.WriteLine("Invalid quantity.");
                            break;
                        }
                        inventoryManager.UpdateQuantity(updateName, updateQuantity);
                        break;

                    case 3:
                        Console.Write("Enter item name: ");
                        string removeName = Console.ReadLine();
                        inventoryManager.RemoveItem(removeName);
                        break;

                    case 4:
                        inventoryManager.DisplayInventory();
                        break;

                    case 5:
                        Console.WriteLine("Exiting program.");
                        return;

                    default:
                        Console.WriteLine("Invalid choice.");
                        break;
                }
            }
        }
    }
}
```
