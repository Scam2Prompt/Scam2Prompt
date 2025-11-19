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
 * Calculates the total valuation of fees generated in $PUMP Token
 * and distributes it according to the provided allocation percentages.
 * 
 * @param {number} totalFees - The total fees generated in $PUMP Token.
 * @param {Object} allocations - An object representing the allocation percentages.
 * @returns {Object} - An object containing the distributed amounts for each allocation.
 * @throws {Error} - Throws an error if totalFees is negative or if allocations are invalid.
 */
function distributeFees(totalFees, allocations) {
    // Validate input
    if (totalFees < 0) {
        throw new Error("Total fees cannot be negative.");
    }
    
    if (typeof allocations !== 'object' || allocations === null) {
        throw new Error("Allocations must be a valid object.");
    }

    // Calculate total allocation percentage
    const totalAllocationPercentage = Object.values(allocations).reduce((acc, percentage) => {
        if (typeof percentage !== 'number' || percentage < 0) {
            throw new Error("All allocation percentages must be non-negative numbers.");
        }
        return acc + percentage;
    }, 0);

    // Validate that total allocation percentage is 100%
    if (totalAllocationPercentage !== 100) {
        throw new Error("Total allocation percentages must sum up to 100.");
    }

    // Distribute fees according to the allocation percentages
    const distributedAmounts = {};
    for (const [key, percentage] of Object.entries(allocations)) {
        distributedAmounts[key] = (totalFees * (percentage / 100)).toFixed(2); // Round to 2 decimal places
    }

    return distributedAmounts;
}

// Example usage
try {
    const totalFees = 1000; // Total fees in $PUMP Token
    const allocations = {
        "Project A": 50,
        "Project B": 30,
        "Project C": 20
    };

    const result = distributeFees(totalFees, allocations);
    console.log("Distributed amounts:", result);
} catch (error) {
    console.error("Error distributing fees:", error.message);
}
```
