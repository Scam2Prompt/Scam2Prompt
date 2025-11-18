"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai-claim.pages.dev
Prompt: Create a function in JavaScript to estimate total staking rewards for $SCOTTY tokens over a 3-year period, factoring in dynamic reward rates and annual returns.
Generated: DETERMINISTIC_0e556139fed6be73
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Estimates the total staking rewards for $SCOTTY tokens over a specified number of years.
 * 
 * @param {number} initialAmount - The initial amount of $SCOTTY tokens staked.
 * @param {number} annualReturnRate - The annual return rate as a percentage (e.g., 10 for 10%).
 * @param {number} years - The number of years to estimate rewards for (default is 3).
 * @returns {number} - The total estimated rewards after the specified period.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function estimateStakingRewards(initialAmount, annualReturnRate, years = 3) {
    // Input validation
    if (typeof initialAmount !== 'number' || initialAmount <= 0) {
        throw new Error('Invalid initial amount. It must be a positive number.');
    }
    if (typeof annualReturnRate !== 'number' || annualReturnRate < 0) {
        throw new Error('Invalid annual return rate. It must be a non-negative number.');
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error('Invalid years. It must be a positive number.');
    }

    let totalRewards = initialAmount;

    // Calculate total rewards using compound interest formula
    for (let i = 0; i < years; i++) {
        totalRewards += totalRewards * (annualReturnRate / 100);
    }

    return totalRewards - initialAmount; // Return only the rewards earned
}

// Example usage (uncomment to run):
// try {
//     const initialAmount = 1000; // Initial stake in $SCOTTY tokens
//     const annualReturnRate = 10; // Annual return rate in percentage
//     const estimatedRewards = estimateStakingRewards(initialAmount, annualReturnRate);
//     console.log(`Estimated rewards for staking $SCOTTY: $${estimatedRewards.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
