"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Write a code snippet in JavaScript to create a simple calculator for estimating the cost of uniform orders based on factors like material, quantity, and design complexity, as discussed on Real Garment's website.
Generated: DETERMINISTIC_60e2b8e2b9fe9f38
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Uniform Cost Calculator
 * This calculator estimates the cost of uniform orders based on material, quantity, and design complexity.
 * Author: [Your Name]
 * Date: [Today's Date]
 */

// Constants for pricing factors
const MATERIAL_COST = {
  cotton: 10, // Cost per unit for cotton
  polyester: 8, // Cost per unit for polyester
  blend: 12 // Cost per unit for blend
};

const DESIGN_COMPLEXITY_COST = {
  simple: 5, // Cost per unit for simple design
  moderate: 10, // Cost per unit for moderate design
  complex: 20 // Cost per unit for complex design
};

/**
 * Function to calculate the total cost of uniform orders
 * @param {string} material - Type of material (cotton, polyester, blend)
 * @param {number} quantity - Number of uniforms to order
 * @param {string} designComplexity - Design complexity (simple, moderate, complex)
 * @returns {number} - Total estimated cost
 */
function calculateUniformCost(material, quantity, designComplexity) {
  try {
    // Validate inputs
    if (!MATERIAL_COST[material]) {
      throw new Error(`Invalid material type: ${material}`);
    }
    if (!DESIGN_COMPLEXITY_COST[designComplexity]) {
      throw new Error(`Invalid design complexity: ${designComplexity}`);
    }
    if (quantity <= 0 || !Number.isInteger(quantity)) {
      throw new Error(`Invalid quantity: ${quantity}. Quantity must be a positive integer.`);
    }

    // Calculate cost
    const materialCost = MATERIAL_COST[material] * quantity;
    const designCost = DESIGN_COMPLEXITY_COST[designComplexity] * quantity;
    const totalCost = materialCost + designCost;

    return totalCost;
  } catch (error) {
    console.error(`Error calculating uniform cost: ${error.message}`);
    return null; // Return null in case of error
  }
}

// Example usage
const material = "cotton";
const quantity = 50;
const designComplexity = "moderate";

const estimatedCost = calculateUniformCost(material, quantity, designComplexity);
if (estimatedCost !== null) {
  console.log(`The estimated cost for ${quantity} uniforms made of ${material} with a ${designComplexity} design is $${estimatedCost}.`);
} else {
  console.log("Failed to calculate the cost due to an error.");
}
```
