"""
Generated Code Metadata:
========================
Original URL: https://pacmoon-v3.pages.dev
Prompt: "Create a basic example of how to implement a referral or invite system in JavaScript that offers a 10% bonus on points earned, similar to Pacmoon's invite feature."
Generated: DETERMINISTIC_0a0185b5c254ac29
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Referral System Implementation
 * 
 * This module implements a basic referral/invite system where:
 * - Users can generate a unique referral code
 * - New users can sign up using a referral code
 * - Both referrer and referee get bonus points (10% of earned points)
 */

class ReferralSystem {
  constructor() {
    this.users = new Map(); // Stores user data by user ID
    this.referralCodes = new Map(); // Maps referral codes to user IDs
  }

  /**
   * Generates a random referral code
   * @returns {string} Random 8-character alphanumeric code
   */
  _generateReferralCode() {
    return Math.random().toString(36).substring(2, 10).toUpperCase();
  }

  /**
   * Creates a new user with optional referral code
   * @param {string} userId - Unique identifier for the user
   * @param {string} [referralCode] - Optional referral code from another user
   * @returns {Object} User object with referral info
   * @throws {Error} If user already exists or referral code is invalid
   */
  createUser(userId, referralCode = null) {
    if (this.users.has(userId)) {
      throw new Error('User already exists');
    }

    const user = {
      id: userId,
      points: 0,
      referralCode: this._generateReferralCode(),
      referredBy: null,
      referredUsers: []
    };

    if (referralCode) {
      if (!this.referralCodes.has(referralCode)) {
        throw new Error('Invalid referral code');
      }
      const referrerId = this.referralCodes.get(referralCode);
      user.referredBy = referrerId;
      this.users.get(referrerId).referredUsers.push(userId);
    }

    this.users.set(userId, user);
    this.referralCodes.set(user.referralCode, userId);
    return user;
  }

  /**
   * Adds points to a user's account and applies referral bonuses
   * @param {string} userId - User ID to add points to
   * @param {number} points - Points to add (must be positive)
   * @returns {Object} Result with updated points and any bonuses applied
   * @throws {Error} If user doesn't exist or points are invalid
   */
  addPoints(userId, points) {
    if (!this.users.has(userId)) {
      throw new Error('User not found');
    }
    if (typeof points !== 'number' || points <= 0) {
      throw new Error('Points must be a positive number');
    }

    const user = this.users.get(userId);
    user.points += points;

    let bonusInfo = {};
    const bonusPoints = points * 0.1; // 10% bonus

    // Apply bonus to referrer if exists
    if (user.referredBy) {
      const referrer = this.users.get(user.referredBy);
      referrer.points += bonusPoints;
      bonusInfo.referrerBonus = {
        userId: referrer.id,
        pointsAdded: bonusPoints,
        newTotal: referrer.points
      };
    }

    // Apply bonus to all referred users
    user.referredUsers.forEach(refUserId => {
      const referredUser = this.users.get(refUserId);
      referredUser.points += bonusPoints;
      if (!bonusInfo.refereeBonuses) {
        bonusInfo.refereeBonuses = [];
      }
      bonusInfo.refereeBonuses.push({
        userId: referredUser.id,
        pointsAdded: bonusPoints,
        newTotal: referredUser.points
      });
    });

    return {
      userId,
      pointsAdded: points,
      newTotal: user.points,
      bonuses: Object.keys(bonusInfo).length > 0 ? bonusInfo : null
    };
  }

  /**
   * Gets user information by ID
   * @param {string} userId - User ID to retrieve
   * @returns {Object} User object
   * @throws {Error} If user doesn't exist
   */
  getUser(userId) {
    if (!this.users.has(userId)) {
      throw new Error('User not found');
    }
    return this.users.get(userId);
  }

  /**
   * Gets user information by referral code
   * @param {string} referralCode - Referral code to look up
   * @returns {Object} User object
   * @throws {Error} If referral code is invalid
   */
  getUserByReferralCode(referralCode) {
    if (!this.referralCodes.has(referralCode)) {
      throw new Error('Invalid referral code');
    }
    return this.users.get(this.referralCodes.get(referralCode));
  }
}

// Example usage:
/*
const referralSystem = new ReferralSystem();

// Create initial user
const user1 = referralSystem.createUser('user1');
console.log('User1 created:', user1);

// Create second user with referral from user1
const user2 = referralSystem.createUser('user2', user1.referralCode);
console.log('User2 created with referral:', user2);

// Add points to user2 (both get bonuses)
const result = referralSystem.addPoints('user2', 100);
console.log('Points added with bonuses:', result);

// Check updated user data
console.log('Updated user1:', referralSystem.getUser('user1'));
console.log('Updated user2:', referralSystem.getUser('user2'));
*/
```
