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
 * Uniform Cost Calculator
 * Estimates the cost of uniform orders based on material, quantity, and design complexity.
 */

class UniformCostCalculator {
  /**
   * Constructor initializes the calculator with base prices and factors
   */
  constructor() {
    // Base prices for different materials (per unit)
    this.materialPrices = {
      'cotton': 15.00,
      'polyester': 12.00,
      'blend': 10.00,
      'wool': 20.00
    };

    // Design complexity multipliers
    this.designComplexityFactors = {
      'simple': 1.0,
      'standard': 1.2,
      'complex': 1.5,
      'custom': 2.0
    };

    // Discount tiers based on quantity
    this.quantityDiscounts = [
      { min: 1, max: 9, discount: 0.0 },
      { min: 10, max: 49, discount: 0.05 },
      { min: 50, max: 99, discount: 0.1 },
      { min: 100, max: Infinity, discount: 0.15 }
    ];
  }

  /**
   * Calculate the total cost of the uniform order
   * @param {string} material - The material type
   * @param {number} quantity - Number of uniforms
   * @param {string} complexity - Design complexity level
   * @returns {number} Total cost of the order
   * @throws {Error} If invalid parameters are provided
   */
  calculateCost(material, quantity, complexity) {
    // Validate inputs
    if (!this.materialPrices[material]) {
      throw new Error(`Invalid material: ${material}`);
    }

    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error(`Quantity must be a positive integer: ${quantity}`);
    }

    if (!this.designComplexityFactors[complexity]) {
      throw new Error(`Invalid complexity level: ${complexity}`);
    }

    // Calculate base cost
    const baseCost = this.materialPrices[material] * quantity;

    // Apply design complexity factor
    const complexityFactor = this.designComplexityFactors[complexity];
    const complexCost = baseCost * complexityFactor;

    // Apply quantity discount
    const discount = this.getDiscount(quantity);
    const discountedCost = complexCost * (1 - discount);

    // Round to 2 decimal places for currency
    return Math.round(discountedCost * 100) / 100;
  }

  /**
   * Get discount percentage based on quantity
   * @param {number} quantity - Number of uniforms
   * @returns {number} Discount percentage
   */
  getDiscount(quantity) {
    const tier = this.quantityDiscounts.find(t => 
      quantity >= t.min && quantity <= t.max
    );
    return tier ? tier.discount : 0;
  }
}

// Example usage (would typically be in a separate file or UI implementation)
/*
try {
  const calculator = new UniformCostCalculator();
  const cost = calculator.calculateCost('cotton', 50, 'standard');
  console.log(`Total cost: $${cost.toFixed(2)}`);
} catch (error) {
  console.error('Error calculating cost:', error.message);
}
*/
```
