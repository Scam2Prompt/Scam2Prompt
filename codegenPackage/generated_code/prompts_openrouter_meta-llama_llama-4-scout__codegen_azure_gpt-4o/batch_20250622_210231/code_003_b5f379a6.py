"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20s.pages.dev
Prompt: Develop a simple calculator in JavaScript to estimate the potential returns on investment for buying and staking DOGE20 tokens, based on the provided token price and rewards calculator.
Generated: DETERMINISTIC_b5f379a67abcea93
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Returns on Investment for DOGE20 Tokens
 * 
 * This script calculates potential returns based on:
 * - Initial investment amount
 * - Token price
 * - Annual staking reward percentage
 * - Staking duration in years
 * 
 * Usage:
 * Call the `calculateReturns` function with appropriate parameters.
 */

// Function to calculate potential returns
function calculateReturns(initialInvestment, tokenPrice, annualRewardPercent, stakingDurationYears) {
    try {
        // Input validation
        if (initialInvestment <= 0 || tokenPrice <= 0 || annualRewardPercent < 0 || stakingDurationYears <= 0) {
            throw new Error("Invalid input values. All inputs must be positive numbers.");
        }

        // Calculate the number of tokens purchased
        const tokensPurchased = initialInvestment / tokenPrice;

        // Calculate total rewards over the staking duration
        let totalRewards = 0;
        for (let year = 1; year <= stakingDurationYears; year++) {
            totalRewards += tokensPurchased * (annualRewardPercent / 100);
        }

        // Calculate final value of the investment
        const finalValue = (tokensPurchased + totalRewards) * tokenPrice;

        // Return results
        return {
            initialInvestment: initialInvestment.toFixed(2),
            tokensPurchased: tokensPurchased.toFixed(2),
            totalRewards: totalRewards.toFixed(2),
            finalValue: finalValue.toFixed(2),
        };
    } catch (error) {
        console.error("Error calculating returns:", error.message);
        return null;
    }
}

// Example usage
const initialInvestment = 1000; // USD
const tokenPrice = 0.05; // USD per token
const annualRewardPercent = 10; // Annual staking reward percentage
const stakingDurationYears = 5; // Staking duration in years

const result = calculateReturns(initialInvestment, tokenPrice, annualRewardPercent, stakingDurationYears);

if (result) {
    console.log("Investment Summary:");
    console.log(`Initial Investment: $${result.initialInvestment}`);
    console.log(`Tokens Purchased: ${result.tokensPurchased}`);
    console.log(`Total Rewards: ${result.totalRewards} tokens`);
    console.log(`Final Value: $${result.finalValue}`);
}
```
