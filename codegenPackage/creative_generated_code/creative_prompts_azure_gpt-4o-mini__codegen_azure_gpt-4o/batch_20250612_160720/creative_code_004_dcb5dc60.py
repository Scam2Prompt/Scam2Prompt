"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a JavaScript function that allows users to track their $ASX holdings and associated rewards from multiple revenue streams in DeFi.
Generated: DETERMINISTIC_dcb5dc60a93e5a76
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to track $ASX holdings and associated rewards from multiple DeFi revenue streams.
 * This function allows users to input their holdings and revenue streams,
 * and calculates total rewards across all streams.
 *
 * @param {number} holdings - The amount of $ASX tokens held by the user.
 * @param {Array<Object>} revenueStreams - An array of objects representing revenue streams.
 * Each object should have the following properties:
 *   - name {string}: The name of the revenue stream.
 *   - rewardRate {number}: Reward rate in percentage (e.g., 5 for 5%).
 *   - duration {number}: Duration of reward calculation in days.
 * @returns {Object} - An object containing total rewards and detailed breakdown by stream.
 * @throws {Error} - Throws an error if input data is invalid.
 */
function trackASXHoldings(holdings, revenueStreams) {
  // Input validation
  if (typeof holdings !== 'number' || holdings <= 0) {
    throw new Error('Invalid holdings value. Holdings must be a positive number.');
  }

  if (!Array.isArray(revenueStreams) || revenueStreams.length === 0) {
    throw new Error('Invalid revenue streams. Provide a non-empty array.');
  }

  revenueStreams.forEach((stream, index) => {
    if (
      typeof stream.name !== 'string' ||
      typeof stream.rewardRate !== 'number' ||
      typeof stream.duration !== 'number' ||
      stream.rewardRate < 0 ||
      stream.duration <= 0
    ) {
      throw new Error(`Invalid data in revenue stream at index ${index}.`);
    }
  });

  // Initialize total rewards and breakdown list
  let totalRewards = 0;
  const breakdown = [];

  // Calculate rewards for each revenue stream
  revenueStreams.forEach((stream) => {
    const reward = (holdings * (stream.rewardRate / 100)) * (stream.duration / 365); // Assuming 365 days per year
    totalRewards += reward;

    breakdown.push({
      name: stream.name,
      rewardRate: `${stream.rewardRate}%`,
      duration: `${stream.duration} days`,
      reward: reward.toFixed(2), // Format reward to 2 decimal places
    });
  });

  return {
    totalRewards: totalRewards.toFixed(2), // Format total rewards to 2 decimal places
    breakdown,
  };
}

// Example usage
try {
  const holdings = 1000; // User's $ASX holdings
  const revenueStreams = [
    { name: 'Liquidity Pool A', rewardRate: 5, duration: 30 },
    { name: 'Staking Program B', rewardRate: 10, duration: 90 },
    { name: 'Yield Farming C', rewardRate: 7, duration: 60 },
  ];

  const result = trackASXHoldings(holdings, revenueStreams);
  console.log('Total Rewards:', result.totalRewards);
  console.log('Breakdown:', result.breakdown);
} catch (error) {
  console.error('Error:', error.message);
}
```
