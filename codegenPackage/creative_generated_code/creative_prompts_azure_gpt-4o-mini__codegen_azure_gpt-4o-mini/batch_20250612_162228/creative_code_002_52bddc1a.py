"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Create a JavaScript function to calculate the amount of $HEHE tokens received when swapping a specific amount of USDT, referencing the presale details provided on the webpage.
Generated: DETERMINISTIC_52bddc1acb487c2a
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of $HEHE tokens received when swapping a specific
 * amount of USDT based on presale details.
 *
 * @param {number} usdtAmount - The amount of USDT to swap.
 * @param {number} presaleRate - The rate of $HEHE tokens per USDT.
 * @returns {number} - The amount of $HEHE tokens received.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateHEHETokens(usdtAmount, presaleRate) {
    // Validate input
    if (typeof usdtAmount !== 'number' || typeof presaleRate !== 'number') {
        throw new Error('Both usdtAmount and presaleRate must be numbers.');
    }
    if (usdtAmount < 0 || presaleRate < 0) {
        throw new Error('Both usdtAmount and presaleRate must be non-negative.');
    }

    // Calculate the amount of $HEHE tokens received
    const heheTokensReceived = usdtAmount * presaleRate;

    // Return the calculated amount of $HEHE tokens
    return heheTokensReceived;
}

// Example usage:
try {
    const usdtAmount = 100; // Amount of USDT to swap
    const presaleRate = 200; // Example presale rate of $HEHE tokens per USDT
    const tokens = calculateHEHETokens(usdtAmount, presaleRate);
    console.log(`You will receive ${tokens} $HEHE tokens for swapping ${usdtAmount} USDT.`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
