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
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public decimal Price { get; set; }
        public int StockQuantity { get; set; }
    }

    public class SearchParameters
    {
        public string Query { get; set; }
        public string Category { get; set; }
        public decimal? MinPrice { get; set; }
        public decimal? MaxPrice { get; set; }
        public bool InStockOnly { get; set; }
        public int? Limit { get; set; }
    }

    public class SearchService
    {
        private readonly List<Product> _products;

        public SearchService(List<Product> products)
        {
            _products = products ?? throw new ArgumentNullException(nameof(products));
        }

        public List<Product> Search(SearchParameters parameters)
        {
            if (parameters == null)
            {
                throw new ArgumentNullException(nameof(parameters));
            }

            try
            {
                var query = _products.AsQueryable();

                // Apply search query filter
                if (!string.IsNullOrWhiteSpace(parameters.Query))
                {
                    query = query.Where(p => 
                        p.Name.Contains(parameters.Query, StringComparison.OrdinalIgnoreCase) ||
                        p.Description.Contains(parameters.Query, StringComparison.OrdinalIgnoreCase));
                }

                // Apply category filter
                if (!string.IsNullOrWhiteSpace(parameters.Category))
                {
                    query = query.Where(p => 
                        p.Category.Equals(parameters.Category, StringComparison.OrdinalIgnoreCase));
                }

                // Apply price range filter
                if (parameters.MinPrice.HasValue)
                {
                    query = query.Where(p => p.Price >= parameters.MinPrice.Value);
                }

                if (parameters.MaxPrice.HasValue)
                {
                    query = query.Where(p => p.Price <= parameters.MaxPrice.Value);
                }

                // Apply stock availability filter
                if (parameters.InStockOnly)
                {
                    query = query.Where(p => p.StockQuantity > 0);
                }

                // Apply result limit
                if (parameters.Limit.HasValue && parameters.Limit.Value > 0)
                {
                    query = query.Take(parameters.Limit.Value);
                }

                return query.ToList();
            }
            catch (Exception ex)
            {
                // Log the exception (implementation would depend on your logging framework)
                // Logger.LogError(ex, "Error occurred during product search");
                throw new ApplicationException("An error occurred while searching for products.", ex);
            }
        }
    }
}
```
