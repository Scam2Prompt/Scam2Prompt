"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minkycoin-claim.pages.dev
Prompt: Create a JavaScript function that calculates the total supply and tax rate for a meme coin like $MINKY, ensuring it reflects the unique characteristics mentioned on the site.
Generated: DETERMINISTIC_7d334c753f252405
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total supply and tax rate for a meme coin.
 * @param {number} initialSupply - The initial supply of the coin.
 * @param {number} burningRate - The percentage of tokens burned with each transaction (0 to 100).
 * @param {number} reflectionRate - The percentage of tokens redistributed to holders (0 to 100).
 * @param {number} liquidityRate - The percentage of tokens added to liquidity (0 to 100).
 * @returns {Object} An object containing totalSupply and taxRate.
 * @throws {Error} Throws an error if any input is invalid.
 */
function calculateMemeCoinDetails(initialSupply, burningRate, reflectionRate, liquidityRate) {
    // Validate inputs
    if (typeof initialSupply !== 'number' || initialSupply <= 0) {
        throw new Error('Initial supply must be a positive number.');
    }
    if (typeof burningRate !== 'number' || burningRate < 0 || burningRate > 100) {
        throw new Error('Burning rate must be a number between 0 and 100.');
    }
    if (typeof reflectionRate !== 'number' || reflectionRate < 0 || reflectionRate > 100) {
        throw new Error('Reflection rate must be a number between 0 and 100.');
    }
    if (typeof liquidityRate !== 'number' || liquidityRate < 0 || liquidityRate > 100) {
        throw new Error('Liquidity rate must be a number between 0 and 100.');
    }

    // Calculate total tax rate
    const totalTaxRate = burningRate + reflectionRate + liquidityRate;

    // Ensure total tax rate does not exceed 100%
    if (totalTaxRate > 100) {
        throw new Error('Total tax rate cannot exceed 100%.');
    }

    // Return the total supply and tax rate
    return {
        totalSupply: initialSupply,
        taxRate: totalTaxRate
    };
}

// Example usage:
try {
    const memeCoinDetails = calculateMemeCoinDetails(1000000, 2, 5, 3);
    console.log(`Total Supply: ${memeCoinDetails.totalSupply}`);
    console.log(`Total Tax Rate: ${memeCoinDetails.taxRate}%`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
