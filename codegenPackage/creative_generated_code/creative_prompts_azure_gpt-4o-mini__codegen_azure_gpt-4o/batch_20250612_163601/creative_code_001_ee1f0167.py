"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefi-ai.pages.dev
Prompt: Write a JavaScript function to calculate the rewards distribution for QuDefi token holders based on their token balance and the monthly revenue generated from trading software licensing fees.
Generated: DETERMINISTIC_ee1f0167f4373b08
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate rewards distribution for QuDefi token holders
 * based on their token balance and the monthly revenue generated.
 *
 * @param {Object[]} holders - Array of token holder objects with `address` and `balance`.
 * @param {number} monthlyRevenue - Total monthly revenue generated (in dollars).
 * @param {number} rewardPercentage - Percentage of monthly revenue allocated for rewards (e.g., 10 for 10%).
 * @returns {Object[]} - Array of rewards distribution objects with `address` and `reward`.
 */
function calculateRewards(holders, monthlyRevenue, rewardPercentage) {
  // Input validation
  if (!Array.isArray(holders) || holders.length === 0) {
    throw new Error("Invalid holders array. Must be a non-empty array.");
  }
  if (typeof monthlyRevenue !== "number" || monthlyRevenue < 0) {
    throw new Error("Invalid monthly revenue. Must be a non-negative number.");
  }
  if (typeof rewardPercentage !== "number" || rewardPercentage <= 0 || rewardPercentage > 100) {
    throw new Error("Invalid reward percentage. Must be a number between 0 and 100.");
  }

  // Calculate total balance of all holders
  const totalBalance = holders.reduce((sum, holder) => {
    if (typeof holder.balance !== "number" || holder.balance < 0) {
      throw new Error(`Invalid balance for holder ${holder.address}. Must be a non-negative number.`);
    }
    return sum + holder.balance;
  }, 0);

  if (totalBalance === 0) {
    throw new Error("Total balance of all holders is zero. Cannot distribute rewards.");
  }

  // Calculate total rewards pool
  const rewardsPool = (monthlyRevenue * rewardPercentage) / 100;

  // Calculate individual rewards
  const rewardsDistribution = holders.map((holder) => {
    const reward = (holder.balance / totalBalance) * rewardsPool;
    return {
      address: holder.address,
      reward: parseFloat(reward.toFixed(2)) // Round reward to two decimal places
    };
  });

  return rewardsDistribution;
}

// Example usage
try {
  const tokenHolders = [
    { address: "0x123", balance: 500 },
    { address: "0x456", balance: 1500 },
    { address: "0x789", balance: 1000 }
  ];
  const monthlyRevenue = 100000; // $100,000
  const rewardPercentage = 10; // 10% of revenue goes to rewards

  const rewards = calculateRewards(tokenHolders, monthlyRevenue, rewardPercentage);
  console.log("Rewards Distribution:", rewards);
} catch (error) {
  console.error("Error calculating rewards:", error.message);
}
```
