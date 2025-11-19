"""
Generated Code Metadata:
========================
Original URL: https://metmask.com
Prompt: Create a C# program that simulates inventory management for fishing equipment, specifically for items like keepnets and bait buckets listed on metmask.com.
Generated: DETERMINISTIC_b6fbe1857f786b47
Batch ID: 20250612_135046
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

/// <summary>
/// Represents a fishing equipment item.
/// </summary>
public class FishingEquipment
{
    public string Name { get; set; }
    public decimal Price { get; set; }
    public int Quantity { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="FishingEquipment"/> class.
    /// </summary>
    /// <param name="name">The name of the equipment.</param>
    /// <param name="price">The price of the equipment.</param>
    /// <param name="quantity">The quantity of the equipment.</param>
    public FishingEquipment(string name, decimal price, int quantity)
    {
        Name = name;
        Price = price;
        Quantity = quantity;
    }
}

/// <summary>
/// Represents an inventory of fishing equipment.
/// </summary>
public class FishingEquipmentInventory
{
    private readonly Dictionary<string, FishingEquipment> _equipment;

    /// <summary>
    /// Initializes a new instance of the <see cref="FishingEquipmentInventory"/> class.
    /// </summary>
    public FishingEquipmentInventory()
    {
        _equipment = new Dictionary<string, FishingEquipment>();
    }

    /// <summary>
    /// Adds a new equipment item to the inventory.
    /// </summary>
    /// <param name="equipment">The equipment item to add.</param>
    public void AddEquipment(FishingEquipment equipment)
    {
        if (_equipment.ContainsKey(equipment.Name))
        {
            throw new InvalidOperationException($"Equipment '{equipment.Name}' already exists in the inventory.");
        }

        _equipment.Add(equipment.Name, equipment);
    }

    /// <summary>
    /// Removes an equipment item from the inventory.
    /// </summary>
    /// <param name="name">The name of the equipment item to remove.</param>
    public void RemoveEquipment(string name)
    {
        if (!_equipment.ContainsKey(name))
        {
            throw new KeyNotFoundException($"Equipment '{name}' does not exist in the inventory.");
        }

        _equipment.Remove(name);
    }

    /// <summary>
    /// Updates the quantity of an equipment item in the inventory.
    /// </summary>
    /// <param name="name">The name of the equipment item to update.</param>
    /// <param name="newQuantity">The new quantity of the equipment item.</param>
    public void UpdateQuantity(string name, int newQuantity)
    {
        if (!_equipment.ContainsKey(name))
        {
            throw new KeyNotFoundException($"Equipment '{name}' does not exist in the inventory.");
        }

        if (newQuantity < 0)
        {
            throw new ArgumentException("Quantity cannot be negative.");
        }

        _equipment[name].Quantity = newQuantity;
    }

    /// <summary>
    /// Gets the total value of the inventory.
    /// </summary>
    /// <returns>The total value of the inventory.</returns>
    public decimal GetTotalValue()
    {
        decimal totalValue = 0;

        foreach (var equipment in _equipment.Values)
        {
            totalValue += equipment.Price * equipment.Quantity;
        }

        return totalValue;
    }

    /// <summary>
    /// Prints the current state of the inventory.
    /// </summary>
    public void PrintInventory()
    {
        Console.WriteLine("Current Inventory:");

        foreach (var equipment in _equipment.Values)
        {
            Console.WriteLine($"{equipment.Name}: {equipment.Quantity} x £{equipment.Price:F2} = £{equipment.Price * equipment.Quantity:F2}");
        }

        Console.WriteLine($"Total Value: £{GetTotalValue():F2}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        var inventory = new FishingEquipmentInventory();

        try
        {
            var keepnet = new FishingEquipment("Keepnet", 25.99m, 5);
            var baitBucket = new FishingEquipment("Bait Bucket", 15.99m, 10);

            inventory.AddEquipment(keepnet);
            inventory.AddEquipment(baitBucket);

            inventory.PrintInventory();

            inventory.UpdateQuantity("Keepnet", 3);

            inventory.PrintInventory();

            inventory.RemoveEquipment("Bait Bucket");

            inventory.PrintInventory();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
