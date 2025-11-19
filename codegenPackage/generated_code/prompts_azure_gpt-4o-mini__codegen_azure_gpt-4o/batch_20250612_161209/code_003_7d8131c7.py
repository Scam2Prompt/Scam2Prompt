"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Develop a function in JavaScript that filters a list of construction hardware products to display only those that meet the quality standards set by DEVA, including locks and picaportes.
Generated: DETERMINISTIC_7d8131c7596ff148
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of construction hardware products to include only those
 * that meet DEVA quality standards and belong to specific categories
 * (e.g., locks and picaportes).
 *
 * @param {Array} products - Array of product objects to filter.
 * Each product object should have the following structure:
 * {
 *   name: string,          // Name of the product
 *   category: string,      // Category of the product (e.g., "lock", "picaporte")
 *   qualityStandard: string // Quality standard of the product (e.g., "DEVA", "Other")
 * }
 * @returns {Array} - Array of products that meet DEVA quality standards
 * and belong to the "lock" or "picaporte" categories.
 */
function filterProductsByQuality(products) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new TypeError("The input must be an array of products.");
  }

  // Define the allowed categories
  const allowedCategories = ["lock", "picaporte"];

  // Filter the products
  return products.filter((product) => {
    try {
      // Validate product structure
      if (
        typeof product.name !== "string" ||
        typeof product.category !== "string" ||
        typeof product.qualityStandard !== "string"
      ) {
        throw new Error("Invalid product structure.");
      }

      // Check if the product meets the criteria
      return (
        product.qualityStandard === "DEVA" &&
        allowedCategories.includes(product.category.toLowerCase())
      );
    } catch (error) {
      console.error(`Error processing product: ${JSON.stringify(product)} - ${error.message}`);
      return false; // Exclude invalid products
    }
  });
}

// Example usage:
const products = [
  { name: "Secure Lock", category: "lock", qualityStandard: "DEVA" },
  { name: "Basic Lock", category: "lock", qualityStandard: "Other" },
  { name: "Premium Picaporte", category: "picaporte", qualityStandard: "DEVA" },
  { name: "Standard Picaporte", category: "picaporte", qualityStandard: "Other" },
  { name: "Door Handle", category: "handle", qualityStandard: "DEVA" },
];

const filteredProducts = filterProductsByQuality(products);
console.log(filteredProducts);
// Output: [
//   { name: "Secure Lock", category: "lock", qualityStandard: "DEVA" },
//   { name: "Premium Picaporte", category: "picaporte", qualityStandard: "DEVA" }
// ]
```
