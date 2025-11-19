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

// Class representing a fishing equipment item
public class FishingEquipment
{
    public string Name { get; private set; }
    public int Quantity { get; private set; }

    public FishingEquipment(string name, int quantity)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("Name cannot be null or empty.", nameof(name));
        if (quantity < 0)
            throw new ArgumentOutOfRangeException(nameof(quantity), "Quantity cannot be negative.");

        Name = name;
        Quantity = quantity;
    }

    public void AddStock(int amount)
    {
        if (amount < 0)
            throw new ArgumentOutOfRangeException(nameof(amount), "Amount to add cannot be negative.");

        Quantity += amount;
    }

    public void RemoveStock(int amount)
    {
        if (amount < 0)
            throw new ArgumentOutOfRangeException(nameof(amount), "Amount to remove cannot be negative.");
        if (amount > Quantity)
            throw new InvalidOperationException("Not enough stock to remove.");

        Quantity -= amount;
    }

    public override string ToString()
    {
        return $"{Name}: {Quantity} in stock";
    }
}

// Class representing the inventory
public class Inventory
{
    private readonly Dictionary<string, FishingEquipment> _items;

    public Inventory()
    {
        _items = new Dictionary<string, FishingEquipment>();
    }

    // Method to add a new item to the inventory
    public void AddItem(string name, int quantity)
    {
        if (_items.ContainsKey(name))
        {
            _items[name].AddStock(quantity);
        }
        else
        {
            _items[name] = new FishingEquipment(name, quantity);
        }
    }

    // Method to remove an item from the inventory
    public void RemoveItem(string name, int quantity)
    {
        if (!_items.ContainsKey(name))
            throw new KeyNotFoundException($"Item '{name}' not found in inventory.");

        _items[name].RemoveStock(quantity);

        // Remove item from inventory if quantity is zero
        if (_items[name].Quantity == 0)
            _items.Remove(name);
    }

    // Method to display the current inventory
    public void DisplayInventory()
    {
        if (_items.Count == 0)
        {
            Console.WriteLine("Inventory is empty.");
            return;
        }

        Console.WriteLine("Current Inventory:");
        foreach (var item in _items.Values)
        {
            Console.WriteLine(item);
        }
    }
}

// Main program to simulate inventory management
public class Program
{
    public static void Main(string[] args)
    {
        var inventory = new Inventory();

        try
        {
            // Adding items to inventory
            inventory.AddItem("Keepnet", 10);
            inventory.AddItem("Bait Bucket", 5);

            // Display current inventory
            inventory.DisplayInventory();

            // Removing some items
            inventory.RemoveItem("Keepnet", 3);
            inventory.RemoveItem("Bait Bucket", 2);

            // Display updated inventory
            inventory.DisplayInventory();

            // Attempt to remove more than available
            inventory.RemoveItem("Bait Bucket", 5);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
