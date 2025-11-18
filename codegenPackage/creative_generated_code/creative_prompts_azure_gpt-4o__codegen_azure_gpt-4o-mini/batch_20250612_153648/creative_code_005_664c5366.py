"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Create a JavaScript function to calculate and display token rewards for users participating in Manta CeDeFi, based on APR and asset type (e.g., BTC, ETH, USDT, USDC).
Generated: DETERMINISTIC_664c5366427be766
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates token rewards for users participating in Manta CeDeFi.
 * 
 * @param {number} principal - The amount of assets deposited (in the respective asset's unit).
 * @param {number} apr - The Annual Percentage Rate as a decimal (e.g., 0.05 for 5%).
 * @param {number} timeInDays - The time the assets are held in days.
 * @param {string} assetType - The type of asset (e.g., 'BTC', 'ETH', 'USDT', 'USDC').
 * @returns {object} - An object containing the asset type and calculated rewards.
 * @throws {Error} - Throws an error if the input values are not valid.
 */
function calculateTokenRewards(principal, apr, timeInDays, assetType) {
    // Validate inputs
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof apr !== 'number' || apr < 0) {
        throw new Error('Invalid APR. It must be a non-negative number.');
    }
    if (typeof timeInDays !== 'number' || timeInDays <= 0) {
        throw new Error('Invalid time in days. It must be a positive number.');
    }
    if (typeof assetType !== 'string' || assetType.trim() === '') {
        throw new Error('Invalid asset type. It must be a non-empty string.');
    }

    // Calculate the daily interest rate
    const dailyRate = apr / 365;

    // Calculate the total rewards earned over the specified time period
    const rewards = principal * dailyRate * timeInDays;

    // Return the results in a formatted object
    return {
        assetType: assetType.toUpperCase(),
        rewards: parseFloat(rewards.toFixed(6)) // Format rewards to 6 decimal places
    };
}

// Example usage:
try {
    const userPrincipal = 1000; // Amount in USDT
    const userApr = 0.08; // 8% APR
    const userDays = 30; // Time in days
    const userAssetType = 'USDT';

    const rewardResult = calculateTokenRewards(userPrincipal, userApr, userDays, userAssetType);
    console.log(`Rewards for ${rewardResult.assetType}: ${rewardResult.rewards}`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
