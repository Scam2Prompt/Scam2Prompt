"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Write a C# application that can manage a shopping cart for computer accessories available at Central Multi Computer, including items like SSDs and flash drives.
Generated: DETERMINISTIC_4233db0d3452687c
Batch ID: 20250612_162051
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

// Define a class to represent a product
public class Product
{
    public string Name { get; }
    public decimal Price { get; }

    public Product(string name, decimal price)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("Product name cannot be empty.", nameof(name));
        
        if (price < 0)
            throw new ArgumentOutOfRangeException(nameof(price), "Price cannot be negative.");

        Name = name;
        Price = price;
    }
}

// Define a class to manage the shopping cart
public class ShoppingCart
{
    private readonly List<Product> _items;

    public ShoppingCart()
    {
        _items = new List<Product>();
    }

    // Adds a product to the cart
    public void AddProduct(Product product)
    {
        if (product == null)
            throw new ArgumentNullException(nameof(product), "Product cannot be null.");
        
        _items.Add(product);
    }

    // Removes a product from the cart
    public bool RemoveProduct(Product product)
    {
        if (product == null)
            throw new ArgumentNullException(nameof(product), "Product cannot be null.");

        return _items.Remove(product);
    }

    // Calculates the total price of items in the cart
    public decimal CalculateTotal()
    {
        decimal total = 0;
        foreach (var item in _items)
        {
            total += item.Price;
        }
        return total;
    }

    // Displays products in the cart
    public void DisplayCart()
    {
        if (_items.Count == 0)
        {
            Console.WriteLine("Your cart is empty.");
            return;
        }

        Console.WriteLine("Shopping Cart Contents:");
        foreach (var item in _items)
        {
            Console.WriteLine($"- {item.Name}: ${item.Price:F2}");
        }
    }
}

// Main application to manage the shopping cart
public class Program
{
    public static void Main(string[] args)
    {
        ShoppingCart cart = new ShoppingCart();

        // Sample products
        var ssd = new Product("1TB SSD", 99.99m);
        var flashDrive = new Product("32GB Flash Drive", 14.99m);

        // Add products to the cart
        cart.AddProduct(ssd);
        cart.AddProduct(flashDrive);
        
        // Display current cart
        cart.DisplayCart();

        // Calculate total
        decimal total = cart.CalculateTotal();
        Console.WriteLine($"Total Price: ${total:F2}");

        // Remove a product
        cart.RemoveProduct(flashDrive);
        Console.WriteLine("\nAfter removing the flash drive:");
        cart.DisplayCart();

        // Final total
        total = cart.CalculateTotal();
        Console.WriteLine($"Total Price after removal: ${total:F2}");
    }
}
```
