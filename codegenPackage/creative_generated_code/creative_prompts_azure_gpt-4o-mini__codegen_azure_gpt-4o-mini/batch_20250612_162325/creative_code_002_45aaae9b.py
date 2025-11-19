"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Generate a JavaScript function that calculates the total amount of PLINU tokens received when purchasing with USDT, including the 10% bonus.
Generated: DETERMINISTIC_45aaae9b7e63f7b5
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the total amount of PLINU tokens received when purchasing with USDT.
 * This function includes a 10% bonus on the purchased amount of PLINU tokens.
 * 
 * @param {number} usdtAmount - The amount of USDT being used for the purchase.
 * @param {number} tokenPrice - The price of one PLINU token in USDT.
 * @returns {number} - The total amount of PLINU tokens received, including bonus.
 * @throws {Error} - Throws an error if usdtAmount or tokenPrice is not a positive number.
 */
function calculatePlinuTokens(usdtAmount, tokenPrice) {
    // Validate input parameters
    if (typeof usdtAmount !== 'number' || typeof tokenPrice !== 'number') {
        throw new Error('USDT amount and token price must be numbers.');
    }
    if (usdtAmount <= 0 || tokenPrice <= 0) {
        throw new Error('USDT amount and token price must be positive numbers.');
    }

    // Calculate the number of tokens purchased without the bonus
    const tokensPurchased = usdtAmount / tokenPrice;

    // Calculate the 10% bonus
    const bonus = tokensPurchased * 0.10;

    // Calculate the total tokens received
    const totalTokens = tokensPurchased + bonus;

    return totalTokens;
}

// Example usage of the function
try {
    const usdtAmount = 100; // Amount of USDT to spend
    const tokenPrice = 2;   // Price of one PLINU token in USDT
    const totalTokens = calculatePlinuTokens(usdtAmount, tokenPrice);
    console.log(`Total PLINU tokens received: ${totalTokens}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
