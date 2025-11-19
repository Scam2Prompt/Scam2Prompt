"""
Generated Code Metadata:
========================
Original URL: https://pulsedapp.pages.dev
Prompt: Create a JavaScript function to calculate the amount of PLS tokens received after bridging from Ethereum, considering the fee structure provided by the PulseChain Bridge.
Generated: DETERMINISTIC_a5ed1f49f7945f14
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the amount of PLS tokens received after bridging from Ethereum,
 * considering the PulseChain Bridge fee structure.
 * 
 * @param {number} amountEth - The amount of ETH to bridge (in wei or smallest unit)
 * @param {number} feePercentage - The bridge fee percentage (e.g., 0.1 for 10%)
 * @param {number} exchangeRate - The ETH to PLS exchange rate (1 ETH = X PLS)
 * @param {boolean} [isWei=true] - Whether the input amount is in wei (true) or ETH (false)
 * @returns {number} The amount of PLS tokens received after fees
 * @throws {Error} If input parameters are invalid
 */
function calculatePlsReceived(amountEth, feePercentage, exchangeRate, isWei = true) {
    // Validate input parameters
    if (typeof amountEth !== 'number' || amountEth <= 0) {
        throw new Error('Amount must be a positive number');
    }
    if (typeof feePercentage !== 'number' || feePercentage < 0 || feePercentage >= 100) {
        throw new Error('Fee percentage must be between 0 and 100');
    }
    if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
        throw new Error('Exchange rate must be a positive number');
    }

    // Convert from wei to ETH if needed
    let amountInEth = isWei ? amountEth / 1e18 : amountEth;

    // Calculate amount after fees
    const feeAmount = amountInEth * (feePercentage / 100);
    const amountAfterFees = amountInEth - feeAmount;

    // Convert to PLS using exchange rate
    const plsReceived = amountAfterFees * exchangeRate;

    // Return the result with 8 decimal places precision
    return parseFloat(plsReceived.toFixed(8));
}

// Example usage:
// try {
//     const pls = calculatePlsReceived(1e18, 0.1, 10000, true);
//     console.log(`PLS received: ${pls}`);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
