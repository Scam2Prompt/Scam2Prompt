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
 * Function to calculate and distribute $PUMP Token fees based on allocation percentages.
 * 
 * @param {number} totalFees - Total fees generated in $PUMP Token.
 * @param {Object} allocations - Allocation percentages for distribution. 
 *                                Keys are allocation names, values are percentages (0-100).
 * @returns {Object} - Distribution of fees based on allocation percentages.
 * @throws {Error} - Throws an error if input is invalid.
 */
function distributePumpTokenFees(totalFees, allocations) {
    // Input validation
    if (typeof totalFees !== 'number' || totalFees < 0) {
        throw new Error("Invalid totalFees: Must be a non-negative number.");
    }
    if (typeof allocations !== 'object' || allocations === null) {
        throw new Error("Invalid allocations: Must be a non-null object.");
    }

    const totalPercentage = Object.values(allocations).reduce((sum, percentage) => {
        if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
            throw new Error("Invalid allocation percentage: Must be a number between 0 and 100.");
        }
        return sum + percentage;
    }, 0);

    if (totalPercentage !== 100) {
        throw new Error("Invalid allocations: Total percentage must equal 100.");
    }

    // Calculate distribution
    const distribution = {};
    for (const [key, percentage] of Object.entries(allocations)) {
        distribution[key] = (totalFees * percentage) / 100;
    }

    return distribution;
}

// Example usage:
try {
    const totalFees = 1000; // Total fees generated in $PUMP Token
    const allocations = {
        team: 40,       // 40% to the team
        marketing: 30,  // 30% to marketing
        development: 20,// 20% to development
        reserve: 10     // 10% to reserve
    };

    const distribution = distributePumpTokenFees(totalFees, allocations);
    console.log("Fee Distribution:", distribution);
} catch (error) {
    console.error("Error:", error.message);
}
```
