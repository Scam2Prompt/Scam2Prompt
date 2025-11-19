"""
Generated Code Metadata:
========================
Original URL: https://convexfinance.io
Prompt: Design a function in JavaScript that calculates the estimated rewards for staking cvxCRV on Convex Finance, taking into account the current APY and compounding frequency.
Generated: DETERMINISTIC_42c0e20d8bd7b6c2
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated rewards for staking cvxCRV on Convex Finance.
 * 
 * @param {number} principal - The amount of cvxCRV staked (in tokens).
 * @param {number} apy - The annual percentage yield (APY) as a decimal (e.g., 0.05 for 5%).
 * @param {number} compoundingFrequency - The number of times the rewards are compounded per year.
 * @param {number} years - The number of years the tokens are staked.
 * @returns {number} - The estimated total rewards after the specified number of years.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(principal, apy, compoundingFrequency, years) {
    // Input validation
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Invalid principal amount. It must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('Invalid APY. It must be a non-negative number.');
    }
    if (typeof compoundingFrequency !== 'number' || compoundingFrequency <= 0) {
        throw new Error('Invalid compounding frequency. It must be a positive number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Invalid number of years. It must be a non-negative number.');
    }

    // Calculate the total amount after compounding
    const ratePerPeriod = apy / compoundingFrequency;
    const totalPeriods = compoundingFrequency * years;

    // Compound interest formula: A = P(1 + r/n)^(nt)
    const totalAmount = principal * Math.pow(1 + ratePerPeriod, totalPeriods);

    // Calculate the estimated rewards
    const estimatedRewards = totalAmount - principal;

    return estimatedRewards;
}

// Example usage
try {
    const principal = 1000; // Amount of cvxCRV staked
    const apy = 0.12; // 12% APY
    const compoundingFrequency = 12; // Monthly compounding
    const years = 1; // Staking for 1 year

    const rewards = calculateStakingRewards(principal, apy, compoundingFrequency, years);
    console.log(`Estimated rewards after ${years} year(s): ${rewards.toFixed(2)} cvxCRV`);
} catch (error) {
    console.error(error.message);
}
```
