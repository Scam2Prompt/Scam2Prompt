"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Create a JavaScript function to filter and sort baby products by category, price, and age range."
Generated: DETERMINISTIC_95ddc2a3b1fa40ae
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and sorts baby products by category, price, and age range.
 * 
 * @param {Array} products - Array of product objects. Each product should have:
 *                           - `name` (string): Name of the product
 *                           - `category` (string): Category of the product (e.g., "toys", "clothing")
 *                           - `price` (number): Price of the product
 *                           - `ageRange` (string): Age range for the product (e.g., "0-6 months", "1-2 years")
 * @param {Object} filters - Filtering criteria:
 *                           - `category` (string): Category to filter by (optional)
 *                           - `minPrice` (number): Minimum price (optional)
 *                           - `maxPrice` (number): Maximum price (optional)
 *                           - `ageRange` (string): Age range to filter by (optional)
 * @param {string} sortBy - Sorting criteria: "priceAsc" (ascending price), "priceDesc" (descending price)
 * @returns {Array} - Filtered and sorted array of products.
 */
function filterAndSortBabyProducts(products, filters, sortBy) {
  try {
    // Validate input
    if (!Array.isArray(products)) {
      throw new Error("Invalid input: 'products' must be an array.");
    }
    if (typeof filters !== "object" || filters === null) {
      throw new Error("Invalid input: 'filters' must be an object.");
    }
    if (typeof sortBy !== "string") {
      throw new Error("Invalid input: 'sortBy' must be a string.");
    }

    // Apply filters
    let filteredProducts = products.filter(product => {
      // Filter by category
      if (filters.category && product.category !== filters.category) {
        return false;
      }
      // Filter by price range
      if (filters.minPrice && product.price < filters.minPrice) {
        return false;
      }
      if (filters.maxPrice && product.price > filters.maxPrice) {
        return false;
      }
      // Filter by age range
      if (filters.ageRange && product.ageRange !== filters.ageRange) {
        return false;
      }
      return true;
    });

    // Sort products
    filteredProducts.sort((a, b) => {
      if (sortBy === "priceAsc") {
        return a.price - b.price; // Ascending price
      } else if (sortBy === "priceDesc") {
        return b.price - a.price; // Descending price
      } else {
        throw new Error("Invalid 'sortBy' value. Use 'priceAsc' or 'priceDesc'.");
      }
    });

    return filteredProducts;
  } catch (error) {
    console.error("Error in filterAndSortBabyProducts:", error.message);
    return []; // Return an empty array in case of error
  }
}

// Example usage:
const products = [
  { name: "Baby Toy", category: "toys", price: 15, ageRange: "0-6 months" },
  { name: "Baby Clothes", category: "clothing", price: 25, ageRange: "1-2 years" },
  { name: "Baby Bottle", category: "feeding", price: 10, ageRange: "0-6 months" },
  { name: "Baby Shoes", category: "clothing", price: 30, ageRange: "1-2 years" }
];

const filters = { category: "clothing", minPrice: 20, maxPrice: 30, ageRange: "1-2 years" };
const sortBy = "priceAsc";

const result = filterAndSortBabyProducts(products, filters, sortBy);
console.log(result);
```
