"""
Generated Code Metadata:
========================
Original URL: https://moonbagg.com
Prompt: "Generate a referral code system using JavaScript, where users earn $MBAG tokens for referring friends who make purchases of $25 or more, with rewards structured according to a leaderboard ranking."
Generated: DETERMINISTIC_19535678a57a55b5
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// referralSystem.js

/**
 * Referral System Class
 */
class ReferralSystem {
  /**
   * Constructor
   * @param {Object} config - Configuration object
   * @param {number} config.referralReward - Reward for successful referral
   * @param {number} config.minPurchase - Minimum purchase required for referral
   */
  constructor(config) {
    this.config = config;
    this.users = {}; // Store user data
    this.leaderboard = {}; // Store leaderboard data
    this.referralCodes = {}; // Store referral codes
  }

  /**
   * Generate a unique referral code
   * @returns {string} Referral code
   */
  generateReferralCode() {
    const code = Math.random().toString(36).substr(2, 10);
    if (this.referralCodes[code]) {
      return this.generateReferralCode(); // Recursively generate new code if duplicate
    }
    return code;
  }

  /**
   * Create a new user
   * @param {string} id - User ID
   * @param {string} [referralCode] - Referral code used
   */
  createUser(id, referralCode) {
    if (this.users[id]) {
      throw new Error(`User ${id} already exists`);
    }
    const newUser = {
      id,
      balance: 0,
      referrals: 0,
      referralCode: referralCode || this.generateReferralCode(),
    };
    this.users[id] = newUser;
    this.referralCodes[newUser.referralCode] = id;
  }

  /**
   * Process a purchase
   * @param {string} userId - User ID
   * @param {number} amount - Purchase amount
   * @param {string} [referralCode] - Referral code used
   */
  processPurchase(userId, amount, referralCode) {
    if (!this.users[userId]) {
      throw new Error(`User ${userId} does not exist`);
    }
    if (amount < this.config.minPurchase) {
      throw new Error(`Purchase amount must be $${this.config.minPurchase} or more`);
    }
    if (referralCode && this.referralCodes[referralCode]) {
      const referrerId = this.referralCodes[referralCode];
      this.users[referrerId].balance += this.config.referralReward;
      this.users[referrerId].referrals++;
      this.updateLeaderboard(referrerId);
    }
    // Update user balance (assuming $MBAG tokens are earned)
    this.users[userId].balance += amount;
  }

  /**
   * Update leaderboard
   * @param {string} userId - User ID
   */
  updateLeaderboard(userId) {
    const user = this.users[userId];
    if (!this.leaderboard[userId]) {
      this.leaderboard[userId] = {
        referrals: user.referrals,
        balance: user.balance,
      };
    } else {
      this.leaderboard[userId].referrals = user.referrals;
      this.leaderboard[userId].balance = user.balance;
    }
    // Sort leaderboard by referrals and then balance
    const sortedLeaderboard = Object.keys(this.leaderboard).sort((a, b) => {
      if (this.leaderboard[a].referrals === this.leaderboard[b].referrals) {
        return this.leaderboard[b].balance - this.leaderboard[a].balance;
      }
      return this.leaderboard[b].referrals - this.leaderboard[a].referrals;
    });
    this.leaderboard = sortedLeaderboard.reduce((acc, key) => {
      acc[key] = this.leaderboard[key];
      return acc;
    }, {});
  }

  /**
   * Get leaderboard
   * @returns {Object} Leaderboard data
   */
  getLeaderboard() {
    return this.leaderboard;
  }

  /**
   * Get user data
   * @param {string} userId - User ID
   * @returns {Object} User data
   */
  getUser(userId) {
    return this.users[userId];
  }
}

// Example usage
const config = {
  referralReward: 10, // $MBAG tokens
  minPurchase: 25,
};

const referralSystem = new ReferralSystem(config);

try {
  referralSystem.createUser('user1');
  referralSystem.createUser('user2', referralSystem.getUser('user1').referralCode);

  referralSystem.processPurchase('user2', 30);

  console.log(referralSystem.getLeaderboard());
  console.log(referralSystem.getUser('user1'));
  console.log(referralSystem.getUser('user2'));
} catch (error) {
  console.error(error.message);
}
```
