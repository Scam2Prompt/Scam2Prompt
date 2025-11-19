"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksprut.shop
Prompt: Create a function in JavaScript that filters products on the BLACKSPRUT marketplace by category and displays them in a user-friendly format.
Generated: DETERMINISTIC_b3c9a021e283af4c
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters products by category and displays them in a user-friendly format.
 *
 * @param {Array<Object>} products - Array of product objects. Each product should have 'name', 'description', 'price', and 'category'.
 * @param {string} category - The category to filter products by.
 * @returns {string} - Formatted string representing the filtered products.
 */
function filterProductsByCategory(products, category) {
  try {
    // Validate inputs
    if (!Array.isArray(products)) {
      throw new Error("The 'products' parameter must be an array.");
    }
    if (typeof category !== "string") {
      throw new Error("The 'category' parameter must be a string.");
    }

    // Filter products by category
    const filteredProducts = products.filter(
      (product) => product.category.toLowerCase() === category.toLowerCase()
    );

    // Check if no products match the category
    if (filteredProducts.length === 0) {
      return `No products found in the category: ${category}`;
    }

    // Format the filtered products into a user-friendly string
    const formattedProducts = filteredProducts.map((product) => {
      return `Product Name: ${product.name}\nDescription: ${product.description}\nPrice: $${product.price.toFixed(
        2
      )}\nCategory: ${product.category}\n---`;
    });

    // Join all formatted products into a single string
    return formattedProducts.join("\n");
  } catch (error) {
    // Handle any errors gracefully
    console.error("Error filtering products by category:", error.message);
    return "An error occurred while filtering products. Please try again.";
  }
}

// Example usage:
const products = [
  {
    name: "Laptop",
    description: "A high-performance laptop for work and play.",
    price: 999.99,
    category: "Electronics",
  },
  {
    name: "Headphones",
    description: "Noise-cancelling over-ear headphones.",
    price: 199.99,
    category: "Electronics",
  },
  {
    name: "Coffee Mug",
    description: "A sturdy ceramic mug for your favorite beverage.",
    price: 14.99,
    category: "Home",
  },
];

const categoryToFilter = "Electronics";
console.log(filterProductsByCategory(products, categoryToFilter));
```
