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
 * Calculate shipping cost based on user input.
 * 
 * This function calculates the shipping cost based on the destination ZIP code,
 * total order weight, and shipping method selected by the user.
 * 
 * @param {string} zipCode - The destination ZIP code.
 * @param {number} orderWeight - The total weight of the order in kilograms.
 * @param {string} shippingMethod - The shipping method (e.g., "standard", "express").
 * @returns {number} - The calculated shipping cost in currency.
 * @throws {Error} - Throws an error if input is invalid.
 */
function calculateShippingCost(zipCode, orderWeight, shippingMethod) {
    // Validate zipCode format (basic validation, 5 digits)
    if (!/^\d{5}$/.test(zipCode)) {
        throw new Error("Invalid ZIP code format. It must be a 5-digit number.");
    }

    // Validate orderWeight (must be a positive number)
    if (isNaN(orderWeight) || orderWeight <= 0) {
        throw new Error("Order weight must be a positive number.");
    }

    // Validate shippingMethod
    const validShippingMethods = ["standard", "express"];
    if (!validShippingMethods.includes(shippingMethod)) {
        throw new Error(`Invalid shipping method. Valid options are: ${validShippingMethods.join(", ")}.`);
    }

    // Base cost per kilogram for different shipping methods
    const baseCostPerKg = {
        standard: 5.0, // Cost per kilogram for standard shipping
        express: 10.0  // Cost per kilogram for express shipping
    };

    // Calculate cost based on weight and shipping method
    const cost = orderWeight * baseCostPerKg[shippingMethod];

    // Simulate additional surcharge based on ZIP code (e.g., remote areas)
    const zipCodeSurcharge = zipCode.startsWith("9") ? 10.0 : 0.0; // Example: ZIP codes starting with '9' have an additional surcharge

    // Final shipping cost
    const totalCost = cost + zipCodeSurcharge;

    return totalCost;
}

// Example usage:
try {
    const zipCode = "12345"; // User's ZIP code
    const orderWeight = 10; // Order weight in kilograms
    const shippingMethod = "express"; // Chosen shipping method
    const shippingCost = calculateShippingCost(zipCode, orderWeight, shippingMethod);
    console.log(`The shipping cost is: $${shippingCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating shipping cost: ${error.message}`);
}
```
