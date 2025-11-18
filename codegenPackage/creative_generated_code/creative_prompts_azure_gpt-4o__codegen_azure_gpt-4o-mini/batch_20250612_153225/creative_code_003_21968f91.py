"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Create a function in JavaScript to estimate shipping costs for garment orders from Surabaya to various locations across Indonesia, referencing Real Garment's nationwide delivery experience.
Generated: DETERMINISTIC_21968f915155cfbf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Estimates shipping costs for garment orders from Surabaya to various locations across Indonesia.
 * 
 * @param {string} destination - The destination city for the shipment.
 * @param {number} weight - The weight of the garment order in kilograms.
 * @returns {number} - Estimated shipping cost in Indonesian Rupiah (IDR).
 * @throws {Error} - Throws an error if the destination is invalid or weight is negative.
 */
function estimateShippingCost(destination, weight) {
    // Define a base shipping cost per kilogram
    const baseCostPerKg = 50000; // Base cost in IDR

    // Define shipping cost multipliers based on destination
    const destinationMultipliers = {
        'Jakarta': 1.0,
        'Bandung': 1.1,
        'Bali': 1.2,
        'Makassar': 1.3,
        'Medan': 1.4,
        'Surabaya': 1.0, // No cost for local shipping
        // Add more cities as necessary
    };

    // Validate weight input
    if (weight < 0) {
        throw new Error('Weight must be a non-negative number.');
    }

    // Get the multiplier for the specified destination
    const multiplier = destinationMultipliers[destination];

    // Validate destination input
    if (multiplier === undefined) {
        throw new Error('Invalid destination. Please provide a valid city name.');
    }

    // Calculate the estimated shipping cost
    const estimatedCost = baseCostPerKg * weight * multiplier;

    return estimatedCost;
}

// Example usage:
try {
    const cost = estimateShippingCost('Jakarta', 2);
    console.log(`Estimated shipping cost: IDR ${cost.toLocaleString()}`);
} catch (error) {
    console.error(error.message);
}
```
