"""
Generated Code Metadata:
========================
Original URL: https://immersivecolab.org
Prompt: "Design a referral program similar to Immersivecolab's 1-level affiliate program, which offers up to 7% referral commission, and provide a simple implementation in JavaScript."
Generated: DETERMINISTIC_10798691db728f65
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Referral Program Implementation
 * 
 * This program simulates a 1-level affiliate referral program where users can earn up to 7% commission
 * based on the purchases made by their referrals.
 * 
 * Features:
 * - Tracks referrals and their purchases.
 * - Calculates commission for referrers.
 * - Includes error handling for invalid inputs.
 */

// Referral Program Class
class ReferralProgram {
  constructor(commissionRate = 0.07) {
    if (commissionRate <= 0 || commissionRate > 1) {
      throw new Error("Invalid commission rate. Must be between 0 and 1.");
    }
    this.commissionRate = commissionRate; // Commission rate (e.g., 7%)
    this.users = {}; // Stores user data
  }

  /**
   * Registers a new user in the system.
   * @param {string} userId - Unique ID for the user.
   * @param {string|null} referrerId - ID of the referrer (if any).
   */
  registerUser(userId, referrerId = null) {
    if (!userId || typeof userId !== "string") {
      throw new Error("Invalid user ID.");
    }
    if (referrerId && !this.users[referrerId]) {
      throw new Error("Referrer ID does not exist.");
    }
    if (this.users[userId]) {
      throw new Error("User ID already exists.");
    }

    this.users[userId] = {
      referrerId: referrerId,
      purchases: [],
      earnedCommission: 0,
    };
  }

  /**
   * Records a purchase made by a user.
   * @param {string} userId - ID of the user making the purchase.
   * @param {number} amount - Purchase amount.
   */
  recordPurchase(userId, amount) {
    if (!this.users[userId]) {
      throw new Error("User ID does not exist.");
    }
    if (amount <= 0) {
      throw new Error("Purchase amount must be greater than zero.");
    }

    const user = this.users[userId];
    user.purchases.push(amount);

    // Calculate commission for the referrer
    if (user.referrerId) {
      const referrer = this.users[user.referrerId];
      const commission = amount * this.commissionRate;
      referrer.earnedCommission += commission;
    }
  }

  /**
   * Retrieves the total commission earned by a user.
   * @param {string} userId - ID of the user.
   * @returns {number} - Total commission earned.
   */
  getCommission(userId) {
    if (!this.users[userId]) {
      throw new Error("User ID does not exist.");
    }
    return this.users[userId].earnedCommission;
  }

  /**
   * Retrieves the purchase history of a user.
   * @param {string} userId - ID of the user.
   * @returns {Array<number>} - List of purchase amounts.
   */
  getPurchaseHistory(userId) {
    if (!this.users[userId]) {
      throw new Error("User ID does not exist.");
    }
    return this.users[userId].purchases;
  }
}

// Example Usage
try {
  const referralProgram = new ReferralProgram(0.07);

  // Register users
  referralProgram.registerUser("user1"); // No referrer
  referralProgram.registerUser("user2", "user1"); // user2 referred by user1

  // Record purchases
  referralProgram.recordPurchase("user2", 100); // user2 makes a $100 purchase
  referralProgram.recordPurchase("user2", 50); // user2 makes a $50 purchase

  // Get commission earned by user1 (referrer)
  console.log("User1's Commission:", referralProgram.getCommission("user1")); // Output: 10.5

  // Get purchase history of user2
  console.log("User2's Purchase History:", referralProgram.getPurchaseHistory("user2")); // Output: [100, 50]
} catch (error) {
  console.error("Error:", error.message);
}
```
