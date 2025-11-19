"""
Generated Code Metadata:
========================
Original URL: https://whitelist-gummyonsol.pages.dev
Prompt: Generate a code snippet in JavaScript to calculate the $Gummy token allocation for a user who claims the airdrop, considering the provided tokenomics breakdown.
Generated: DETERMINISTIC_d2921ff96b967d9f
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates Gummy token allocation for a user based on tokenomics breakdown
 * @param {Object} user - User details
 * @param {number} user.eligibleTokens - Number of tokens user is eligible for
 * @param {Object} tokenomics - Token distribution breakdown
 * @param {number} tokenomics.airdropAllocation - Percentage allocated for airdrop (e.g., 15 for 15%)
 * @param {number} tokenomics.totalSupply - Total token supply
 * @param {number} totalEligibleTokens - Total eligible tokens across all users
 * @returns {Object} - Allocation details
 */
function calculateGummyAllocation(user, tokenomics, totalEligibleTokens) {
    // Validate input parameters
    if (!user || typeof user.eligibleTokens !== 'number' || user.eligibleTokens <= 0) {
        throw new Error('Invalid user data: eligibleTokens must be a positive number');
    }
    if (!tokenomics || typeof tokenomics.airdropAllocation !== 'number' || 
        typeof tokenomics.totalSupply !== 'number' || tokenomics.totalSupply <= 0) {
        throw new Error('Invalid tokenomics data: airdropAllocation and totalSupply must be positive numbers');
    }
    if (typeof totalEligibleTokens !== 'number' || totalEligibleTokens <= 0) {
        throw new Error('totalEligibleTokens must be a positive number');
    }

    // Calculate user's share of the airdrop pool
    const airdropPool = (tokenomics.airdropAllocation / 100) * tokenomics.totalSupply;
    const userShare = user.eligibleTokens / totalEligibleTokens;
    const userAllocation = userShare * airdropPool;

    // Round to avoid floating point precision issues
    const roundedAllocation = Math.round(userAllocation * 100) / 100;

    return {
        allocation: roundedAllocation,
        airdropPool: airdropPool,
        userShare: userShare,
        eligibleTokens: user.eligibleTokens
    };
}

// Example usage:
/*
const user = { eligibleTokens: 5000 };
const tokenomics = { airdropAllocation: 15, totalSupply: 10000000 };
const totalEligibleTokens = 25000000;

try {
    const result = calculateGummyAllocation(user, tokenomics, totalEligibleTokens);
    console.log('Allocation Result:', result);
} catch (error) {
    console.error('Error calculating allocation:', error.message);
}
*/
```
