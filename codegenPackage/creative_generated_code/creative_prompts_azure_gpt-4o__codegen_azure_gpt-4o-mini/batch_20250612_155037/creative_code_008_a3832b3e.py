"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Write a JavaScript function to calculate the number of $WING tokens a user will receive based on the current exchange rate and payment method (ETH or USDT), as described on the Dopawing website.
Generated: DETERMINISTIC_a3832b3e579bc110
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the number of $WING tokens a user will receive based on the current exchange rate 
 * and payment method (ETH or USDT).
 * 
 * @param {number} amount - The amount of payment in either ETH or USDT.
 * @param {string} paymentMethod - The payment method, either 'ETH' or 'USDT'.
 * @param {number} ethRate - The current exchange rate for ETH to $WING tokens.
 * @param {number} usdtRate - The current exchange rate for USDT to $WING tokens.
 * @returns {number} The number of $WING tokens received.
 * @throws {Error} Throws an error if the payment method is invalid or if the amount is negative.
 */
function calculateWingTokens(amount, paymentMethod, ethRate, usdtRate) {
    // Validate the payment method
    if (paymentMethod !== 'ETH' && paymentMethod !== 'USDT') {
        throw new Error("Invalid payment method. Please use 'ETH' or 'USDT'.");
    }

    // Validate the amount
    if (amount < 0) {
        throw new Error("Amount must be a non-negative number.");
    }

    // Calculate the $WING tokens based on payment method
    let wingTokens;
    if (paymentMethod === 'ETH') {
        wingTokens = amount * ethRate;
    } else if (paymentMethod === 'USDT') {
        wingTokens = amount * usdtRate;
    }

    // Return the calculated number of $WING tokens
    return wingTokens;
}

// Example usage
try {
    const ethRate = 100; // Example rate: 1 ETH = 100 WING
    const usdtRate = 50; // Example rate: 1 USDT = 50 WING

    const tokensReceived = calculateWingTokens(1, 'ETH', ethRate, usdtRate);
    console.log(`Tokens received: ${tokensReceived}`);
} catch (error) {
    console.error(error.message);
}
```
