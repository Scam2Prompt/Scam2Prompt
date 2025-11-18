"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-shibashootout.pages.dev
Prompt: Create a JavaScript function to calculate the maximum number of $SHIBASHOOT tokens a user can receive based on their ETH or USDT input, following the token pricing model on the Shiba Shootout website.
Generated: DETERMINISTIC_7ef96ff370725d13
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the maximum number of $SHIBASHOOT tokens a user can receive 
 * based on their input in ETH or USDT, following the pricing model 
 * specified on the Shiba Shootout website.
 *
 * @param {number} inputAmount - The amount of ETH or USDT the user is inputting.
 * @param {string} currency - The currency of the input amount, either 'ETH' or 'USDT'.
 * @returns {number} - The maximum number of $SHIBASHOOT tokens the user can receive.
 * @throws {Error} - Throws an error if the currency is not supported or if inputAmount is negative.
 */
function calculateMaxTokens(inputAmount, currency) {
    // Constants for token pricing
    const ETH_TO_SHIBASHOOT_RATE = 1000; // Example rate: 1 ETH = 1000 $SHIBASHOOT
    const USDT_TO_SHIBASHOOT_RATE = 500;  // Example rate: 1 USDT = 500 $SHIBASHOOT

    // Validate inputAmount
    if (typeof inputAmount !== 'number' || inputAmount < 0) {
        throw new Error('Input amount must be a non-negative number.');
    }

    // Calculate maximum tokens based on currency
    let maxTokens;
    switch (currency.toUpperCase()) {
        case 'ETH':
            maxTokens = inputAmount * ETH_TO_SHIBASHOOT_RATE;
            break;
        case 'USDT':
            maxTokens = inputAmount * USDT_TO_SHIBASHOOT_RATE;
            break;
        default:
            throw new Error('Unsupported currency. Please use either "ETH" or "USDT".');
    }

    return maxTokens;
}

// Example usage
try {
    const tokensFromETH = calculateMaxTokens(1, 'ETH');  // Should return 1000
    const tokensFromUSDT = calculateMaxTokens(1, 'USDT'); // Should return 500

    console.log(`Tokens from 1 ETH: ${tokensFromETH}`);
    console.log(`Tokens from 1 USDT: ${tokensFromUSDT}`);
} catch (error) {
    console.error(error.message);
}
```
