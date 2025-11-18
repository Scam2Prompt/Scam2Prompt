"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Create a function in JavaScript that calculates shipping costs based on user input, similar to the "Calcule seu frete na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_0e3bb698072dd750
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the shipping cost based on user input such as weight, distance, and shipping method.
 * @param {number} weight - The weight of the package in kilograms.
 * @param {number} distance - The distance to be shipped in kilometers.
 * @param {string} method - The shipping method ('standard', 'express', 'overnight').
 * @returns {number} - The calculated shipping cost, or throws an error for invalid input.
 */
function calculateShippingCost(weight, distance, method) {
    // Validate input types
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Invalid weight: Weight must be a positive number.');
    }
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error('Invalid distance: Distance must be a positive number.');
    }
    if (typeof method !== 'string' || !['standard', 'express', 'overnight'].includes(method)) {
        throw new Error('Invalid method: Method must be one of "standard", "express", or "overnight".');
    }

    // Base rates
    const baseRate = 5; // Base cost in currency units
    const weightRate = 2; // Cost per kilogram
    const distanceRate = 0.5; // Cost per kilometer

    // Calculate cost based on method
    let methodMultiplier;
    switch (method) {
        case 'standard':
            methodMultiplier = 1; // No extra cost
            break;
        case 'express':
            methodMultiplier = 1.5; // 50% extra for express
            break;
        case 'overnight':
            methodMultiplier = 2; // 100% extra for overnight
            break;
        default:
            methodMultiplier = 1; // Fallback, should not happen due to validation
    }

    // Calculate total cost
    const totalCost = baseRate + (weight * weightRate) + (distance * distanceRate);
    return totalCost * methodMultiplier;
}

// Example usage
try {
    const shippingCost = calculateShippingCost(10, 100, 'express');
    console.log(`The shipping cost is: $${shippingCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
