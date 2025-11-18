"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a JavaScript function to calculate gas fees for minting NFTs on the Ethereum blockchain, referencing the minting process described on the Robots NFT Minting website.
Generated: DETERMINISTIC_d975b25b198c84ab
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates gas fees for minting NFTs on the Ethereum blockchain.
 * 
 * @param {number} gasPrice - The price of gas in gwei.
 * @param {number} gasLimit - The limit of gas used for the minting transaction.
 * @returns {string} - The total gas fee in Ether, formatted to 18 decimal places.
 * @throws {Error} - Throws an error if gasPrice or gasLimit is not a positive number.
 */
function calculateGasFees(gasPrice, gasLimit) {
    // Validate input parameters
    if (typeof gasPrice !== 'number' || gasPrice <= 0) {
        throw new Error('Invalid gas price. It must be a positive number.');
    }
    if (typeof gasLimit !== 'number' || gasLimit <= 0) {
        throw new Error('Invalid gas limit. It must be a positive number.');
    }

    // Calculate total gas fee in gwei
    const totalGasFeeGwei = gasPrice * gasLimit;

    // Convert gas fee from gwei to Ether (1 Ether = 1e9 gwei)
    const totalGasFeeEther = totalGasFeeGwei / 1e9;

    // Return the total gas fee formatted to 18 decimal places
    return totalGasFeeEther.toFixed(18);
}

// Example usage:
try {
    const gasPrice = 100; // Gas price in gwei
    const gasLimit = 21000; // Gas limit for minting an NFT
    const gasFees = calculateGasFees(gasPrice, gasLimit);
    console.log(`Total gas fees for minting: ${gasFees} ETH`);
} catch (error) {
    console.error(error.message);
}
```
