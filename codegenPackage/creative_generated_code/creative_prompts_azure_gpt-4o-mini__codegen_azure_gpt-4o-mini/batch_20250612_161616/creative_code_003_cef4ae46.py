"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://widophlogistics.com.au
Prompt: Develop a JavaScript function that calculates shipping costs based on the global network and customer-centric services highlighted by Widoph Logistics.
Generated: DETERMINISTIC_cef4ae469a2c7b74
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates shipping costs based on destination and shipping method.
 * 
 * @param {string} destination - The destination of the shipment (e.g., 'domestic', 'international').
 * @param {string} shippingMethod - The shipping method chosen (e.g., 'standard', 'express').
 * @param {number} weight - The weight of the package in kilograms.
 * @returns {number} - The calculated shipping cost.
 * @throws {Error} - Throws error for invalid parameters.
 */
function calculateShippingCost(destination, shippingMethod, weight) {
    // Define base rates for different destinations and shipping methods
    const rates = {
        domestic: {
            standard: 5.0,
            express: 10.0
        },
        international: {
            standard: 15.0,
            express: 25.0
        }
    };

    // Validate input parameters
    if (typeof destination !== 'string' || typeof shippingMethod !== 'string' || typeof weight !== 'number') {
        throw new Error('Invalid input types. Destination and shipping method should be strings, weight should be a number.');
    }

    if (!rates[destination]) {
        throw new Error('Invalid destination. Valid options are: domestic, international.');
    }

    if (!rates[destination][shippingMethod]) {
        throw new Error('Invalid shipping method. Valid options are: standard, express.');
    }

    if (weight <= 0) {
        throw new Error('Invalid weight. Weight must be a positive number.');
    }

    // Calculate the cost based on the base rate and weight
    const baseRate = rates[destination][shippingMethod];
    const shippingCost = baseRate + (weight * 2); // Add $2 per kilogram to the base rate

    return parseFloat(shippingCost.toFixed(2)); // Return cost rounded to two decimal places
}

// Example usage
try {
    const cost = calculateShippingCost('international', 'express', 5);
    console.log(`Shipping cost: $${cost}`);
} catch (error) {
    console.error(`Error calculating shipping cost: ${error.message}`);
}
```
