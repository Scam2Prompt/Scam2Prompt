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
 * Calculates and displays token rewards for users participating in Manta CeDeFi.
 * 
 * @param {number} principal - The amount of asset deposited by the user.
 * @param {number} apr - Annual Percentage Rate (APR) provided for the asset.
 * @param {string} assetType - The type of asset (e.g., BTC, ETH, USDT, USDC).
 * @param {number} durationInDays - Duration of participation in days.
 * 
 * @throws {Error} If input parameters are invalid.
 * 
 * @returns {string} A message with the calculated reward and asset type.
 */
function calculateTokenRewards(principal, apr, assetType, durationInDays) {
  // Validate input parameters
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error("Invalid principal amount. Must be a positive number.");
  }
  if (typeof apr !== 'number' || apr <= 0) {
    throw new Error("Invalid APR. Must be a positive number.");
  }
  if (typeof assetType !== 'string' || !['BTC', 'ETH', 'USDT', 'USDC'].includes(assetType)) {
    throw new Error("Invalid asset type. Must be one of BTC, ETH, USDT, USDC.");
  }
  if (typeof durationInDays !== 'number' || durationInDays <= 0) {
    throw new Error("Invalid duration. Must be a positive number.");
  }

  // Calculate reward
  const annualReward = (principal * apr) / 100; // Reward for a full year
  const dailyReward = annualReward / 365;      // Reward per day
  const totalReward = dailyReward * durationInDays; // Reward for the given duration

  // Format the result
  const rewardMessage = `For your deposit of ${principal} ${assetType}, 
                         at an APR of ${apr}% over ${durationInDays} days, 
                         your total reward is ${totalReward.toFixed(2)} ${assetType}.`;

  return rewardMessage;
}

// Example usage:
try {
  const principal = 1000; // Example principal amount
  const apr = 5;          // Example APR
  const assetType = 'BTC';// Example asset type
  const durationInDays = 30; // Example duration in days

  const rewardMessage = calculateTokenRewards(principal, apr, assetType, durationInDays);
  console.log(rewardMessage);
} catch (error) {
  console.error(error.message);
}
```
