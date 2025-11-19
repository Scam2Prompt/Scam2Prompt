"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol-51d.pages.dev
Prompt: Generate a code snippet in JavaScript to calculate the $Gummy token distribution based on the provided percentages for airdrop, CEX liquidity, market makers, LP, and team founders.
Generated: DETERMINISTIC_6ef5ce0212247660
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates Gummy token distribution based on predefined allocation percentages.
 * @param {number} totalSupply - Total supply of Gummy tokens
 * @returns {Object} An object containing the distribution amounts
 * @throws {Error} If totalSupply is not a positive number
 */
function calculateGummyDistribution(totalSupply) {
    // Validate input
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Total supply must be a positive number');
    }

    // Allocation percentages
    const allocation = {
        airdrop: 0.15,       // 15%
        cexLiquidity: 0.25,  // 25%
        marketMakers: 0.10,  // 10%
        lp: 0.30,            // 30%
        teamFounders: 0.20   // 20%
    };

    // Calculate token amounts for each category
    const distribution = {
        airdrop: Math.floor(totalSupply * allocation.airdrop),
        cexLiquidity: Math.floor(totalSupply * allocation.cexLiquidity),
        marketMakers: Math.floor(totalSupply * allocation.marketMakers),
        lp: Math.floor(totalSupply * allocation.lp),
        teamFounders: Math.floor(totalSupply * allocation.teamFounders)
    };

    // Calculate remaining tokens due to flooring
    const distributed = Object.values(distribution).reduce((sum, val) => sum + val, 0);
    distribution.remaining = totalSupply - distributed;

    return distribution;
}

// Example usage:
try {
    const totalTokens = 1000000000; // 1 billion tokens
    const tokenDistribution = calculateGummyDistribution(totalTokens);
    console.log('Token Distribution:', tokenDistribution);
} catch (error) {
    console.error('Error calculating token distribution:', error.message);
}
```
