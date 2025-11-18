"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Write a function in JavaScript that calculates the maximum $WAI tokens a user can receive based on their ETH payment, factoring in the current $WAI price and gas fees.
Generated: DETERMINISTIC_ff6b048cc6c3b533
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the maximum WAI tokens a user can receive
 * based on their ETH payment, current WAI price, and gas fees.
 *
 * @param {number} ethPayment - The amount of ETH the user is paying.
 * @param {number} waiPrice - The current price of WAI in ETH.
 * @param {number} gasFees - The gas fees in ETH for the transaction.
 * @returns {number} - The maximum WAI tokens the user can receive.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateMaxWaiTokens(ethPayment, waiPrice, gasFees) {
    // Validate input types
    if (typeof ethPayment !== 'number' || typeof waiPrice !== 'number' || typeof gasFees !== 'number') {
        throw new Error('Invalid input type: ethPayment, waiPrice, and gasFees must be numbers.');
    }

    // Validate input values
    if (ethPayment < 0 || waiPrice <= 0 || gasFees < 0) {
        throw new Error('Invalid input value: ethPayment and gasFees must be >= 0, and waiPrice must be > 0.');
    }

    // Calculate the net ETH available for WAI purchase after deducting gas fees
    const netEth = ethPayment - gasFees;

    // If net ETH is less than or equal to zero, return 0 tokens
    if (netEth <= 0) {
        return 0;
    }

    // Calculate the maximum WAI tokens the user can receive
    const maxWaiTokens = netEth / waiPrice;

    // Return the maximum WAI tokens, ensuring it is rounded down to the nearest whole number
    return Math.floor(maxWaiTokens);
}

// Example Usage:
try {
    const ethPayment = 1.0; // User's ETH payment
    const waiPrice = 0.01;  // Current WAI price in ETH
    const gasFees = 0.002;   // Gas fees in ETH

    const maxTokens = calculateMaxWaiTokens(ethPayment, waiPrice, gasFees);
    console.log(`Maximum WAI tokens you can receive: ${maxTokens}`);
} catch (error) {
    console.error(`Error calculating WAI tokens: ${error.message}`);
}
```
