"""
Generated Code Metadata:
========================
Original URL: https://cashb90.org
Prompt: Generate a JavaScript code snippet for a loyalty program rewards system, similar to BaxBet's, that offers cashback on losses and bonuses for active players.
Generated: DETERMINISTIC_d5034d0c5961c9e8
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Loyalty Program Rewards System
 * This system calculates cashback on losses and bonuses for active players.
 * It is designed to be clean, efficient, and production-ready.
 */

// Constants for the loyalty program
const LOYALTY_TIERS = [
  { tier: "Bronze", cashbackRate: 0.05, bonusThreshold: 500 },
  { tier: "Silver", cashbackRate: 0.07, bonusThreshold: 1000 },
  { tier: "Gold", cashbackRate: 0.10, bonusThreshold: 2000 },
  { tier: "Platinum", cashbackRate: 0.15, bonusThreshold: 5000 },
];

// Error class for handling invalid inputs
class LoyaltyProgramError extends Error {
  constructor(message) {
    super(message);
    this.name = "LoyaltyProgramError";
  }
}

/**
 * Calculate cashback based on losses and loyalty tier.
 * @param {number} losses - Total losses of the player.
 * @param {string} tier - Loyalty tier of the player.
 * @returns {number} - Cashback amount.
 */
function calculateCashback(losses, tier) {
  if (losses < 0) {
    throw new LoyaltyProgramError("Losses cannot be negative.");
  }

  const tierInfo = LOYALTY_TIERS.find((t) => t.tier === tier);
  if (!tierInfo) {
    throw new LoyaltyProgramError("Invalid loyalty tier.");
  }

  return losses * tierInfo.cashbackRate;
}

/**
 * Calculate bonus for active players based on their activity.
 * @param {number} activityPoints - Activity points accumulated by the player.
 * @param {string} tier - Loyalty tier of the player.
 * @returns {number} - Bonus amount.
 */
function calculateBonus(activityPoints, tier) {
  if (activityPoints < 0) {
    throw new LoyaltyProgramError("Activity points cannot be negative.");
  }

  const tierInfo = LOYALTY_TIERS.find((t) => t.tier === tier);
  if (!tierInfo) {
    throw new LoyaltyProgramError("Invalid loyalty tier.");
  }

  return activityPoints >= tierInfo.bonusThreshold ? activityPoints * 0.02 : 0;
}

/**
 * Main function to calculate rewards for a player.
 * @param {object} player - Player object containing losses, activityPoints, and tier.
 * @returns {object} - Rewards object containing cashback and bonus.
 */
function calculateRewards(player) {
  if (!player || typeof player !== "object") {
    throw new LoyaltyProgramError("Invalid player data.");
  }

  const { losses, activityPoints, tier } = player;

  return {
    cashback: calculateCashback(losses, tier),
    bonus: calculateBonus(activityPoints, tier),
  };
}

// Example usage
try {
  const player = {
    losses: 1200,
    activityPoints: 1500,
    tier: "Silver",
  };

  const rewards = calculateRewards(player);
  console.log("Rewards:", rewards);
} catch (error) {
  if (error instanceof LoyaltyProgramError) {
    console.error("Error:", error.message);
  } else {
    console.error("Unexpected error:", error);
  }
}
```
