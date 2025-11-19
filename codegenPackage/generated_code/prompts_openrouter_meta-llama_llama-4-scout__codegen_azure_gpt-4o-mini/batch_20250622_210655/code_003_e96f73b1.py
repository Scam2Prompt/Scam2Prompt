"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a code snippet in JavaScript to create a simple calculator for estimating cleaning service costs based on the services offered by Maria HouseKeepers.
Generated: DETERMINISTIC_e96f73b16172b321
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Cleaning Service Costs
 * Maria HouseKeepers
 */

class CleaningServiceCalculator {
    constructor() {
        // Define base rates for different cleaning services
        this.baseRates = {
            'standard': 50, // Standard cleaning service
            'deep': 100,    // Deep cleaning service
            'moveOut': 150, // Move-out cleaning service
            'office': 80    // Office cleaning service
        };
    }

    /**
     * Calculate the total cost based on selected services and quantity
     * @param {Object} services - An object containing service types and their quantities
     * @returns {number} - Total estimated cost
     * @throws {Error} - Throws an error if an invalid service type is provided
     */
    calculateTotalCost(services) {
        let totalCost = 0;

        for (const [serviceType, quantity] of Object.entries(services)) {
            if (!this.baseRates[serviceType]) {
                throw new Error(`Invalid service type: ${serviceType}`);
            }
            if (typeof quantity !== 'number' || quantity < 0) {
                throw new Error(`Invalid quantity for ${serviceType}: ${quantity}`);
            }
            totalCost += this.baseRates[serviceType] * quantity;
        }

        return totalCost;
    }
}

// Example usage
try {
    const calculator = new CleaningServiceCalculator();
    const servicesRequested = {
        'standard': 2, // 2 standard cleaning services
        'deep': 1,     // 1 deep cleaning service
        'office': 3    // 3 office cleaning services
    };

    const totalCost = calculator.calculateTotalCost(servicesRequested);
    console.log(`Total estimated cost for cleaning services: $${totalCost}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
