"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Generate a code snippet in JavaScript to calculate the token distribution of $Gummy based on the provided tokenomics: 30% CEX Liquidity, 10% Market Makers, 20% Marketing LP, and 40% burnt.
Generated: DETERMINISTIC_ca573d257e984d70
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
 * Calculates token distribution based on specified tokenomics.
 * @param {number} totalSupply - Total supply of $Gummy tokens
 * @returns {Object} - Object containing distribution amounts
 */
function calculateTokenDistribution(totalSupply) {
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Total supply must be a positive number');
    }

    const distribution = {
        cexLiquidity: 0,
        marketMakers: 0,
        marketingLP: 0,
        burnt: 0
    };

    try {
        distribution.cexLiquidity = totalSupply * 0.30;
        distribution.marketMakers = totalSupply * 0.10;
        distribution.marketingLP = totalSupply * 0.20;
        distribution.burnt = totalSupply * 0.40;

        // Validate sum equals total supply (accounting for floating point precision)
        const sum = Object.values(distribution).reduce((acc, val) => acc + val, 0);
        if (Math.abs(sum - totalSupply) > 0.0001) {
            throw new Error('Distribution calculation error: sum does not match total supply');
        }

        return distribution;
    } catch (error) {
        console.error('Error calculating token distribution:', error.message);
        throw error;
    }
}

// Example usage:
// const totalSupply = 1000000; // 1 million tokens
// const distribution = calculateTokenDistribution(totalSupply);
// console.log(distribution);
```
