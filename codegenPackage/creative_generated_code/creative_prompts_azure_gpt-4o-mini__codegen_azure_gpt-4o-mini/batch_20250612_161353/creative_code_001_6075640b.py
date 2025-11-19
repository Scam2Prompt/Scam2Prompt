"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Write a JavaScript function that calculates the total rewards earned by a delegator in the bitsCrunch Network based on their delegated amount and query fee cut.
Generated: DETERMINISTIC_6075640b8fd2f7b0
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total rewards earned by a delegator in the bitsCrunch Network.
 *
 * @param {number} delegatedAmount - The amount of tokens delegated by the user.
 * @param {number} queryFeeCut - The percentage of the query fees that the delegator receives, represented as a decimal (e.g., 0.20 for 20%).
 * @param {number} totalQueryFees - The total query fees collected within the relevant period.
 * @returns {number} - The total rewards earned by the delegator.
 * @throws {Error} - Throws an error if any input is invalid (negative values or non-numeric inputs).
 */
function calculateDelegatorRewards(delegatedAmount, queryFeeCut, totalQueryFees) {
    // Input validation
    if (typeof delegatedAmount !== 'number' || delegatedAmount < 0) {
        throw new Error('Invalid delegated amount. It must be a non-negative number.');
    }
    if (typeof queryFeeCut !== 'number' || queryFeeCut < 0 || queryFeeCut > 1) {
        throw new Error('Invalid query fee cut. It must be a number between 0 and 1.');
    }
    if (typeof totalQueryFees !== 'number' || totalQueryFees < 0) {
        throw new Error('Invalid total query fees. It must be a non-negative number.');
    }

    // Calculate total rewards
    const rewardsFromQueryFees = totalQueryFees * queryFeeCut;

    // Calculate total rewards based on the delegated amount (optional aspect)
    const totalRewards = rewardsFromQueryFees + delegatedAmount;

    return totalRewards;
}

// Example usage:
try {
    const rewards = calculateDelegatorRewards(1000, 0.20, 500);
    console.log(`Total rewards earned: ${rewards}`);
} catch (error) {
    console.error(error.message);
}
```
