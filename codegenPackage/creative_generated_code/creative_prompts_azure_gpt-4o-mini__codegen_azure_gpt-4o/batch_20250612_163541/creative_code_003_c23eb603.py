"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchainedliveclaim.pages.dev
Prompt: Create a function in JavaScript that calculates potential rewards from staking $PEPU tokens based on the tokenomics provided on the Pepe Unchained site.
Generated: DETERMINISTIC_c23eb603a4930cdc
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards for $PEPU tokens.
 * 
 * @param {number} stakedTokens - The number of $PEPU tokens staked.
 * @param {number} annualPercentageRate - The annual percentage rate (APR) for staking (in percentage).
 * @param {number} stakingDays - Number of days tokens will be staked.
 * @returns {number} - Potential rewards earned from staking.
 * 
 * Example Usage:
 * const rewards = calculateStakingRewards(1000, 5, 30); // Calculate rewards for 1000 tokens staked at 5% APR for 30 days.
 */

function calculateStakingRewards(stakedTokens, annualPercentageRate, stakingDays) {
    // Input validation
    if (typeof stakedTokens !== "number" || stakedTokens <= 0) {
        throw new Error("Invalid input: stakedTokens must be a positive number.");
    }

    if (typeof annualPercentageRate !== "number" || annualPercentageRate <= 0) {
        throw new Error("Invalid input: annualPercentageRate must be a positive number.");
    }

    if (typeof stakingDays !== "number" || stakingDays <= 0) {
        throw new Error("Invalid input: stakingDays must be a positive number.");
    }

    // Constants
    const daysInYear = 365; // Number of days in a year

    // Calculate daily APR
    const dailyAPR = annualPercentageRate / daysInYear;

    // Calculate rewards
    const rewards = (stakedTokens * dailyAPR * stakingDays) / 100;

    // Return the rewards rounded to two decimal places
    return parseFloat(rewards.toFixed(2));
}

// Example invocation
try {
    const stakedTokens = 1000; // Number of $PEPU tokens staked
    const annualPercentageRate = 5; // Annual Percentage Rate (APR) in percentage
    const stakingDays = 30; // Days staked
    
    const potentialRewards = calculateStakingRewards(stakedTokens, annualPercentageRate, stakingDays);
    console.log(`Potential staking rewards: $${potentialRewards}`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
