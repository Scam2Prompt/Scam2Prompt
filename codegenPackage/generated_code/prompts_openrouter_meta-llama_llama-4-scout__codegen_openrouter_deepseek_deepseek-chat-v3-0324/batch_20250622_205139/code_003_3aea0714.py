"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Develop a simple pricing calculator in JavaScript that scales with the number of sewing machines in a factory, using OpenSeam's linear pricing model with exponential benefits.
Generated: DETERMINISTIC_3aea0714e11931ae
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Pricing calculator for OpenSeam's linear pricing model with exponential benefits.
 * The cost scales linearly with the number of machines, but discounts are applied
 * exponentially based on the quantity.
 */
class PricingCalculator {
    /**
     * @param {number} basePrice - The base price per machine
     * @param {number} discountFactor - The factor by which discount increases exponentially (0 < discountFactor < 1)
     * @throws {Error} If basePrice is negative or discountFactor is outside valid range
     */
    constructor(basePrice, discountFactor) {
        if (basePrice < 0) {
            throw new Error('Base price must be non-negative');
        }
        if (discountFactor <= 0 || discountFactor >= 1) {
            throw new Error('Discount factor must be between 0 and 1');
        }

        this.basePrice = basePrice;
        this.discountFactor = discountFactor;
    }

    /**
     * Calculates the total price for a given number of machines
     * @param {number} numMachines - Number of sewing machines (must be positive integer)
     * @returns {number} Total price after applying exponential benefits
     * @throws {Error} If numMachines is not a positive integer
     */
    calculatePrice(numMachines) {
        if (!Number.isInteger(numMachines) || numMachines <= 0) {
            throw new Error('Number of machines must be a positive integer');
        }

        const discount = 1 - Math.pow(this.discountFactor, numMachines);
        const pricePerMachine = this.basePrice * (1 - discount);
        return pricePerMachine * numMachines;
    }
}

// Example usage:
try {
    const calculator = new PricingCalculator(100, 0.05);
    const machines = 5;
    const totalPrice = calculator.calculatePrice(machines);
    console.log(`Total price for ${machines} machines: $${totalPrice.toFixed(2)}`);
} catch (error) {
    console.error('Error:', error.message);
}
```
