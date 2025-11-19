"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Write a JavaScript code to implement a product filtering system, similar to the one used on the webpage, to filter shoes by brand (e.g., Nike, Mizuno, Puma) and price range.
Generated: DETERMINISTIC_5ae3c1da72e3ff70
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Filtering System
// This script filters a list of shoes by brand and price range.

// Sample data: Array of shoe objects
const shoes = [
  { id: 1, brand: "Nike", price: 120 },
  { id: 2, brand: "Mizuno", price: 80 },
  { id: 3, brand: "Puma", price: 100 },
  { id: 4, brand: "Nike", price: 150 },
  { id: 5, brand: "Mizuno", price: 60 },
  { id: 6, brand: "Puma", price: 200 },
];

// Function to filter shoes by brand and price range
/**
 * Filters the shoes array based on the provided brand and price range.
 * @param {Array} shoes - Array of shoe objects to filter.
 * @param {string} brand - Brand to filter by (e.g., "Nike", "Mizuno", "Puma"). Pass null to ignore brand filtering.
 * @param {number} minPrice - Minimum price for filtering. Pass null to ignore minimum price.
 * @param {number} maxPrice - Maximum price for filtering. Pass null to ignore maximum price.
 * @returns {Array} - Array of filtered shoe objects.
 */
function filterShoes(shoes, brand = null, minPrice = null, maxPrice = null) {
  try {
    // Validate input
    if (!Array.isArray(shoes)) {
      throw new Error("Invalid input: 'shoes' must be an array.");
    }

    // Filter shoes based on criteria
    return shoes.filter((shoe) => {
      const matchesBrand = brand ? shoe.brand.toLowerCase() === brand.toLowerCase() : true;
      const matchesMinPrice = minPrice !== null ? shoe.price >= minPrice : true;
      const matchesMaxPrice = maxPrice !== null ? shoe.price <= maxPrice : true;

      return matchesBrand && matchesMinPrice && matchesMaxPrice;
    });
  } catch (error) {
    console.error("Error filtering shoes:", error.message);
    return [];
  }
}

// Example usage
const filteredShoes = filterShoes(shoes, "Nike", 100, 150);
console.log("Filtered Shoes:", filteredShoes);

// Example output:
// Filtered Shoes: [ { id: 1, brand: 'Nike', price: 120 }, { id: 4, brand: 'Nike', price: 150 } ]
```
