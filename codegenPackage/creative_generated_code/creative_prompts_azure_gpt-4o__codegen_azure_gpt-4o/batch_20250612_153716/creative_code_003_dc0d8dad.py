"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfty.web.app
Prompt: Create a JavaScript function to calculate rewards in $TNSR tokens based on user activity metrics provided by Tensor's NFT trading platform.
Generated: DETERMINISTIC_dc0d8dadf4be47b3
Batch ID: 20250612_153716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateRewards
 * @description Calculates rewards in $TNSR tokens based on user activity metrics.
 * @param {Object} activityMetrics - An object containing user activity data.
 * @param {number} activityMetrics.volume - The trading volume in USD.
 * @param {number} activityMetrics.trades - Number of trades executed.
 * @param {number} activityMetrics.referrals - Number of referrals made.
 * @returns {number} The calculated rewards in $TNSR tokens.
 * @throws Will throw an error if any input is invalid.
 */
function calculateRewards(activityMetrics) {
  // Input validation
  if (
    typeof activityMetrics !== 'object' ||
    typeof activityMetrics.volume !== 'number' ||
    typeof activityMetrics.trades !== 'number' ||
    typeof activityMetrics.referrals !== 'number'
  ) {
    throw new Error(
      'Invalid input: activityMetrics must be an object with numeric properties volume, trades, and referrals.'
    );
  }

  // Constants for reward calculation
  const VOLUME_FACTOR = 0.01; // 1% of trading volume
  const TRADE_FACTOR = 0.5;  // $TNSR per trade
  const REFERRAL_FACTOR = 20; // $TNSR per referral

  // Calculate rewards
  const volumeRewards = activityMetrics.volume * VOLUME_FACTOR;
  const tradeRewards = activityMetrics.trades * TRADE_FACTOR;
  const referralRewards = activityMetrics.referrals * REFERRAL_FACTOR;

  // Total rewards in $TNSR tokens
  const totalRewards = volumeRewards + tradeRewards + referralRewards;

  // Ensure rewards are not negative
  return Math.max(totalRewards, 0);
}

// Example Usage
try {
  const metrics = {
    volume: 15000, // USD
    trades: 42,    // Number of trades
    referrals: 3   // Number of referrals
  };

  const rewards = calculateRewards(metrics);
  console.log(`Rewards in $TNSR tokens: ${rewards}`);
} catch (error) {
  console.error(`Error calculating rewards: ${error.message}`);
}
```
