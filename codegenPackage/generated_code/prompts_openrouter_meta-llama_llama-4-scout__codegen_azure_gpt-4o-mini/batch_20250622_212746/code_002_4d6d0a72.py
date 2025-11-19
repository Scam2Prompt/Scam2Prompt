"""
Generated Code Metadata:
========================
Original URL: https://www.resolver.in
Prompt: Generate a code snippet to calculate metrics for consumer claims, like Resolver's track record of over £2bn saved by consumers, using JavaScript and JSON data.
Generated: DETERMINISTIC_4d6d0a7273e0f7de
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates metrics for consumer claims based on provided JSON data.
 * This function computes the total claims amount and the average claim amount.
 * 
 * @param {Array} claimsData - An array of claim objects, each containing an amount.
 * @returns {Object} An object containing total claims and average claim amount.
 * @throws {Error} Throws an error if claimsData is not an array or is empty.
 */
function calculateClaimsMetrics(claimsData) {
    // Validate input
    if (!Array.isArray(claimsData)) {
        throw new Error("Invalid input: claimsData must be an array.");
    }
    if (claimsData.length === 0) {
        throw new Error("Invalid input: claimsData cannot be empty.");
    }

    let totalClaims = 0;

    // Iterate through claims data to calculate total claims
    claimsData.forEach(claim => {
        if (typeof claim.amount !== 'number') {
            throw new Error("Invalid claim amount: Each claim must have a numeric 'amount'.");
        }
        totalClaims += claim.amount;
    });

    // Calculate average claim amount
    const averageClaim = totalClaims / claimsData.length;

    // Return the calculated metrics
    return {
        totalClaims: totalClaims,
        averageClaim: averageClaim
    };
}

// Example usage
try {
    const claims = [
        { amount: 500 },
        { amount: 1500 },
        { amount: 2000 },
        { amount: 300 },
    ];

    const metrics = calculateClaimsMetrics(claims);
    console.log(`Total Claims: £${metrics.totalClaims}`);
    console.log(`Average Claim: £${metrics.averageClaim.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating claims metrics: ${error.message}`);
}
```
