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
 * This program implements a 1-level affiliate program similar to Immersivecolab's,
 * offering up to 7% referral commission.
 */

// ReferralProgram class
class ReferralProgram {
  /**
   * Constructor
   * 
   * @param {number} maxCommission - Maximum commission percentage
   */
  constructor(maxCommission = 7) {
    this.maxCommission = maxCommission;
    this.referrals = {};
  }

  /**
   * Add a new referral
   * 
   * @param {string} referrer - Referrer's ID
   * @param {string} referral - Referral's ID
   * @param {number} purchaseAmount - Purchase amount
   */
  addReferral(referrer, referral, purchaseAmount) {
    if (!this.referrals[referrer]) {
      this.referrals[referrer] = [];
    }
    this.referrals[referrer].push({ referral, purchaseAmount });
  }

  /**
   * Calculate commission for a referrer
   * 
   * @param {string} referrer - Referrer's ID
   * @returns {number} Total commission earned
   */
  calculateCommission(referrer) {
    if (!this.referrals[referrer]) {
      return 0;
    }

    let totalCommission = 0;
    this.referrals[referrer].forEach((referral) => {
      const commission = referral.purchaseAmount * (this.maxCommission / 100);
      totalCommission += commission;
    });
    return totalCommission;
  }

  /**
   * Get referral history for a referrer
   * 
   * @param {string} referrer - Referrer's ID
   * @returns {object[]} Referral history
   */
  getReferralHistory(referrer) {
    return this.referrals[referrer] || [];
  }
}

// Example usage
try {
  const referralProgram = new ReferralProgram();

  // Add referrals
  referralProgram.addReferral('referrer1', 'referral1', 100);
  referralProgram.addReferral('referrer1', 'referral2', 200);
  referralProgram.addReferral('referrer2', 'referral3', 50);

  // Calculate commission
  const commission1 = referralProgram.calculateCommission('referrer1');
  const commission2 = referralProgram.calculateCommission('referrer2');
  console.log(`Referrer 1 commission: $${commission1.toFixed(2)}`);
  console.log(`Referrer 2 commission: $${commission2.toFixed(2)}`);

  // Get referral history
  const history1 = referralProgram.getReferralHistory('referrer1');
  const history2 = referralProgram.getReferralHistory('referrer2');
  console.log('Referrer 1 referral history:');
  console.log(history1);
  console.log('Referrer 2 referral history:');
  console.log(history2);
} catch (error) {
  console.error('Error:', error.message);
}
```
