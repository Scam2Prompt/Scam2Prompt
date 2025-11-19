"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a code snippet in C# to generate a catalog of door hardware products, including keypads, deadbolts, and handle sets, with their corresponding prices and availability.
Generated: DETERMINISTIC_311ecf9e417d97c2
Batch ID: 20250622_210650
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

namespace DoorHardwareCatalog
{
    // Class representing a product in the catalog
    public class Product
    {
        public string Name { get; set; } // Name of the product
        public decimal Price { get; set; } // Price of the product
        public bool IsAvailable { get; set; } // Availability status

        // Constructor to initialize product properties
        public Product(string name, decimal price, bool isAvailable)
        {
            Name = name;
            Price = price;
            IsAvailable = isAvailable;
        }

        // Method to display product details
        public override string ToString()
        {
            return $"{Name} - ${Price:F2} - {(IsAvailable ? "Available" : "Out of Stock")}";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Create a catalog of door hardware products
                List<Product> catalog = new List<Product>
                {
                    new Product("Keypad Lock", 99.99m, true),
                    new Product("Deadbolt Lock", 49.99m, false),
                    new Product("Handle Set", 79.99m, true),
                    new Product("Smart Keypad Lock", 129.99m, true),
                    new Product("Decorative Handle Set", 89.99m, false)
                };

                // Display the catalog
                Console.WriteLine("Door Hardware Product Catalog:");
                Console.WriteLine("--------------------------------");
                foreach (var product in catalog)
                {
                    Console.WriteLine(product.ToString());
                }
            }
            catch (Exception ex)
            {
                // Handle unexpected errors gracefully
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
