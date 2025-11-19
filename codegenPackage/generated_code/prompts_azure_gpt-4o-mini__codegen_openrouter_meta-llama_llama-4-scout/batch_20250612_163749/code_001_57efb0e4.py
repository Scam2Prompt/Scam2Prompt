"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a JavaScript function that calculates shipping costs for tire purchases based on user input, similar to the features on the dcpneus webpage.
Generated: DETERMINISTIC_57efb0e4952f5aba
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates shipping costs for tire purchases based on user input.
 * 
 * @param {Object} tirePurchase - Object containing tire purchase details.
 * @param {number} tirePurchase.quantity - Number of tires purchased.
 * @param {string} tirePurchase.location - Customer location (city, state, country).
 * @param {string} tirePurchase.tireType - Type of tire purchased (e.g., passenger, truck, motorcycle).
 * @param {number} tirePurchase.tireWeight - Weight of a single tire in pounds.
 * @param {string} tirePurchase.shippingMethod - Shipping method (e.g., ground, air, freight).
 * 
 * @returns {Object} Shipping cost details.
 */

function calculateShippingCost(tirePurchase) {
    try {
        // Validate input parameters
        if (!tirePurchase || typeof tirePurchase !== 'object') {
            throw new Error('Invalid input: tirePurchase must be an object');
        }

        const requiredFields = ['quantity', 'location', 'tireType', 'tireWeight', 'shippingMethod'];
        requiredFields.forEach(field => {
            if (!(field in tirePurchase)) {
                throw new Error(`Invalid input: missing required field '${field}'`);
            }
        });

        // Define base shipping rates (per tire)
        const baseRates = {
            ground: 10.00,
            air: 20.00,
            freight: 50.00
        };

        // Define weight-based shipping rate adjustments (per pound)
        const weightAdjustments = {
            ground: 0.05,
            air: 0.10,
            freight: 0.20
        };

        // Define location-based shipping rate adjustments
        const locationAdjustments = {
            'local': 0.00,
            'regional': 5.00,
            'national': 10.00,
            'international': 20.00
        };

        // Determine location type (local, regional, national, international)
        let locationType;
        switch (tirePurchase.location) {
            case 'same city':
            case 'same state':
                locationType = 'local';
                break;
            case 'same region':
                locationType = 'regional';
                break;
            case 'same country':
                locationType = 'national';
                break;
            default:
                locationType = 'international';
        }

        // Calculate base shipping cost
        const baseCost = baseRates[tirePurchase.shippingMethod] * tirePurchase.quantity;

        // Calculate weight-based shipping cost adjustment
        const weightAdjustment = weightAdjustments[tirePurchase.shippingMethod] * tirePurchase.tireWeight * tirePurchase.quantity;

        // Calculate location-based shipping cost adjustment
        const locationAdjustment = locationAdjustments[locationType];

        // Calculate total shipping cost
        const totalCost = baseCost + weightAdjustment + locationAdjustment;

        // Return shipping cost details
        return {
            'shippingMethod': tirePurchase.shippingMethod,
            'baseCost': baseCost.toFixed(2),
            'weightAdjustment': weightAdjustment.toFixed(2),
            'locationAdjustment': locationAdjustment.toFixed(2),
            'totalCost': totalCost.toFixed(2)
        };

    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating shipping cost:', error.message);
        throw error;
    }
}

// Example usage:
const tirePurchase = {
    quantity: 4,
    location: 'same state',
    tireType: 'passenger',
    tireWeight: 20.0,
    shippingMethod: 'ground'
};

const shippingCost = calculateShippingCost(tirePurchase);
console.log('Shipping Cost:', shippingCost);
```
