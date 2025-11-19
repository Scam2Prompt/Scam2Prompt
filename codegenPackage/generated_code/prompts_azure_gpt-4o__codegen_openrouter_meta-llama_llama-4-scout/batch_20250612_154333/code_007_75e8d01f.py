"""
Generated Code Metadata:
========================
Original URL: https://flockerz-staking.pages.dev
Prompt: Write a script in JavaScript to calculate the annual percentage yield (APY) for $FLOCK staking, given the dynamic rewards rate of 1017% p/a, and display the monthly and daily breakdown.
Generated: DETERMINISTIC_75e8d01fbdfa21fe
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the annual percentage yield (APY) for $FLOCK staking.
 * 
 * @param {number} principal - The initial amount of $FLOCK staked.
 * @param {number} annualRewardsRate - The dynamic rewards rate in percentage per annum.
 * @returns {object} An object containing the monthly and daily APY breakdown.
 */
function calculateAPY(principal, annualRewardsRate) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof annualRewardsRate !== 'number' || annualRewardsRate <= 0) {
        throw new Error('Annual rewards rate must be a positive number.');
    }

    // Convert annual rewards rate from percentage to a decimal
    const annualRewardsRateDecimal = annualRewardsRate / 100;

    // Calculate the total amount after 1 year
    const totalAmountAfter1Year = principal * (1 + annualRewardsRateDecimal);

    // Calculate the annual APY
    const annualAPY = (totalAmountAfter1Year / principal - 1) * 100;

    // Calculate the monthly APY
    const monthlyAPY = Math.pow(1 + annualRewardsRateDecimal, 1/12) - 1;

    // Calculate the daily APY (assuming 365 days per year)
    const dailyAPY = Math.pow(1 + annualRewardsRateDecimal, 1/365) - 1;

    // Return the APY breakdown
    return {
        annualAPY: annualAPY.toFixed(2),
        monthlyAPY: (monthlyAPY * 100).toFixed(2),
        dailyAPY: (dailyAPY * 100).toFixed(2),
    };
}

// Example usage:
const principal = 1000; // Initial amount of $FLOCK staked
const annualRewardsRate = 1017; // Dynamic rewards rate of 1017% p/a

try {
    const apyBreakdown = calculateAPY(principal, annualRewardsRate);
    console.log(`APY Breakdown:`);
    console.log(`Annual APY: ${apyBreakdown.annualAPY}%`);
    console.log(`Monthly APY: ${apyBreakdown.monthlyAPY}%`);
    console.log(`Daily APY: ${apyBreakdown.dailyAPY}%`);
} catch (error) {
    console.error(error.message);
}
```
