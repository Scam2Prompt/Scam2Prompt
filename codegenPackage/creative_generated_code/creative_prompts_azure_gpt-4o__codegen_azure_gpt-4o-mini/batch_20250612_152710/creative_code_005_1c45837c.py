"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Write a JavaScript function that uses the DOGE20 returns calculator logic to estimate the future value of purchased tokens based on user input for token quantity and price.
Generated: DETERMINISTIC_1c45837c85a0ac73
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the future value of DOGE20 tokens based on the quantity purchased,
 * the current price per token, and an estimated return percentage.
 * 
 * @param {number} quantity - The number of DOGE20 tokens purchased.
 * @param {number} pricePerToken - The current price per DOGE20 token.
 * @param {number} estimatedReturnPercentage - The projected percentage return.
 * @returns {number} The estimated future value of the tokens.
 * @throws Will throw an error if any of the inputs are not valid numbers.
 */
function calculateFutureValue(quantity, pricePerToken, estimatedReturnPercentage) {
    // Validate inputs
    if (typeof quantity !== 'number' || typeof pricePerToken !== 'number' || typeof estimatedReturnPercentage !== 'number') {
        throw new Error('All inputs must be valid numbers.');
    }
    if (quantity < 0 || pricePerToken < 0 || estimatedReturnPercentage < 0) {
        throw new Error('All inputs must be non-negative numbers.');
    }

    // Calculate the initial investment value
    const initialInvestment = quantity * pricePerToken;

    // Calculate the estimated future value based on the return percentage
    const futureValue = initialInvestment * (1 + estimatedReturnPercentage / 100);

    return futureValue;
}

// Example usage:
// To estimate the future value of 100 tokens purchased at $0.05 each with a 20% estimated return:
// const futureValue = calculateFutureValue(100, 0.05, 20);
// console.log(`Estimated future value: $${futureValue.toFixed(2)}`);
```

This code provides a function to calculate the future value of DOGE20 tokens, ensuring proper validation, error handling, and documentation for maintainability and clarity.
