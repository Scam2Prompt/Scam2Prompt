"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a JavaScript code to create a simple product filter for a sports equipment website, allowing users to filter by sport (e.g., beach volleyball, handball, etc.) and product type (e.g., balls, shoes, etc.).
Generated: DETERMINISTIC_4fc72dbbefdbfdda
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Filter for a Sports Equipment Website

// Sample product data
const products = [
  { id: 1, name: "Beach Volleyball Ball", sport: "Beach Volleyball", type: "Ball" },
  { id: 2, name: "Handball Shoes", sport: "Handball", type: "Shoes" },
  { id: 3, name: "Beach Volleyball Net", sport: "Beach Volleyball", type: "Net" },
  { id: 4, name: "Handball Ball", sport: "Handball", type: "Ball" },
  { id: 5, name: "Running Shoes", sport: "Running", type: "Shoes" },
];

// Function to filter products by sport and type
/**
 * Filters products based on sport and product type.
 * @param {string} sport - The sport to filter by (e.g., "Beach Volleyball").
 * @param {string} type - The product type to filter by (e.g., "Ball").
 * @returns {Array} - Array of filtered products.
 */
function filterProducts(sport, type) {
  try {
    // Validate input
    if (typeof sport !== "string" || typeof type !== "string") {
      throw new Error("Invalid input: sport and type must be strings.");
    }

    // Filter products based on sport and type
    const filteredProducts = products.filter(
      (product) =>
        product.sport.toLowerCase() === sport.toLowerCase() &&
        product.type.toLowerCase() === type.toLowerCase()
    );

    return filteredProducts;
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Example usage
const sportFilter = "Beach Volleyball";
const typeFilter = "Ball";

const filteredResults = filterProducts(sportFilter, typeFilter);
console.log("Filtered Products:", filteredResults);

// Output:
// Filtered Products: [ { id: 1, name: 'Beach Volleyball Ball', sport: 'Beach Volleyball', type: 'Ball' } ]
```
