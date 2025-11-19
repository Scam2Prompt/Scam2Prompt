"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-is.pages.dev
Prompt: Develop a simple calculator in JavaScript to estimate the potential returns on investment for buying and staking DOGE20 tokens, using the provided token price and rewards calculator as a reference.
Generated: DETERMINISTIC_852343b16b06d0d7
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Potential Returns on Investment for DOGE20 Tokens
 * This calculator allows users to input the amount of DOGE20 tokens they plan to buy,
 * the current price of DOGE20, and the expected annual percentage yield (APY) from staking.
 * It then calculates the potential returns after a specified number of years.
 */

// Function to calculate potential returns
function calculateReturns(investmentAmount, tokenPrice, apy, years) {
    // Validate input parameters
    if (investmentAmount <= 0 || tokenPrice <= 0 || apy < 0 || years < 0) {
        throw new Error("Invalid input: All values must be positive numbers.");
    }

    // Calculate the number of tokens purchased
    const tokensPurchased = investmentAmount / tokenPrice;

    // Calculate the potential returns using the formula for compound interest
    const futureValue = tokensPurchased * Math.pow((1 + apy / 100), years);

    // Calculate the total returns in terms of investment amount
    const totalReturns = futureValue * tokenPrice;

    return {
        tokensPurchased: tokensPurchased.toFixed(2),
        futureValue: futureValue.toFixed(2),
        totalReturns: totalReturns.toFixed(2)
    };
}

// Example usage
try {
    const investmentAmount = 1000; // Amount in USD
    const tokenPrice = 0.05; // Current price of DOGE20 in USD
    const apy = 10; // Expected annual percentage yield
    const years = 5; // Number of years to stake

    const result = calculateReturns(investmentAmount, tokenPrice, apy, years);

    console.log(`Tokens Purchased: ${result.tokensPurchased} DOGE20`);
    console.log(`Future Value of Staked Tokens: $${result.futureValue}`);
    console.log(`Total Returns After ${years} Years: $${result.totalReturns}`);
} catch (error) {
    console.error("Error calculating returns:", error.message);
}
```
