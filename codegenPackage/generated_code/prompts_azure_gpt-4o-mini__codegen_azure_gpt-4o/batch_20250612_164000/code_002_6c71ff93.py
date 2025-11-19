"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Create a JavaScript function that filters a list of herbal products based on their health benefits, particularly those related to boosting stamina and immune support as highlighted on HNU's website.
Generated: DETERMINISTIC_6c71ff932b34b885
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of herbal products based on health benefits.
 * Specifically filters products that boost stamina and immune support.
 *
 * @param {Array} products - Array of herbal product objects.
 * Each product object should have the following structure:
 * {
 *   name: {string}, // Name of the product
 *   benefits: {Array<string>} // List of health benefits
 * }
 * @returns {Array} - Array of filtered products that match the criteria.
 */
function filterHerbalProducts(products) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: products must be an array.");
  }

  // Define the target benefits
  const targetBenefits = ["boost stamina", "immune support"];

  // Filter products based on the target benefits
  return products.filter((product) => {
    // Validate product structure
    if (
      typeof product !== "object" ||
      !product.name ||
      !Array.isArray(product.benefits)
    ) {
      throw new Error("Invalid product structure.");
    }

    // Check if the product has any of the target benefits
    return product.benefits.some((benefit) =>
      targetBenefits.includes(benefit.toLowerCase())
    );
  });
}

// Example usage:
const herbalProducts = [
  {
    name: "Ginseng Tea",
    benefits: ["Boost stamina", "Improve focus"],
  },
  {
    name: "Echinacea Extract",
    benefits: ["Immune support", "Reduce inflammation"],
  },
  {
    name: "Chamomile Tea",
    benefits: ["Relaxation", "Improve sleep"],
  },
];

try {
  const filteredProducts = filterHerbalProducts(herbalProducts);
  console.log("Filtered Products:", filteredProducts);
} catch (error) {
  console.error("Error:", error.message);
}
```
