"""
Generated Code Metadata:
========================
Original URL: https://claim-dogecoin20.web.app
Prompt: How can I implement a rewards calculator for DOGE20 token purchases based on different price scenarios using JavaScript?
Generated: DETERMINISTIC_9c0c4a59da9d46d7
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Rewards Calculator for DOGE20 Token Purchases
 * 
 * This script calculates rewards based on different price scenarios for DOGE20 token purchases.
 * 
 * Assumptions:
 * - Rewards are calculated based on the number of tokens purchased and the price per token.
 * - Different price ranges yield different reward percentages.
 * - Rewards are returned as an object containing the total reward and details.
 * 
 * Usage:
 * Call `calculateRewards(purchaseAmount, pricePerToken)` with the purchase amount and price per token.
 */

// Constants for reward tiers
const REWARD_TIERS = [
  { minPrice: 0, maxPrice: 0.1, rewardPercentage: 5 },  // 5% reward for price <= 0.1
  { minPrice: 0.1, maxPrice: 0.5, rewardPercentage: 3 }, // 3% reward for price > 0.1 and <= 0.5
  { minPrice: 0.5, maxPrice: 1, rewardPercentage: 2 },   // 2% reward for price > 0.5 and <= 1
  { minPrice: 1, maxPrice: Infinity, rewardPercentage: 1 } // 1% reward for price > 1
];

/**
 * Calculate rewards based on purchase amount and price per token.
 * 
 * @param {number} purchaseAmount - The number of DOGE20 tokens purchased.
 * @param {number} pricePerToken - The price per DOGE20 token.
 * @returns {object} - An object containing the total reward and details.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateRewards(purchaseAmount, pricePerToken) {
  // Input validation
  if (typeof purchaseAmount !== 'number' || purchaseAmount <= 0) {
    throw new Error('Invalid purchase amount. Must be a positive number.');
  }
  if (typeof pricePerToken !== 'number' || pricePerToken <= 0) {
    throw new Error('Invalid price per token. Must be a positive number.');
  }

  // Determine the applicable reward tier
  const applicableTier = REWARD_TIERS.find(
    tier => pricePerToken > tier.minPrice && pricePerToken <= tier.maxPrice
  );

  if (!applicableTier) {
    throw new Error('No applicable reward tier found for the given price.');
  }

  // Calculate reward
  const rewardPercentage = applicableTier.rewardPercentage;
  const totalReward = (purchaseAmount * pricePerToken * rewardPercentage) / 100;

  // Return reward details
  return {
    purchaseAmount,
    pricePerToken,
    rewardPercentage,
    totalReward
  };
}

// Example usage
try {
  const purchaseAmount = 1000; // Number of tokens purchased
  const pricePerToken = 0.3;  // Price per token
  const rewards = calculateRewards(purchaseAmount, pricePerToken);
  console.log('Reward Details:', rewards);
} catch (error) {
  console.error('Error calculating rewards:', error.message);
}
```
