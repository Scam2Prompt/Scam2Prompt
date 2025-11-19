"""
Generated Code Metadata:
========================
Original URL: https://bafybeigoo2ajgc5d32j7sqglri2pqwtnmpnm6g2yfmlmcdzm2oyww2ny3u.ipfs.dweb.link
Prompt: Generate a code snippet in JavaScript to calculate the total valuation of fees generated in $PUMP Token and distribute it according to the provided allocation percentages.
Generated: DETERMINISTIC_aeee48d221818dce
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total valuation of fees generated in $PUMP Token and distributes it
 * according to the provided allocation percentages.
 * 
 * @param {number} totalFees - Total fees generated in $PUMP Token
 * @param {Object} allocationPercentages - Object containing allocation percentages
 * @returns {Object} - Object containing distributed amounts for each allocation
 * @throws {Error} - If inputs are invalid or percentages don't sum to 100%
 */
function distributeFees(totalFees, allocationPercentages) {
    // Validate inputs
    if (typeof totalFees !== 'number' || totalFees < 0) {
        throw new Error('Total fees must be a positive number');
    }

    if (!allocationPercentages || typeof allocationPercentages !== 'object') {
        throw new Error('Allocation percentages must be an object');
    }

    // Calculate total percentage to ensure it sums to 100%
    const totalPercentage = Object.values(allocationPercentages).reduce(
        (sum, percentage) => sum + percentage, 0
    );

    if (Math.abs(totalPercentage - 100) > 0.01) { // Allow for minor floating point errors
        throw new Error('Allocation percentages must sum to 100%');
    }

    // Calculate distributed amounts
    const distributedAmounts = {};
    for (const [key, percentage] of Object.entries(allocationPercentages)) {
        if (typeof percentage !== 'number' || percentage < 0) {
            throw new Error(`Invalid percentage for ${key}`);
        }
        distributedAmounts[key] = (totalFees * percentage) / 100;
    }

    return distributedAmounts;
}

// Example usage:
/*
const totalFees = 1000; // 1000 $PUMP
const allocationPercentages = {
    team: 20,
    development: 30,
    marketing: 25,
    liquidity: 15,
    community: 10
};

try {
    const distributed = distributeFees(totalFees, allocationPercentages);
    console.log(distributed);
} catch (error) {
    console.error('Error distributing fees:', error.message);
}
*/
```
