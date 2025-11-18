"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Develop a JavaScript function to use zkSwap Finance's ZAP feature for converting multiple tokens into liquidity pool shares in one transaction.
Generated: DETERMINISTIC_933818a884245d21
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function zapToLiquidityPool
 * @description Converts multiple tokens into liquidity pool shares using zkSwap Finance's ZAP feature.
 * @param {Object} zkSwap - The zkSwap object containing the necessary methods for interacting with the zkSwap API.
 * @param {string} poolAddress - The address of the liquidity pool to which tokens will be added.
 * @param {Array} tokenAmounts - An array of objects, each containing 'tokenAddress' and 'amount' to be converted.
 * @param {string} userAddress - The address of the user performing the transaction.
 * @returns {Promise<Object>} - A promise that resolves to the transaction receipt or an error message.
 * @throws {Error} - Throws an error if the transaction fails or parameters are invalid.
 */
async function zapToLiquidityPool(zkSwap, poolAddress, tokenAmounts, userAddress) {
    // Validate parameters
    if (!zkSwap || !poolAddress || !Array.isArray(tokenAmounts) || tokenAmounts.length === 0 || !userAddress) {
        throw new Error('Invalid parameters: Ensure all parameters are provided and valid.');
    }

    try {
        // Prepare the transaction details for the ZAP feature
        const zapTx = await zkSwap.zap({
            pool: poolAddress,
            tokens: tokenAmounts,
            user: userAddress
        });

        // Wait for the transaction to be mined and confirmed
        const receipt = await zapTx.wait();

        // Return the transaction receipt for confirmation
        return receipt;
    } catch (error) {
        // Handle errors, logging the error message for debugging
        console.error('Error during ZAP transaction:', error);
        throw new Error('Transaction failed: ' + error.message);
    }
}
```
