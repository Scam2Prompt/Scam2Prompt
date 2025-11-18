"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write JavaScript code to implement a search functionality for a website selling Panasonic products, allowing users to filter by categories like "Đèn LED Panel Panasonic" or "Quạt Trần Đèn Panasonic."
Generated: DETERMINISTIC_b7e9625c08912aa1
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to implement search functionality for a website selling Panasonic products

// Sample dataset of Panasonic products
const products = [
  { id: 1, name: "Đèn LED Panel Panasonic", category: "Đèn LED Panel" },
  { id: 2, name: "Quạt Trần Đèn Panasonic", category: "Quạt Trần Đèn" },
  { id: 3, name: "Đèn LED Âm Trần Panasonic", category: "Đèn LED Âm Trần" },
  { id: 4, name: "Quạt Trần Panasonic 5 Cánh", category: "Quạt Trần Đèn" },
];

// Function to filter products by category
/**
 * Filters products based on the category provided by the user.
 * @param {Array} productList - List of product objects to search within.
 * @param {string} query - The category or search term to filter by.
 * @returns {Array} - List of filtered products matching the search query.
 */
function filterProductsByCategory(productList, query) {
  try {
    // Validate input
    if (!Array.isArray(productList) || typeof query !== "string") {
      throw new Error("Invalid input. Please provide a valid product list and search query.");
    }

    // Perform filtering
    const filteredProducts = productList.filter(
      (product) =>
        product.category.toLowerCase().includes(query.toLowerCase()) ||
        product.name.toLowerCase().includes(query.toLowerCase())
    );

    // Return filtered products
    return filteredProducts;
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return []; // Return an empty array in case of an error
  }
}

// Example usage
/**
 * Runs the search functionality and logs results to the console.
 * @param {string} searchQuery - The category or search term provided by the user.
 */
function runSearch(searchQuery) {
  console.log("Search Query:", searchQuery);
  const results = filterProductsByCategory(products, searchQuery);
  console.log("Search Results:", results);
}

// Example: Filtering products based on user input
runSearch("Đèn LED Panel Panasonic"); // Example search for "Đèn LED Panel Panasonic"
runSearch("Quạt Trần Đèn"); // Example search for "Quạt Trần Đèn"
```
