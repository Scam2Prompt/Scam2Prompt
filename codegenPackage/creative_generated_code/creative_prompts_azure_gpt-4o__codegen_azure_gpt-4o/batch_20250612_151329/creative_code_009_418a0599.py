"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.insectshieldzoro.com
Prompt: Write a JavaScript function to filter product options for mosquito nets based on fitment type (e.g., Velcro, magnetic, sliding) and material (e.g., stainless steel, fiberglass), as described on the Insect Shield ZORO webpage.
Generated: DETERMINISTIC_418a0599fd3cd6b4
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters product options for mosquito nets based on fitment type and material.
 *
 * @param {Array<Object>} products - Array of product objects to filter. Each product object should have `fitmentType` and `material` properties.
 * @param {String} fitmentType - Desired fitment type (e.g., 'Velcro', 'Magnetic', 'Sliding').
 * @param {String} material - Desired material (e.g., 'Stainless Steel', 'Fiberglass').
 * @returns {Array<Object>} - Array of filtered product objects matching the criteria.
 */
function filterMosquitoNets(products, fitmentType, material) {
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: products must be an array of objects.");
  }

  if (typeof fitmentType !== "string" || typeof material !== "string") {
    throw new Error("Invalid input: fitmentType and material must be strings.");
  }

  return products.filter((product) => {
    // Validate product object structure
    if (typeof product !== "object" || product === null) {
      console.warn("Skipping invalid product: ", product);
      return false;
    }

    const { fitmentType: productFitmentType, material: productMaterial } = product;

    // Check for matching fitment type and material
    return (
      productFitmentType?.toLowerCase() === fitmentType.toLowerCase() &&
      productMaterial?.toLowerCase() === material.toLowerCase()
    );
  });
}

// Example usage
const mosquitoNets = [
  { id: 1, name: "Net A", fitmentType: "Velcro", material: "Stainless Steel" },
  { id: 2, name: "Net B", fitmentType: "Magnetic", material: "Fiberglass" },
  { id: 3, name: "Net C", fitmentType: "Sliding", material: "Stainless Steel" },
  { id: 4, name: "Net D", fitmentType: "Velcro", material: "Fiberglass" },
];

try {
  const filteredNets = filterMosquitoNets(mosquitoNets, "Velcro", "Fiberglass");
  console.log("Filtered Nets:", filteredNets);
} catch (error) {
  console.error("Error filtering mosquito nets:", error.message);
}
```
