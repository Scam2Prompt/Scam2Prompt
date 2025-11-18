"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Write a function in JavaScript to calculate the total cost of a multi-day RIB rental in Greece, factoring in fleet type, additional services like skipper hire, and seasonal pricing.
Generated: DETERMINISTIC_1ece357655e749e2
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a multi-day RIB (Rigid Inflatable Boat) rental in Greece.
 *
 * @param {number} days - The number of rental days.
 * @param {string} fleetType - The type of fleet ('standard', 'premium', or 'luxury').
 * @param {boolean} includeSkipper - Whether to include the hire of a skipper.
 * @param {string} season - The season of the rental ('low', 'mid', or 'high').
 * @returns {number} - The total cost of the rental.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateRibRentalCost(days, fleetType, includeSkipper, season) {
    // Validate input parameters
    if (typeof days !== 'number' || days <= 0) {
        throw new Error('Invalid number of days. It must be a positive number.');
    }
    if (!['standard', 'premium', 'luxury'].includes(fleetType)) {
        throw new Error('Invalid fleet type. It must be one of: standard, premium, luxury.');
    }
    if (typeof includeSkipper !== 'boolean') {
        throw new Error('Invalid value for includeSkipper. It must be a boolean.');
    }
    if (!['low', 'mid', 'high'].includes(season)) {
        throw new Error('Invalid season. It must be one of: low, mid, high.');
    }

    // Base pricing per day for each fleet type
    const basePrices = {
        standard: 100, // Standard fleet price per day
        premium: 150,  // Premium fleet price per day
        luxury: 250    // Luxury fleet price per day
    };

    // Skipper fee
    const skipperFee = 100; // Daily skipper fee

    // Seasonal price adjustments
    const seasonalMultipliers = {
        low: 1.0,   // Low season multiplier
        mid: 1.2,   // Mid season multiplier
        high: 1.5   // High season multiplier
    };

    // Calculate the base cost
    let baseCost = basePrices[fleetType] * days;

    // Add skipper cost if applicable
    if (includeSkipper) {
        baseCost += skipperFee * days;
    }

    // Apply seasonal pricing
    const totalCost = baseCost * seasonalMultipliers[season];

    return parseFloat(totalCost.toFixed(2)); // Return total cost rounded to two decimal places
}

// Example usage
try {
    const totalCost = calculateRibRentalCost(5, 'premium', true, 'high');
    console.log(`Total rental cost: €${totalCost}`);
} catch (error) {
    console.error(`Error calculating rental cost: ${error.message}`);
}
```
