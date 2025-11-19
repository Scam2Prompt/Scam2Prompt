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
 * Uniform Order Cost Estimator
 * 
 * Estimates the cost of uniform orders based on material, quantity, and design complexity.
 */

// Define a class for the Uniform Order Cost Estimator
class UniformOrderEstimator {
  /**
   * Material costs per unit
   * @type {Object}
   */
  static MATERIAL_COSTS = {
    basic: 5.00,
    premium: 10.00,
    deluxe: 15.00
  };

  /**
   * Design complexity levels and their corresponding costs
   * @type {Object}
   */
  static DESIGN_COMPLEXITY_COSTS = {
    simple: 0.00,
    moderate: 2.00,
    complex: 5.00
  };

  /**
   * Estimates the cost of a uniform order
   * @param {string} material - The material type (basic, premium, deluxe)
   * @param {number} quantity - The quantity of uniforms ordered
   * @param {string} designComplexity - The design complexity level (simple, moderate, complex)
   * @returns {number} The estimated cost of the uniform order
   */
  static estimateCost(material, quantity, designComplexity) {
    // Validate input parameters
    if (!UniformOrderEstimator.MATERIAL_COSTS[material]) {
      throw new Error(`Invalid material type: ${material}`);
    }

    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Quantity must be a positive number');
    }

    if (!UniformOrderEstimator.DESIGN_COMPLEXITY_COSTS[designComplexity]) {
      throw new Error(`Invalid design complexity level: ${designComplexity}`);
    }

    // Calculate the material cost
    const materialCost = UniformOrderEstimator.MATERIAL_COSTS[material];

    // Calculate the design complexity cost
    const designComplexityCost = UniformOrderEstimator.DESIGN_COMPLEXITY_COSTS[designComplexity];

    // Calculate the total cost
    const totalCost = (materialCost + designComplexityCost) * quantity;

    return totalCost;
  }
}

// Example usage
try {
  const material = 'premium';
  const quantity = 100;
  const designComplexity = 'moderate';

  const estimatedCost = UniformOrderEstimator.estimateCost(material, quantity, designComplexity);
  console.log(`Estimated cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
