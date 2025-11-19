"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write a function in JavaScript to calculate the total cost of a multi-day RIB rental in Greece, factoring in fleet type, additional services like skipper hire, and seasonal pricing.
Generated: DETERMINISTIC_1ece357655e749e2
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a multi-day RIB rental in Greece.
 * 
 * @param {Object} options - Rental options
 * @param {string} options.fleetType - Type of RIB fleet (e.g., 'small', 'medium', 'large')
 * @param {number} options.duration - Rental duration in days
 * @param {boolean} [options.skipper=false] - Whether to include a skipper
 * @param {boolean} [options.insurance=false] - Whether to include insurance
 * @param {string} [options.season='low'] - Rental season ('low', 'mid', 'high')
 * @returns {number} Total rental cost in EUR
 * @throws {Error} If invalid parameters are provided
 */
function calculateRentalCost(options) {
    // Validate input
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options parameter');
    }

    const { fleetType, duration, skipper = false, insurance = false, season = 'low' } = options;

    // Validate required parameters
    if (!fleetType || !['small', 'medium', 'large'].includes(fleetType)) {
        throw new Error('Invalid fleet type. Must be small, medium, or large');
    }

    if (!duration || typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration. Must be a positive number');
    }

    if (!['low', 'mid', 'high'].includes(season)) {
        throw new Error('Invalid season. Must be low, mid, or high');
    }

    // Base prices per fleet type (per day)
    const basePrices = {
        small: 150,
        medium: 250,
        large: 400
    };

    // Seasonal multipliers
    const seasonMultipliers = {
        low: 1.0,
        mid: 1.3,
        high: 1.7
    };

    // Additional services costs
    const additionalServices = {
        skipper: 100, // per day
        insurance: 50 // per day
    };

    // Calculate base cost
    const basePrice = basePrices[fleetType];
    const seasonalPrice = basePrice * seasonMultipliers[season];
    const baseCost = seasonalPrice * duration;

    // Calculate additional services
    let extrasCost = 0;
    if (skipper) {
        extrasCost += additionalServices.skipper * duration;
    }
    if (insurance) {
        extrasCost += additionalServices.insurance * duration;
    }

    // Calculate total cost
    const totalCost = baseCost + extrasCost;

    return totalCost;
}
```
