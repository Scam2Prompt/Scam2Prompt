"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hvneh.com
Prompt: Create a JavaScript function to calculate gas fees for Ethereum transactions in a DeFi application.
Generated: DETERMINISTIC_d906def5c7989692
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated gas fees for Ethereum transactions.
 * 
 * @param {number} gasPrice - The price of gas (in Gwei) for the transaction.
 * @param {number} gasLimit - The maximum amount of gas units that the transaction may consume.
 * @returns {string} - The estimated gas fee in Ether.
 * @throws {Error} - Throws an error if gasPrice or gasLimit is not a positive number.
 */
function calculateGasFees(gasPrice, gasLimit) {
    // Validate inputs
    if (typeof gasPrice !== 'number' || gasPrice <= 0) {
        throw new Error('Invalid gas price. It must be a positive number.');
    }
    if (typeof gasLimit !== 'number' || gasLimit <= 0) {
        throw new Error('Invalid gas limit. It must be a positive number.');
    }

    // Convert gas price from Gwei to Ether (1 Ether = 1e9 Gwei)
    const gasPriceInEther = gasPrice / 1e9;

    // Calculate gas fees in Ether
    const gasFeesInEther = gasPriceInEther * gasLimit;

    // Return gas fees formatted to 18 decimal places for precision
    return gasFeesInEther.toFixed(18);
}

// Example usage:
try {
    const gasPrice = 100; // Gas price in Gwei
    const gasLimit = 21000; // Gas limit for a standard ETH transfer
    const estimatedFees = calculateGasFees(gasPrice, gasLimit);
    console.log(`Estimated gas fees: ${estimatedFees} ETH`);
} catch (error) {
    console.error(`Error calculating gas fees: ${error.message}`);
}
```
