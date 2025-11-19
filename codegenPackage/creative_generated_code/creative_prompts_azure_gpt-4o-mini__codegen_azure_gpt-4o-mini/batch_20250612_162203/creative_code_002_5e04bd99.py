"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lermlinstrate.pages.dev
Prompt: Create a JavaScript function that calculates the token price for $MP in relation to BTC and M-BTC based on the details provided by MerlinSwap.
Generated: DETERMINISTIC_5e04bd997b30d437
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the token price for $MP in relation to BTC and M-BTC based on 
 * the details provided by MerlinSwap.
 * 
 * @param {number} mpSupply - The total supply of $MP tokens.
 * @param {number} totalSupplyBtc - The total supply of BTC.
 * @param {number} totalSupplyMBtc - The total supply of M-BTC.
 * @param {number} mpLiquidity - The current liquidity of $MP in the market.
 * @param {number} btcPrice - The current price of BTC in USD.
 * @param {number} mBtcPrice - The current price of M-BTC in USD.
 * @returns {number} - The calculated price of one $MP token in relation to BTC and M-BTC.
 * @throws {Error} - Throws an error if any input is invalid or if the supply is zero.
 */
function calculateTokenPrice(mpSupply, totalSupplyBtc, totalSupplyMBtc, mpLiquidity, btcPrice, mBtcPrice) {
    // Input validation
    if (mpSupply <= 0 || totalSupplyBtc <= 0 || totalSupplyMBtc <= 0 || mpLiquidity <= 0 || btcPrice <= 0 || mBtcPrice <= 0) {
        throw new Error("Invalid input: All inputs must be positive numbers greater than zero.");
    }

    // Calculate the value of total liquidity in terms of BTC and M-BTC
    const totalLiquidityValue = (mpLiquidity * (btcPrice + mBtcPrice)) / 2;

    // Calculate the price of one $MP token
    const tokenPrice = totalLiquidityValue / mpSupply;

    return tokenPrice;
}

// Example usage
try {
    const mpSupply = 1000000; // Total supply of $MP tokens
    const totalSupplyBtc = 21000000; // Total supply of BTC
    const totalSupplyMBtc = 1000000; // Total supply of M-BTC
    const mpLiquidity = 500000; // Current liquidity of $MP
    const btcPrice = 45000; // Current price of BTC in USD
    const mBtcPrice = 0.045; // Current price of M-BTC in USD

    const price = calculateTokenPrice(mpSupply, totalSupplyBtc, totalSupplyMBtc, mpLiquidity, btcPrice, mBtcPrice);
    console.log(`The calculated price of one $MP token is: $${price.toFixed(4)}`);
} catch (error) {
    console.error(`Error calculating token price: ${error.message}`);
}
```
