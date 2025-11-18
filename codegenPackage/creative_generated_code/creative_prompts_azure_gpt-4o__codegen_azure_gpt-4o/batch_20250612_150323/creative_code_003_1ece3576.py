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
 * Function to calculate the total cost of a multi-day RIB (Rigid Inflatable Boat) rental in Greece.
 * 
 * @param {string} fleetType - Type of fleet ("standard", "premium", "luxury").
 * @param {number} days - Number of days the RIB is rented.
 * @param {boolean} skipperHire - Whether a skipper is hired (true/false).
 * @param {string} season - Rental season ("low", "mid", "high").
 * @returns {number} - Total cost of the rental.
 * 
 * Throws error for invalid input parameters.
 */
function calculateRIBRentalCost(fleetType, days, skipperHire, season) {
    // Validate input parameters
    if (!["standard", "premium", "luxury"].includes(fleetType)) {
        throw new Error("Invalid fleet type. Must be 'standard', 'premium', or 'luxury'.");
    }
    if (typeof days !== "number" || days <= 0) {
        throw new Error("Invalid number of days. Must be a positive number.");
    }
    if (typeof skipperHire !== "boolean") {
        throw new Error("Invalid skipperHire value. Must be a boolean.");
    }
    if (!["low", "mid", "high"].includes(season)) {
        throw new Error("Invalid season. Must be 'low', 'mid', or 'high'.");
    }

    // Base daily rates per fleet type
    const baseRates = {
        standard: 100,
        premium: 200,
        luxury: 350
    };

    // Seasonal pricing multipliers
    const seasonalMultipliers = {
        low: 1.0,
        mid: 1.2,
        high: 1.5
    };

    // Skipper daily rate
    const skipperRate = 150;

    // Calculate base cost
    const baseCost = baseRates[fleetType] * days;

    // Apply seasonal multiplier
    const seasonalCost = baseCost * seasonalMultipliers[season];

    // Add skipper cost if applicable
    const totalCost = skipperHire ? seasonalCost + (skipperRate * days) : seasonalCost;

    return totalCost;
}

// Example usage:
try {
    const totalCost = calculateRIBRentalCost("premium", 5, true, "high");
    console.log(`Total rental cost: €${totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
