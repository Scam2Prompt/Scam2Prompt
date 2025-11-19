"""
Generated Code Metadata:
========================
Original URL: https://dridmachine.com
Prompt: "Create a basic JavaScript function to calculate shipping costs for orders of prints and textiles based on weight and destination."
Generated: DETERMINISTIC_ff83876213002dd1
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates shipping costs for orders of prints and textiles based on weight and destination.
 * 
 * @param {string} destination - The destination of the shipment (local, national, international).
 * @param {number} weight - The weight of the shipment in kilograms.
 * @param {string} itemType - The type of item being shipped (print, textile).
 * @returns {number} The calculated shipping cost.
 */
function calculateShippingCost(destination, weight, itemType) {
    // Define base rates for each destination
    const baseRates = {
        local: 5.00,
        national: 10.00,
        international: 20.00
    };

    // Define weight-based rates for each item type
    const weightRates = {
        print: 0.50,
        textile: 1.00
    };

    // Check if destination and itemType are valid
    if (!baseRates[destination]) {
        throw new Error(`Invalid destination: ${destination}. Must be one of: ${Object.keys(baseRates).join(', ')}`);
    }
    if (!weightRates[itemType]) {
        throw new Error(`Invalid item type: ${itemType}. Must be one of: ${Object.keys(weightRates).join(', ')}`);
    }
    if (weight <= 0) {
        throw new Error('Weight must be a positive number');
    }

    // Calculate base cost
    let baseCost = baseRates[destination];

    // Calculate weight-based cost
    let weightCost = weight * weightRates[itemType];

    // Apply discounts for bulk orders
    let discount = 0;
    if (weight > 5) {
        discount = 0.1; // 10% discount for orders over 5kg
    }

    // Calculate total cost
    let totalCost = (baseCost + weightCost) * (1 - discount);

    return totalCost.toFixed(2); // Return cost to 2 decimal places
}

// Example usage:
try {
    const shippingCost = calculateShippingCost('national', 3.5, 'print');
    console.log(`Shipping cost: $${shippingCost}`);
} catch (error) {
    console.error(error.message);
}
```
