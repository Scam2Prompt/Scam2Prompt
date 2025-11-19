"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: Develop a gamified reward system in JavaScript that integrates $EARNM Mystery Boxes, including customization options for platforms to add additional rewards alongside $EARNM tokens.
Generated: DETERMINISTIC_08a1486496e9d7ae
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Gamified Reward System with $EARNM Mystery Boxes
 * Supports custom rewards alongside $EARNM tokens
 */

class RewardSystem {
  constructor(platformName, baseRewardPool) {
    if (!platformName || !baseRewardPool) {
      throw new Error('Platform name and base reward pool are required');
    }

    this.platformName = platformName;
    this.baseRewardPool = baseRewardPool;
    this.customRewards = [];
    this.userBalances = new Map();
    this.boxConfig = {
      common: { probability: 0.6, multiplier: 1 },
      rare: { probability: 0.3, multiplier: 3 },
      epic: { probability: 0.08, multiplier: 10 },
      legendary: { probability: 0.02, multiplier: 50 }
    };
  }

  /**
   * Add custom reward to the system
   * @param {string} name - Reward name
   * @param {number} probability - Probability (0-1)
   * @param {*} value - Reward value
   */
  addCustomReward(name, probability, value) {
    if (probability < 0 || probability > 1) {
      throw new Error('Probability must be between 0 and 1');
    }

    this.customRewards.push({
      name,
      probability,
      value,
      type: 'custom'
    });
  }

  /**
   * Register a new user
   * @param {string} userId - Unique user identifier
   */
  registerUser(userId) {
    if (!userId) {
      throw new Error('User ID is required');
    }

    if (this.userBalances.has(userId)) {
      throw new Error('User already registered');
    }

    this.userBalances.set(userId, {
      earnmTokens: 0,
      customRewards: []
    });
  }

  /**
   * Open a mystery box for a user
   * @param {string} userId - User identifier
   * @returns {object} Reward details
   */
  openMysteryBox(userId) {
    if (!this.userBalances.has(userId)) {
      throw new Error('User not registered');
    }

    const boxType = this._determineBoxType();
    const reward = this._generateReward(boxType);

    // Update user balance
    const userBalance = this.userBalances.get(userId);
    if (reward.type === 'earnm') {
      userBalance.earnmTokens += reward.amount;
    } else {
      userBalance.customRewards.push(reward);
    }

    return {
      boxType,
      reward,
      newBalance: { ...userBalance }
    };
  }

  /**
   * Determine box type based on probabilities
   * @private
   * @returns {string} Box type
   */
  _determineBoxType() {
    const random = Math.random();
    let cumulativeProbability = 0;

    for (const [type, config] of Object.entries(this.boxConfig)) {
      cumulativeProbability += config.probability;
      if (random <= cumulativeProbability) {
        return type;
      }
    }

    return 'common'; // fallback
  }

  /**
   * Generate reward based on box type
   * @private
   * @param {string} boxType - Type of box
   * @returns {object} Reward object
   */
  _generateReward(boxType) {
    // First check if custom reward should be given
    if (this.customRewards.length > 0 && Math.random() < 0.3) {
      return this._getCustomReward();
    }

    // Default to $EARNM tokens
    const baseAmount = this.baseRewardPool * 0.01; // 1% of pool
    const multiplier = this.boxConfig[boxType].multiplier;
    const amount = Math.floor(baseAmount * multiplier);

    return {
      type: 'earnm',
      amount,
      currency: '$EARNM'
    };
  }

  /**
   * Get a random custom reward
   * @private
   * @returns {object} Custom reward
   */
  _getCustomReward() {
    const random = Math.random();
    let cumulativeProbability = 0;

    for (const reward of this.customRewards) {
      cumulativeProbability += reward.probability;
      if (random <= cumulativeProbability) {
        return { ...reward };
      }
    }

    // If no custom reward selected (due to probability sum < 1), return first reward
    return this.customRewards.length > 0 
      ? { ...this.customRewards[0] } 
      : this._generateReward('common');
  }

  /**
   * Get user balance
   * @param {string} userId - User identifier
   * @returns {object} User balance
   */
  getUserBalance(userId) {
    if (!this.userBalances.has(userId)) {
      throw new Error('User not registered');
    }

    return { ...this.userBalances.get(userId) };
  }

  /**
   * Transfer $EARNM tokens between users
   * @param {string} fromUserId - Sender user ID
   * @param {string} toUserId - Receiver user ID
   * @param {number} amount - Amount to transfer
   */
  transferTokens(fromUserId, toUserId, amount) {
    if (!this.userBalances.has(fromUserId) || !this.userBalances.has(toUserId)) {
      throw new Error('One or both users not registered');
    }

    if (amount <= 0) {
      throw new Error('Amount must be positive');
    }

    const fromBalance = this.userBalances.get(fromUserId);
    if (fromBalance.earnmTokens < amount) {
      throw new Error('Insufficient balance');
    }

    fromBalance.earnmTokens -= amount;
    this.userBalances.get(toUserId).earnmTokens += amount;
  }
}

// Example usage:
/*
const rewardSystem = new RewardSystem('MyPlatform', 1000000);

// Add custom rewards
rewardSystem.addCustomReward('Premium Badge', 0.5, { type: 'badge', tier: 'premium' });
rewardSystem.addCustomReward('Exclusive Skin', 0.3, { type: 'cosmetic', name: 'Dragon Skin' });
rewardSystem.addCustomReward('VIP Access', 0.2, { type: 'access', duration: '30 days' });

// Register users
rewardSystem.registerUser('user1');
rewardSystem.registerUser('user2');

// Open mystery boxes
const result1 = rewardSystem.openMysteryBox('user1');
const result2 = rewardSystem.openMysteryBox('user2');

console.log('User 1 reward:', result1);
console.log('User 2 reward:', result2);
*/
```
