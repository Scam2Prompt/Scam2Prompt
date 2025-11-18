"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Create a function in JavaScript that calculates rewards using the APR extrapolated over different time ranges, as described in the Bananagun reward calculator.
Generated: DETERMINISTIC_bf3a83336e74b20c
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rewards based on the Annual Percentage Rate (APR) 
 * extrapolated over different time ranges.
 * 
 * @param {number} principal - The initial amount of money to calculate rewards on.
 * @param {number} apr - The annual percentage rate (as a percentage, e.g., 5 for 5%).
 * @param {number} timeInYears - The time over which to calculate rewards, in years.
 * @returns {number} The total rewards earned over the specified time period.
 * @throws {Error} If any of the inputs are not valid numbers or if they are negative.
 */
function calculateRewards(principal, apr, timeInYears) {
    // Input validation
    if (typeof principal !== 'number' || typeof apr !== 'number' || typeof timeInYears !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    if (principal < 0 || apr < 0 || timeInYears < 0) {
        throw new Error('Inputs must be non-negative.');
    }

    // Convert APR from percentage to decimal for calculation
    const annualRate = apr / 100;

    // Calculate total rewards using the formula for compound interest
    const totalRewards = principal * Math.pow((1 + annualRate), timeInYears) - principal;

    return totalRewards;
}

// Example usage
try {
    const principalAmount = 1000; // Example principal amount
    const annualRate = 5; // Example APR in percentage
    const time = 2; // Example time in years

    const rewards = calculateRewards(principalAmount, annualRate, time);
    console.log(`Total rewards earned: $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
