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
 * Function to calculate upgrade costs for flights based on airline policies.
 * 
 * @param {string} airline - The name of the airline ('Delta Airlines' or 'Air Canada').
 * @param {number} baseFare - The original fare of the flight.
 * @param {string} upgradeType - The type of upgrade ('economy to premium economy', 'premium economy to business class', or 'economy to business class').
 * @returns {number} - The calculated upgrade cost. Returns -1 if invalid input is provided.
 */
function calculateUpgradeCost(airline, baseFare, upgradeType) {
    // Validate input parameters
    if (typeof airline !== 'string' || typeof baseFare !== 'number' || baseFare < 0 || typeof upgradeType !== 'string') {
        console.error('Invalid input parameters');
        return -1;
    }

    // Define policies for upgrade percentages
    const upgradePolicies = {
        "Delta Airlines": {
            "economy to premium economy": 0.35, // 35% of base fare
            "premium economy to business class": 0.55, // 55% of base fare
            "economy to business class": 0.80 // 80% of base fare
        },
        "Air Canada": {
            "economy to premium economy": 0.30, // 30% of base fare
            "premium economy to business class": 0.50, // 50% of base fare
            "economy to business class": 0.75 // 75% of base fare
        }
    };

    // Check if airline and upgrade type are valid
    if (!upgradePolicies[airline] || !upgradePolicies[airline][upgradeType]) {
        console.error('Invalid airline or upgrade type');
        return -1;
    }

    // Calculate the upgrade cost based on the policy
    const upgradePercentage = upgradePolicies[airline][upgradeType];
    const upgradeCost = baseFare * upgradePercentage;

    // Return the calculated upgrade cost
    return upgradeCost;
}

// Example usage:
// console.log(calculateUpgradeCost('Delta Airlines', 500, 'economy to premium economy')); // Expected output: 175
// console.log(calculateUpgradeCost('Air Canada', 800, 'economy to business class')); // Expected output: 600
```
