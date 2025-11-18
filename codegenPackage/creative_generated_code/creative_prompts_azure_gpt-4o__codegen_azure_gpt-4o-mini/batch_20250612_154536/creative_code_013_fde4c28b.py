"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Write a function in JavaScript that calculates upgrade costs for flights based on the upgrade policies for Delta Airlines and Air Canada, as described on Airlines Manage Booking.
Generated: DETERMINISTIC_fde4c28bfde679ec
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the upgrade cost for flights based on the airline and upgrade policies.
 * 
 * @param {string} airline - The name of the airline ('Delta' or 'Air Canada').
 * @param {number} currentFare - The current fare class (1 for Economy, 2 for Premium Economy, 3 for Business, 4 for First).
 * @param {number} targetFare - The desired fare class to upgrade to (1 for Economy, 2 for Premium Economy, 3 for Business, 4 for First).
 * @returns {number} - The cost of the upgrade, or an error message if inputs are invalid.
 */
function calculateUpgradeCost(airline, currentFare, targetFare) {
    // Define upgrade cost policies for Delta Airlines
    const deltaUpgradeCosts = {
        1: { 2: 100, 3: 300, 4: 500 }, // From Economy
        2: { 3: 200, 4: 400 },         // From Premium Economy
        3: { 4: 250 }                  // From Business
    };

    // Define upgrade cost policies for Air Canada
    const airCanadaUpgradeCosts = {
        1: { 2: 120, 3: 350, 4: 600 }, // From Economy
        2: { 3: 250, 4: 450 },         // From Premium Economy
        3: { 4: 300 }                  // From Business
    };

    // Validate inputs
    const validAirlines = ['Delta', 'Air Canada'];
    if (!validAirlines.includes(airline)) {
        throw new Error('Invalid airline. Please use "Delta" or "Air Canada".');
    }
    if (![1, 2, 3, 4].includes(currentFare) || ![1, 2, 3, 4].includes(targetFare)) {
        throw new Error('Fare classes must be between 1 (Economy) and 4 (First).');
    }
    if (currentFare >= targetFare) {
        return 0; // No cost if current fare is equal to or higher than target fare
    }

    // Calculate upgrade cost based on the airline and fare classes
    let upgradeCost = 0;

    if (airline === 'Delta') {
        upgradeCost = deltaUpgradeCosts[currentFare]?.[targetFare];
    } else if (airline === 'Air Canada') {
        upgradeCost = airCanadaUpgradeCosts[currentFare]?.[targetFare];
    }

    // Handle cases where upgrade is not possible
    if (upgradeCost === undefined) {
        return `Upgrade from fare class ${currentFare} to ${targetFare} is not available for ${airline}.`;
    }

    return upgradeCost;
}

// Example usage:
// try {
//     console.log(calculateUpgradeCost('Delta', 1, 3)); // Output: 300
// } catch (error) {
//     console.error(error.message);
// }
```
