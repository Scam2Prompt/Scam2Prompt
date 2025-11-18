"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmeme.life
Prompt: Develop a JavaScript function that calculates the total token allocation for liquidity, marketing, airdrop, and Binance Launchpool based on the TRUMP MEME tokenomics percentages.
Generated: DETERMINISTIC_c02582a3fea372c5
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total token allocation based on specified percentages for different categories
 * in TRUMP MEME tokenomics.
 *
 * @param {number} totalSupply - The total supply of tokens.
 * @param {Object} allocations - An object containing allocation percentages for each category.
 * @param {number} allocations.liquidity - Percentage allocated for liquidity.
 * @param {number} allocations.marketing - Percentage allocated for marketing.
 * @param {number} allocations.airdrop - Percentage allocated for airdrop.
 * @param {number} allocations.binanceLaunchpool - Percentage allocated for Binance Launchpool.
 * @returns {Object} - An object containing the allocated tokens for each category.
 * @throws {Error} - Throws an error if totalSupply is not positive or if any percentage is invalid.
 */
function calculateTokenAllocations(totalSupply, allocations) {
    // Validate total supply
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Total supply must be a positive number.');
    }

    // Validate allocation percentages
    const { liquidity, marketing, airdrop, binanceLaunchpool } = allocations;

    if (!isValidPercentage(liquidity) || !isValidPercentage(marketing) || 
        !isValidPercentage(airdrop) || !isValidPercentage(binanceLaunchpool)) {
        throw new Error('All allocations must be valid percentages (0-100).');
    }

    // Calculate allocations
    const liquidityAllocation = (totalSupply * liquidity) / 100;
    const marketingAllocation = (totalSupply * marketing) / 100;
    const airdropAllocation = (totalSupply * airdrop) / 100;
    const binanceLaunchpoolAllocation = (totalSupply * binanceLaunchpool) / 100;

    // Return the result as an object
    return {
        liquidity: liquidityAllocation,
        marketing: marketingAllocation,
        airdrop: airdropAllocation,
        binanceLaunchpool: binanceLaunchpoolAllocation,
    };
}

/**
 * Validates if a given percentage is within the acceptable range (0 to 100).
 *
 * @param {number} percentage - The percentage to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
function isValidPercentage(percentage) {
    return typeof percentage === 'number' && percentage >= 0 && percentage <= 100;
}

// Example usage:
try {
    const totalSupply = 1000000; // Example total supply
    const allocations = {
        liquidity: 30, // 30%
        marketing: 20, // 20%
        airdrop: 10,   // 10%
        binanceLaunchpool: 40, // 40%
    };

    const tokenAllocations = calculateTokenAllocations(totalSupply, allocations);
    console.log(tokenAllocations);
} catch (error) {
    console.error(error.message);
}
```
