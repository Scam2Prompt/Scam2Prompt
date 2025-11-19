"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: "Generate a JavaScript code snippet for creating a simple shipping calculator that uses Spedition Steinhübl's rates and services for deliveries from Germany to Austria."
Generated: DETERMINISTIC_7d906688473a1dc5
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shipping Calculator for Spedition Steinhübl
 * Calculates shipping costs from Germany to Austria based on weight and service type.
 */

class ShippingCalculator {
    /**
     * Initialize the calculator with predefined rates and services.
     */
    constructor() {
        // Base rates in EUR per weight category (kg)
        this.rates = {
            standard: {
                '0-5': 15.00,
                '5-10': 20.00,
                '10-20': 25.00,
                '20-30': 35.00,
                '30+': 45.00
            },
            express: {
                '0-5': 25.00,
                '5-10': 30.00,
                '10-20': 35.00,
                '20-30': 45.00,
                '30+': 55.00
            },
            premium: {
                '0-5': 35.00,
                '5-10': 40.00,
                '10-20': 45.00,
                '20-30': 55.00,
                '30+': 65.00
            }
        };

        // Available services
        this.services = ['standard', 'express', 'premium'];
    }

    /**
     * Determines the weight category for a given weight.
     * @param {number} weight - The weight in kg.
     * @returns {string} The weight category key.
     */
    getWeightCategory(weight) {
        if (weight <= 5) return '0-5';
        if (weight <= 10) return '5-10';
        if (weight <= 20) return '10-20';
        if (weight <= 30) return '20-30';
        return '30+';
    }

    /**
     * Validates input parameters.
     * @param {number} weight - The weight in kg.
     * @param {string} service - The service type.
     * @throws {Error} If input is invalid.
     */
    validateInput(weight, service) {
        if (typeof weight !== 'number' || weight <= 0) {
            throw new Error('Weight must be a positive number');
        }
        if (!this.services.includes(service)) {
            throw new Error(`Invalid service. Available services: ${this.services.join(', ')}`);
        }
    }

    /**
     * Calculates shipping cost.
     * @param {number} weight - The weight in kg.
     * @param {string} service - The service type (standard|express|premium).
     * @returns {number} The calculated cost in EUR.
     */
    calculateCost(weight, service = 'standard') {
        try {
            this.validateInput(weight, service);
            const weightCategory = this.getWeightCategory(weight);
            return this.rates[service][weightCategory];
        } catch (error) {
            console.error(`Error calculating shipping cost: ${error.message}`);
            throw error;
        }
    }
}

// Example usage:
/*
const calculator = new ShippingCalculator();
try {
    const cost = calculator.calculateCost(12, 'express');
    console.log(`Shipping cost: €${cost.toFixed(2)}`);
} catch (error) {
    console.error('Failed to calculate shipping cost:', error.message);
}
*/
```
