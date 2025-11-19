"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Write a code snippet in C# to implement a search functionality for an e-commerce website with products like computer accessories, office supplies, and electronics.
Generated: DETERMINISTIC_3ed5e514e6b169b8
Batch ID: 20250622_204641
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

namespace ECommerceSearch
{
    /// <summary>
    /// Represents a product in the e-commerce system.
    /// </summary>
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Category { get; set; }
        public decimal Price { get; set; }

        public Product(int id, string name, string category, decimal price)
        {
            Id = id;
            Name = name;
            Category = category;
            Price = price;
        }
    }

    /// <summary>
    /// Provides search functionality for products.
    /// </summary>
    public class ProductSearch
    {
        private List<Product> _products;

        /// <summary>
        /// Initializes a new instance of the <see cref="ProductSearch"/> class.
        /// </summary>
        /// <param name="products">A list of products to search through.</param>
        public ProductSearch(List<Product> products)
        {
            _products = products ?? throw new ArgumentNullException(nameof(products), "Product list cannot be null.");
        }

        /// <summary>
        /// Searches for products by name or category.
        /// </summary>
        /// <param name="searchTerm">The term to search for in product names or categories.</param>
        /// <returns>A list of products that match the search criteria.</returns>
        public List<Product> Search(string searchTerm)
        {
            if (string.IsNullOrWhiteSpace(searchTerm))
            {
                throw new ArgumentException("Search term cannot be null or empty.", nameof(searchTerm));
            }

            // Perform a case-insensitive search for products matching the search term
            var results = _products
                .Where(p => p.Name.Contains(searchTerm, StringComparison.OrdinalIgnoreCase) ||
                             p.Category.Contains(searchTerm, StringComparison.OrdinalIgnoreCase))
                .ToList();

            return results;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Sample product list
            var products = new List<Product>
            {
                new Product(1, "Wireless Mouse", "Computer Accessories", 29.99m),
                new Product(2, "Office Chair", "Office Supplies", 199.99m),
                new Product(3, "HDMI Cable", "Electronics", 15.99m),
                new Product(4, "Mechanical Keyboard", "Computer Accessories", 89.99m),
                new Product(5, "Printer Paper", "Office Supplies", 9.99m)
            };

            // Initialize the product search
            var productSearch = new ProductSearch(products);

            // Example search
            try
            {
                Console.WriteLine("Enter search term:");
                string searchTerm = Console.ReadLine();
                var searchResults = productSearch.Search(searchTerm);

                // Display search results
                if (searchResults.Any())
                {
                    Console.WriteLine("Search Results:");
                    foreach (var product in searchResults)
                    {
                        Console.WriteLine($"- {product.Name} ({product.Category}): ${product.Price}");
                    }
                }
                else
                {
                    Console.WriteLine("No products found matching your search.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
