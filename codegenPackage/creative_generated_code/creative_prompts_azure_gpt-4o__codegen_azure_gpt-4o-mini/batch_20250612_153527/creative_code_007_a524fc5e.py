"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnice.xyz
Prompt: Write a function in JavaScript to calculate transaction fees for Ethereum-based DeFi operations.
Generated: DETERMINISTIC_a524fc5ee7eeb9ef
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the transaction fees for Ethereum-based DeFi operations.
 * 
 * @param {number} gasPrice - The gas price in Gwei (1 Gwei = 10^-9 ETH).
 * @param {number} gasLimit - The gas limit for the transaction.
 * @returns {number} - The transaction fee in ETH.
 * @throws {Error} - Throws an error if the inputs are not valid numbers or if they are less than or equal to zero.
 */
function calculateTransactionFee(gasPrice, gasLimit) {
    // Validate the input parameters
    if (typeof gasPrice !== 'number' || typeof gasLimit !== 'number') {
        throw new Error('Both gasPrice and gasLimit must be numbers.');
    }
    if (gasPrice <= 0 || gasLimit <= 0) {
        throw new Error('Both gasPrice and gasLimit must be greater than zero.');
    }

    // Convert gas price from Gwei to ETH
    const gasPriceInEth = gasPrice * Math.pow(10, -9);

    // Calculate the transaction fee in ETH
    const transactionFee = gasPriceInEth * gasLimit;

    return transactionFee;
}

// Example usage:
try {
    const gasPrice = 100; // in Gwei
    const gasLimit = 21000; // standard gas limit for a simple transaction
    const fee = calculateTransactionFee(gasPrice, gasLimit);
    console.log(`Transaction Fee: ${fee} ETH`);
} catch (error) {
    console.error(`Error calculating transaction fee: ${error.message}`);
}
```
