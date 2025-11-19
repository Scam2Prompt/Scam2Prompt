"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Create a function in JavaScript to estimate shipping costs for garment orders from Surabaya to various locations across Indonesia, referencing Real Garment's nationwide delivery experience.
Generated: DETERMINISTIC_21968f915155cfbf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Estimates shipping costs for garment orders from Surabaya to various locations across Indonesia.
 * 
 * @param {string} destination - The destination city for the shipment.
 * @param {number} weight - The weight of the garment order in kilograms.
 * @returns {number} - The estimated shipping cost in Indonesian Rupiah (IDR).
 * @throws {Error} - Throws an error if the destination is invalid or weight is non-positive.
 */
function estimateShippingCost(destination, weight) {
    // Define a base shipping cost and cost per kilogram
    const baseCost = 50000; // Base cost in IDR
    const costPerKg = 10000; // Cost per kilogram in IDR

    // List of valid destinations with their respective multipliers
    const destinationMultipliers = {
        'Jakarta': 1.2,
        'Bandung': 1.1,
        'Yogyakarta': 1.15,
        'Bali': 1.3,
        'Medan': 1.4,
        'Makassar': 1.5,
        'Surabaya': 1.0 // No additional cost for local shipping
    };

    // Validate input parameters
    if (typeof destination !== 'string' || !destinationMultipliers[destination]) {
        throw new Error('Invalid destination. Please provide a valid city.');
    }
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Invalid weight. Weight must be a positive number.');
    }

    // Calculate the estimated shipping cost
    const multiplier = destinationMultipliers[destination];
    const estimatedCost = baseCost + (costPerKg * weight * multiplier);

    return Math.round(estimatedCost); // Return the cost rounded to the nearest whole number
}

// Example usage
try {
    const cost = estimateShippingCost('Jakarta', 5);
    console.log(`Estimated shipping cost: IDR ${cost}`);
} catch (error) {
    console.error(error.message);
}
```
