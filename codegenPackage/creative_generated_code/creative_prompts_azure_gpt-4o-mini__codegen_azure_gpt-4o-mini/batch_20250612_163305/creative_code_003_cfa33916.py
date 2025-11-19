"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Create a JavaScript function that calculates the potential passive income from staking BTCBSC based on the current staking pool size.
Generated: DETERMINISTIC_cfa3391688aac26c
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential passive income from staking BTCBSC.
 *
 * @param {number} userStakedAmount - The amount of BTCBSC the user has staked.
 * @param {number} totalPoolSize - The total size of the staking pool.
 * @param {number} annualYieldRate - The annual yield rate as a decimal (e.g., 0.05 for 5%).
 * @param {number} durationInDays - The duration for which the user plans to stake, in days.
 * @returns {number} - The potential passive income from staking.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculatePassiveIncome(userStakedAmount, totalPoolSize, annualYieldRate, durationInDays) {
    // Input validation
    if (typeof userStakedAmount !== 'number' || userStakedAmount <= 0) {
        throw new Error('Invalid user staked amount. Must be a positive number.');
    }
    if (typeof totalPoolSize !== 'number' || totalPoolSize <= 0) {
        throw new Error('Invalid total pool size. Must be a positive number.');
    }
    if (typeof annualYieldRate !== 'number' || annualYieldRate < 0) {
        throw new Error('Invalid annual yield rate. Must be a non-negative number.');
    }
    if (typeof durationInDays !== 'number' || durationInDays <= 0) {
        throw new Error('Invalid duration in days. Must be a positive number.');
    }

    // Calculate daily yield rate
    const dailyYieldRate = annualYieldRate / 365;

    // Calculate the user's percentage of the total pool
    const userPercentage = userStakedAmount / totalPoolSize;

    // Calculate potential income over the specified duration
    const potentialIncome = userPercentage * dailyYieldRate * durationInDays * totalPoolSize;

    return potentialIncome;
}

// Example usage:
try {
    const userIncome = calculatePassiveIncome(1000, 50000, 0.05, 30);
    console.log(`Potential passive income from staking: $${userIncome.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating passive income:', error.message);
}
```
