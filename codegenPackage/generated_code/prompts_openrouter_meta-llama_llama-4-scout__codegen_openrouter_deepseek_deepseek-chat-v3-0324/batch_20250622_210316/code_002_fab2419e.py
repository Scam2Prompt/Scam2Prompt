"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Generate a list of refractory products with their corresponding alumina content, and write a simple C# program to filter products based on a specific alumina content range."
Generated: DETERMINISTIC_fab2419eafcd09cd
Batch ID: 20250622_210316
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
using System.Linq;

namespace RefractoryProductFilter
{
    /// <summary>
    /// Represents a refractory product with its properties
    /// </summary>
    public class RefractoryProduct
    {
        public string Name { get; set; }
        public double AluminaContent { get; set; } // Percentage of alumina content

        public RefractoryProduct(string name, double aluminaContent)
        {
            Name = name;
            AluminaContent = aluminaContent;
        }

        public override string ToString()
        {
            return $"{Name} (Alumina: {AluminaContent}%)";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Create a list of refractory products with their alumina content
                List<RefractoryProduct> products = new List<RefractoryProduct>
                {
                    new RefractoryProduct("Fireclay Brick", 30.0),
                    new RefractoryProduct("High Alumina Brick", 60.0),
                    new RefractoryProduct("Mullite Brick", 70.0),
                    new RefractoryProduct("Silica Brick", 5.0),
                    new RefractoryProduct("Corundum Brick", 90.0),
                    new RefractoryProduct("Chrome Brick", 15.0),
                    new RefractoryProduct("Magnesite Brick", 0.0),
                    new RefractoryProduct("Zirconia Brick", 25.0)
                };

                Console.WriteLine("Available Refractory Products:");
                foreach (var product in products)
                {
                    Console.WriteLine(product);
                }

                Console.WriteLine("\nEnter the minimum alumina content percentage:");
                double minAlumina = double.Parse(Console.ReadLine());

                Console.WriteLine("Enter the maximum alumina content percentage:");
                double maxAlumina = double.Parse(Console.ReadLine());

                if (minAlumina > maxAlumina)
                {
                    throw new ArgumentException("Minimum alumina content cannot be greater than maximum.");
                }

                // Filter products within the specified alumina range
                var filteredProducts = products.Where(p => p.AluminaContent >= minAlumina && p.AluminaContent <= maxAlumina);

                Console.WriteLine($"\nProducts with alumina content between {minAlumina}% and {maxAlumina}%:");
                if (filteredProducts.Any())
                {
                    foreach (var product in filteredProducts)
                    {
                        Console.WriteLine(product);
                    }
                }
                else
                {
                    Console.WriteLine("No products found in the specified range.");
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Please enter valid numbers for alumina content.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }
    }
}
```
