"""
Generated Code Metadata:
========================
Original URL: https://defi-farming.net
Prompt: Create a function in JavaScript to calculate the estimated rewards for a user based on their staked amount and the APY provided by a DeFi farming protocol.
Generated: DETERMINISTIC_ced583458cdf884e
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated rewards for a user based on their staked amount and APY.
 * 
 * @param {number} stakedAmount - The amount of tokens staked by the user.
 * @param {number} apy - The annual percentage yield (APY) provided by the protocol (e.g., 5 for 5%).
 * @param {number} [durationInDays=365] - The duration for which rewards are calculated (default: 365 days).
 * @returns {number} The estimated rewards earned over the specified duration.
 * @throws {Error} If stakedAmount is negative or apy is invalid.
 */
function calculateEstimatedRewards(stakedAmount, apy, durationInDays = 365) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount < 0) {
        throw new Error('Staked amount must be a non-negative number');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number');
    }
    if (typeof durationInDays !== 'number' || durationInDays <= 0) {
        throw new Error('Duration must be a positive number');
    }

    // Calculate rewards
    const apyDecimal = apy / 100; // Convert APY percentage to decimal
    const dailyRate = apyDecimal / 365; // Calculate daily interest rate
    const estimatedRewards = stakedAmount * dailyRate * durationInDays;

    // Return rounded value to avoid floating point precision issues
    return parseFloat(estimatedRewards.toFixed(8));
}

// Example usage:
// try {
//     const rewards = calculateEstimatedRewards(1000, 10, 30);
//     console.log(`Estimated rewards: ${rewards}`);
// } catch (error) {
//     console.error(`Error calculating rewards: ${error.message}`);
// }
```
