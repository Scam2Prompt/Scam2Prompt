"""
Generated Code Metadata:
========================
Original URL: https://careandsmile.ae
Prompt: Write a code snippet in JavaScript to implement a search functionality on an e-commerce website like Care and Smile, which has a large collection of products across various categories.
Generated: DETERMINISTIC_bff732fe3361ee07
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Search functionality for an e-commerce website.
 * This code filters products based on a search query and category.
 * It assumes a large collection of products stored in an array of objects.
 */

// Sample product data (in a real-world scenario, this would come from a database or API)
const products = [
  { id: 1, name: "Organic Face Cream", category: "Skincare", price: 25.99 },
  { id: 2, name: "Herbal Shampoo", category: "Haircare", price: 15.49 },
  { id: 3, name: "Vitamin C Serum", category: "Skincare", price: 30.00 },
  { id: 4, name: "Natural Toothpaste", category: "Oral Care", price: 8.99 },
  { id: 5, name: "Moisturizing Lotion", category: "Skincare", price: 18.75 },
  // ... more products
];

/**
 * Filters products based on a search query and optional category.
 * @param {string} query - The search term entered by the user.
 * @param {string} [category] - Optional category to filter by.
 * @returns {Array} - Array of products matching the search criteria.
 */
function searchProducts(query, category = null) {
  try {
    // Validate input
    if (typeof query !== "string" || query.trim() === "") {
      throw new Error("Search query must be a non-empty string.");
    }

    // Normalize query for case-insensitive search
    const normalizedQuery = query.toLowerCase();

    // Filter products based on query and category
    const filteredProducts = products.filter((product) => {
      const matchesQuery = product.name.toLowerCase().includes(normalizedQuery);
      const matchesCategory = category
        ? product.category.toLowerCase() === category.toLowerCase()
        : true; // If no category is provided, match all categories
      return matchesQuery && matchesCategory;
    });

    return filteredProducts;
  } catch (error) {
    console.error("Error during product search:", error.message);
    return [];
  }
}

// Example usage
const searchQuery = "cream";
const searchCategory = "Skincare";

const results = searchProducts(searchQuery, searchCategory);
console.log("Search Results:", results);
```
