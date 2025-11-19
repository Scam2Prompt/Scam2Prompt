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
 * Immersivecolab-style Referral Program Implementation
 * Features:
 * - 1-level affiliate program
 * - Up to 7% referral commission
 * - Track referrals and calculate commissions
 */

class ReferralProgram {
  /**
   * Initialize the referral program with configuration
   * @param {Object} config - Program configuration
   * @param {number} config.baseCommission - Base commission percentage (0-100)
   * @param {number} config.maxCommission - Maximum commission percentage (0-100)
   */
  constructor(config = {}) {
    this.config = {
      baseCommission: config.baseCommission || 5, // Default 5%
      maxCommission: config.maxCommission || 7,  // Default 7%
    };
    this.referrals = new Map(); // Stores referrer -> [referees]
    this.commissions = new Map(); // Stores referrer -> total commissions
  }

  /**
   * Add a new referral relationship
   * @param {string} referrerId - ID of the referring user
   * @param {string} refereeId - ID of the new user being referred
   * @throws {Error} If referral relationship already exists
   */
  addReferral(referrerId, refereeId) {
    if (this.referrals.has(refereeId)) {
      throw new Error('User has already been referred');
    }

    if (!this.referrals.has(referrerId)) {
      this.referrals.set(referrerId, []);
      this.commissions.set(referrerId, 0);
    }

    this.referrals.get(referrerId).push(refereeId);
    this.referrals.set(refereeId, []); // Mark as referred (empty array means no referrals from them)
  }

  /**
   * Calculate commission for a purchase
   * @param {string} userId - ID of the purchasing user
   * @param {number} amount - Purchase amount
   * @returns {number} Commission amount
   */
  calculateCommission(userId, amount) {
    if (!this.referrals.has(userId) || this.referrals.get(userId).length === 0) {
      return 0; // No referrals from this user
    }

    const commissionRate = Math.min(
      this.config.baseCommission + Math.log10(this.referrals.get(userId).length + 1),
      this.config.maxCommission
    );

    return (amount * commissionRate) / 100;
  }

  /**
   * Record a purchase and distribute commission
   * @param {string} userId - ID of the purchasing user
   * @param {number} amount - Purchase amount
   * @returns {number} Total commission awarded
   */
  recordPurchase(userId, amount) {
    if (!this.referrals.has(userId)) {
      return 0; // User wasn't referred by anyone
    }

    // Find who referred this user
    let referrer = null;
    for (const [key, value] of this.referrals.entries()) {
      if (value.includes(userId)) {
        referrer = key;
        break;
      }
    }

    if (!referrer) {
      return 0; // No referrer found
    }

    const commission = this.calculateCommission(referrer, amount);
    this.commissions.set(referrer, (this.commissions.get(referrer) || 0) + commission);
    return commission;
  }

  /**
   * Get total commissions earned by a user
   * @param {string} userId - ID of the referring user
   * @returns {number} Total commissions earned
   */
  getTotalCommissions(userId) {
    return this.commissions.get(userId) || 0;
  }

  /**
   * Get all referrals made by a user
   * @param {string} userId - ID of the referring user
   * @returns {string[]} Array of referred user IDs
   */
  getReferrals(userId) {
    return this.referrals.get(userId) || [];
  }
}

// Example usage:
/*
const program = new ReferralProgram({ baseCommission: 5, maxCommission: 7 });

// User A refers User B
program.addReferral('userA', 'userB');

// User B makes a $100 purchase
const commission = program.recordPurchase('userB', 100);
console.log(`Commission earned: $${commission}`);

// Check User A's total commissions
console.log(`User A total commissions: $${program.getTotalCommissions('userA')}`);
*/
```
