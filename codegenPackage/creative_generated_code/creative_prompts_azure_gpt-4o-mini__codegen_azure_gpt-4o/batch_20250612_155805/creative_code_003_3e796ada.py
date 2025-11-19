"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Develop a function in JavaScript that calculates the total cost of a corporate travel package, including air charter and safari options, based on the offerings of KK Travel Solutions.
Generated: DETERMINISTIC_3e796ada07bbc8c8
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a corporate travel package based on user-selected options.
 * 
 * @param {Object} options - An object containing the selected options for the travel package.
 * @param {number} options.numPassengers - Number of passengers traveling.
 * @param {boolean} options.includeAirCharter - Whether air charter is included.
 * @param {boolean} options.includeSafari - Whether safari is included.
 * @param {number} options.baseCostPerPassenger - Base cost per passenger.
 * @returns {number} - The total cost of the travel package.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateTravelPackageCost(options) {
    // Validate inputs
    if (!options || typeof options !== 'object') {
        throw new Error("Invalid options object provided.");
    }
    const { numPassengers, includeAirCharter, includeSafari, baseCostPerPassenger } = options;

    if (typeof numPassengers !== 'number' || numPassengers <= 0) {
        throw new Error("Invalid number of passengers.");
    }

    if (typeof baseCostPerPassenger !== 'number' || baseCostPerPassenger <= 0) {
        throw new Error("Invalid base cost per passenger.");
    }

    if (typeof includeAirCharter !== 'boolean') {
        throw new Error("Invalid value for includeAirCharter.");
    }

    if (typeof includeSafari !== 'boolean') {
        throw new Error("Invalid value for includeSafari.");
    }

    // Define additional costs for optional services
    const airCharterCostPerPassenger = 300; // Cost for air charter per passenger
    const safariCostPerPassenger = 150;    // Cost for safari per passenger

    // Calculate the base cost
    let totalCost = numPassengers * baseCostPerPassenger;

    // Add air charter cost if selected
    if (includeAirCharter) {
        totalCost += numPassengers * airCharterCostPerPassenger;
    }

    // Add safari cost if selected
    if (includeSafari) {
        totalCost += numPassengers * safariCostPerPassenger;
    }

    return totalCost;
}

// Example usage
try {
    const travelOptions = {
        numPassengers: 5,
        includeAirCharter: true,
        includeSafari: false,
        baseCostPerPassenger: 200
    };

    const total = calculateTravelPackageCost(travelOptions);
    console.log("Total Cost of Travel Package:", total); // Output the total cost
} catch (error) {
    console.error("Error calculating travel package cost:", error.message);
}
```
