"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: Develop a JavaScript function to calculate the potential returns of DOGE20 tokens using the presale price and a user-defined future price.
Generated: DETERMINISTIC_6b81d507f3418371
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential returns of DOGE20 tokens based on the presale price and future price.
 * 
 * @param {number} presalePrice - The price at which the DOGE20 tokens were purchased.
 * @param {number} futurePrice - The projected price of DOGE20 tokens in the future.
 * @param {number} tokensOwned - The number of DOGE20 tokens owned by the user.
 * @returns {object} An object containing the total investment, potential future value, and total profit.
 * @throws {Error} If any input is not a positive number or tokensOwned is not an integer.
 */
function calculateDoge20Returns(presalePrice, futurePrice, tokensOwned) {
    // Validate input parameters
    if (typeof presalePrice !== 'number' || presalePrice <= 0) {
        throw new Error('Presale price must be a positive number.');
    }
    if (typeof futurePrice !== 'number' || futurePrice <= 0) {
        throw new Error('Future price must be a positive number.');
    }
    if (!Number.isInteger(tokensOwned) || tokensOwned < 0) {
        throw new Error('Tokens owned must be a non-negative integer.');
    }

    // Calculate total investment
    const totalInvestment = presalePrice * tokensOwned;

    // Calculate potential future value
    const potentialFutureValue = futurePrice * tokensOwned;

    // Calculate total profit
    const totalProfit = potentialFutureValue - totalInvestment;

    // Return the results as an object
    return {
        totalInvestment: totalInvestment.toFixed(2), // Format to 2 decimal places
        potentialFutureValue: potentialFutureValue.toFixed(2), // Format to 2 decimal places
        totalProfit: totalProfit.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage of the function
try {
    const returns = calculateDoge20Returns(0.05, 0.10, 1000);
    console.log('Potential Returns:', returns);
} catch (error) {
    console.error('Error calculating returns:', error.message);
}
```
