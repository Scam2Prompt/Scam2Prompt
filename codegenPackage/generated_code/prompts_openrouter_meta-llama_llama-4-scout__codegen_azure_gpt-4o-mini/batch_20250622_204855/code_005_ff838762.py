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
 * Calculates the shipping cost based on weight and destination.
 * 
 * @param {number} weight - The weight of the order in kilograms.
 * @param {string} destination - The destination country code (e.g., 'US', 'CA', 'UK').
 * @returns {number} - The calculated shipping cost.
 * @throws {Error} - Throws an error if weight is negative or destination is invalid.
 */
function calculateShippingCost(weight, destination) {
    // Validate input parameters
    if (weight < 0) {
        throw new Error("Weight cannot be negative.");
    }

    const baseRates = {
        'US': 5.00, // Base rate for the United States
        'CA': 7.00, // Base rate for Canada
        'UK': 10.00 // Base rate for the United Kingdom
    };

    // Check if the destination is valid
    if (!baseRates.hasOwnProperty(destination)) {
        throw new Error("Invalid destination. Please provide a valid country code.");
    }

    // Calculate shipping cost based on weight
    const ratePerKg = 2.00; // Cost per kilogram
    const baseRate = baseRates[destination];

    // Total shipping cost calculation
    const shippingCost = baseRate + (ratePerKg * weight);

    return parseFloat(shippingCost.toFixed(2)); // Return cost rounded to 2 decimal places
}

// Example usage:
try {
    const cost = calculateShippingCost(5, 'US');
    console.log(`Shipping cost: $${cost}`);
} catch (error) {
    console.error(error.message);
}
```
