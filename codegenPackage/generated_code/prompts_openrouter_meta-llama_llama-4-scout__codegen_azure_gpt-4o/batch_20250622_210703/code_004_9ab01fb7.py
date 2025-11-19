"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a JavaScript function to calculate the cost of a customized engraving project based on material, size, and complexity.
Generated: DETERMINISTIC_9ab01fb7088a70df
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
 * Function to calculate the cost of a customized engraving project.
 * @param {string} material - The material type (e.g., "wood", "metal", "glass").
 * @param {string} size - The size of the engraving (e.g., "small", "medium", "large").
 * @param {string} complexity - The complexity level (e.g., "simple", "moderate", "complex").
 * @returns {number} - The total cost of the engraving project.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateEngravingCost(material, size, complexity) {
  // Base costs for materials
  const materialCosts = {
    wood: 10,
    metal: 20,
    glass: 15,
  };

  // Size multipliers
  const sizeMultipliers = {
    small: 1,
    medium: 1.5,
    large: 2,
  };

  // Complexity multipliers
  const complexityMultipliers = {
    simple: 1,
    moderate: 1.25,
    complex: 1.5,
  };

  // Validate inputs
  if (!materialCosts[material]) {
    throw new Error(`Invalid material: ${material}. Valid options are: ${Object.keys(materialCosts).join(", ")}`);
  }
  if (!sizeMultipliers[size]) {
    throw new Error(`Invalid size: ${size}. Valid options are: ${Object.keys(sizeMultipliers).join(", ")}`);
  }
  if (!complexityMultipliers[complexity]) {
    throw new Error(`Invalid complexity: ${complexity}. Valid options are: ${Object.keys(complexityMultipliers).join(", ")}`);
  }

  // Calculate cost
  const baseCost = materialCosts[material];
  const sizeMultiplier = sizeMultipliers[size];
  const complexityMultiplier = complexityMultipliers[complexity];

  const totalCost = baseCost * sizeMultiplier * complexityMultiplier;

  // Return the calculated cost
  return totalCost;
}

// Example usage:
try {
  const cost = calculateEngravingCost("wood", "medium", "complex");
  console.log(`The total cost of the engraving project is: $${cost}`);
} catch (error) {
  console.error(error.message);
}
```
