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
    /// Represents a product in the e-commerce website.
    /// </summary>
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
    }

    /// <summary>
    /// Provides search functionality for products.
    /// </summary>
    public class ProductSearch
    {
        private readonly List<Product> _products;

        /// <summary>
        /// Initializes a new instance of the <see cref="ProductSearch"/> class.
        /// </summary>
        /// <param name="products">The list of products.</param>
        public ProductSearch(List<Product> products)
        {
            _products = products;
        }

        /// <summary>
        /// Searches for products by keyword.
        /// </summary>
        /// <param name="keyword">The search keyword.</param>
        /// <returns>A list of products matching the search keyword.</returns>
        public List<Product> SearchByKeyword(string keyword)
        {
            if (string.IsNullOrWhiteSpace(keyword))
            {
                throw new ArgumentException("Keyword cannot be empty", nameof(keyword));
            }

            return _products
                .Where(p => p.Name.Contains(keyword, StringComparison.OrdinalIgnoreCase) ||
                            p.Description.Contains(keyword, StringComparison.OrdinalIgnoreCase))
                .ToList();
        }

        /// <summary>
        /// Searches for products by category.
        /// </summary>
        /// <param name="category">The product category.</param>
        /// <returns>A list of products in the specified category.</returns>
        public List<Product> SearchByCategory(string category)
        {
            if (string.IsNullOrWhiteSpace(category))
            {
                throw new ArgumentException("Category cannot be empty", nameof(category));
            }

            return _products
                .Where(p => p.Category.Equals(category, StringComparison.OrdinalIgnoreCase))
                .ToList();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var products = new List<Product>
            {
                new Product { Id = 1, Name = "Wireless Mouse", Description = "A wireless mouse for computers", Category = "Computer Accessories" },
                new Product { Id = 2, Name = "Pen", Description = "A writing pen", Category = "Office Supplies" },
                new Product { Id = 3, Name = "Laptop", Description = "A portable computer", Category = "Electronics" },
                new Product { Id = 4, Name = "Keyboard", Description = "A computer keyboard", Category = "Computer Accessories" },
                new Product { Id = 5, Name = "Notebook", Description = "A notebook for writing", Category = "Office Supplies" },
            };

            var productSearch = new ProductSearch(products);

            Console.WriteLine("Search by keyword:");
            var keywordResults = productSearch.SearchByKeyword("computer");
            foreach (var product in keywordResults)
            {
                Console.WriteLine($"Id: {product.Id}, Name: {product.Name}, Category: {product.Category}");
            }

            Console.WriteLine("\nSearch by category:");
            var categoryResults = productSearch.SearchByCategory("Office Supplies");
            foreach (var product in categoryResults)
            {
                Console.WriteLine($"Id: {product.Id}, Name: {product.Name}, Category: {product.Category}");
            }
        }
    }
}
```
