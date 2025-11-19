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

/// <summary>
/// Represents a refractory product with its alumina content.
/// </summary>
public class RefractoryProduct
{
    public string Name { get; set; }
    public double AluminaContent { get; set; }

    public RefractoryProduct(string name, double aluminaContent)
    {
        Name = name;
        AluminaContent = aluminaContent;
    }
}

public class RefractoryProductFilter
{
    private List<RefractoryProduct> products;

    public RefractoryProductFilter(List<RefractoryProduct> products)
    {
        this.products = products;
    }

    /// <summary>
    /// Filters refractory products based on a specific alumina content range.
    /// </summary>
    /// <param name="minAluminaContent">The minimum alumina content.</param>
    /// <param name="maxAluminaContent">The maximum alumina content.</param>
    /// <returns>A list of refractory products within the specified alumina content range.</returns>
    public List<RefractoryProduct> FilterByAluminaContent(double minAluminaContent, double maxAluminaContent)
    {
        if (minAluminaContent < 0 || maxAluminaContent < 0)
        {
            throw new ArgumentException("Alumina content cannot be negative.");
        }

        if (minAluminaContent > maxAluminaContent)
        {
            throw new ArgumentException("Invalid alumina content range.");
        }

        return products
            .Where(p => p.AluminaContent >= minAluminaContent && p.AluminaContent <= maxAluminaContent)
            .ToList();
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Sample refractory products with their alumina content.
        var products = new List<RefractoryProduct>
        {
            new RefractoryProduct("Product A", 70.0),
            new RefractoryProduct("Product B", 85.0),
            new RefractoryProduct("Product C", 90.0),
            new RefractoryProduct("Product D", 60.0),
            new RefractoryProduct("Product E", 80.0),
        };

        var filter = new RefractoryProductFilter(products);

        try
        {
            double minAluminaContent = 80.0;
            double maxAluminaContent = 90.0;

            var filteredProducts = filter.FilterByAluminaContent(minAluminaContent, maxAluminaContent);

            Console.WriteLine($"Refractory products with alumina content between {minAluminaContent}% and {maxAluminaContent}%:");
            foreach (var product in filteredProducts)
            {
                Console.WriteLine($"{product.Name}: {product.AluminaContent}%");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
