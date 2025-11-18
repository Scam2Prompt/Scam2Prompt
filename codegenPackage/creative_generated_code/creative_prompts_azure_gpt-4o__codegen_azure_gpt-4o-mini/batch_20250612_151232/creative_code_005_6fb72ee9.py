"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingoclaims.pages.dev
Prompt: Write a function in JavaScript to calculate exponential growth in rewards based on increasing contributions to the RWA pool and community engagement, as outlined in the Lingo ecosystem.
Generated: DETERMINISTIC_6fb72ee9a54c7b32
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the exponential growth in rewards based on contributions to the RWA pool
 * and community engagement in the Lingo ecosystem.
 *
 * @param {number} initialReward - The initial amount of rewards.
 * @param {number} contributionFactor - A factor that represents the increase in contributions.
 * @param {number} engagementFactor - A factor that represents community engagement.
 * @param {number} time - The time period over which the rewards are calculated (in years).
 * @returns {number} - The calculated rewards after the specified time period.
 * @throws {Error} - Throws an error if any input is invalid (non-positive numbers).
 */
function calculateExponentialGrowth(initialReward, contributionFactor, engagementFactor, time) {
    // Validate inputs
    if (initialReward <= 0 || contributionFactor <= 0 || engagementFactor <= 0 || time <= 0) {
        throw new Error('All input values must be positive numbers.');
    }

    // Calculate the growth using the formula: 
    // rewards = initialReward * (contributionFactor ^ time) * (engagementFactor ^ time)
    const rewards = initialReward * Math.pow(contributionFactor, time) * Math.pow(engagementFactor, time);

    return rewards;
}

// Example usage:
try {
    const initialReward = 100; // Initial reward amount
    const contributionFactor = 1.05; // 5% increase in contributions per year
    const engagementFactor = 1.03; // 3% increase in engagement per year
    const time = 5; // 5 years

    const totalRewards = calculateExponentialGrowth(initialReward, contributionFactor, engagementFactor, time);
    console.log(`Total rewards after ${time} years: $${totalRewards.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating rewards:', error.message);
}
```
