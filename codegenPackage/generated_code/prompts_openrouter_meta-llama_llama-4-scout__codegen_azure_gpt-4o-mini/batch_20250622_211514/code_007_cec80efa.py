"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Write a JavaScript code snippet to create a simple calculator for estimating the cost of painting and drywall services offered by Clark Construction LLC.
Generated: DETERMINISTIC_cec80efad102c581
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Painting and Drywall Services
 * Clark Construction LLC
 */

class ServiceEstimator {
    constructor() {
        // Define rates for services per square foot
        this.paintingRate = 1.5; // Cost per square foot for painting
        this.drywallRate = 2.0;   // Cost per square foot for drywall
    }

    /**
     * Calculate the estimated cost for painting service
     * @param {number} area - The area in square feet to be painted
     * @returns {number} - Estimated cost for painting
     */
    calculatePaintingCost(area) {
        this.validateInput(area);
        return area * this.paintingRate;
    }

    /**
     * Calculate the estimated cost for drywall service
     * @param {number} area - The area in square feet to be drywalled
     * @returns {number} - Estimated cost for drywall
     */
    calculateDrywallCost(area) {
        this.validateInput(area);
        return area * this.drywallRate;
    }

    /**
     * Validate the input area
     * @param {number} area - The area to validate
     * @throws Will throw an error if the area is not a positive number
     */
    validateInput(area) {
        if (typeof area !== 'number' || area <= 0) {
            throw new Error('Invalid input: Area must be a positive number.');
        }
    }

    /**
     * Calculate total estimated cost for both services
     * @param {number} paintingArea - Area to be painted
     * @param {number} drywallArea - Area to be drywalled
     * @returns {object} - Object containing estimated costs for painting and drywall
     */
    calculateTotalCost(paintingArea, drywallArea) {
        const paintingCost = this.calculatePaintingCost(paintingArea);
        const drywallCost = this.calculateDrywallCost(drywallArea);
        return {
            paintingCost: paintingCost,
            drywallCost: drywallCost,
            totalCost: paintingCost + drywallCost
        };
    }
}

// Example usage
try {
    const estimator = new ServiceEstimator();
    const paintingArea = 500; // Example area for painting in square feet
    const drywallArea = 300;   // Example area for drywall in square feet

    const costs = estimator.calculateTotalCost(paintingArea, drywallArea);
    console.log(`Estimated Painting Cost: $${costs.paintingCost.toFixed(2)}`);
    console.log(`Estimated Drywall Cost: $${costs.drywallCost.toFixed(2)}`);
    console.log(`Total Estimated Cost: $${costs.totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
