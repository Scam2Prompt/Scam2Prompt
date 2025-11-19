"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Create a JavaScript function that filters a list of herbal products based on their health benefits, particularly those related to boosting stamina and immune support as highlighted on HNU's website.
Generated: DETERMINISTIC_6c71ff932b34b885
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of herbal products based on specific health benefits.
 * 
 * @param {Array<Object>} products - The list of herbal products. Each product is an object with `name` and `benefits` properties.
 * @param {Array<String>} targetBenefits - The health benefits to filter by (e.g., "stamina", "immune support").
 * @returns {Array<Object>} - A filtered list of herbal products that match the target health benefits.
 */
function filterHerbalProductsByBenefits(products, targetBenefits) {
  // Validate inputs
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: products must be an array.");
  }
  if (!Array.isArray(targetBenefits)) {
    throw new Error("Invalid input: targetBenefits must be an array.");
  }

  // Filter the products
  return products.filter(product => {
    if (!product || !product.benefits || !Array.isArray(product.benefits)) {
      // Skip invalid product entries
      return false;
    }

    // Check if at least one of the target benefits is included in the product's benefits
    return targetBenefits.some(benefit => product.benefits.includes(benefit));
  });
}

// Example usage:
// A list of herbal products with their associated health benefits
const herbalProducts = [
  { name: "Ginseng Root", benefits: ["stamina", "energy boost", "immune support"] },
  { name: "Elderberry Syrup", benefits: ["immune support", "cold relief"] },
  { name: "Ashwagandha Powder", benefits: ["stress relief", "stamina"] },
  { name: "Chamomile Tea", benefits: ["calming", "sleep aid"] }
];

// Desired health benefits to filter by
const targetBenefits = ["stamina", "immune support"];

// Call the function and log the result
const filteredProducts = filterHerbalProductsByBenefits(herbalProducts, targetBenefits);
console.log(filteredProducts);

// Output:
// [
//   { name: "Ginseng Root", benefits: ["stamina", "energy boost", "immune support"] },
//   { name: "Elderberry Syrup", benefits: ["immune support", "cold relief"] },
//   { name: "Ashwagandha Powder", benefits: ["stress relief", "stamina"] }
// ]
```
