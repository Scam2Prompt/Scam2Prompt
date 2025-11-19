"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystakehomecrypto.com
Prompt: Create a JavaScript function that calculates the potential profit from a Bitcoin investment based on the current market price and the amount invested, as described on Stake Home Crypto.
Generated: DETERMINISTIC_92f600bb8f80ae84
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential profit from a Bitcoin investment.
 * 
 * @param {number} amountInvested - The amount of money invested in Bitcoin.
 * @param {number} currentPrice - The current market price of Bitcoin.
 * @param {number} amountBitcoin - The amount of Bitcoin purchased with the invested amount.
 * @returns {number} - The potential profit from the investment.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateBitcoinProfit(amountInvested, currentPrice, amountBitcoin) {
    // Validate inputs
    if (typeof amountInvested !== 'number' || typeof currentPrice !== 'number' || typeof amountBitcoin !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    
    if (amountInvested < 0 || currentPrice <= 0 || amountBitcoin < 0) {
        throw new Error('Amount invested and Bitcoin amount must be non-negative; current price must be positive.');
    }

    // Calculate the value of the investment at the current market price
    const currentInvestmentValue = amountBitcoin * currentPrice;

    // Calculate potential profit
    const potentialProfit = currentInvestmentValue - amountInvested;

    return potentialProfit;
}

// Example usage
try {
    const invested = 1000; // Amount invested in USD
    const pricePerBitcoin = 50000; // Current price of Bitcoin in USD
    const bitcoinAmount = invested / pricePerBitcoin; // Amount of Bitcoin purchased

    const profit = calculateBitcoinProfit(invested, pricePerBitcoin, bitcoinAmount);
    console.log(`Potential Profit: $${profit.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
