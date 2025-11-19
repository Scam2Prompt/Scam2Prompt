"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Develop a function in JavaScript that calculates the total cost of a corporate travel package, including air charter and safari options, based on the offerings of KK Travel Solutions.
Generated: DETERMINISTIC_3e796ada07bbc8c8
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a corporate travel package.
 * 
 * @param {Object} travelPackage - Travel package details.
 * @param {number} travelPackage.airCharterCost - Cost of air charter.
 * @param {number} travelPackage.safariCostPerPerson - Cost of safari per person.
 * @param {number} travelPackage.numberOfPeople - Number of people.
 * @param {boolean} [travelPackage.airCharterRequired=true] - Whether air charter is required.
 * @param {boolean} [travelPackage.safariRequired=false] - Whether safari is required.
 * 
 * @returns {number} The total cost of the travel package.
 */
function calculateTravelPackageCost(travelPackage) {
    // Set default values for optional parameters
    const airCharterRequired = travelPackage.airCharterRequired !== undefined ? travelPackage.airCharterRequired : true;
    const safariRequired = travelPackage.safariRequired !== undefined ? travelPackage.safariRequired : false;

    // Validate input parameters
    if (typeof travelPackage.airCharterCost !== 'number' || travelPackage.airCharterCost < 0) {
        throw new Error('Air charter cost must be a non-negative number.');
    }
    if (typeof travelPackage.safariCostPerPerson !== 'number' || travelPackage.safariCostPerPerson < 0) {
        throw new Error('Safari cost per person must be a non-negative number.');
    }
    if (typeof travelPackage.numberOfPeople !== 'number' || travelPackage.numberOfPeople <= 0) {
        throw new Error('Number of people must be a positive integer.');
    }
    if (typeof airCharterRequired !== 'boolean') {
        throw new Error('Air charter required must be a boolean.');
    }
    if (typeof safariRequired !== 'boolean') {
        throw new Error('Safari required must be a boolean.');
    }

    // Calculate air charter cost
    let airCharterCost = 0;
    if (airCharterRequired) {
        airCharterCost = travelPackage.airCharterCost;
    }

    // Calculate safari cost
    let safariCost = 0;
    if (safariRequired) {
        safariCost = travelPackage.safariCostPerPerson * travelPackage.numberOfPeople;
    }

    // Calculate total cost
    const totalCost = airCharterCost + safariCost;

    return totalCost;
}

// Example usage:
try {
    const travelPackage = {
        airCharterCost: 10000,
        safariCostPerPerson: 500,
        numberOfPeople: 10,
        safariRequired: true,
        airCharterRequired: true
    };
    const totalCost = calculateTravelPackageCost(travelPackage);
    console.log(`The total cost of the travel package is: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
