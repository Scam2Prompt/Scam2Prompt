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
 * Simple Calculator for Estimating Uniform Order Costs
 * This calculator estimates the cost based on material, quantity, and design complexity.
 */

// Define a class for the UniformOrderCalculator
class UniformOrderCalculator {
    constructor() {
        // Define base prices for materials
        this.materialPrices = {
            cotton: 10,
            polyester: 15,
            blended: 12
        };

        // Define additional costs for design complexity
        this.designComplexityCosts = {
            simple: 5,
            moderate: 10,
            complex: 20
        };
    }

    /**
     * Calculate the total cost of the uniform order
     * @param {string} material - The material type for the uniforms
     * @param {number} quantity - The number of uniforms to order
     * @param {string} designComplexity - The complexity of the design
     * @returns {number} - The estimated total cost
     * @throws {Error} - Throws an error if invalid parameters are provided
     */
    calculateCost(material, quantity, designComplexity) {
        // Validate input parameters
        if (!this.materialPrices[material]) {
            throw new Error(`Invalid material type: ${material}. Valid options are: ${Object.keys(this.materialPrices).join(', ')}`);
        }
        if (quantity <= 0 || isNaN(quantity)) {
            throw new Error('Quantity must be a positive number.');
        }
        if (!this.designComplexityCosts[designComplexity]) {
            throw new Error(`Invalid design complexity: ${designComplexity}. Valid options are: ${Object.keys(this.designComplexityCosts).join(', ')}`);
        }

        // Calculate the total cost
        const materialCost = this.materialPrices[material] * quantity;
        const designCost = this.designComplexityCosts[designComplexity];
        const totalCost = materialCost + designCost;

        return totalCost;
    }
}

// Example usage
try {
    const calculator = new UniformOrderCalculator();
    const totalCost = calculator.calculateCost('cotton', 50, 'moderate');
    console.log(`The estimated total cost for your uniform order is: $${totalCost}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
