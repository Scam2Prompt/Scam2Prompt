"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Develop a JavaScript function to calculate the cost of a basketball camp based on the number of campers, similar to L-Zero's camp pricing at Courtside Fitness, and provide a discount for early registration.
Generated: DETERMINISTIC_3fbc25482df103a9
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a basketball camp based on the number of campers and registration timing.
 * 
 * @param {number} numCampers - The number of campers attending the camp.
 * @param {boolean} isEarlyRegistration - Whether the registration is early (eligible for discount).
 * @returns {number} The total cost of the camp after applying discounts if applicable.
 * @throws {Error} If numCampers is not a positive integer.
 */
function calculateCampCost(numCampers, isEarlyRegistration) {
    // Validate input
    if (!Number.isInteger(numCampers) || numCampers <= 0) {
        throw new Error('Number of campers must be a positive integer.');
    }

    // Base pricing constants
    const BASE_PRICE_PER_CAMPER = 200; // Base price per camper
    const EARLY_REGISTRATION_DISCOUNT = 0.1; // 10% discount for early registration
    const GROUP_DISCOUNT_THRESHOLD = 5; // Minimum campers for group discount
    const GROUP_DISCOUNT_RATE = 0.05; // 5% discount for groups

    // Calculate base cost
    let totalCost = numCampers * BASE_PRICE_PER_CAMPER;

    // Apply early registration discount if applicable
    if (isEarlyRegistration) {
        totalCost *= (1 - EARLY_REGISTRATION_DISCOUNT);
    }

    // Apply group discount if applicable
    if (numCampers >= GROUP_DISCOUNT_THRESHOLD) {
        totalCost *= (1 - GROUP_DISCOUNT_RATE);
    }

    // Round to 2 decimal places for currency
    totalCost = Math.round(totalCost * 100) / 100;

    return totalCost;
}

// Example usage:
// try {
//     const cost = calculateCampCost(6, true);
//     console.log(`Total camp cost: $${cost.toFixed(2)}`);
// } catch (error) {
//     console.error('Error calculating camp cost:', error.message);
// }
```
