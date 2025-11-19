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

namespace RefractoryProductsFilter
{
    class Program
    {
        // Define a class to represent a refractory product
        public class RefractoryProduct
        {
            public string Name { get; set; } // Name of the product
            public double AluminaContent { get; set; } // Alumina content percentage
        }

        static void Main(string[] args)
        {
            try
            {
                // Initialize a list of refractory products with their alumina content
                List<RefractoryProduct> products = new List<RefractoryProduct>
                {
                    new RefractoryProduct { Name = "Product A", AluminaContent = 45.0 },
                    new RefractoryProduct { Name = "Product B", AluminaContent = 60.5 },
                    new RefractoryProduct { Name = "Product C", AluminaContent = 70.0 },
                    new RefractoryProduct { Name = "Product D", AluminaContent = 80.0 },
                    new RefractoryProduct { Name = "Product E", AluminaContent = 90.0 }
                };

                // Prompt the user for the alumina content range
                Console.WriteLine("Enter the minimum alumina content percentage:");
                double minContent = GetValidDoubleInput();

                Console.WriteLine("Enter the maximum alumina content percentage:");
                double maxContent = GetValidDoubleInput();

                // Filter the products based on the specified range
                var filteredProducts = products
                    .Where(p => p.AluminaContent >= minContent && p.AluminaContent <= maxContent)
                    .ToList();

                // Display the filtered products
                Console.WriteLine("\nFiltered Products:");
                if (filteredProducts.Any())
                {
                    foreach (var product in filteredProducts)
                    {
                        Console.WriteLine($"- {product.Name} (Alumina Content: {product.AluminaContent}%)");
                    }
                }
                else
                {
                    Console.WriteLine("No products found within the specified range.");
                }
            }
            catch (Exception ex)
            {
                // Handle unexpected errors gracefully
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Reads and validates user input as a double value.
        /// </summary>
        /// <returns>A valid double value entered by the user.</returns>
        private static double GetValidDoubleInput()
        {
            while (true)
            {
                string input = Console.ReadLine();
                if (double.TryParse(input, out double result))
                {
                    return result;
                }
                Console.WriteLine("Invalid input. Please enter a valid number:");
            }
        }
    }
}
```
